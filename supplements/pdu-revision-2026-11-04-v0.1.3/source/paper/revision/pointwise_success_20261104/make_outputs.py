"""Table 1 and Figure 3 from frozen evaluations; run in conda straxion.

No model calls, rescoring, reference reselection, or changed paper eligibility.
Writes review artifacts only; manuscript inclusion is a separate explicit edit.
"""
import hashlib
import json
import os
from pathlib import Path
import tempfile

os.environ.setdefault('MPLCONFIGDIR', str(Path(tempfile.gettempdir()) / 'aal-pdu-mpl'))
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

OUT = Path(__file__).resolve().parent
REV = OUT.parent
B = 20000
SEED = 20261104
ARMS = [
    ('agent_fable', 'Fable 5 agent', '#c0392b', '-', 2.2),
    ('agent_opus', 'Opus 4.8 agent', '#e67e22', '--', 1.6),
    ('agent_haiku', 'Haiku 4.5 agent', '#d7a86e', ':', 1.6),
    ('pipeline_fable', 'Fable 5 pipeline', '#1f4e79', '-', 1.8),
    ('pipeline_opus', 'Opus 4.8 pipeline', '#2e86c1', '--', 1.4),
    ('pipeline_haiku', 'Haiku 4.5 pipeline', '#7f8c8d', ':', 1.6),
]


def bootstrap(outcomes, key):
    """Resample papers jointly across outcome columns, percentile interval."""
    a = np.asarray(outcomes, dtype=float)
    if a.ndim == 1:
        a = a[:, None]
    seed = SEED + int.from_bytes(hashlib.sha256(key.encode()).digest()[:4], 'little')
    rng = np.random.default_rng(seed)
    ix = rng.integers(0, len(a), (B, len(a)))
    means = a[ix].mean(axis=1)
    ci = np.percentile(means, [2.5, 97.5], axis=0)
    return [{'n': len(a), 'passed': int(a[:, j].sum()),
             'fraction': float(a[:, j].mean()), 'ci95': ci[:, j].tolist(),
             'degenerate': bool(ci[0, j] == ci[1, j])}
            for j in range(a.shape[1])]


