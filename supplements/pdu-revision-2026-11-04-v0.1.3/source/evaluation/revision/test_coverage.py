import pytest

from .coverage import support, fraction, domain_flags


def test_extra_prediction_support_is_not_penalized():
    assert fraction([[0, 1]], [[-1, 2]]) == 1
    assert fraction([[0, 2]], [[0, 1]]) == .5


def test_explicit_gaps_are_not_bridged():
    p, _ = support([[1, 1], [10, 1], [float('nan'), float('nan')], [100, 1], [1000, 1]])
    assert p == [[0, 1], [2, 3]]
    assert fraction([[0, 3]], p) == pytest.approx(2/3)


def test_closed_contour_projects_once_onto_mass_axis():
    p, _ = support([[1, 2], [100, 2], [100, 3], [1, 3], [1, 2]])
    assert p == [[0, 2]]
    assert fraction([[0, 2]], p) == 1


def test_point_prediction_has_zero_interval_coverage():
    p, _ = support([[10, 2]])
    assert fraction([[0, 2]], p) == 0
    assert fraction([], [[0, 2]]) is None


def test_domain_screen_uses_reference_only_without_trimming():
    r, pieces = support([[1e-30, 1e-8], [1e-4, 1e-8], [1e-2, 1e-7]], reference=True)
    assert r == [[-30, -2]]
    assert domain_flags(pieces, 'PVLAS') == ['terminal_reference_spacing_at_least_3_dex']
    assert domain_flags([[0, 1, 2]], 'normal') == []


def test_reference_closure_marker_is_not_support():
    r, _ = support([[1, 1e-9], [10, 2e-9], [100, 1e20]], reference=True)
    assert r == [[0, 1]]


def test_reversed_curve_and_coupling_values_do_not_change_mass_coverage():
    r, _ = support([[100, 9], [10, 8], [1, 7]])
    p, _ = support([[1, 0], [100, 100000]])
    assert fraction(r, p) == 1
