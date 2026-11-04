import pytest

from .cohort_coverage import assess
from .ml4ps_coverage import above90, finish_row, summarize


def result(prediction, reference, median=.1, pointwise=1.):
    row = assess(prediction, reference, 'AxionPhoton', 'test.txt')
    row.update(archived_median_residual_dex=median,
               archived_fraction_within_0_3dex=pointwise)
    return finish_row(row)


def test_excess_range_fails_even_with_complete_reference_coverage():
    row = result([[.01, 1e-9], [10000, 1e-9]], [[1, 1e-9], [100, 1e-9]])
    assert row['reference_coverage'] == 1
    assert row['extraction_coverage'] == pytest.approx(1/3)
    assert not row['coverage_pass']


def test_exact_90_is_not_sufficient_and_roundoff_does_not_change_result():
    assert not above90(.9)
    assert not above90(.9+1e-14)
    assert above90(.900001)


def test_point_reference_excluded_but_collapsed_extraction_retained():
    excluded = result([[1, 1e-9], [100, 1e-9]], [[10, 1e-9]])
    failed = result([[10, 1e-9]], [[1, 1e-9], [100, 1e-9]])
    assert excluded['status'] == 'point_reference_excluded'
    assert failed['reference_coverage'] == 0
    assert failed['extraction_coverage'] is None
    assert not failed['excluded_from_coverage_denominator']
    summary = summarize([excluded, failed])
    assert summary['coverage_denominator'] == 1
    assert summary['both_gt90_n'] == 0


def test_good_median_does_not_hide_pointwise_tail():
    points = [[1, 1e-9], [100, 1e-9]]
    row = result(points, points, median=.01, pointwise=.8)
    assert row['sensitivity_joint_median']
    assert not row['joint_success']
    assert result(points, points, pointwise=.9)['joint_success']


def test_partial_reference_with_good_pointwise_agreement_is_not_joint_success():
    row = result([[1, 1e-9], [10, 1e-9]], [[1, 1e-9], [100, 1e-9]])
    assert row['reference_coverage'] == .5
    assert row['extraction_coverage'] == 1
    assert not row['joint_success']
