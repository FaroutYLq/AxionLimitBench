"""Coverage for every paper in the original reported finite-comparison cohorts.

The pipeline cohorts are Table 2 of the PDU paper. Agent cohorts come from
the available AxionLimitBench metrics. Ten explicitly approved special cases
remain in the audit but are excluded from coverage denominators.
"""
from __future__ import annotations

import argparse
from collections import Counter
import json
import math
from pathlib import Path

import numpy as np

from .coverage import support, fraction, domain_flags
from .rescore import HERE, NAMES, digest, dump, load_reference, reference_type

PIPELINE = {'fable': 'final347_fable', 'opus': 'final347_remediated', 'haiku': 'final2_haiku_n1'}
AGENT = {'fable': 'fable5', 'opus': 'opus48', 'haiku': 'haiku45'}
EXPECTED = {'pipeline_fable': 267, 'pipeline_opus': 265, 'pipeline_haiku': 229,
            'agent_fable': 281, 'agent_opus': 271, 'agent_haiku': 218}
REQUESTED = {**EXPECTED, 'agent_fable': 283, 'agent_opus': 272, 'agent_haiku': 219}


def cohort(metrics):
    rows = []
    for row in metrics['per_paper']:
        med = (row.get('interp_metrics') or {}).get('median_residual_dex')
        if row.get('comparison_status') == 'compared' and med is not None and math.isfinite(med):
            rows.append(row)
    if len({r['arxiv_id'] for r in rows}) != len(rows):
        raise ValueError('Duplicate paper in cohort')
    return rows


def assess(prediction, reference, ct, ref_file):
    """Flags annotate the result; they never remove a member or change its score."""
    try:
        ref_support, ref_points = support(reference, reference=True, coupling=ct)
    except (ValueError, TypeError, IndexError) as exc:
        return {'status': 'unresolved', 'reason': 'reference_coordinates: '+str(exc), 'coverage': None}
    flags = domain_flags(ref_points, ref_file)
    try:
        pred_support, pred_points = support(prediction)
    except (ValueError, TypeError, IndexError) as exc:
        return {'status': 'unresolved', 'reason': 'prediction_coordinates: '+str(exc), 'coverage': None,
                'domain_flags': flags}
    if ref_support:
        value, kind = fraction(ref_support, pred_support), 'log_mass_interval'
    else:
        targets = sorted({x for piece in ref_points for x in piece})
        ppoints = {x for piece in pred_points for x in piece}
        hits = sum(any(a-1e-12 <= x <= b+1e-12 for a, b in pred_support)
                   or any(abs(x-y) <= 1e-12 for y in ppoints) for x in targets)
        value, kind = hits / len(targets), 'discrete_reference_masses'
    return {'status': 'measured', 'coverage': value, 'kind': kind, 'domain_flags': flags,
            'reference_intervals_log10_eV': ref_support, 'prediction_intervals_log10_eV': pred_support,
            'reference_mass_points_log10_eV': ref_points if not ref_support else None}


def apply_special_cases(records, cases):
    lookup = {(r['arm'], r['arxiv_id']): r for r in records}
    if len({(c['arm'], c['arxiv_id']) for c in cases}) != len(cases):
        raise ValueError('Duplicate special-case exclusion')
    for case in cases:
        row = lookup[(case['arm'], case['arxiv_id'])]
        if row['status'] != 'unresolved' or row.get('reason') != 'prediction_coordinates: invalid_mass_or_nonfinite_coordinate':
            raise ValueError('Special-case source outcome changed; review the explicit exclusion')
        row.update(status='special_case_excluded', excluded_from_coverage_denominator=True,
                   special_case_label=case['label'], special_case_reason=case['reason'])


