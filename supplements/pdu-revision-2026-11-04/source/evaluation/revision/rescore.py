"""Offline, conservative rescoring of archived AxionLimitBench outputs.

No extractor, network client, or legacy evaluate module is imported. Input
snapshots and references are read-only; outputs go to a separate directory.
Run: python -m evaluation.revision.rescore --benchmark-root ../AxionLimitBench
"""
from __future__ import annotations

import argparse
from collections import Counter, defaultdict
import hashlib
import json
import math
from pathlib import Path

import numpy as np

from .vendor import conventions as conv

HERE = Path(__file__).resolve().parent
ARMS = {
    "agent_fable": "results/agent_claude_code/fable5",
    "pipeline_fable": "results/aal_harness/fable5",
    "agent_opus": "results/agent_claude_code/opus48",
    "pipeline_opus": "results/aal_harness/opus48",
    "agent_haiku": "results/agent_claude_code/haiku45",
    "pipeline_haiku": "results/aal_harness/haiku45",
}
NAMES = {"agent_fable": "Agent / Fable 5", "pipeline_fable": "Pipeline / Fable 5",
         "agent_opus": "Agent / Opus 4.8", "pipeline_opus": "Pipeline / Opus 4.8",
         "agent_haiku": "Agent / Haiku 4.5", "pipeline_haiku": "Pipeline / Haiku 4.5"}


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def dump(path, value):
    path.write_text(json.dumps(value, indent=2, allow_nan=False) + "\n")


def reference_type(entry):
    directory = Path(entry.get("reference_repo_file") or "").parent.name
    return {"VectorB-L": "VectorBL", "fa": "AxionMass"}.get(
        directory, directory if directory in conv._CANONICAL else entry["coupling_type"])


def strict_convert(points, ct, declaration, *, reference_file=None, density=None):
    """Reuse formula vocabulary, never reinterpret a declaration by magnitude.

    The old formulas/parser are frozen in vendor/. Explicit reciprocal and
    squared declarations mean precisely that. Axis-rewritten declarations are
    conflicts; they cannot be disambiguated from final snapshots alone.
    """
    if reference_file is None and not declaration:
        raise ValueError("missing_convention")
    if reference_file is None and "axis read-back" in (declaration or "").lower():
        raise ValueError("axis_declaration_conflict")
    token = (conv.file_source_convention(reference_file, ct) if reference_file
             else conv.classify_reported_convention(ct, declaration))
    if token == conv.UNCONVERTIBLE:
        raise ValueError("unsupported_convention")
    arr = np.asarray(points, dtype=float).copy()
    mask = np.isfinite(arr).all(axis=1) & (arr > 0).all(axis=1)
    valid = arr[mask]
    if not len(valid):
        return arr, "no positive finite points"
    tok = (token or "").lower()
    if tok.endswith("_axis"):
        raise ValueError("axis_declaration_conflict")
    if tok == "f_a_gev":
        arr[mask, 1] = 1 / valid[:, 1]
        return arr, "declared f_a [GeV] -> reciprocal; no magnitude override"
    if ct in ("ScalarPhoton", "ScalarElectron", "ScalarNucleon", "ScalarBaryon") and tok in (
        "gev_inv_scalar", "ev_inv_scalar", "g_phi_gev_inv", "lambda_inv_gev", "lambda_scale_gev"
    ):
        # The legacy converter guesses Lambda versus 1/Lambda from magnitude.
        # Only unambiguous inverse-energy declarations can take this branch.
        label = (declaration or "").lower().replace(" ", "")
        if tok == "lambda_scale_gev":
            arr[mask, 1] = math.sqrt(2) * conv._M_PL_GEV / valid[:, 1]
            return arr, "explicit scalar scale in GeV -> reciprocal conversion"
        if not any(t in label for t in ("gev^-1", "gev^{-1}", "gev-1", "1/gev", "ev^-1", "ev^{-1}")):
            raise ValueError("scalar_scale_direction_ambiguous")
        arr[mask, 1] *= math.sqrt(2) * conv._M_PL_GEV * (1e9 if tok == "ev_inv_scalar" else 1)
        return arr, "explicit inverse-GeV scalar conversion; no magnitude direction choice"
    if ct == "AxionEDM" and tok in ("d_n_ecm", "d_n", "e*cm", "ecm"):
        if density is None or not math.isfinite(float(density)) or float(density) <= 0:
            raise ValueError("edm_density_missing")
        arr[mask, 1] = conv._K_DN_ECM * valid[:, 1] * valid[:, 0] * math.sqrt(0.4 / float(density))
        return arr, "EDM amplitude conversion with explicitly recorded density"
    converted, note = conv.to_canonical(ct, valid.tolist(), token)
    if note.startswith(conv.GUARD_REFUSED) or "mislabeled" in note or "compared raw" in note:
        raise ValueError("convention_requires_review")
    if len(converted) != len(valid):
        raise ValueError("conversion_changed_support")
    arr[mask] = converted
    return arr, note or "declared canonical / registry identity"


