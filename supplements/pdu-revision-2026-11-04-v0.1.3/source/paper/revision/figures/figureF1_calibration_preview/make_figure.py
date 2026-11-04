"""Confidence calibration preview from archived ML4PS results, conda straxion.

Median-residual-only diagnostic, not the revised coverage-qualified success rate.
Frozen confidence values come from saved predictions, never scorer defaults.
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
METRICS = OUT.parent / 'figure4_residual_cdf_preview' / 'data'
SNAPSHOTS = Path(os.environ.get("AXLB_BENCHMARK_ROOT", str(OUT.parents[3] / "benchmark"))) / "results"
MODELS = [('fable', 'fable5', 'Fable 5', '#c0392b', '#1f4e79'),
          ('opus', 'opus48', 'Opus 4.8', '#e67e22', '#2e86c1'),
          ('haiku', 'haiku45', 'Haiku 4.5', '#d7a86e', '#7f8c8d')]
EDGES = [0, .5, .7, .8, .9, 1.0]


def freeze_inputs(arm, system, model):
    path = OUT / 'data' / f'{arm}_metrics.json'
    if not path.exists():
        shutil.copy2(METRICS / path.name, path)
    conf_path = OUT / 'data' / f'{arm}_confidences.json'
    if not conf_path.exists():
        conf = {}
        for source in sorted((SNAPSHOTS / system / model).glob('*.json')):
            if not (source.name[0].isdigit() or source.name.startswith(('hep', 'astro', 'quant'))):
                continue
            snap = json.loads(source.read_text())
            key = snap.get('arxiv_id')
            assert key and key not in conf
            conf[key] = {'confidence': snap.get('extraction_confidence'),
                         'source_file': source.name,
                         'source_sha256': hashlib.sha256(source.read_bytes()).hexdigest()}
        assert conf, 'Missing archived snapshots'
        conf_path.write_text(json.dumps(conf, indent=2) + '\n')
    return json.loads(path.read_text()), json.loads(conf_path.read_text()), {
        'metrics_sha256': hashlib.sha256(path.read_bytes()).hexdigest(),
        'confidences_sha256': hashlib.sha256(conf_path.read_bytes()).hexdigest()}


def summarize(metrics, confidences):
    rows, missing, excluded = [], [], []
    for row in metrics['per_paper']:
        status = row.get('comparison_status') or row.get('status')
        if status in {'excluded_gt', 'gt_unusable', None}:
            excluded.append(row['arxiv_id'])
            continue
        confidence = confidences.get(row['arxiv_id'], {}).get('confidence')
        if (not isinstance(confidence, (int, float)) or isinstance(confidence, bool)
                or not math.isfinite(confidence) or not 0 <= confidence <= 1):
            missing.append(row['arxiv_id'])
            continue
        value = (row.get('interp_metrics') or {}).get('median_residual_dex')
        hit = (status == 'compared' and value is not None
               and math.isfinite(value) and value <= .3)
        rows.append({'arxiv_id': row['arxiv_id'], 'confidence': confidence,
                     'hit': hit, 'comparison_status': status,
                     'median_residual_dex': value if value is not None and math.isfinite(value) else None})
    assert len({p['arxiv_id'] for p in rows}) == len(rows)
    bins = []
    for i, (lo, hi) in enumerate(zip(EDGES[:-1], EDGES[1:])):
        selected = [p for p in rows if lo <= p['confidence']
                    and (p['confidence'] < hi or (i == 4 and p['confidence'] <= hi))]
        n = len(selected)
        if not n:
            continue
        k = sum(p['hit'] for p in selected)
        proportion = k/n
        z = 1.959963984540054
        denominator = 1 + z*z/n
        centre = (proportion + z*z/(2*n))/denominator
        half = z * math.sqrt(proportion*(1-proportion)/n + z*z/(4*n*n))/denominator
        bins.append({'bin_lo': lo, 'bin_hi': hi, 'n': n, 'hits': k,
                     'mean_confidence': float(np.mean([p['confidence'] for p in selected])),
                     'hit_fraction': proportion,
                     'ci95_lo': max(0., centre-half), 'ci95_hi': min(1., centre+half)})
    assert sum(b['n'] for b in bins) == len(rows)
    return {'n': len(rows), 'missing_confidence_ids': missing,
            'excluded_ungradeable_ids': excluded, 'bins': bins, 'papers': rows}


def main():
    (OUT / 'data').mkdir(exist_ok=True)
    report = {'source_commit': 'ac1542965b7c6b254238312a4d735d90c5a3a472',
              'criterion': 'Finite median residual <= 0.3 dex. No coverage requirement.',
              'scope': 'ML4PS scorable papers with a reported numeric confidence. Nonfinite or failed comparisons are misses.',
              'bin_edges': EDGES, 'last_bin_includes_one': True,
              'interval': '95% Wilson binomial interval',
              'marker_area': '0.65 times bin sample size, in points squared',
              'arms': {}}
    plt.rcParams.update({'font.size': 11, 'axes.grid': True, 'grid.alpha': .3,
                         'figure.dpi': 150, 'savefig.bbox': 'tight',
                         'pdf.fonttype': 42, 'ps.fonttype': 42, 'svg.fonttype': 'none'})
    fig, axes = plt.subplots(1, 3, figsize=(6.0, 3.5), sharex=True, sharey=True)
    for ax, (key, model, title, agent_color, pipeline_color) in zip(axes, MODELS):
        ax.plot([0, 1], [0, 1], ls=':', color='.4', lw=1, zorder=1)
        handles = []
        for system_key, system_dir, label, color, marker, ls in [
                ('agent', 'agent_claude_code', 'Agent', agent_color, 'o', '-'),
                ('pipeline', 'aal_harness', 'Pipeline', pipeline_color, 's', '--')]:
            arm = f'{system_key}_{key}'
            metrics, confidence, hashes = freeze_inputs(arm, system_dir, model)
            data = summarize(metrics, confidence)
            report['arms'][arm] = {**hashes, **data}
            bins = data['bins']
            x = np.asarray([b['mean_confidence'] for b in bins])
            y = np.asarray([b['hit_fraction'] for b in bins])
            lo = np.asarray([b['ci95_lo'] for b in bins])
            hi = np.asarray([b['ci95_hi'] for b in bins])
            ns = np.asarray([b['n'] for b in bins])
            ax.errorbar(x, y, yerr=[y-lo, hi-y], color=color, ls='none',
                        lw=1.4, elinewidth=.9, capsize=2.5, zorder=2)
            ax.scatter(x, y, s=.65*ns, marker=marker, c=color,
                       edgecolors='white', linewidths=.4, zorder=3)
            handles.append(Line2D([], [], color=color, marker=marker, ls='none',
                                  lw=1.4, markersize=4.5, label=f'{label} (N={data["n"]})'))
            print(arm, 'N', data['n'], 'missing confidence', len(data['missing_confidence_ids']),
                  'bin Ns', ns.tolist())
        ax.text(.04, .96, title, transform=ax.transAxes,
                fontsize=11, ha='left', va='top', zorder=5)
        ax.legend(handles=handles, loc='lower left', bbox_to_anchor=(0, 1.01), borderaxespad=0, fontsize=7, frameon=False,
                  handlelength=1.2)
        ax.set_xlim(-.02, 1.02)
        ax.set_ylim(-.02, 1.02)
        ax.set_xticks(np.linspace(0, 1, 6))
        ax.set_yticks(np.linspace(0, 1, 6))
        ax.tick_params(labelsize=8)
        ax.set_xlabel('Mean reported\nconfidence', fontsize=9)
    axes[0].set_ylabel('Fraction with median\nresidual ≤0.3 dex', fontsize=9)
    fig.tight_layout(w_pad=.7)
    for ext in ('pdf', 'png', 'svg'):
        fig.savefig(OUT / f'figureF1_calibration.{ext}', dpi=300)
    plt.close(fig)
    (OUT / 'plot_data.json').write_text(json.dumps(report, indent=2, allow_nan=False)+'\n')


if __name__ == '__main__':
    main()
