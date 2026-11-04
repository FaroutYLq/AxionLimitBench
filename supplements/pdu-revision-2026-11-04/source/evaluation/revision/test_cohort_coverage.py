from .cohort_coverage import assess, cohort, apply_special_cases


def test_cohort_retains_all_original_finite_comparisons():
    rows = [{'arxiv_id': str(i), 'comparison_status': 'compared',
             'interp_metrics': {'median_residual_dex': v}} for i, v in enumerate([0, 9, float('inf'), None])]
    assert [r['arxiv_id'] for r in cohort({'per_paper': rows})] == ['0', '1']


def test_domain_flags_do_not_exclude_or_clip():
    r = assess([[1e-4, 1e-9], [1e-2, 1e-9]], [[1e-30, 1e-9], [1e-4, 1e-9], [1e-2, 1e-9]], 'AxionPhoton', 'PVLAS')
    assert r['status'] == 'measured'
    assert r['coverage'] == 2/28
    assert r['domain_flags']


def test_discrete_reference_is_assessed_without_invented_window():
    r = assess([[1, 1e-9], [100, 1e-9]], [[10, 1e-9]], 'AxionPhoton', 'point')
    assert r['coverage'] == 1
    assert r['kind'] == 'discrete_reference_masses'
    r = assess([[1, 1e-9], [5, 1e-9]], [[10, 1e-9]], 'AxionPhoton', 'point')
    assert r['coverage'] == 0


def test_invalid_mass_is_unresolved_not_dropped_or_assigned_zero():
    r = assess([[0, 1e-9]], [[1, 1e-9], [10, 1e-9]], 'AxionPhoton', 'reference')
    assert r['status'] == 'unresolved'
    assert r['coverage'] is None


def test_only_explicit_paper_model_cases_are_excluded():
    rows = [{'arm': arm, 'arxiv_id': '1', 'status': 'unresolved', 'coverage': None,
             'reason': 'prediction_coordinates: invalid_mass_or_nonfinite_coordinate'}
            for arm in ('pipeline_fable', 'agent_fable')]
    apply_special_cases(rows, [{'arm': 'pipeline_fable', 'arxiv_id': '1', 'label': 'test', 'reason': 'zero sentinel'}])
    assert rows[0]['status'] == 'special_case_excluded'
    assert rows[1]['status'] == 'unresolved'
    assert len(rows) == 2