def segments(points, *, reference=False, coupling=None):
    """Keep contiguous, single-valued pieces; never invent cross-gap support.

    Reference closure sentinels and non-finite separators break the polyline.
    Predictions with nonpositive/invalid numeric rows fail, except NaN separator
    rows which can explicitly delimit pieces. Flat and narrow curves are valid.
    """
    arr = np.asarray(points, dtype=float)
    if arr.ndim != 2 or arr.shape[1] != 2 or not len(arr):
        raise ValueError("invalid_or_empty_curve")
    if np.isinf(arr).any():
        raise ValueError("infinite_coordinate")
    finite = np.isfinite(arr).all(axis=1)
    positive = (arr > 0).all(axis=1)
    if not reference and np.any(finite & ~positive):
        raise ValueError("nonpositive_prediction_coordinate")
    keep = finite & positive
    seam_removed = 0
    if reference:
        keep &= arr[:, 1] < 1e19
        if coupling in {"DarkPhoton", "VectorBL", "AxionMass", "AxionCPV", "MonopoleDipole",
                        "AxionPhoton", "AxionElectron", "AxionNeutron", "AxionProton", "AxionEDM"}:
            keep &= arr[:, 1] != 1.0
        # A polygon's vertical closure can have a finite, nonstandard height.
        # Remove only a terminal row at exactly the adjacent row's mass, with
        # coupling >=1000 times larger. This never inspects an extraction.
        valid_indices = np.flatnonzero(keep)
        for end in (valid_indices[:2], valid_indices[-2:][::-1]):
            if len(end) == 2:
                i, j = end
                if arr[i, 0] == arr[j, 0] and arr[i, 1] >= 1000 * arr[j, 1]:
                    keep[i] = False
                    seam_removed += 1
    groups = []
    for idx in np.split(np.arange(len(arr)), np.flatnonzero(~keep)):
        idx = idx[keep[idx]]
        if not len(idx):
            continue
        a = np.log10(arr[idx])
        steps = np.diff(a[:, 0])
        span = float(np.ptp(a[:, 0]))
        backward = min(float(steps[steps > 0].sum()), float(-steps[steps < 0].sum()))
        if span > 0 and backward > 0.05 * span + 1e-12:
            raise ValueError("multibranch_geometry_requires_review")
        if a[-1, 0] < a[0, 0]:
            a = a[::-1]  # preserve the sides of vertical jumps in reversed files
        a = a[np.argsort(a[:, 0], kind="stable")]
        # Exact repeated vertices add no information. A vertical jump has
        # zero log-mass measure: preserve its two one-sided limits rather than
        # averaging them or picking the more favorable coupling.
        a = a[np.r_[True, np.any(np.diff(a, axis=0) != 0, axis=1)]]
        cuts = np.flatnonzero(np.diff(a[:, 0]) == 0) + 1
        groups.extend(piece for piece in np.split(a, cuts) if len(piece))
    groups.sort(key=lambda a: a[0, 0])
    for a, b in zip(groups, groups[1:]):
        if a[-1, 0] > b[0, 0] + 1e-12:
            raise ValueError("overlapping_segments_require_review")
    if not groups:
        raise ValueError("no_usable_curve_points")
    return groups, {"input_points": len(arr), "removed_reference_rows": int((~keep).sum()),
                    "terminal_closure_rows": seam_removed, "segments": len(groups)}


