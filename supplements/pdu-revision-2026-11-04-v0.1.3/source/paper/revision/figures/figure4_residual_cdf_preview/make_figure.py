"""PDU-format preview of the six-arm ML4PS residual CDF.

Run in conda straxion. Reuses ML4PS data and scorable-pool normalization;
does not apply coverage exclusions or change manuscript figures.
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
import numpy as np

OUT = Path(__file__).resolve().parent
SOURCE = Path(os.environ.get("AXLB_BENCHMARK_ROOT", str(OUT.parents[3] / "benchmark"))) / "results"
ARMS = [
    ('agent_fable', 'agent_claude_code', 'fable5', 'Fable 5 agent', '#c0392b', '-', 2.2),
    ('agent_opus', 'agent_claude_code', 'opus48', 'Opus 4.8 agent', '#e67e22', '--', 1.6),
    ('agent_haiku', 'agent_claude_code', 'haiku45', 'Haiku 4.5 agent', '#d7a86e', ':', 1.6),
    ('pipeline_fable', 'aal_harness', 'fable5', 'Fable 5 pipeline', '#1f4e79', '-', 1.8),
    ('pipeline_opus', 'aal_harness', 'opus48', 'Opus 4.8 pipeline', '#2e86c1', '--', 1.4),
    ('pipeline_haiku', 'aal_harness', 'haiku45', 'Haiku 4.5 pipeline', '#7f8c8d', ':', 1.6),
]


def main():
    plt.rcParams.update({'font.size': 11, 'axes.grid': True, 'grid.alpha': .3,
                         'figure.dpi': 150, 'savefig.bbox': 'tight',
                         'pdf.fonttype': 42, 'ps.fonttype': 42, 'svg.fonttype': 'none'})
    fig, ax = plt.subplots(figsize=(4.2, 3.3))
    report = {'normalization': 'ML4PS scorable pool; no coverage exclusions applied',
              'source_commit': 'ac1542965b7c6b254238312a4d735d90c5a3a472',
              'interpretation': 'Median-residual diagnostic, not joint coverage and pointwise success',
              'arms': {}}
    out_data = OUT / 'data'
    out_data.mkdir(exist_ok=True)
    for arm, system, model, label, color, ls, lw in ARMS:
        path = out_data / f'{arm}_metrics.json'
        if not path.exists():
            shutil.copy2(SOURCE / system / model / 'metrics.json', path)
        m = json.loads(path.read_text())
        pp = m['per_paper']
        pool = (m.get('pool') or {}).get('n_pool_papers') or len(pp)
        def status(r):
            return r.get('comparison_status') if r.get('comparison_status') is not None else (
                'excluded_gt' if r.get('status') == 'excluded_gt' else None)
        n = pool - sum(status(r) in {'excluded_gt', 'gt_unusable', None} for r in pp)
        finite = []
        for row in pp:
            value = (row.get('interp_metrics') or {}).get('median_residual_dex')
            if status(row) == 'compared' and value is not None and math.isfinite(value):
                finite.append({'arxiv_id': row['arxiv_id'], 'residual_dex': value})
        r = np.sort([p['residual_dex'] for p in finite])
        assert 0 < len(r) <= n and np.all(r >= 0)
        # A monotone ECDF including exact zeros in the left-boundary value.
        x = np.unique(np.concatenate(([.01], r[(r > .01) & (r < 100)], [100.])))
        y = np.searchsorted(r, x, side='right') / n
        assert np.all(np.diff(x) > 0) and np.all(np.diff(y) >= 0)
        assert y[-1] == len(r) / n
        ax.step(x, y, where='post', color=color, ls=ls, lw=lw,
                label=f'{label} (N={n})')
        report['arms'][arm] = {
            'input_sha256': hashlib.sha256(path.read_bytes()).hexdigest(),
            'pool_n': pool, 'scorable_n': n, 'finite_n': len(r),
            'within_10_percent_n': int(np.sum(r <= math.log10(1.1))),
            'within_0_3_dex_n': int(np.sum(r <= .3)),
            'finite_fraction': len(r)/n, 'ecdf_x': x.tolist(), 'ecdf_y': y.tolist(),
            'finite_papers': finite,
        }
    for threshold, text in [(math.log10(1.1), '10%'), (3., '3 dex')]:
        ax.axvline(threshold, color='k', lw=.8, ls='-.', alpha=.6)
        ax.annotate(text, (threshold, .025), xytext=(4, 0), textcoords='offset points',
                    fontsize=8, ha='left', va='bottom',
                    bbox={'facecolor': 'white', 'edgecolor': 'none', 'alpha': .9, 'pad': 1.5})
    ax.set_xscale('log')
    ax.set_xlim(.01, 100)
    ax.set_ylim(0, 1)
    ax.set_xlabel('Per-paper median residual [dex]')
    ax.set_ylabel('Fraction of scorable papers')
    ax.grid(alpha=.3, which='both')
    ax.legend(loc='lower left', bbox_to_anchor=(0, 1.015, 1, .2), ncol=2,
              mode='expand', borderaxespad=0, fontsize=7, frameon=False, handlelength=2)
    fig.tight_layout()
    for ext in ('pdf', 'png', 'svg'):
        fig.savefig(OUT / f'figure4_residual_cdf.{ext}', dpi=300)
    plt.close(fig)
    (OUT / 'plot_data.json').write_text(json.dumps(report, indent=2) + '\n')
    for arm, data in report['arms'].items():
        print(arm, 'N', data['scorable_n'], 'finite', data['finite_n'],
              'within 10%', data['within_10_percent_n'])


if __name__ == '__main__':
    main()
