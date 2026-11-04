import json
import math

import numpy as np
import pytest

from evaluation.revision.rescore import (
    HERE, ARMS, choose_reference, compare, qualifies, run, segments, strict_convert,
)

P = json.loads((HERE / "protocol.json").read_text())


def scored(pred, ref):
    return compare(segments(pred)[0], segments(ref)[0], P)


def test_partial_perfect_curve_is_not_success():
    c = scored([[1, 1e-5], [2, 1e-5]], [[1, 1e-5], [100, 1e-5]])
    assert c["forward"]["median_dex"] == 0
    assert c["forward"]["coverage"] == pytest.approx(math.log10(2) / 2)
    assert not qualifies(c, 2.0)


def test_excess_support_fails_reverse_coverage():
    c = scored([[1e-3, 1e-5], [1e3, 1e-5]], [[1, 1e-5], [10, 1e-5]])
    assert c["forward"]["coverage"] == pytest.approx(1)
    assert c["reverse"]["coverage"] == pytest.approx(1 / 6)
    assert not qualifies(c, 2.0)


def test_flat_narrow_limits_are_allowed():
    points = [[1, 1e-12], [1.001, 1e-12]]
    assert qualifies(scored(points, points), 1.1)


def test_point_output_cannot_claim_full_curve():
    c = scored([[2, 1e-12]], [[1, 1e-12], [10, 1e-12]])
    assert c["kind"] == "point_or_zero_span"
    assert not qualifies(c, 2.0)


def test_good_median_does_not_hide_bad_tail():
    c = scored([[1, 1e-5], [4, 1e-5], [4.01, 1e-3], [10, 1e-3]],
               [[1, 1e-5], [10, 1e-5]])
    assert c["forward"]["median_dex"] == 0
    assert c["forward"]["p90_dex"] > 1.9
    assert not qualifies(c, 2.0)


def test_vertex_density_does_not_change_weight():
    ref = [[1, 1e-5], [100, 1e-5]]
    dense_ref = [[x, 1e-5] for x in np.r_[np.linspace(1, 2, 1000), 100]]
    pred = [[1, 1e-5], [10, 1e-4], [100, 1e-3]]
    sparse, dense = scored(pred, ref), scored(pred, dense_ref)
    for direction in ("forward", "reverse"):
        assert sparse[direction]["median_dex"] == pytest.approx(dense[direction]["median_dex"], abs=1e-12)
        assert sparse[direction]["agreement"] == pytest.approx(dense[direction]["agreement"], abs=1e-12)


def test_exact_integral_linear_residual():
    c = scored([[1, 1e-6], [100, 1e-4]], [[1, 1e-6], [100, 1e-6]])
    m = c["forward"]
    assert m["median_dex"] == pytest.approx(1)
    assert m["p90_dex"] == pytest.approx(1.8)
    assert m["max_dex"] == pytest.approx(2)
    assert m["agreement"]["2.0"] == pytest.approx(math.log10(2) / 2)


def test_exact_integral_crosses_zero():
    c = scored([[1, 1e-7], [100, 1e-5]], [[1, 1e-6], [100, 1e-6]])
    assert c["forward"]["median_dex"] == pytest.approx(0.5)
    assert c["forward"]["agreement"]["2.0"] == pytest.approx(math.log10(2))


def test_explicit_gaps_are_not_bridged():
    ref = [[1, 1e-5], [2, 1e-5], [np.nan, np.nan], [20, 1e-5], [40, 1e-5]]
    c = scored([[1, 1e-5], [40, 1e-5]], ref)
    assert c["reverse"]["coverage"] == pytest.approx(2 * math.log10(2) / math.log10(40))
    assert not qualifies(c, 2.0)


def test_multibranch_is_not_silently_lower_enveloped():
    with pytest.raises(ValueError, match="multibranch"):
        segments([[1, 1e-5], [10, 1e-6], [1, 1e-3]])


def test_vertical_step_preserves_both_one_sided_limits():
    curve = [[1, 1e-6], [10, 1e-6], [10, 1e-3], [100, 1e-3]]
    parts, _ = segments(curve)
    assert len(parts) == 2
    c = scored([[1, 1e-6], [100, 1e-6]], curve)
    assert c["forward"]["agreement"]["2.0"] == pytest.approx(0.5)
    assert not qualifies(c, 2.0)
    assert qualifies(scored(curve, curve[::-1]), 1.1)