def grid_on_support(parts, size):
    """Equal log-mass weight; each segment receives at least two midpoint cells."""
    total = sum(float(p[-1, 0] - p[0, 0]) for p in parts)
    if total <= 0:
        return np.array([]), np.array([]), np.array([])
    xx, yy, ww = [], [], []
    for p in parts:
        span = float(p[-1, 0] - p[0, 0])
        if span <= 0:
            continue
        n = max(2, int(math.ceil(size * span / total)))
        x = p[0, 0] + (np.arange(n) + 0.5) * span / n
        xx.extend(x); yy.extend(np.interp(x, p[:, 0], p[:, 1])); ww.extend([span / n] * n)
    return np.asarray(xx), np.asarray(yy), np.asarray(ww)


def evaluate_at(parts, x):
    values = np.full(len(x), np.nan)
    for p in parts:
        inside = (x >= p[0, 0] - 1e-12) & (x <= p[-1, 0] + 1e-12)
        values[inside] = np.interp(x[inside], p[:, 0], p[:, 1])
    return values


def weighted_quantile(vals, weights, q):
    if not len(vals):
        return None
    order = np.argsort(vals)
    return float(vals[order][np.searchsorted(np.cumsum(weights[order]), q * weights.sum(), side="left")])


def direction(target, other, size, factors):
    x, y, w = grid_on_support(target, size)
    if not len(x):
        return None
    pred = evaluate_at(other, x)
    ok = np.isfinite(pred)
    residuals = np.abs(pred[ok] - y[ok])
    weights = w[ok]
    span = float(w.sum())
    overlap = float(weights.sum())
    # Exact support coverage; numerical agreement uses weighted quadrature.
    intersection = sum(max(0.0, min(a[-1, 0], b[-1, 0]) - max(a[0, 0], b[0, 0]))
                       for a in target for b in other)
    return {"coverage": min(1.0, float(intersection / span)), "support_dex": span,
            "median_dex": weighted_quantile(residuals, weights, 0.5),
            "p90_dex": weighted_quantile(residuals, weights, 0.9),
            "max_grid_dex": float(residuals.max()) if len(residuals) else None,
            "agreement": {str(f): float(weights[residuals <= math.log10(f) + 1e-12].sum() / overlap)
                          if overlap else 0.0 for f in factors},
            "covered_and_accurate": {str(f): float(weights[residuals <= math.log10(f) + 1e-12].sum() / span)
                                    for f in factors}}


def compare_quadrature(pred, ref, protocol):
    fwd = direction(ref, pred, protocol["grid_size"], protocol["tolerances_factors"])
    rev = direction(pred, ref, protocol["grid_size"], protocol["tolerances_factors"])
    if fwd is None or rev is None:
        # Exact operating masses only: no nearest-mass rescue or invented
        # support. These residuals never contribute to full-curve matches.
        point_diagnostics = []
        for role, target, other in (("reference", ref, pred), ("prediction", pred, ref)):
            for part in target:
                if len(part) == 1:
                    value = evaluate_at(other, part[:, 0])[0]
                    point_diagnostics.append({"role": role, "log10_mass": float(part[0, 0]),
                        "residual_dex": abs(float(value - part[0, 1])) if np.isfinite(value) else None})
        return {"kind": "point_or_zero_span", "forward": fwd, "reverse": rev,
                "point_diagnostics": point_diagnostics}
    return {"kind": "curve", "forward": fwd, "reverse": rev}


