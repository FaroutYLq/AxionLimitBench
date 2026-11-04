"""Matched-style pipeline/agent repeatability panels. Run in conda straxion.

The historical pipeline inputs and its 96-paper pairing are preserved.
The agent panel uses two new runs, not comparisons with archived predictions.
No extraction or rescoring occurs here. Each panel has its own sample.
"""
from pathlib import Path
import hashlib
import json
import math
import os
import tempfile

os.environ.setdefault('MPLCONFIGDIR', str(Path(tempfile.gettempdir()) / 'aal-pdu-mpl'))
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

OUT = Path(__file__).resolve().parent
ROOT = OUT.parents[3]
AGENT = ROOT / 'paper/revision/repeatability_fable5_agent_100papers'
PIPELINE = ROOT / 'evaluation/eval_runs/noise_floor_100_reuse'
EDGES = np.array([0, .01, .03, .1, .3, 1, 3, np.inf])
LABELS = [r'$<0.01$', '0.01–\n0.03', '0.03–\n0.1', '0.1–\n0.3', '0.3–1', '1–3', r'$\geq3$']


def read(path):
    return json.loads(path.read_text())


def finite_map(path, require_compared):
    result = {}
    for row in read(path)['per_paper']:
        residual = (row.get('interp_metrics') or {}).get('median_residual_dex')
        status = row.get('comparison_status') or row.get('status')
        if residual is not None and math.isfinite(residual):
            if not require_compared or status == 'compared':
                result[row.get('arxiv_id') or row['id']] = float(residual)
    return result


def summarize(name, first, second, selected, require_compared):
    a, b = finite_map(first, require_compared), finite_map(second, require_compared)
    ids = sorted(set(a) & set(b) & set(selected))
    values = np.array([abs(b[key] - a[key]) for key in ids])
    counts, _ = np.histogram(values, EDGES)
    assert int(counts.sum()) == len(ids)
    return {'name': name, 'n': len(ids), 'median_absolute_change_dex': float(np.median(values)),
            'count_below_1e4': int(sum(values < 1e-4)),
            'count_below_003': int(sum(values < .03)),
            'count_at_least_003': int(sum(values >= .03)), 'counts': counts.tolist(),
            'papers': [{'arxiv_id': key, 'first_residual': a[key], 'second_residual': b[key],
                        'absolute_change_dex': abs(b[key] - a[key])} for key in ids],
            'inputs': {str(path.relative_to(ROOT)): hashlib.sha256(path.read_bytes()).hexdigest()
                       for path in [first, second]}}


def main():
    pipeline = summarize('Pipeline', ROOT / 'evaluation/eval_runs/final347_fable/metrics_noproj.json',
                         PIPELINE / 'fable_repeat2/metrics_noproj.json',
                         read(PIPELINE / 'frozen_ids.json')['ids'], False)
    agent = summarize('Agent', AGENT / 'scoring/repeat1/metrics.json',
                      AGENT / 'scoring/repeat2/metrics.json',
                      read(AGENT / 'protocol/selected_ids.json')['ids_in_draw_order'], True)
    assert pipeline['n'] == 96 and pipeline['counts'] == [44, 5, 20, 12, 11, 3, 1]
    assert agent['n'] == 92 and agent['counts'] == [73, 8, 4, 5, 2, 0, 0]
    assert agent['counts'] == read(AGENT / 'analysis/summary.json')['histogram_abs_delta_residual_dex']['bin_counts']
    provenance = {'quantity': 'Absolute difference between two per-paper median residual scores in dex; not direct curve difference.',
                  'samples': 'Different frozen 100-paper samples; pipeline benchmark versus reread, agent two fresh sessions.',
                  'bins_dex': [0, .01, .03, .1, .3, 1, 3, 'infinity'],
                  'pipeline': pipeline, 'agent': agent}
    (OUT / 'plot_data.json').write_text(json.dumps(provenance, indent=2) + '\n')
    plt.rcParams.update({'font.size': 10, 'axes.grid': True, 'grid.alpha': .3,
                         'figure.dpi': 150, 'pdf.fonttype': 42, 'ps.fonttype': 42})
    fig, axes = plt.subplots(1, 2, figsize=(7.1, 3.6), sharey=True)
    for ax, data, letter in zip(axes, [pipeline, agent], ['a', 'b']):
        counts = data['counts']; x = np.arange(len(counts))
        ax.bar(x, counts, width=.92, color=['C0', 'C0'] + ['C1'] * 5,
               edgecolor='k', linewidth=.5, zorder=2)
        for xi, count in zip(x, counts):
            if count:
                ax.text(xi, count + 1.2, str(count), ha='center', va='bottom', fontsize=9)
        ax.axvline(1.5, ymax=.88, color='.4', linestyle='--', linewidth=.9, zorder=1)
        ax.set_ylim(0, 105)
        ax.set_yticks([0, 20, 40, 60, 80, 100])
        ax.text(.03, .97, f'({letter}) Fable 5 {data["name"].lower()}',
                transform=ax.transAxes, ha='left', va='top', fontsize=10)
        ax.text(.5, 89, f'$<0.03$ dex\n({data["count_below_003"]} papers)',
                ha='center', va='top', fontsize=8.5, color='C0')
        ax.text(4, 89, f'$\\geq0.03$ dex\n({data["count_at_least_003"]} papers)',
                ha='center', va='top', fontsize=8.5, color='C1')
        ax.text(.97, .60, f'median $|\\Delta|$ = {data["median_absolute_change_dex"]:.3f} dex\n'
                f'{data["count_below_1e4"]}/{data["n"]} below $10^{{-4}}$ dex',
                transform=ax.transAxes, ha='right', va='top', fontsize=8.3,
                bbox=dict(boxstyle='round', facecolor='white', edgecolor='.7', alpha=.95))
        ax.set_xticks(x, LABELS, fontsize=8)
        ax.set_ylabel(f'Papers (of {data["n"]})', fontsize=10)
        ax.grid(axis='x', visible=False)
    fig.supxlabel('Run-to-run change in per-paper median residual [dex]', fontsize=10, y=.015)
    fig.subplots_adjust(left=.10, right=.99, top=.97, bottom=.19, wspace=.25)
    fig.savefig(OUT / 'repeatability_agent_pipeline.pdf')
    fig.savefig(OUT / 'repeatability_agent_pipeline.png', dpi=200)
    plt.close(fig)
    print(json.dumps({d['name']: {k:v for k,v in d.items() if k not in ['papers','inputs']}
                      for d in [pipeline, agent]}, indent=2))


if __name__ == '__main__':
    main()
