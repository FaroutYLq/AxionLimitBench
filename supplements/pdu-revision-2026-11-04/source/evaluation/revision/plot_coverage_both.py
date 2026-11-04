"""Plot 1-C_ref and 1-C_ext, retaining fixed post-special-case denominators.

Run in straxion: python -m evaluation.revision.plot_coverage_both
"""
import hashlib
import argparse
import json
from pathlib import Path

from .plot_coverage_log import STYLES, plt, np, FixedLocator


def both_coverages(row):
    ref = row['reference_intervals_log10_eV']
    ext = row['prediction_intervals_log10_eV']
    reference = row['coverage']  # includes the documented discrete-mass check
    ref_span = sum(b-a for a, b in ref)
    ext_span = sum(b-a for a, b in ext)
    if ref_span <= 0 or ext_span <= 0:
        return reference, None
    overlap = sum(max(0, min(b, d)-max(a, c)) for a, b in ref for c, d in ext)
    assert abs(overlap/ref_span-reference) < 1e-10
    extraction = min(1., overlap/ext_span)
    assert 0 <= extraction <= 1
    return reference, extraction


def main(linear=False, report_dir=None):
    out = Path(report_dir) if report_dir is not None else Path(__file__).resolve().parents[2] / 'paper/revision/cohort_coverage'
    source = out/'per_paper.json'
    rows = json.loads(source.read_text())
    summary = json.loads((out/'summary.json').read_text())
    tolerance = 1e-12
    arms, all_positive, per_paper = {}, [], []
    for model in ('fable', 'opus', 'haiku'):
        for system in ('agent', 'pipeline'):
            arm = system+'_'+model
            included = [r for r in rows if r['arm']==arm
                        and not r.get('excluded_from_coverage_denominator', r['status']=='special_case_excluded')]
            assert len(included) == summary[arm]['coverage_denominator']
            assert all(r['status']=='measured' for r in included)
            measures = [(r['reference_coverage'], r['extraction_coverage'])
                        if 'reference_coverage' in r else both_coverages(r) for r in included]
            for row, (cr, ce) in zip(included, measures):
                per_paper.append({'arm': arm, 'arxiv_id': row['arxiv_id'], 'reference_coverage': cr,
                                  'extraction_coverage': ce,
                                  'extraction_coverage_na': None if ce is not None else row.get('extraction_coverage_na_reason', 'no continuous mass range on reference or extraction')})
            arms[arm] = {'n': len(included), 'measures': measures}
            all_positive.extend(1-v for pair in measures for v in pair if v is not None and 1-v > tolerance)
    lower = int(np.floor(np.log10(min(all_positive))))
    edges = np.logspace(lower, 0, -lower*4+1)
    if linear:
        edges = np.arange(0, 101, 10)
    plt.rcdefaults()
    # Match the shared journal figures used by the PDU manuscript
    # (paper/make_journal_figures.py), retaining the six configuration colors.
    plt.rcParams.update({'font.size': 11, 'axes.grid': True, 'grid.alpha': .3,
                         'figure.dpi': 150, 'savefig.bbox': 'tight',
                         'pdf.fonttype': 42, 'ps.fonttype': 42,
                         'svg.fonttype': 'none'})
    fig, axes = plt.subplots(2, 3, figsize=(10.8, 6.4), sharex=True, sharey=True)
    bins = {'input_sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
            'bin_edges': edges.tolist(), 'bin_units': 'coverage percent' if linear else 'uncovered fraction',
            'full_tolerance': tolerance,
            'normalization': 'fixed report coverage denominator after recorded exclusions; N/A retained in denominator; full coverage included in final bin for linear plots', 'arms': {}}
    max_height = 0
    for col, (model, title) in enumerate([('fable', 'Fable 5'), ('opus', 'Opus 4.8'), ('haiku', 'Haiku 4.5')]):
        axes[0, col].set_title(title, fontsize=11)
        for dim, name in enumerate(('reference', 'extraction')):
            ax = axes[dim, col]
            for system in ('agent', 'pipeline'):
                arm = system+'_'+model
                n = arms[arm]['n']
                values = [pair[dim] for pair in arms[arm]['measures'] if pair[dim] is not None]
                gaps = 1-np.asarray(values)
                full = int(np.count_nonzero(gaps <= tolerance))
                na = n-len(values)
                plotted = 100*np.asarray(values) if linear else gaps[gaps > tolerance]
                counts, _ = np.histogram(plotted, bins=edges)
                assert int(counts.sum())+(0 if linear else full)+na == n
                fractions = counts/n
                max_height = max(max_height, fractions.max())
                if linear:
                    label = f'{system} (n={n})' if dim==0 else f'{system} (n={n}; N/A={na})'
                    style = STYLES[arm]
                    ax.bar(edges[:-1]+(.5 if system=='agent' else 5), fractions, width=4.3,
                           align='edge', color=style['color'], label=label, zorder=3)
                else:
                    label = f'{system} (n={n}; full={full})' if dim==0 else f'{system} (full={full}; N/A={na})'
                    ax.stairs(fractions, edges, label=label, **STYLES[arm])
                bins['arms'].setdefault(arm, {'n': n})[name] = {
                    'counts': counts.tolist(), 'fractions': fractions.tolist(), 'full': full, 'na': na}
            ax.axvline(90 if linear else .1, color='k', lw=.7, ls='-.', alpha=.6)
            ax.set_xscale('linear' if linear else 'log')
            ax.set_xlim(edges[0], edges[-1])
            ax.xaxis.set_major_locator(FixedLocator(np.arange(0, 101, 20) if linear else 10.**np.arange(0, lower-1, -2)[::-1]))
            ax.tick_params(labelbottom=True)
            label = (r'$C_{\rm ref}$ [%]' if dim==0 else r'$C_{\rm ext}$ [%]') if linear else (r'$1-C_{\rm ref}$' if dim==0 else r'$1-C_{\rm ext}$')
            ax.set_xlabel(label)
            ax.set_axisbelow(True)
            ax.grid(alpha=.3, which='both')
            ax.legend(fontsize=8, loc='upper left')
    axes[0, 0].set_ylim(0, min(1., np.ceil(max_height*1.3/.05)*.05))
    axes[0, 0].set_ylabel('reference denominator\nfraction of papers per bin')
    axes[1, 0].set_ylabel('extraction denominator\nfraction of papers per bin')
    fig.tight_layout(w_pad=.8, h_pad=1.5)
    stem = 'coverage_both_histograms_linear' if linear else 'coverage_both_uncovered_histograms_log'
    for ext in ('png', 'svg'):
        fig.savefig(out/f'{stem}.{ext}', dpi=300, facecolor='white')
    plt.close(fig)
    (out/f'{stem}_bins.json').write_text(json.dumps(bins, indent=2)+'\n')
    (out/'both_coverages_per_paper.json').write_text(json.dumps(per_paper, indent=2)+'\n')
    print(out/f'{stem}.png')
    for arm, data in bins['arms'].items():
        print(arm, 'N', data['n'], 'extraction coverage N/A', data['extraction']['na'])


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--linear', action='store_true', help='Plot coverage itself in 10-percentage-point bins')
    parser.add_argument('--report-dir', type=Path, help='Coverage report directory; defaults to the historical PDU-cohort report')
    args = parser.parse_args()
    main(args.linear, args.report_dir)
