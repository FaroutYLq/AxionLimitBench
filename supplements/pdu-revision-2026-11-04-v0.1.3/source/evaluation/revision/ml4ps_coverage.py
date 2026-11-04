"""Agreed two-way coverage on frozen ML4PS finite-comparison cohorts.

No extractor calls. Keeps archived reference identities and pointwise scores.
Run in straxion with --benchmark-root pointing to the frozen snapshot or bundle.
"""
from __future__ import annotations

import argparse
from collections import Counter
import json
import math
from pathlib import Path

import numpy as np

from .cohort_coverage import assess, apply_special_cases, cohort
from .coverage import fraction
from .rescore import ARMS, NAMES, HERE, digest, dump, load_reference, reference_type

COMMIT = 'ac1542965b7c6b254238312a4d735d90c5a3a472'
EXPECTED = dict(agent_fable=281, agent_opus=271, agent_haiku=218,
                pipeline_fable=261, pipeline_opus=259, pipeline_haiku=222)
COVERAGE_TOLERANCE = 1e-12


def above90(value):
    # Equality within numerical roundoff does not satisfy the strict >90% rule.
    return value is not None and value > .9 + COVERAGE_TOLERANCE


def finish_row(row):
    """Apply the agreed point-reference exclusion and retain collapsed predictions."""
    row.setdefault('excluded_from_coverage_denominator', False)
    row.update(reference_coverage=None, extraction_coverage=None,
               coverage_pass=False, joint_success=False,
               sensitivity_joint_median=False)
    if row['status'] != 'measured':
        return row
    reference = row['reference_intervals_log10_eV']
    prediction = row['prediction_intervals_log10_eV']
    if not reference:
        row.update(status='point_reference_excluded', excluded_from_coverage_denominator=True,
                   exclusion_reason='No positive-length reference mass interval; interval coverage undefined.')
        return row
    cr = row['coverage']
    ce = fraction(prediction, reference) if prediction else None
    row.update(reference_coverage=cr, extraction_coverage=ce,
               collapsed_prediction=not bool(prediction),
               extraction_coverage_na_reason='No positive-length extracted interval' if ce is None else None)
    row['coverage_pass'] = above90(cr) and above90(ce)
    pointwise = row['archived_fraction_within_0_3dex']
    row['joint_success'] = row['coverage_pass'] and pointwise >= .9
    row['sensitivity_joint_median'] = row['coverage_pass'] and row['archived_median_residual_dex'] <= .3
    assert not row['joint_success'] or row['sensitivity_joint_median']
    return row


def summarize(rows):
    included = [r for r in rows if not r['excluded_from_coverage_denominator']]
    measured = [r for r in included if r['status'] == 'measured']
    n = len(included)
    result = {'finite_cohort_n': len(rows), 'coverage_denominator': n,
              'special_cases_excluded': sum(r['status'] == 'special_case_excluded' for r in rows),
              'point_references_excluded': sum(r['status'] == 'point_reference_excluded' for r in rows),
              'unresolved': sum(r['status'] == 'unresolved' for r in included),
              'collapsed_predictions_included': sum(r.get('collapsed_prediction', False) for r in included),
              'domain_flagged_included': sum(bool(r.get('domain_flags')) for r in included),
              'reference_gt90_n': sum(above90(r['reference_coverage']) for r in included),
              'extraction_gt90_n': sum(above90(r['extraction_coverage']) for r in included),
              'both_gt90_n': sum(r['coverage_pass'] for r in included),
              'joint_success_n': sum(r['joint_success'] for r in included),
              'sensitivity_joint_median_n': sum(r['sensitivity_joint_median'] for r in included),
              'pointwise90_without_coverage_n': sum(r['archived_fraction_within_0_3dex'] >= .9 for r in included),
              'median_without_coverage_n': sum(r['archived_median_residual_dex'] <= .3 for r in included)}
    for label in ('reference', 'extraction'):
        values = [r[f'{label}_coverage'] for r in measured if r[f'{label}_coverage'] is not None]
        result[f'{label}_defined_n'] = len(values)
        result[f'median_{label}_coverage'] = float(np.median(values)) if values else None
    for key in list(result):
        if key.endswith('_n') and key not in {'finite_cohort_n', 'reference_defined_n', 'extraction_defined_n'}:
            result[key[:-2]+'_fraction'] = result[key]/n if n else None
    assert n + result['special_cases_excluded'] + result['point_references_excluded'] == len(rows)
    assert len(measured) + result['unresolved'] == n
    return result