def load_data():
    path = REV / 'ml4ps_coverage/per_paper.json'
    source = json.loads(path.read_text())
    summary = json.loads((REV / 'ml4ps_coverage/summary.json').read_text())
    report = {'input_sha256': hashlib.sha256(path.read_bytes()).hexdigest(),
              'bootstrap_resamples': B, 'bootstrap_seed': SEED,
              'bootstrap_method': 'Percentile, resample papers with replacement; outcome columns resampled together.',
              'cohort': 'Pointwise agreement: all finite comparisons. Coverage and joint success: existing N_curve. No reference reselection.',
              'arms': {}}
    rows_by_arm = {}
    for arm, *_ in ARMS:
        all_rows = sorted([r for r in source if r['arm'] == arm], key=lambda r: r['arxiv_id'])
        rows = sorted([r for r in all_rows if not r['excluded_from_coverage_denominator']],
                      key=lambda r: r['arxiv_id'])
        s = summary[arm]
        assert len(all_rows) == s['finite_cohort_n']
        assert len(rows) == len({r['arxiv_id'] for r in rows}) == s['coverage_denominator']
        scores = np.array([r['archived_fraction_within_0_3dex'] for r in rows])
        assert np.isfinite(scores).all() and ((scores >= 0) & (scores <= 1)).all()
        point = scores >= .9
        ref = np.array([r['reference_coverage'] is not None and r['reference_coverage'] > .9 for r in rows])
        ext = np.array([r['extraction_coverage'] is not None and r['extraction_coverage'] > .9 for r in rows])
        both = ref & ext
        joint = both & point
        assert all(bool(joint[i]) == r['joint_success'] and bool(both[i]) == r['coverage_pass']
                   for i, r in enumerate(rows))
        for name, values in [('reference_gt90_n', ref), ('extraction_gt90_n', ext),
                             ('both_gt90_n', both), ('pointwise90_without_coverage_n', point),
                             ('joint_success_n', joint)]:
            assert int(values.sum()) == s[name], (arm, name)
        curve_point_stats, joint_stats = bootstrap(np.column_stack((point, joint)), arm)
        finite_scores = np.array([r['archived_fraction_within_0_3dex'] for r in all_rows])
        assert np.isfinite(finite_scores).all() and ((finite_scores >= 0) & (finite_scores <= 1)).all()
        point_stats = bootstrap(finite_scores >= .9, arm + '/finite')[0]
        types = {}
        for coupling in sorted({r['comparison_coupling'] for r in rows}):
            outcomes = [r['archived_fraction_within_0_3dex'] >= .9 for r in rows
                        if r['comparison_coupling'] == coupling]
            types[coupling] = bootstrap(outcomes, arm + '/' + coupling)[0]
        assert sum(t['n'] for t in types.values()) == len(rows)
        assert sum(t['passed'] for t in types.values()) == curve_point_stats['passed']
        thresholds = np.unique(np.r_[0., finite_scores, .9, 1.])
        passing = np.array([(finite_scores >= t).mean() for t in thresholds])
        assert (np.diff(passing) <= 0).all()
        assert passing[np.flatnonzero(thresholds == .9)[0]] == point_stats['fraction']
        report['arms'][arm] = {'finite_n': len(all_rows), 'curve_n': len(rows),
                              'reference_coverage_fraction': float(ref.mean()),
                              'extraction_coverage_fraction': float(ext.mean()),
                              'both_coverage_fraction': float(both.mean()),
                              'pointwise': point_stats, 'pointwise_curve': curve_point_stats, 'joint': joint_stats,
                              'per_type': types, 'thresholds': thresholds.tolist(),
                              'passing_fractions': passing.tolist(),
                              'paper_ids': [r['arxiv_id'] for r in rows],
                              'pointwise_paper_ids': [r['arxiv_id'] for r in all_rows]}
        rows_by_arm[arm] = rows
    return report, rows_by_arm


def table(report):
    data = [report['arms'][arm] for arm, *_ in ARMS]
    lines = [r'\begin{table}[tp]',
             r'% Generated by paper/revision/pointwise_success_20261104/make_outputs.py.',
             r'\caption{Comparison of three language models (Fable~5, Opus~4.8, and',
             r'Haiku~4.5), each using either an autonomous extraction agent or the fixed',
             r'multi-channel pipeline, on a common benchmark of 329 measured-limit papers.',
             r'Pointwise agreement uses all $N$ finite comparisons; coverage and joint success',
             r'use the $N_{\rm curve}$ comparisons remaining after the exclusions described',
             r'in the text. Pointwise agreement $\geq90\%$ requires at least',
             r'90\% of compared points to lie within 0.3~dex of the reference. Joint success',
             r'requires this condition and both mass-range coverages $>90\%$, using the same',
             r'reference. Brackets give 95\% bootstrap confidence intervals over papers.}',
             r'\label{tab:results}', r'\centering', r'\begingroup',
             r'\fontsize{9}{10.8}\selectfont', r'\setlength{\tabcolsep}{2pt}',
             r'\renewcommand{\arraystretch}{1.16}',
             r'\begin{tabularx}{\textwidth}{@{}p{108pt}*{6}{>{\centering\arraybackslash}X}@{}}',
             r'\toprule',
             r' & \multicolumn{3}{c}{\textbf{Agent}} & \multicolumn{3}{c}{\textbf{Pipeline}} \\',
             r'\cmidrule(lr){2-4}\cmidrule(l){5-7}',
             r' & Fable 5 & Opus 4.8 & Haiku 4.5 & Fable 5 & Opus 4.8 & Haiku 4.5 \\',
             r'\midrule']
    def row(label, cells):
        lines.append(label + ' & ' + ' & '.join(cells) + r' \\')
    def intervals(key, bold=False):
        cells = []
        for d in data:
            st = d[key]
            value = f"{100*st['fraction']:.1f}"
            if bold:
                value = r'\textbf{' + value + '}'
            lo, hi = [100*x for x in st['ci95']]
            cells.append(r'\shortstack{' + value + r'\\{\fontsize{7}{8}\selectfont ['
                         + f'{lo:.1f}--{hi:.1f}' + r']}}')
        return cells
    lines.append(r'\multicolumn{7}{l}{\textit{Pointwise agreement}} \\')
    row(r'Finite comparisons, $N$', [str(d['finite_n']) for d in data])
    row(r'\shortstack[l]{Pointwise agreement\\$\geq90\%$ (\%)}', intervals('pointwise'))
    lines.append(r'\midrule')
    lines.append(r'\multicolumn{7}{l}{\textit{Coverage and joint success}} \\')
    row(r'Eligible curves, $N_{\rm curve}$', [str(d['curve_n']) for d in data])
    row(r'$C_{\rm ref}>90\%$ (\%)', [f"{100*d['reference_coverage_fraction']:.1f}" for d in data])
    row(r'$C_{\rm ext}>90\%$ (\%)', [f"{100*d['extraction_coverage_fraction']:.1f}" for d in data])
    row(r'Both coverages $>90\%$ (\%)', [f"{100*d['both_coverage_fraction']:.1f}" for d in data])
    row(r'\textbf{Joint success (\%)}', intervals('joint', True))
    lines += [r'\bottomrule', r'\end{tabularx}', r'\endgroup', r'\end{table}']
    (OUT / 'table1.tex').write_text('\n'.join(lines) + '\n')