def run(pipeline_root, agent_root, out):
    records, manifests, sources = [], {}, {}
    decisions = json.loads((HERE/'reference_decisions.json').read_text())['papers']
    def track(path, root, source):
        sources[source+':'+str(path.relative_to(root))] = digest(path)
    for system, model_dirs, root in [('pipeline', PIPELINE, pipeline_root), ('agent', AGENT, agent_root)]:
        registry = root / ('evaluation/ground_truth/papers.json' if system == 'pipeline' else 'data/papers.json')
        track(registry, root, system)
        entries = json.loads(registry.read_text())['papers']
        for model, folder in model_dirs.items():
            arm = system+'_'+model
            directory = root / ('evaluation/eval_runs/'+folder if system == 'pipeline' else 'results/agent_claude_code/'+folder)
            metric_path = directory / ('metrics_noproj.json' if system == 'pipeline' else 'metrics.json')
            track(metric_path, root, system)
            members = cohort(json.loads(metric_path.read_text()))
            if len(members) != EXPECTED[arm]:
                raise ValueError(f'{arm}: cohort count changed, expected {EXPECTED[arm]}, found {len(members)}')
            manifests[arm] = {'requested_count': REQUESTED[arm], 'verified_count': len(members),
                              'metrics_path': str(metric_path.relative_to(root)), 'metrics_sha256': digest(metric_path),
                              'paper_ids': sorted(r['arxiv_id'] for r in members)}
            for member in members:
                pid, ref_file = member['arxiv_id'], member.get('gt_file')
                row = {'arm': arm, 'arxiv_id': pid, 'reference_file': ref_file,
                       'reference_assignment': 'frozen original evaluation assignment; no new residual selection',
                       'identity_note': decisions.get(pid, {}).get('evidence'), 'coverage': None}
                records.append(row)
                candidates = [e for e in entries if e['arxiv_id'] == pid and e.get('reference_repo_file') == ref_file]
                targets = {(e.get('ground_truth_data_file'), reference_type(e)) for e in candidates}
                if not candidates or len(targets) != 1:
                    row.update(status='unresolved', reason='archived_reference_mapping_not_unique'); continue
                entry = candidates[0]
                row['equivalent_registry_entries'] = len(candidates)
                ref_path = root / ('evaluation/ground_truth/data' if system == 'pipeline' else 'data/ground_truth') / (entry.get('ground_truth_data_file') or '__missing__')
                if not ref_path.is_file():
                    # The original evaluator falls back to this same-version
                    # repository reference when no cached GT data file exists.
                    ref_path = root / ref_file
                pred_path = directory / (pid.replace('/', '_')+'.json')
                if not ref_path.is_file() or not pred_path.is_file():
                    row.update(status='unresolved', reason='missing_source_file'); continue
                track(ref_path, root, system); track(pred_path, root, system)
                try:
                    pred = json.loads(pred_path.read_text())
                    ref = load_reference(ref_path)
                    row.update(assess(pred.get('data_points', []), ref, reference_type(entry), ref_file))
                except (ValueError, TypeError, IndexError) as exc:
                    row.update(status='unresolved', reason='source_read: '+str(exc))
    special_cases = json.loads((HERE/'coverage_special_cases.json').read_text())['cases']
    apply_special_cases(records, special_cases)
    summary = {}
    for arm, manifest in manifests.items():
        rows = [r for r in records if r['arm'] == arm]
        values = [r['coverage'] for r in rows if r['coverage'] is not None]
        high = sum(v+1e-12 >= .9 for v in values)
        n = len(rows)
        excluded = sum(r['status'] == 'special_case_excluded' for r in rows)
        denominator, unknown = n-excluded, n-excluded-len(values)
        manifest['special_case_excluded_ids'] = sorted(r['arxiv_id'] for r in rows if r['status'] == 'special_case_excluded')
        manifest['coverage_denominator'] = denominator
        summary[arm] = {'cohort_n': n, 'special_cases_excluded': excluded, 'coverage_denominator': denominator,
                        'coverage_ge90': high, 'coverage_lt90': len(values)-high,
                        'unresolved': unknown, 'fraction_ge90_of_full_cohort': high/n,
                        'fraction_ge90_of_coverage_denominator': high/denominator,
                        'fraction_ge90_upper_if_all_unresolved_pass': (high+unknown)/denominator,
                        'median_measured_coverage': float(np.median(values)) if values else None,
                        'domain_flagged_included': sum(bool(r.get('domain_flags')) for r in rows),
                        'kinds': dict(Counter(r.get('kind', r['status']) for r in rows)),
                        'unresolved_reasons': dict(Counter(r['reason'] for r in rows if r['status']=='unresolved'))}
        assert high + summary[arm]['coverage_lt90'] + unknown + excluded == n == manifest['verified_count']
    out.mkdir(parents=True, exist_ok=True)
    dump(out/'cohorts.json', manifests)
    dump(out/'per_paper.json', records)
    dump(out/'summary.json', summary)
    dump(out/'special_cases.json', [r for r in records if r['status'] == 'special_case_excluded'])
    dump(out/'provenance.json', {'pipeline_commit': 'ff26c6407bd6756a27ed5259583d96af983cc7be',
         'agent_commit': 'ac1542965b7c6b254238312a4d735d90c5a3a472', 'input_sha256': sources,
         'analysis_sha256': {str(p.relative_to(HERE)): digest(p) for p in HERE.rglob('*.py')},
         'identity_annotation_sha256': digest(HERE/'reference_decisions.json'),
         'special_case_policy_sha256': digest(HERE/'coverage_special_cases.json')})
    lines = ['# Coverage on the original reported cohorts', '',
             'Every paper in each original finite-residual cohort is retained in the audit. Pipeline membership is taken from the exact metrics used for Table 2 (267/265/229). Available agent metrics and the ML4PS numbers.tex verify 281/271/218, rather than the tentative 283/272/219. At the user\'s explicit request, the ten listed zero-mass special cases are excluded from coverage denominators only. No other screening exclusions are applied.', '',
             'Coverage = overlap with the archived reference mass support / archived reference mass support, uniformly in log mass. Extra prediction range is not penalized. A reference containing only discrete masses is assessed by the fraction of those masses covered; this is labelled separately in per_paper.json. Coupling accuracy is not measured here.', '',
             '**Interpretation:** these are literal archived-reference coverage diagnostics. The historically chosen reference is retained, including any bias from the old reference-selection procedure. Long reference extensions, mixed targets and prior identity concerns are annotations rather than exclusions. They can make coverage low without establishing an extraction failure. This report does not certify recovery of the scientifically intended domain. Reference closure sanitation follows coverage.py; explicit gaps are retained. Closed contours are projected onto mass support, not scored as recovered areas.', '',
             '| Configuration | Original cohort | Special cases excluded | Coverage denominator | Coverage >=90% | Coverage <90% | Unresolved | >=90% / coverage denominator |',
             '|---|---:|---:|---:|---:|---:|---:|---:|']
    for arm, s in summary.items():
        lines.append(f"| {NAMES[arm]} | {s['cohort_n']} | {s['special_cases_excluded']} | {s['coverage_denominator']} | {s['coverage_ge90']} | {s['coverage_lt90']} | {s['unresolved']} | {100*s['fraction_ge90_of_coverage_denominator']:.1f}% |")
    lines += ['', 'The three outcome columns sum to the coverage denominator; adding the special cases recovers the original cohort. These are coverage fractions, not end-to-end extraction success rates. The original cohorts already condition on finite residuals. Any future unresolved case stays in the denominator unless explicitly authorized for exclusion.', '',
              '## Excluded special cases', '',
              'Ten paper-model cases, representing eight distinct papers, are excluded. This is a representation/domain exception, not an extraction-failure classification. The original saved outputs remain unchanged.', '',
              '| Configuration | arXiv ID | Result | Reason |', '|---|---|---|---|']
    for case in special_cases:
        lines.append(f"| {NAMES[case['arm']]} | {case['arxiv_id']} | {case['label']} | {case['reason']} |")
    lines += ['',
              '## Reference-domain flags and medians', '',
              '| Configuration | Domain-flagged papers retained | Median among measured coverage values |', '|---|---:|---:|']
    for arm, s in summary.items():
        lines.append(f"| {NAMES[arm]} | {s['domain_flagged_included']} | {100*s['median_measured_coverage']:.1f}% |")
    lines += ['', 'Terminal reference mass spacing >=3 decades and the mixed LUX target trigger annotations only; no additional clipping or exclusion is performed. The median uses measured coverage values; excluding the ten previously unresolved special cases does not change it.', '',
              '## Reproduce', '',
              'Run in straxion: `python -m evaluation.revision.cohort_coverage --pipeline-root PATH_TO_AUTOAXIONLIMITS_SNAPSHOT --agent-root PATH_TO_AXIONLIMITBENCH_SNAPSHOT`. No model calls or new extractions. The source hashes and exact paper IDs are recorded. Earlier reports using 291 or screened subsets are superseded for cohort coverage.']
    (out/'report.md').write_text('\n'.join(lines)+'\n')


if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--pipeline-root', type=Path, required=True)
    p.add_argument('--agent-root', type=Path, required=True)
    p.add_argument('--out', type=Path, default=Path('paper/revision/cohort_coverage'))
    args = p.parse_args()
    for root in (args.pipeline_root.resolve(), args.agent_root.resolve()):
        if args.out.resolve() == root or root in args.out.resolve().parents:
            p.error('Output must be outside source snapshots')
    run(args.pipeline_root.resolve(), args.agent_root.resolve(), args.out.resolve())