def compare(pred, ref, protocol):
    """Integrate the log-linear polylines exactly over shared support.

    Between consecutive knots the signed log-coupling difference is linear.
    Its threshold crossings determine the exact interval measure within a
    factor tolerance. Vertical steps have zero measure. Quantiles invert this
    continuous measure by bisection; constant-error intervals retain their
    full probability mass. Coverage has no sampling error.
    """
    spans = [sum(float(p[-1, 0] - p[0, 0]) for p in parts) for parts in (ref, pred)]
    if min(spans) <= 0:
        return compare_quadrature(pred, ref, protocol)
    lengths, left, right = [], [], []
    for a in ref:
        for b in pred:
            lo, hi = max(a[0, 0], b[0, 0]), min(a[-1, 0], b[-1, 0])
            if hi <= lo:
                continue
            knots = np.unique(np.r_[lo, a[(a[:, 0] > lo) & (a[:, 0] < hi), 0],
                                    b[(b[:, 0] > lo) & (b[:, 0] < hi), 0], hi])
            difference = np.interp(knots, a[:, 0], a[:, 1]) - np.interp(knots, b[:, 0], b[:, 1])
            lengths.extend(np.diff(knots)); left.extend(difference[:-1]); right.extend(difference[1:])
    lengths, left, right = (np.asarray(x, dtype=float) for x in (lengths, left, right))
    overlap = float(lengths.sum())
    delta = right - left

    def measure(tolerance):
        flat = np.abs(delta) < 1e-15
        fraction = np.zeros(len(lengths))
        fraction[flat] = (np.abs(left[flat]) <= tolerance + 1e-12)
        changing = ~flat
        r0 = (-tolerance - left[changing]) / delta[changing]
        r1 = (tolerance - left[changing]) / delta[changing]
        fraction[changing] = np.maximum(0, np.minimum(1, np.maximum(r0, r1)) - np.maximum(0, np.minimum(r0, r1)))
        return float(lengths @ fraction)

    maximum = float(max(np.abs(left).max(), np.abs(right).max())) if overlap else None
    def quantile(q):
        if not overlap:
            return None
        lo, hi = 0.0, maximum
        if measure(0) >= q * overlap:
            return 0.0
        for _ in range(52):
            mid = (lo + hi) / 2
            if measure(mid) >= q * overlap:
                hi = mid
            else:
                lo = mid
        return float(hi)

    within = {str(f): measure(math.log10(f)) for f in protocol["tolerances_factors"]}
    base = {"median_dex": quantile(0.5), "p90_dex": quantile(0.9), "max_dex": maximum,
            "agreement": {f: v / overlap if overlap else 0.0 for f, v in within.items()}}
    return {"kind": "curve", **{key: dict(base, coverage=min(1.0, overlap / span), support_dex=span,
              covered_and_accurate={f: v / span for f, v in within.items()})
              for key, span in zip(("forward", "reverse"), spans)}}


def qualifies(comparison, factor, coverage=0.9, pointwise=0.9):
    if not comparison or comparison["kind"] != "curve":
        return False
    return all(comparison[d]["coverage"] + 1e-12 >= coverage
               and comparison[d]["agreement"][str(factor)] + 1e-12 >= pointwise
               for d in ("forward", "reverse"))


def choose_reference(entries, prediction, decision, arm):
    """No numerical arrays or residuals participate in selection."""
    if decision.get("withhold"):
        return None, "identity_review", decision["evidence"]
    eligible = [e for e in entries if reference_type(e) == prediction.get("coupling_type")]
    selected = decision.get("select", {}).get(arm)
    if selected:
        matches = [e for e in eligible if e.get("reference_repo_file") == selected]
        if len(matches) != 1 or not decision.get("evidence"):
            raise ValueError("invalid evidence-led reference decision")
        return matches[0], "source_evidence_mapping", decision["evidence"]
    if not eligible:
        return None, "no_reference_for_declared_type", "No exact-type reference; no automatic plane alias."
    if len(eligible) != 1:
        return None, "identity_review", "Multiple same-type references; no source-evidence mapping."
    return eligible[0], "unique_available_reference", "Unique same-type reference; physical scenario/version identity remains unverified."


def load_reference(path):
    try:
        return np.loadtxt(path, ndmin=2)
    except ValueError:
        return np.loadtxt(path, delimiter=",", ndmin=2)