def save(fig, stem):
    for ext in ('pdf', 'png', 'svg'):
        fig.savefig(OUT / f'{stem}.{ext}', dpi=220)
    plt.close(fig)


def distribution(report):
    fig, ax = plt.subplots(figsize=(4.8, 3.8))
    for arm, label, color, ls, lw in ARMS:
        d = report['arms'][arm]
        # >= threshold is left-continuous: at each observed value, retain ties.
        ax.step(100*np.asarray(d['thresholds']), 100*np.asarray(d['passing_fractions']),
                where='pre', color=color, ls=ls, lw=lw, label=f"{label} (N={d['finite_n']})")
        ax.plot(90, 100*d['pointwise']['fraction'], 'o', ms=3, color=color, zorder=4)
    ax.axvline(90, color='0.3', lw=.9, ls='-.', zorder=1)
    ax.set(xlim=(0, 100), ylim=(0, 102), xticks=np.arange(0, 101, 20),
           yticks=np.arange(0, 101, 20), xlabel='Required pointwise agreement (%)',
           ylabel='Papers meeting requirement (%)')
    ax.legend(loc='lower center', bbox_to_anchor=(.5, 1.015), ncol=2,
              borderaxespad=0, fontsize=7.5, frameon=False, handlelength=1.8,
              columnspacing=1.2)
    fig.tight_layout()
    save(fig, 'pointwise_agreement_distribution')


def main():
    plt.rcParams.update({'font.size': 11, 'axes.grid': True, 'grid.alpha': .3,
                         'figure.dpi': 150, 'savefig.bbox': 'tight',
                         'pdf.fonttype': 42, 'ps.fonttype': 42, 'svg.fonttype': 'none'})
    report, _ = load_data()
    table(report)
    distribution(report)
    (OUT / 'results.json').write_text(json.dumps(report, indent=2) + '\n')
    for arm, d in report['arms'].items():
        print(arm, 'N', d['finite_n'], 'N_curve', d['curve_n'], 'pointwise', d['pointwise'], 'joint', d['joint'])
    print('All archived cohort, coverage, joint-success, per-type sum, and Figure 3 threshold checks passed.')


if __name__ == '__main__':
    main()