def reconciliation(old_rows, new_metrics):
    new_finite = {r['arxiv_id']: r for r in cohort(new_metrics)}
    new_all = {r['arxiv_id']: r for r in new_metrics['per_paper']}
    old = {r['arxiv_id']: r for r in old_rows}
    removed = []
    for pid in sorted(old.keys() - new_finite.keys()):
        row = new_all.get(pid, {})
        value = (row.get('interp_metrics') or {}).get('median_residual_dex')
        removed.append({'arxiv_id': pid, 'ml4ps_status': row.get('comparison_status', row.get('status')),
                        'ml4ps_finite_residual': value if value is not None and math.isfinite(value) else None,
                        'old_reference': old[pid].get('reference_file'),
                        'ml4ps_reference': row.get('gt_file')})
    changed_refs = [{'arxiv_id': pid, 'old_reference': old[pid]['reference_file'],
                     'ml4ps_reference': new_finite[pid]['gt_file']}
                    for pid in sorted(old.keys() & new_finite.keys())
                    if old[pid]['reference_file'] != new_finite[pid]['gt_file']]
    return {'old_finite_n': len(old), 'ml4ps_finite_n': len(new_finite),
            'removed': removed, 'added_ids': sorted(new_finite.keys()-old.keys()),
            'shared_n': len(old.keys() & new_finite.keys()),
            'shared_reference_changes': changed_refs}