def inventory(root, out):
    entries = json.loads((root / "data/papers.json").read_text())["papers"]
    groups = defaultdict(list)
    for e in entries:
        if not e["is_projection"] and not e.get("excluded"):
            groups[e["arxiv_id"]].append(e)
    # Inventory intentionally omits numerical coordinates and scores.
    rows = []
    for pid, es in sorted(groups.items()):
        if len(es) <= 1:
            continue
        row = {"arxiv_id": pid, "references": [{k: e.get(k) for k in
               ("reference_repo_file", "coupling_type", "paper_title", "notes", "confidence_level", "dm_density_assumed")}
               for e in es], "predictions": {}}
        for arm, rel in ARMS.items():
            path = root / rel / (pid.replace("/", "_") + ".json")
            if path.exists():
                p = json.loads(path.read_text())
                row["predictions"][arm] = {k: p.get(k) for k in
                    ("coupling_type", "suggested_experiment_name", "notes", "confidence_level", "dm_density_assumed")}
        rows.append(row)
    dump(out / "identity_inventory.json", rows)


def run(root, out, protocol, decisions):
    provenance = {}
    def track(path):
        rel = str(path.relative_to(root))
        if rel not in provenance:
            provenance[rel] = digest(path)
    registry = root / "data/papers.json"
    track(registry)
    for name in ("fable5_miss_audit_2x_A.json", "fable5_miss_audit_2x_B.json", "fable5_miss_audit_2x.md"):
        path = root / "results/agent_claude_code" / name
        if path.exists():
            track(path)
    raw = json.loads(registry.read_text())["papers"]
    groups = defaultdict(list)
    for e in raw:
        if not e["is_projection"]:
            groups[e["arxiv_id"]].append(e)
    ids = sorted(pid for pid, es in groups.items() if any(not e.get("excluded") for e in es))
    pool = {"measured_ids": sorted(groups), "evaluation_ids": ids,
            "excluded": [{"arxiv_id": pid, "reasons": [e.get("exclusion_reason") for e in groups[pid]]}
                         for pid in sorted(set(groups) - set(ids))]}
    records = []
    for arm, rel in ARMS.items():
        for pid in ids:
            record = {"arm": arm, "arxiv_id": pid, "comparison": None}
            records.append(record)
            path = root / rel / (pid.replace("/", "_") + ".json")
            if not path.exists():
                record["status"] = "missing_snapshot"; continue
            track(path)
            try:
                pred = json.loads(path.read_text())
            except (ValueError, OSError):
                record["status"] = "invalid_snapshot"; continue
            record["prediction_sha256"] = provenance[str(path.relative_to(root))]
            record["declared_type"] = pred.get("coupling_type")
            record["declaration"] = pred.get("coupling_convention")
            record["confidence"] = pred.get("extraction_confidence")
            if pred.get("error") or pred.get("status") == "error":
                record["status"] = "extraction_error"; continue
            if not pred.get("data_points") or pred.get("is_projection") or pred.get("is_new_limit") is False:
                record["status"] = "no_measured_curve"; continue
            es = [e for e in groups[pid] if not e.get("excluded")]
            chosen, identity, evidence = choose_reference(es, pred, decisions.get(pid, {}), arm)
            record.update(identity_status=identity, identity_evidence=evidence,
                          candidate_references=[e.get("reference_repo_file") for e in es])
            if chosen is None:
                record["status"] = identity; continue
            record["reference_file"] = chosen.get("reference_repo_file")
            ct = reference_type(chosen)
            expected = conv.canonical_convention(ct)[0]
            if chosen.get("coupling_convention") not in (None, expected):
                record["status"] = "reference_plane_review"; continue
            ref_path = root / "data/ground_truth" / (chosen.get("ground_truth_data_file") or "__missing__")
            if not ref_path.is_file():
                record["status"] = "reference_missing"; continue
            track(ref_path)
            try:
                r = load_reference(ref_path)
                # Sentinel removal must precede conversion and preserve gaps.
                rparts, rstats = segments(r, reference=True, coupling=ct)
                r = np.vstack([np.vstack([10 ** p, [[np.nan, np.nan]]]) for p in rparts])
                r, rnote = strict_convert(r, ct, None, reference_file=chosen["reference_repo_file"])
                rparts, _ = segments(r)
            except (ValueError, TypeError, IndexError, OverflowError) as exc:
                record.update(status="reference_review", reason=str(exc)); continue
            try:
                pparts, pstats = segments(pred["data_points"])
                p = np.vstack([np.vstack([10 ** p, [[np.nan, np.nan]]]) for p in pparts])
                p, pnote = strict_convert(p, ct, pred.get("coupling_convention"), density=pred.get("dm_density_assumed"))
                pparts, _ = segments(p)
            except (ValueError, TypeError, IndexError, OverflowError) as exc:
                record.update(status="prediction_review", reason=str(exc)); continue
            record.update(reference_geometry=rstats, prediction_geometry=pstats,
                          reference_conversion=rnote, prediction_conversion=pnote)
            comparison = compare(pparts, rparts, protocol)
            record.update(status="compared" if comparison["kind"] == "curve" else "point_diagnostic",
                          comparison=comparison)
    summary = {}
    for arm in ARMS:
        rows = [r for r in records if r["arm"] == arm]
        comparable = [r for r in rows if r["status"] == "compared"]
        finite = [r["comparison"]["forward"]["median_dex"] for r in comparable
                  if r["comparison"]["forward"]["median_dex"] is not None]
        success = {str(f): sum(qualifies(r["comparison"], f, protocol["coverage_min"], protocol["pointwise_fraction_min"]) for r in rows)
                   for f in protocol["tolerances_factors"]}
        summary[arm] = {"denominator": len(ids), "status_counts": dict(Counter(r["status"] for r in rows)),
                        "conditional_median_dex": float(np.median(finite)) if finite else None,
                        "n_finite": len(finite), "qualified_matches": success,
                        "coverage_only": sum(r["comparison"]["forward"]["coverage"] >= protocol["coverage_min"]
                                             and r["comparison"]["reverse"]["coverage"] >= protocol["coverage_min"]
                                             for r in comparable),
                        "sensitivity_factor2": [{"coverage": c, "pointwise": p,
                            "matches": sum(qualifies(r["comparison"], 2.0, c, p) for r in rows)}
                            for c in protocol["sensitivity_coverage"] for p in protocol["sensitivity_pointwise"]]}
    # Verify that source artifacts did not change while scoring.
    for rel, sha in provenance.items():
        if digest(root / rel) != sha:
            raise RuntimeError(f"Input changed during analysis: {rel}")
    dump(out / "pool.json", pool)
    dump(out / "per_paper.json", records)
    dump(out / "summary.json", summary)
    dump(out / "provenance.json", {"benchmark_root": str(root), "input_sha256": provenance,
         "analysis_sha256": {str(p.relative_to(HERE)): digest(p) for p in sorted(HERE.rglob("*"))
                             if p.is_file() and p.suffix in (".py", ".json") and "__pycache__" not in p.parts},
         "numpy_version": np.__version__})
    write_report(out, pool, records, summary, protocol)
    print(json.dumps(summary, indent=2))


