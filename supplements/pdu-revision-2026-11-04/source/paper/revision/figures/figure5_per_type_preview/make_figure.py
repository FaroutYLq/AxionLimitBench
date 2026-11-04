"""Fable agent/pipeline per-type preview; run in conda straxion.

Uses the same frozen ML4PS metrics as Figure 4. Checks saved aggregates
against individual paper scores; never runs extraction or edits the manuscript.
"""
import hashlib
import json
import math
import os
from pathlib import Path
import shutil
import tempfile

os.environ.setdefault('MPLCONFIGDIR', str(Path(tempfile.gettempdir()) / 'aal-pdu-mpl'))
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import numpy as np

OUT = Path(__file__).resolve().parent
SOURCE = OUT.parent / 'figure4_residual_cdf_preview' / 'data'
ARMS = [('agent_fable', 'Fable 5 agent', '#c0392b', 'o', -.17),
        ('pipeline_fable', 'Fable 5 pipeline', '#1f4e79', 's', .17)]


def checked_aggregate(metrics):
    grouped = {}
    for row in metrics['per_paper']:
        value = (row.get('interp_metrics') or {}).get('median_residual_dex')
        if row.get('comparison_status') != 'compared' or value is None or not math.isfinite(value):
            continue
        grouped.setdefault(row['comparison_coupling'], []).append(value)
    saved = metrics['per_type_aggregate']
    assert set(grouped) == set(saved['per_type'])
    for coupling, values in grouped.items():
        data = saved['per_type'][coupling]
        arr = np.asarray(values)
        rng = np.random.default_rng(0)
        medians = np.median(arr[rng.integers(0, len(arr), (1000, len(arr)))], axis=1)
        lo, hi = np.percentile(medians, [2.5, 97.5])
        assert len(values) == data['n']
        assert np.allclose([np.median(arr), lo, hi],
                           [data['median_residual_dex'], data['ci95_lo'], data['ci95_hi']],
                           rtol=1e-10, atol=1e-12)
    all_values = [v for values in grouped.values() for v in values]
    assert len(all_values) == saved['n_papers_compared']
    assert np.isclose(np.median(all_values), saved['micro_median_residual_dex'])
    assert np.isclose(np.mean([np.median(v) for v in grouped.values()]),
                      saved['macro_median_residual_dex'])
    return saved