def run(root, out, old_report):
    sources = {}
    def track(path):
        sources[str(path.relative_to(root))] = digest(path)
    registry = root/'data/papers.json'
    track(registry)
    entries = json.loads(registry.read_text())['papers']
    decisions = json.loads((HERE/'reference_decisions.json').read_text())['papers']
    old_rows = json.loads((old_report/'per_paper.json').read_text())
    records, manifests, comparisons = [], {}, {}
    for arm, folder in ARMS.items():
        metric_path = root/folder/'metrics.json'
        track(metric_path)
        metrics = json.loads(metric_path.read_text())
        members = cohort(metrics)
        assert len(members) == EXPECTED[arm], (arm, len(members))
        manifests[arm] = {'metrics_path': str(metric_path.relative_to(root)),
                          'metrics_sha256': digest(metric_path),
                          'finite_paper_ids': sorted(r['arxiv_id'] for r in members)}
        comparisons[arm] = reconciliation([r for r in old_rows if r['arm'] == arm], metrics)
        for member in members:
            pid, ref_file = member['arxiv_id'], member['gt_file']
            im = member['interp_metrics']
            pointwise = im['frac_within_0_3dex']
            assert math.isfinite(pointwise) and 0 <= pointwise <= 1
            row = {'arm': arm, 'arxiv_id': pid, 'reference_file': ref_file,
                   'reference_assignment': 'Frozen ML4PS selected reference; no new residual selection',
                   'comparison_coupling': member.get('comparison_coupling'),
                   'scored_via': member.get('scored_via'),
                   'archived_median_residual_dex': im['median_residual_dex'],
                   'archived_fraction_within_0_3dex': pointwise,
                   'archived_comparable_points': im['num_interpolatable'],
                   'identity_note': decisions.get(pid, {}).get('evidence')}
            candidates = [e for e in entries if e['arxiv_id'] == pid and e.get('reference_repo_file') == ref_file]
            targets = {(e.get('ground_truth_data_file'), reference_type(e)) for e in candidates}
            if not candidates or len(targets) != 1:
                raise ValueError(f'Ambiguous frozen reference: {arm} {pid}')
            entry = candidates[0]
            ref_path = root/'data/ground_truth'/(entry.get('ground_truth_data_file') or '__missing__')
            if not ref_path.is_file():
                ref_path = root/ref_file
            pred_path = root/folder/(pid.replace('/', '_')+'.json')
            track(ref_path); track(pred_path)
            prediction = json.loads(pred_path.read_text())
            row.update(assess(prediction.get('data_points', []), load_reference(ref_path),
                              reference_type(entry), ref_file))
            records.append(row)
    special_cases = json.loads((HERE/'coverage_special_cases.json').read_text())['cases']
    apply_special_cases(records, special_cases)
    records = [finish_row(r) for r in records]
    summary = {}
    for arm in ARMS:
        rows = [r for r in records if r['arm'] == arm]
        summary[arm] = summarize(rows)
        manifests[arm].update(coverage_denominator=summary[arm]['coverage_denominator'],
            included_ids=sorted(r['arxiv_id'] for r in rows if not r['excluded_from_coverage_denominator']),
            special_case_ids=sorted(r['arxiv_id'] for r in rows if r['status']=='special_case_excluded'),
            point_reference_ids=sorted(r['arxiv_id'] for r in rows if r['status']=='point_reference_excluded'))
    for rel, sha in sources.items():
        assert digest(root/rel) == sha, f'Input changed during evaluation: {rel}'
    out.mkdir(parents=True, exist_ok=True)
    dump(out/'per_paper.json', records)
    dump(out/'summary.json', summary)
    dump(out/'cohorts.json', manifests)
    dump(out/'cohort_reconciliation.json', comparisons)
    dump(out/'excluded_cases.json', [r for r in records if r['excluded_from_coverage_denominator']])
    dump(out/'protocol.json', {
        'coverage': 'Intersection length / reference or extraction support length, uniformly in log10 mass.',
        'coverage_pass': 'Both C_ref > 0.9 and C_ext > 0.9; equality within 1e-12 does not pass.',
        'exclusions': 'Only ten previously approved special cases and point-only references.',
        'point_prediction': 'Retained; C_ref=0, C_ext undefined, coverage pass=False.',
        'approved_pointwise': 'At least 90% of archived comparable points have residual <=0.3 dex.',
        'sensitivity_median': 'Archived median residual <=0.3 dex.',
        'criterion_status': 'User approved: both coverages >90% and at least 90% of compared points within 0.3 dex. Median-only variant is sensitivity analysis.',
        'pointwise_weighting': 'Original discrete interpolation sample weighting, not uniform log-mass weighting.',
        'direction': 'Archived effective forward score, with reverse or sparse-point fallback as recorded; no directional pooling.',
        'cohort': 'Finite ML4PS comparisons only; conditional on comparison, not end-to-end success.',
        'reference_sanitation': 'Unchanged support() policy from the previous agreed coverage calculation.',
        'reference_flags': 'Annotations only; no clipping or additional exclusions.'})
    dump(out/'provenance.json', {'benchmark_commit': COMMIT, 'input_sha256': sources,
        'analysis_sha256': {str(p.relative_to(HERE)): digest(p) for p in sorted(HERE.rglob('*.py'))},
        'old_cohort_audit_sha256': digest(old_report/'per_paper.json'),
        'special_case_policy_sha256': digest(HERE/'coverage_special_cases.json')})
    write_report(out, summary, comparisons)
    return summary