def write_report(out, pool, records, summary, protocol):
    n = len(pool["evaluation_ids"])
    lines = ["# Offline revision evaluation", "", f"Protocol: `{protocol['version']}`. No model calls or re-extractions.", "",
             "**Coverage update:** the revised one-way coverage analysis is in [../coverage/report.md](../coverage/report.md). It supersedes the two-way coverage interpretation below; these original counts remain for audit.", "",
             f"Fixed pool: {n} papers from {len(pool['measured_ids'])} measured-paper IDs; {len(pool['excluded'])} papers have only previously excluded references.", "",
             "## Supported claim", "",
             "This retrospective analysis reports numerical agreement with assigned repository references on the subsets the evaluator can compare. It does not estimate overall extraction success. Reference identity, geometry and convention restrictions leave other cases unscored or point-only; these are reported separately and are not established extraction failures. The compared subsets differ between systems, so their conditional statistics do not establish a paired performance advantage.", "",
             "The combined coverage-and-agreement counts below are provisional diagnostics, not headline performance rates. Stored reference domains can include long low-mass extensions or multiple scientific targets. Requiring an extraction to cover those entire domains is not justified without an independently specified target interval and scenario. A unique available reference does not verify scenario, figure, confidence level or paper version.", "",
             "## Provisional numerical diagnostics", "",
             "A qualified match needs >=90% reference support coverage, >=90% prediction support coverage, and >=90% weighted pointwise agreement in each direction. Weight is uniform in log mass, not reference vertex count. Both directions must pass; no minimum-error selection or reverse-pass rescue is used. Flat and arbitrarily narrow curves are allowed.", "",
             "| Arm | Fixed N | Finite numerical comparisons | Conditional median dex | Provisional combined count at 10% | Provisional combined count at factor 2 |",
             "|---|---:|---:|---:|---:|---:|"]
    tex = [r"\begin{tabular}{@{}lrrrr@{}}", r"\toprule", r"System / model & Compared & Median [dex] & 10\% & Factor 2 \\", r"\midrule"]
    for arm, s in summary.items():
        a, b = s["qualified_matches"]["1.1"], s["qualified_matches"]["2.0"]
        med = s["conditional_median_dex"]
        label = f"{med:.3f}" if med is not None else "--"
        lines.append(f"| {NAMES[arm]} | {n} | {s['n_finite']} | {label} | {a}/{n} ({100*a/n:.1f}%) | {b}/{n} ({100*b/n:.1f}%) |")
        tex.append(f"{NAMES[arm]} & {s['n_finite']} & {label} & {a} ({100*a/n:.1f}\\%) & {b} ({100*b/n:.1f}\\%) \\\\")
    tex += [r"\bottomrule", r"\end{tabular}"]
    lines += ["", "## Coverage and comparison availability", "",
              "An eligible curve comparison means that both sides can be represented over nonzero mass intervals. It does not mean that either curve is complete, accurate, or even overlapping. Coverage below is computed from stored mass support; its scientific target remains provisional.", "",
              "| Arm | Eligible curve comparisons | Other cases | Median reference coverage | Median prediction coverage | Both coverages >=90% |",
              "|---|---:|---:|---:|---:|---:|"]
    for arm, s in summary.items():
        comparable = [r for r in records if r["arm"] == arm and r["status"] == "compared"]
        medians = [f"{100*np.median([r['comparison'][d]['coverage'] for r in comparable]):.1f}%" if comparable else "--"
                   for d in ("forward", "reverse")]
        lines.append(f"| {NAMES[arm]} | {len(comparable)} | {n-len(comparable)} | {medians[0]} | {medians[1]} | {s['coverage_only']}/{len(comparable)} |")
    lines += ["", "The Fable pipeline has 189 eligible curve comparisons and 102 other cases: 41 unresolved identities, 24 reference-geometry reviews, 14 prediction-geometry/convention reviews, 12 point-only diagnostics, 6 without an exact-type reference, and 5 without an eligible measured curve. Its 42 provisional combined passes must not be described as a 14.4% extraction success rate. Switching to 42/189 would still leave reference-domain and subset-selection problems unresolved.", "",
              "Examples of reference-domain problems: the PVLAS reference spans 1e-30 to 10 eV, versus the pipeline's 1e-4 to 1e-2 eV; the ALPS photon reference spans 1e-20 to 10 eV. These stored endpoints dominate log-mass coverage. The LUX reference contains a low-mass plateau followed by a keV-scale curve, while the prediction explicitly targets the galactic-ALP result. These cases require target-domain/scenario adjudication, not automatic extraction-failure labels."]
    lines += ["", "## Dispositions", "", "Unresolved identities, reference limitations, missing predictions and point-only results remain in the fixed denominator; they are not all demonstrated model errors.", ""]
    for arm, s in summary.items():
        lines += [f"- {NAMES[arm]}: `{json.dumps(s['status_counts'], sort_keys=True)}`"]
    lines += ["", "## Review ledger", "", "See `review_ledger.json` for every withheld comparison, its reason and candidate references. `identity_inventory.json` contains score-free metadata for multi-reference papers. Decisions are in `evaluation/revision/reference_decisions.json`.", "",
              "## Limits", "", "This is a retrospective reanalysis. The reference collection informed development and was itself amended after earlier model errors were examined. No independent test, human timing study, or guard-removal ablation is supplied. No lower envelope is silently chosen for a multibranch contour. Sparse point references are not treated as evidence of full-curve recovery. Unsupported geometry remains for review.", "",
              "Coverage is measured on the support represented by each saved polyline. Explicit gaps are preserved. Unrecorded gaps, scenario choices and source-version mismatches require source-level review. The two-point flat reference may be a quoted best limit rather than an exclusion curve; numerical agreement alone cannot establish which.", "",
              "The historical scorer used forward residuals when reference vertices overlapped, reverse residuals only when forward interpolation had no points, and then a sparse-point fallback. It selected the minimum residual among eligible same-type references. The new evaluator uses neither fallback nor numerical reference selection."]
    (out / "report.md").write_text("\n".join(lines) + "\n")
    (out / "comparison_table.tex").write_text("\n".join(tex) + "\n")
    macros = [f"\\newcommand{{\\RevisionPool}}{{{n}}}",
              f"\\newcommand{{\\RevisionMeasured}}{{{len(pool['measured_ids'])}}}",
              f"\\newcommand{{\\RevisionExcluded}}{{{len(pool['excluded'])}}}"]
    for arm, prefix in (("agent_fable", "RevisionAgent"), ("pipeline_fable", "RevisionPipeline")):
        s = summary[arm]
        macros += [f"\\newcommand{{\\{prefix}TwoN}}{{{s['qualified_matches']['2.0']}}}",
                   f"\\newcommand{{\\{prefix}TwoPct}}{{{100*s['qualified_matches']['2.0']/n:.1f}\\%}}"]
    (out / "numbers.tex").write_text("\n".join(macros) + "\n")
    dispositions = [r"\begin{tabular}{@{}lrr@{}}", r"\toprule",
                    r"Disposition (Fable 5) & Agent & Pipeline \\", r"\midrule"]
    def count_group(arm, group):
        s = summary[arm]
        if group == "qualified":
            return s["qualified_matches"]["2.0"]
        if group == "numerical":
            return s["status_counts"].get("compared", 0) - s["qualified_matches"]["2.0"]
        return sum(s["status_counts"].get(k, 0) for k in group)
    groups = [("Qualified numerical agreement (factor 2)", "qualified"),
              ("Compared, criterion not met", "numerical"),
              ("Reference identity unresolved", ["identity_review"]),
              ("No reference for declared coupling", ["no_reference_for_declared_type"]),
              ("Reference geometry/plane/data review", ["reference_review", "reference_plane_review", "reference_missing"]),
              ("Prediction geometry/convention review", ["prediction_review"]),
              ("Point-only diagnostic", ["point_diagnostic"]),
              ("Absent, invalid or no measured output", ["missing_snapshot", "invalid_snapshot", "extraction_error", "no_measured_curve"])]
    for label, group in groups:
        dispositions.append(f"{label} & {count_group('agent_fable', group)} & {count_group('pipeline_fable', group)} \\\\")
    dispositions += [r"\midrule", f"Total & {n} & {n} \\\\", r"\bottomrule", r"\end{tabular}"]
    (out / "disposition_table.tex").write_text("\n".join(dispositions) + "\n")
    dump(out / "review_ledger.json", [r for r in records if r["status"] != "compared"])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--benchmark-root", type=Path, required=True)
    parser.add_argument("--out", type=Path, default=Path("paper/revision/rescored"))
    parser.add_argument("--inventory-only", action="store_true")
    args = parser.parse_args()
    root, out = args.benchmark_root.resolve(), args.out.resolve()
    if out == root or root in out.parents:
        parser.error("Output must be outside the source benchmark checkout")
    out.mkdir(parents=True, exist_ok=True)
    inventory(root, out)
    if not args.inventory_only:
        run(root, out, json.loads((HERE / "protocol.json").read_text()),
            json.loads((HERE / "reference_decisions.json").read_text())["papers"])


if __name__ == "__main__":
    main()