def main():
    (OUT / 'data').mkdir(exist_ok=True)
    report = {'source_commit': 'ac1542965b7c6b254238312a4d735d90c5a3a472',
              'scope': 'Finite comparisons from ML4PS, consistent with Figure 4; no coverage filtering.',
              'uncertainty': 'Per-type percentile bootstrap of paper medians, 1000 resamples, seed 0, 95% interval.',
              'comparison': 'Each arm uses its own finite papers; not a paired-paper comparison.',
              'macro': 'Mean of available type medians: 13 agent types and 12 pipeline types; not a common-type comparison.',
              'arms': {}}
    aggregates = {}
    for arm, label, color, marker, offset in ARMS:
        path = OUT / 'data' / f'{arm}_metrics.json'
        if not path.exists():
            shutil.copy2(SOURCE / path.name, path)
        aggregates[arm] = checked_aggregate(json.loads(path.read_text()))
        report['arms'][arm] = {'input_sha256': hashlib.sha256(path.read_bytes()).hexdigest(),
                               **aggregates[arm]}
    pipeline = aggregates['pipeline_fable']['per_type']
    agent = aggregates['agent_fable']['per_type']
    # Retain the original figure's ordering principle: hardest pipeline types first.
    names = sorted(pipeline, key=lambda name: pipeline[name]['median_residual_dex'], reverse=True)
    names += sorted(set(agent) - set(pipeline))
    report['coupling_order'] = names
    plt.rcParams.update({'font.size': 11, 'axes.grid': True, 'grid.alpha': .3,
                         'figure.dpi': 150, 'savefig.bbox': 'tight',
                         'pdf.fonttype': 42, 'ps.fonttype': 42, 'svg.fonttype': 'none'})
    fig, (ax, count_ax) = plt.subplots(1, 2, figsize=(6.5, 5.5), sharey=True,
                                      gridspec_kw={'width_ratios': [5.5, 1.15], 'wspace': .04})
    for i in range(len(names)):
        if i % 2 == 0:
            for panel in (ax, count_ax):
                panel.axhspan(i-.48, i+.48, color='0.96', zorder=0)
    summary_y = [len(names)+.65, len(names)+1.65]
    for arm_index, (arm, label, color, marker, offset) in enumerate(ARMS):
        aggregate = aggregates[arm]
        for i, name in enumerate(names):
            data = aggregate['per_type'].get(name)
            if data is None:
                count_ax.text(arm_index, i, '0', color=color, ha='center', va='center', fontsize=8)
                continue
            median, lo, hi = (data[k] for k in ('median_residual_dex', 'ci95_lo', 'ci95_hi'))
            assert 0 < lo <= median <= hi
            ax.errorbar(median, i+offset, xerr=[[median-lo], [hi-median]],
                        fmt=marker, markersize=4.8, color=color,
                        markerfacecolor='white' if data['small_sample'] else color,
                        markeredgewidth=1.1, elinewidth=1.0, capsize=2.2, zorder=3)
            count_ax.text(arm_index, i, f"{data['n']}" + ('*' if data['small_sample'] else ''),
                          color=color, ha='center', va='center', fontsize=8)
        for y, key in zip(summary_y, ['micro_median_residual_dex', 'macro_median_residual_dex']):
            ax.plot(aggregate[key], y+offset, marker=marker, color=color, markersize=4.8)
        count_ax.text(arm_index, summary_y[0], str(aggregate['n_papers_compared']),
                      color=color, ha='center', va='center', fontsize=8)
        count_ax.text(arm_index, summary_y[1], f"{aggregate['n_types']}\ntypes",
                      color=color, ha='center', va='center', fontsize=8)
    ax.axvline(.3, color='0.4', ls=':', lw=.9, zorder=1)
    ax.set_xscale('log')
    ax.set_xlim(1e-3, 20)
    ax.set_ylim(summary_y[-1]+.65, -.65)
    ax.set_yticks(list(range(len(names))) + summary_y)
    ax.set_yticklabels(names + ['All-paper median', 'Mean of type medians'], fontsize=9)
    ax.set_xlabel('Median residual [dex]')
    ax.grid(axis='y', visible=False)
    ax.grid(axis='x', which='major', alpha=.3)
    for panel in (ax, count_ax):
        panel.axhline(len(names)-.25, color='.6', lw=.7)
    handles = [Line2D([], [], color=color, marker=marker, lw=1,
                      markersize=4.8, label=label) for _, label, color, marker, _ in ARMS]
    ax.legend(handles=handles, loc='lower left', bbox_to_anchor=(0, 1.015, 1, .2),
              ncol=2, mode='expand', frameon=False, borderaxespad=0, fontsize=8)
    count_ax.set_xlim(-.6, 1.6)
    count_ax.set_xticks([])
    count_ax.tick_params(axis='y', left=False, labelleft=False)
    count_ax.grid(False)
    for spine in count_ax.spines.values():
        spine.set_visible(False)
    count_ax.text(.18, 1.02, 'Agent', transform=count_ax.transAxes,
                  color=ARMS[0][2], fontsize=8, ha='center')
    count_ax.text(.79, 1.02, 'Pipeline', transform=count_ax.transAxes,
                  color=ARMS[1][2], fontsize=8, ha='center')
    # The axis label describes uncertainty and counts; the manuscript supplies the caption.
    count_ax.set_xlabel('N (* < 5)', fontsize=8, labelpad=10)
    ax.set_xlabel('Median residual [dex]; per-type bars: 95% CI', fontsize=10)
    fig.subplots_adjust(left=.21, right=.98, bottom=.11, top=.92)
    for ext in ('pdf', 'png', 'svg'):
        fig.savefig(OUT / f'figure5_per_type.{ext}', dpi=300)
    plt.close(fig)
    (OUT / 'plot_data.json').write_text(json.dumps(report, indent=2) + '\n')
    for arm, data in aggregates.items():
        print(arm, 'finite papers', data['n_papers_compared'], 'types', data['n_types'],
              'micro', data['micro_median_residual_dex'], 'macro', data['macro_median_residual_dex'])


if __name__ == '__main__':
    main()
