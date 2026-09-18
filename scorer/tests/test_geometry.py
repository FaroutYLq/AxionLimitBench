"""AxionLimitBench scorer geometry: closure chords, sparse references, wall vertices.

Run: python3 -m pytest scorer/tests -q   (or python3 scorer/tests/test_v02_geometry.py)
"""
import json
import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from scorer.metrics import (  # noqa: E402
    _lower_envelope_if_contour, _filter_boundary_keep_order, _filter_boundary,
    _strip_wall_vertices, _residuals_at, _ceil_for, compute_interpolation_metrics,
)


def _gt(aid):
    e = [x for x in json.loads((ROOT / "data/papers.json").read_text())["papers"] if x["arxiv_id"] == aid][0]
    return np.loadtxt(ROOT / "data/ground_truth" / e["ground_truth_data_file"], ndmin=2), e["coupling_type"]


def test_closure_chord_dropped_bbn():
    gt, ct = _gt("2002.08370")
    env = _lower_envelope_if_contour(_filter_boundary_keep_order(gt, _ceil_for(ct)), drop_chords=True)
    # the chord vertices (1e-14, 1e-20, 1e-28) are gone; the envelope is the traced curve
    assert env[:, 1].min() > 1e-12, env[:, 1].min()


def test_system_polygon_scored_as_emitted():
    # a system's 2-point flat segment inside its own polygon is NOT dropped as a chord
    d = np.array([[2e-18, 1e-8], [7e-17, 1e-8], [3e-17, 6.5e-11], [4e-17, 6.5e-11]])
    env = _lower_envelope_if_contour(_filter_boundary_keep_order(d, 1e-2))
    assert env[:, 0].min() <= 2e-18


def test_contour_band_still_reduced_2306_01048():
    # the case the envelope was written for: a genuine two-branch band
    gt, ct = _gt("2306.01048")
    f = _filter_boundary_keep_order(gt, _ceil_for(ct))
    env = _lower_envelope_if_contour(f, drop_chords=True)
    assert len(env) >= 10
    # lower envelope is <= every original point at the same mass
    for m, c in f:
        j = np.argmin(np.abs(env[:, 0] - m))
        if abs(np.log10(env[j, 0] / m)) < 1e-9:
            assert env[j, 1] <= c * (1 + 1e-9)


def test_monotonic_curve_untouched():
    d = np.array([[1e-6, 1e-12], [1e-5, 2e-12], [1e-4, 5e-12]])
    out = _lower_envelope_if_contour(d)
    assert np.allclose(out, d)


def test_sparse_reference_uses_curve_minimum_in_window():
    # dense resonance curve: minimum 1e-14 at 1.000e-5 eV, 100x weaker one linewidth away
    m = np.linspace(0.97e-5, 1.03e-5, 61)
    c = 1e-14 * (1 + ((m - 1.0e-5) / 0.002e-5) ** 2)
    curve = np.column_stack([m, c])
    ref = np.array([[1.1e-5, 1e-14]])  # headline quoted at a rounded mass, one window edge away
    res = _residuals_at(curve, ref, 0.3)
    assert res is not None and res[0] < 0.05, res


def test_sparse_reference_rule_not_applied_to_sparse_curve():
    curve = np.array([[1e-5, 1e-14], [2e-5, 1e-14]])  # 2-point flat bound: interpolate as before
    ref = np.array([[1.5e-5, 1e-13]])
    res = _residuals_at(curve, ref, 0.3)
    assert abs(res[0] - 1.0) < 1e-9


def test_wall_vertices_stripped():
    # ORGAN-style: 0.2 walls at both seams around a 5-point curve (main body >= 4)
    d = np.array([[1e-6, 0.2], [1e-6, 1e-12], [1.5e-6, 1.2e-12], [2e-6, 2e-12], [2.5e-6, 1.7e-12], [3e-6, 1.5e-12], [3e-6, 0.2]])
    out = _strip_wall_vertices(d)
    assert len(out) == 5 and out[:, 1].max() < 1e-11


def test_floor_chord_vertices_stripped():
    body = [[10 ** (5 + 0.3 * k), 1e-9 * 10 ** (-0.15 * k)] for k in range(10)]   # 10 traced vertices
    chord = [[body[-1][0], 1e-14], [1e9, 1e-20], [1e5, 1e-28]]                      # 3-vertex floor closure
    out = _strip_wall_vertices(np.array(body + chord))
    assert len(out) == 10 and out[:, 1].min() >= 1e-11


def test_wall_rule_keeps_real_structure():
    # a 3-decade resonance dip in the MIDDLE of a curve is data, not geometry
    d = np.array([[1e-6, 1e-12], [1.05e-6, 1e-12], [1.1e-6, 1e-12], [1.15e-6, 1e-15], [1.2e-6, 1e-12], [1.25e-6, 1e-12]])
    assert len(_strip_wall_vertices(d)) == 6


def test_small_file_with_walls_keeps_real_points():
    # fa/K40.txt shape: wall, point, point, wall; ceiling 1e0 removes walls, the 2 real points must survive
    d = np.array([[3e-23, 1.0], [3e-23, 1e-14], [9.6e-20, 3.2e-11], [9.6e-20, 1.0]])
    out = _filter_boundary(d, 1e0)
    assert len(out) == 2


def test_two_vertex_flat_reference_scores_best_in_window():
    # RADES-style: the curator stores the quoted best limit as a 2-vertex flat line across a
    # 3-MHz band; a faithful resonance curve is weakest at the band edges. AxionLimitBench scores the
    # curve's best value within the mass window (as for single-mass references), not the edges.
    from scorer.metrics import compute_interpolation_metrics
    gt = np.array([[34.6738e-6, 4e-13], [34.6771e-6, 4e-13], [34.6771e-6, 1.0]])
    m = np.linspace(34.6738e-6, 34.6771e-6, 41)
    g = 4.5e-13 * 10 ** (0.6 * np.abs(np.linspace(-1, 1, 41)))   # 4.5e-13 at centre, 1.8e-12 at the edges
    im = compute_interpolation_metrics("t", np.column_stack([m, g]), gt, coupling_type="AxionPhoton")
    assert im.median_residual_dex < 0.1, im.median_residual_dex


def test_wide_two_vertex_reference_still_interpolated():
    # a genuine two-point line spanning decades (a flat astrophysical bound) is NOT a quoted resonance
    from scorer.metrics import compute_interpolation_metrics
    gt = np.array([[1e-10, 1e-12], [1e-5, 1e-12]])
    m = np.logspace(-10, -5, 20); g = np.full(20, 3e-12)
    im = compute_interpolation_metrics("t", np.column_stack([m, g]), gt, coupling_type="AxionPhoton")
    assert abs(im.median_residual_dex - np.log10(3)) < 1e-6


if __name__ == "__main__":
    for name, fn in list(globals().items()):
        if name.startswith("test_"):
            fn(); print("ok", name)
