"""Log-binned coverage histograms styled like the ML4PS make_figure.py.

Run in straxion: python -m evaluation.revision.plot_coverage_log
"""
from pathlib import Path
import argparse
import hashlib
import json
import os
import tempfile

os.environ.setdefault('MPLCONFIGDIR', str(Path(tempfile.gettempdir()) / 'aal-matplotlib'))
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.ticker import FixedLocator, FuncFormatter
import numpy as np

# Colors, line widths and line styles from AxionLimitBench-paper/make_figure.py.
STYLES = {
    'agent_fable': dict(color='#c0392b', lw=2.2),
    'agent_opus': dict(color='#e67e22', lw=1.6, ls='--'),
    'agent_haiku': dict(color='#d7a86e', lw=1.4, ls=':'),
    'pipeline_fable': dict(color='#1f4e79', lw=1.8),
    'pipeline_opus': dict(color='#2e86c1', lw=1.4, ls='--'),
    'pipeline_haiku': dict(color='#7f8c8d', lw=1.4, ls=':'),
}


def main(uncovered=False):
    out = Path(__file__).resolve().parents[2] / 'paper/revision/cohort_coverage'
    source = out / 'per_paper.json'
    rows = json.loads(source.read_text())
    summary = json.loads((out / 'summary.json').read_text())
    # 0.01% to 100%; 8 equal log bins per decade. Zero is separate.
    edges = np.geomspace(.01, 100, 33)
    full_tolerance = 1e-12
    if uncovered:
        gaps = np.asarray([1-r['coverage'] for r in rows if r['status'] == 'measured'])
        lower_exponent = int(np.floor(np.log10(gaps[gaps > full_tolerance].min())))
        edges = np.logspace(lower_exponent, 0, -lower_exponent*4+1)
    plt.rcdefaults()
    plt.rcParams['svg.fonttype'] = 'none'
    fig, axes = plt.subplots(1, 3, figsize=(7.0, 2.55), sharey=True)
    data = {'source_sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
            'bin_edges': edges.tolist(), 'bin_units': 'uncovered fraction' if uncovered else 'coverage percent',
            'binning': f'{len(edges)-1} equal log bins; zero counted separately',
            'full_coverage_tolerance': full_tolerance if uncovered else None,
            'normalization': 'fraction of the full post-special-case cohort in each bin, including zero cases in denominator',
            'style_reference': '/Users/lanqingyuan/Documents/GitHub/AxionLimitBench-paper/make_figure.py',
            'configurations': {}}
    max_height = 0
    for ax, (model, title) in zip(axes, [('fable', 'Fable 5'), ('opus', 'Opus 4.8'), ('haiku', 'Haiku 4.5')]):
        for system in ('agent', 'pipeline'):
            arm = system+'_'+model
            included = [r for r in rows if r['arm'] == arm and r['status'] != 'special_case_excluded']
            assert len(included) == summary[arm]['coverage_denominator']
            assert all(r['status'] == 'measured' and r['coverage'] is not None for r in included)
            values = 100 * np.asarray([r['coverage'] for r in included])
            if uncovered:
                values = 1-np.asarray([r['coverage'] for r in included])
                values[values <= full_tolerance] = 0  # floating-point equality only
            assert np.isfinite(values).all() and ((values >= 0) & (values <= 100)).all()
            zeros = int(np.count_nonzero(values == 0))
            positive = values[values > 0]
            assert positive.min() >= edges[0]
            counts, _ = np.histogram(positive, bins=edges)
            assert int(counts.sum()) + zeros == len(included)
            heights = counts / len(included)
            max_height = max(max_height, heights.max())
            zero_label = 'full' if uncovered else 'zero'
            ax.stairs(heights, edges, label=f'{system} (n={len(included)}; {zero_label}={zeros})', **STYLES[arm])
            data['configurations'][arm] = {'n': len(included), 'zero_count': zeros,
                'zero_fraction': zeros/len(included), 'counts': counts.tolist(), 'fractions': heights.tolist(),
                'special_cases_excluded': summary[arm]['special_cases_excluded']}
        ax.axvline(.1 if uncovered else 90, color='k', lw=.7, ls='-.', alpha=.6)
        if not uncovered:
            ax.text(80, .4, '90%', rotation=90, ha='right', va='center', fontsize=6.5)
        ax.set_xscale('log')
        ax.set_xlim(edges[0], edges[-1])
        ax.set_ylim(0, 1)
        if uncovered:
            ax.xaxis.set_major_locator(FixedLocator([1e-6, 1e-4, 1e-2, 1]))
        else:
            ax.xaxis.set_major_locator(FixedLocator([.01, .1, 1, 10, 100]))
            ax.xaxis.set_major_formatter(FuncFormatter(lambda x, _: f'{x:g}'))
        ax.set_xlabel(r'$1-\mathrm{coverage}$' if uncovered else 'reference coverage [%]', fontsize=8)
        ax.set_title(title, fontsize=9)
        ax.tick_params(labelsize=7)
        ax.grid(alpha=.25, which='both')
        ax.legend(fontsize=6, loc='upper left', frameon=False, handlelength=2.2, labelspacing=.25)
    axes[0].set_ylabel('fraction of papers per bin', fontsize=8)
    if uncovered:
        axes[0].set_ylim(0, np.ceil(max_height*1.3/.05)*.05)
    fig.tight_layout(w_pad=.8, rect=(0, .13, 1, 1))
    note = (r'Full coverage ($1-\mathrm{coverage}\leq10^{-12}$) is listed in legends. Dashed vertical line: 90% coverage.'
            if uncovered else 'Log-spaced coverage bins; zero-coverage cases are listed in legends and retained in normalization.')
    fig.text(.08, .07, note, fontsize=6.5)
    fig.text(.08, .025, 'Special cases excluded: pipeline Fable 3, Opus 2, Haiku 5. Reference-range flags remain included.', fontsize=6.5)
    stem = 'uncovered_fraction_histograms_log' if uncovered else 'coverage_histograms_log'
    for ext in ('png', 'svg'):
        fig.savefig(out/f'{stem}.{ext}', dpi=300, facecolor='white')
    plt.close(fig)
    (out/f'{stem}_bins.json').write_text(json.dumps(data, indent=2)+'\n')
    print(out/f'{stem}.png')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--uncovered', action='store_true', help='Plot 1 - coverage on a logarithmic axis')
    main(parser.parse_args().uncovered)
