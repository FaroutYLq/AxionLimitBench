"""Plot the full-cohort coverage distributions with the agreed exclusions.

Run in straxion: python -m evaluation.revision.plot_coverage
"""
from pathlib import Path
import hashlib
import json
import os
import tempfile

os.environ.setdefault('MPLCONFIGDIR', str(Path(tempfile.gettempdir()) / 'aal-matplotlib'))
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import numpy as np


def main():
    out = Path(__file__).resolve().parents[2] / 'paper/revision/cohort_coverage'
    source = out / 'per_paper.json'
    rows = json.loads(source.read_text())
    summary = json.loads((out / 'summary.json').read_text())
    edges = np.arange(0, 101, 10)
    colors = {'agent': '#2166AC', 'pipeline': '#D97820'}
    plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 11,
                         'axes.spines.top': False, 'axes.spines.right': False,
                         'svg.fonttype': 'none', 'axes.labelcolor': '#253044',
                         'xtick.color': '#465166', 'ytick.color': '#465166'})
    fig, axes = plt.subplots(1, 3, figsize=(15, 5.8), sharey=True)
    fig.subplots_adjust(left=.065, right=.985, top=.77, bottom=.24, wspace=.13)
    fig.text(.065, .94, 'Coverage distributions', fontsize=23, weight='bold', color='#172235')
    fig.text(.065, .885, 'Agent and pipeline on each model · 10-percentage-point bins · each configuration normalized to 100%',
             fontsize=11.5, color='#536075')
    data = {'source_sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
            'bin_edges_percent': edges.tolist(),
            'bin_convention': '[left, right), except final bin [90, 100]', 'configurations': {}}
    for ax, (model, title) in zip(axes, [('fable', 'Fable 5'), ('opus', 'Opus 4.8'), ('haiku', 'Haiku 4.5')]):
        ax.set_title(title, loc='left', fontsize=15, weight='bold', pad=13, color='#172235')
        ax.set_axisbelow(True)
        ax.grid(axis='y', color='#E2E7EF', linewidth=.8)
        ax.spines['left'].set_color('#C3CAD5')
        ax.spines['bottom'].set_color('#C3CAD5')
        for system, offset in [('agent', .5), ('pipeline', 5.0)]:
            arm = system+'_'+model
            included = [r for r in rows if r['arm'] == arm and r['status'] != 'special_case_excluded']
            assert len(included) == summary[arm]['coverage_denominator']
            assert all(r['status'] == 'measured' and r['coverage'] is not None for r in included), 'Unresolved coverage must be reported, not silently omitted'
            values = np.asarray([r['coverage'] for r in included]) * 100
            assert np.isfinite(values).all() and ((values >= 0) & (values <= 100)).all()
            counts, _ = np.histogram(values, bins=edges)
            assert int(counts.sum()) == len(included)
            percentages = counts * 100 / len(included)
            label = f"{system.capitalize()} (n = {len(included)})"
            ax.bar(edges[:-1]+offset, percentages, width=4.3, align='edge',
                   color=colors[system], label=label, zorder=3)
            data['configurations'][arm] = {'n': len(included), 'counts': counts.tolist(),
                'percentages': percentages.tolist(), 'special_cases_excluded': summary[arm]['special_cases_excluded']}
        ax.axvline(90, color='#788397', linewidth=1, linestyle=(0, (3, 3)), zorder=2)
        ax.text(89, 78, '90%', fontsize=9, ha='right', color='#647084')
        ax.set_xlim(0, 100)
        ax.set_ylim(0, 82)
        ax.set_xticks(np.arange(0, 101, 20))
        ax.xaxis.set_minor_locator(MultipleLocator(10))
        ax.yaxis.set_major_locator(MultipleLocator(20))
        ax.tick_params(axis='both', which='major', length=3)
        ax.set_xlabel('Coverage of archived reference (%)', labelpad=10)
        ax.legend(loc='upper left', frameon=False, fontsize=10, handlelength=1.2)
    axes[0].set_ylabel('Share of papers in each configuration (%)', labelpad=12)
    fig.text(.065, .105, 'Excluded special cases: pipeline Fable 3, Opus 2, Haiku 5. All remaining cohort papers are included.',
             fontsize=10, color='#536075')
    fig.text(.065, .065, 'Coverage measures mass support, not coupling accuracy. Reference-range flags remain included.',
             fontsize=10, color='#536075')
    for ext in ('png', 'svg'):
        fig.savefig(out / f'coverage_histograms.{ext}', dpi=200, facecolor='white')
    plt.close(fig)
    (out/'coverage_histogram_bins.json').write_text(json.dumps(data, indent=2)+'\n')
    print(out/'coverage_histograms.png')


if __name__ == '__main__':
    main()