def test_closed_contour_is_detected_even_in_a_narrow_mass_window():
    with pytest.raises(ValueError, match="multibranch"):
        segments([[1, 1e-6], [1.001, 1e-6], [1.001, 1e-3], [1, 1e-3]])


def test_terminal_fill_wall_not_part_of_curve():
    parts, stats = segments([[1, 1e-4], [1, 1e-14], [2, 1e-14], [2, 1e-4]], reference=True)
    assert stats["terminal_closure_rows"] == 2
    assert qualifies(compare(parts, segments([[1, 1e-14], [2, 1e-14]])[0], P), 1.1)


def test_explicit_declaration_is_not_overridden_by_magnitude():
    a, note = strict_convert([[1, 1e-12]], "AxionMass", "f_a [GeV]")
    assert a[0, 1] == pytest.approx(1e12)
    assert "reciprocal" in note
    with pytest.raises(ValueError, match="axis_declaration_conflict"):
        strict_convert([[1, 1e-12]], "AxionElectron", "g_squared (axis read-back)")


def test_no_numerical_best_match():
    entries = [{"coupling_type": "DarkPhoton", "reference_repo_file": f"limit_data/DarkPhoton/{n}.txt"} for n in ("A", "B")]
    prediction = {"coupling_type": "DarkPhoton", "data_points": [[1, 1e-12]]}
    chosen, state, _ = choose_reference(entries, prediction, {}, "agent_fable")
    assert chosen is None and state == "identity_review"
    decision = {"select": {"agent_fable": entries[1]["reference_repo_file"]}, "evidence": "Figure label B"}
    chosen, state, _ = choose_reference(entries, prediction, decision, "agent_fable")
    assert chosen == entries[1] and state == "source_evidence_mapping"


def test_prediction_values_are_not_clipped_to_reference_ceiling():
    parts, _ = segments([[1, 2], [2, 3]], coupling="DarkPhoton")
    assert len(parts[0]) == 2


def test_reference_sentinel_breaks_support():
    parts, stats = segments([[1, 1e-6], [2, 1e-6], [3, 1e30], [4, 1e-6], [5, 1e-6]], reference=True)
    assert len(parts) == 2 and stats["removed_reference_rows"] == 1


def test_pointwise_threshold_includes_exact_factor_two():
    assert qualifies(scored([[1, 2e-6], [10, 2e-6]], [[1, 1e-6], [10, 1e-6]]), 2.0)


def test_infinite_coordinate_cannot_be_silently_dropped():
    with pytest.raises(ValueError, match="infinite"):
        segments([[1, 1e-6], [2, float("inf")], [10, 1e-6]])


def test_missing_predictions_keep_common_denominator_and_inputs_unchanged(tmp_path, monkeypatch):
    import socket
    monkeypatch.setattr(socket, "socket", lambda *a, **k: (_ for _ in ()).throw(AssertionError("network forbidden")))
    root = tmp_path / "inputs"
    (root / "data/ground_truth").mkdir(parents=True)
    entries = [{"arxiv_id": pid, "is_projection": False, "excluded": excluded,
                "coupling_type": "DarkPhoton", "coupling_convention": "epsilon",
                "ground_truth_data_file": f"{pid}.txt", "reference_repo_file": f"limit_data/DarkPhoton/{pid}.txt"}
               for pid, excluded in (("one", False), ("two", False), ("excluded", True))]
    (root / "data/papers.json").write_text(json.dumps({"papers": entries}))
    for e in entries:
        (root / "data/ground_truth" / e["ground_truth_data_file"]).write_text("1 1e-6\n10 1e-6\n")
    snap = root / ARMS["agent_fable"] / "one.json"
    snap.parent.mkdir(parents=True)
    snap.write_text(json.dumps({"coupling_type": "DarkPhoton", "coupling_convention": "kinetic mixing chi (dimensionless)",
                               "data_points": [[1, 1e-6], [10, 1e-6]], "is_new_limit": True}))
    before = {str(p): p.read_bytes() for p in root.rglob("*") if p.is_file()}
    out = tmp_path / "out"; out.mkdir()
    run(root, out, P, {})
    result = json.loads((out / "summary.json").read_text())
    assert all(s["denominator"] == 2 for s in result.values())
    assert result["agent_fable"]["qualified_matches"]["2.0"] == 1
    assert result["pipeline_fable"]["status_counts"]["missing_snapshot"] == 2
    assert before == {str(p): p.read_bytes() for p in root.rglob("*") if p.is_file()}
