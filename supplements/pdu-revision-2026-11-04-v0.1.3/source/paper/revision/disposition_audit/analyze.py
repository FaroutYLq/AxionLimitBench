"""Reproduce Table C.1 outcome counts from adopted archived Fable metrics."""
import hashlib
import json
import math
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
INPUTS = HERE.parent / 'figures/figure4_residual_cdf_preview/data'
report = {'scope': 'All 329 paper IDs in each adopted Fable 5 run; no rescoring.',
          'arms': {}}
id_sets = []
for arm in ('agent_fable', 'pipeline_fable'):
    source = INPUTS / f'{arm}_metrics.json'
    metrics = json.loads(source.read_text())
    rows = metrics['per_paper']
    ids = {row['arxiv_id'] for row in rows}
    assert len(rows) == len(ids) == 329
    id_sets.append(ids)
    cases = []
    for row in rows:
        status = row.get('comparison_status') or row.get('status')
        value = (row.get('interp_metrics') or {}).get('median_residual_dex')
        finite = isinstance(value, (int, float)) and math.isfinite(value)
        if status == 'compared':
            category = 'finite_comparison' if finite else 'no_comparable_mass_points'
            if not finite:
                im = row['interp_metrics']
                assert im['num_interpolatable'] == 0
                assert im.get('num_interpolatable_reverse', 0) == 0
        else:
            assert not finite
            assert status in {'excluded_gt', 'no_comparable_gt',
                              'convention_mismatch', 'no_extracted_points',
                              'gt_unusable'}
            category = status
        cases.append({'arxiv_id': row['arxiv_id'], 'outcome': category,
                      'archived_status': status,
                      'predicted_coupling': row.get('coupling_type_predicted')})
    counts = Counter(case['outcome'] for case in cases)
    assert sum(counts.values()) == 329
    report['arms'][arm] = {
        'input': str(source.relative_to(HERE.parent)),
        'input_sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
        'total': len(rows), 'counts': dict(counts), 'cases': cases}
assert id_sets[0] == id_sets[1]
(HERE / 'fable_outcomes.json').write_text(json.dumps(report, indent=2) + '\n')
for arm, result in report['arms'].items():
    print(arm, result['counts'], 'total', result['total'])