def write_report(out, summary, comparisons):
    lines = ['# ML4PS coverage and approved joint success', '',
        'This supersedes the original-PDU-cohort coverage report. All six configurations use the frozen ML4PS metrics at commit '+COMMIT+'. No model calls or new extractions were made. Figures 4 and 5 use these same finite residual cohorts; Figure 4 normalizes its CDF by the larger scorable pool.', '',
        'Coverage is the intersection of archived reference and extracted mass supports, divided by each support length separately, measured in log mass. Both coverages must be strictly >90%; values within 1e-12 of equality do not pass. Reference-domain flags are annotations only. The ten approved special cases and point-only references are the only coverage exclusions. All excluded IDs remain in excluded_cases.json.', '',
        '| Configuration | Finite cohort | Special exclusions | Point-reference exclusions | Curve denominator | Unresolved |',
        '|---|---:|---:|---:|---:|---:|']
    for arm,s in summary.items():
        lines.append(f"| {NAMES[arm]} | {s['finite_cohort_n']} | {s['special_cases_excluded']} | {s['point_references_excluded']} | {s['coverage_denominator']} | {s['unresolved']} |")
    lines += ['', '## Coverage results', '',
        '| Configuration | Reference >90% | Extraction >90% | Both >90% | Median reference coverage | Median extraction coverage |',
        '|---|---:|---:|---:|---:|---:|']
    def cell(s,key):
        n=s[key];d=s['coverage_denominator'];return f'{n}/{d} ({100*n/d:.1f}%)'
    for arm,s in summary.items():
        lines.append(f"| {NAMES[arm]} | {cell(s,'reference_gt90_n')} | {cell(s,'extraction_gt90_n')} | {cell(s,'both_gt90_n')} | {100*s['median_reference_coverage']:.1f}% | {100*s['median_extraction_coverage']:.1f}% |")
    lines += ['', 'Point-only predictions against extended references remain in the denominator: reference coverage is zero, extraction coverage is undefined, and the joint coverage requirement fails. Extraction-coverage medians use defined values only; their sample counts are in summary.json. The success fractions above keep the full curve denominator.', '',
        '## Approved joint success and median-only sensitivity', '',
        'The approved criterion requires both coverage tests and at least 90% of archived comparable samples within 0.3 dex (approximately a factor of two), on the same paper and same frozen reference. The median-only variant is retained as a sensitivity comparison, not as the adopted success definition. Neither is an end-to-end rate: the denominator already conditions on a finite comparison. Original interpolation sampling weights are retained; 90% of points is not a claim about 90% of log-mass length. Forward/reverse directions are not averaged or pooled.', '',
        '| Configuration | Both coverages + median <=0.3 dex | Approved: both coverages + >=90% points within 0.3 dex | Difference (papers) |',
        '|---|---:|---:|---:|']
    for arm,s in summary.items():
        lines.append(f"| {NAMES[arm]} | {cell(s,'sensitivity_joint_median_n')} | {cell(s,'joint_success_n')} | {s['sensitivity_joint_median_n']-s['joint_success_n']} |")
    lines += ['', '## Cohort reconciliation', '',
        'The old and ML4PS archives have different scoring/reference versions. The following records membership changes without attributing every change to a single cause. The new metrics and reference assignment are authoritative throughout this report. Full removed-paper statuses, added IDs, and changed selected references are in cohort_reconciliation.json.', '',
        '| Configuration | Old finite N | Removed | Added | ML4PS finite N | Shared papers with changed selected reference |',
        '|---|---:|---:|---:|---:|---:|']
    for arm,c in comparisons.items():
        lines.append(f"| {NAMES[arm]} | {c['old_finite_n']} | {len(c['removed'])} | {len(c['added_ids'])} | {c['ml4ps_finite_n']} | {len(c['shared_reference_changes'])} |")
    lines += ['', '## Reproduction', '',
        'Run in conda straxion: `python -m evaluation.revision.ml4ps_coverage --benchmark-root PATH_TO_SNAPSHOT`. The selected inputs are bundled in `paper/revision/ml4ps_coverage_inputs.tar.gz`; extract it and pass its `benchmark/` directory. Pass `--old-report EXTRACTED/old_cohort` to use the bundled previous cohort audit. No manuscript edits are made.']
    (out/'report.md').write_text('\n'.join(lines)+'\n')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--benchmark-root', type=Path, required=True)
    parser.add_argument('--out', type=Path, default=Path('paper/revision/ml4ps_coverage'))
    parser.add_argument('--old-report', type=Path, default=Path('paper/revision/cohort_coverage'))
    args = parser.parse_args()
    root, out = args.benchmark_root.resolve(), args.out.resolve()
    if root == out or root in out.parents:
        parser.error('Output must be outside the input snapshot')
    result = run(root, out, args.old_report.resolve())
    for arm,s in result.items():
        print(arm, json.dumps(s))
