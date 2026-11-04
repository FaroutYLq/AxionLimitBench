"""One-way mass coverage of archived outputs; no extraction or model calls."""
from __future__ import annotations

import argparse
from collections import Counter, defaultdict
import json
from pathlib import Path

import numpy as np

from .rescore import ARMS, NAMES, HERE, choose_reference, digest, dump, load_reference, reference_type


def union(intervals):
    result = []
    for lo, hi in sorted(intervals):
        if hi <= lo:
            continue
        if result and lo <= result[-1][1]:
            result[-1][1] = max(hi, result[-1][1])
        else:
            result.append([lo, hi])
    return result


def support(points, *, reference=False, coupling=None):
    """Project the saved polyline onto log mass, preserving explicit gaps.

    Coupling conversion and single-valuedness are irrelevant to mass support.
    Reference closure markers use the existing documented sanitation policy.
    """
    arr = np.asarray(points, dtype=float)
    if arr.ndim != 2 or arr.shape[1] != 2 or not len(arr):
        raise ValueError("invalid_coordinates")
    valid = np.isfinite(arr).all(axis=1) & (arr[:, 0] > 0)
    separators = np.isnan(arr).any(axis=1)
    if np.any(~valid & ~separators):
        raise ValueError("invalid_mass_or_nonfinite_coordinate")
    if reference:
        valid &= (arr[:, 1] > 0) & (arr[:, 1] < 1e19)
        if coupling in {"DarkPhoton", "VectorBL", "AxionMass", "AxionCPV", "MonopoleDipole",
                        "AxionPhoton", "AxionElectron", "AxionNeutron", "AxionProton", "AxionEDM"}:
            valid &= arr[:, 1] != 1
        indices = np.flatnonzero(valid)
        for end in (indices[:2], indices[-2:][::-1]):
            if len(end) == 2:
                i, j = end
                if arr[i, 0] == arr[j, 0] and arr[i, 1] >= 1000 * arr[j, 1]:
                    valid[i] = False
    intervals, pieces = [], []
    for ids in np.split(np.arange(len(arr)), np.flatnonzero(~valid)):
        ids = ids[valid[ids]]
        if not len(ids):
            continue
        xs = np.log10(arr[ids, 0])
        pieces.append(sorted(set(float(x) for x in xs)))
        intervals.extend([min(a, b), max(a, b)] for a, b in zip(xs[:-1], xs[1:]))
    if not pieces:
        raise ValueError("no_usable_coordinates")
    return union(intervals), pieces


def fraction(reference, prediction):
    length = sum(b-a for a, b in reference)
    if length == 0:
        return None
    shared = sum(max(0, min(b, d)-max(a, c)) for a, b in reference for c, d in prediction)
    return float(min(1., shared / length))


def domain_flags(pieces, reference_file):
    flags = []
    # A screen for unresolved endpoints, not proof of an artificial extension.
    # The threshold is fixed, reference-only, and never used to trim a curve.
    for piece in pieces:
        if len(piece) >= 2 and max(piece[1]-piece[0], piece[-1]-piece[-2]) >= 3:
            flags.append("terminal_reference_spacing_at_least_3_dex")
    if reference_file == "limit_data/AxionElectron/LUX.txt":
        flags.append("low_mass_plateau_and_galactic_ALP_target_require_separation")
    return sorted(set(flags))


def run(root, out):
    provenance = {}
    def track(path):
        provenance[str(path.relative_to(root))] = digest(path)
    registry = root / "data/papers.json"
    track(registry)
    groups = defaultdict(list)
    for entry in json.loads(registry.read_text())["papers"]:
        if not entry["is_projection"]:
            groups[entry["arxiv_id"]].append(entry)
    ids = sorted(pid for pid, es in groups.items() if any(not e.get("excluded") for e in es))
    decisions = json.loads((HERE / "reference_decisions.json").read_text())["papers"]
    rows = []
    for arm, folder in ARMS.items():
        for pid in ids:
            row = {"arm": arm, "arxiv_id": pid, "coverage": None}
            rows.append(row)
            path = root / folder / (pid.replace("/", "_") + ".json")
            if not path.exists():
                row["status"] = "missing_output"; continue
            track(path)
            try:
                pred = json.loads(path.read_text())
            except ValueError:
                row["status"] = "invalid_output"; continue
            if pred.get("error") or pred.get("status") == "error" or not pred.get("data_points") or pred.get("is_projection") or pred.get("is_new_limit") is False:
                row["status"] = "no_eligible_measured_curve"; continue
            entries = [e for e in groups[pid] if not e.get("excluded")]
            ref, status, evidence = choose_reference(entries, pred, decisions.get(pid, {}), arm)
            row.update(identity_status=status, identity_evidence=evidence)
            if ref is None:
                row["status"] = status; continue
            row["reference_file"] = ref["reference_repo_file"]
            path = root / "data/ground_truth" / (ref.get("ground_truth_data_file") or "__missing__")
            if not path.exists():
                row["status"] = "reference_missing"; continue
            track(path)
            try:
                r, pieces = support(load_reference(path), reference=True, coupling=reference_type(ref))
            except (ValueError, TypeError, IndexError):
                row["status"] = "reference_coordinates_unusable"; continue
            row["reference_intervals_log10_eV"] = r
            flags = domain_flags(pieces, ref["reference_repo_file"])
            row["domain_flags"] = flags
            try:
                p, _ = support(pred["data_points"])
            except (ValueError, TypeError, IndexError):
                row["status"] = "prediction_coordinates_unusable"; continue
            row["prediction_intervals_log10_eV"] = p
            row["stored_range_diagnostic"] = fraction(r, p)
            if not r:
                row["status"] = "point_only_reference"; continue
            if flags:
                row["status"] = "reference_domain_unresolved"; continue
            row.update(status="assessed", coverage=fraction(r, p))
    summary = {}
    for arm in ARMS:
        subset = [r for r in rows if r["arm"] == arm]
        values = [r["coverage"] for r in subset if r["status"] == "assessed"]
        raw_values = [r["stored_range_diagnostic"] for r in subset if r.get("stored_range_diagnostic") is not None]
        summary[arm] = {"pool": len(ids), "assessed": len(values),
                        "status_counts": dict(Counter(r["status"] for r in subset)),
                        "median_reference_coverage": float(np.median(values)) if values else None,
                        "unscreened_stored_range_diagnostic": {"n": len(raw_values),
                            "median": float(np.median(raw_values)) if raw_values else None,
                            "at_least_90_percent": sum(v + 1e-12 >= .9 for v in raw_values)},
                        "threshold_counts": {str(t): sum(v + 1e-12 >= t for v in values) for t in (.5, .8, .9, .95)}}
    # Same paper AND same assigned reference for a descriptive paired comparison.
    paired = {}
    for model in ("fable", "opus", "haiku"):
        a = {r["arxiv_id"]: r for r in rows if r["arm"] == "agent_"+model and r["status"] == "assessed"}
        p = {r["arxiv_id"]: r for r in rows if r["arm"] == "pipeline_"+model and r["status"] == "assessed"}
        common = sorted(pid for pid in a.keys() & p.keys() if a[pid]["reference_file"] == p[pid]["reference_file"])
        paired[model] = {"paper_ids": common, "n": len(common), **{label: {
            "median_reference_coverage": float(np.median([data[pid]["coverage"] for pid in common])) if common else None,
            "at_least_90_percent": sum(data[pid]["coverage"] + 1e-12 >= .9 for pid in common)}
            for label, data in (("agent", a), ("pipeline", p))}}
    for rel, sha in provenance.items():
        if digest(root / rel) != sha:
            raise RuntimeError("Source changed during coverage evaluation")
    out.mkdir(parents=True, exist_ok=True)
    dump(out / "per_paper.json", rows)
    dump(out / "summary.json", summary)
    dump(out / "paired.json", paired)
    domains = {}
    for row in rows:
        if row.get('domain_flags'):
            key = row['arxiv_id'] + ':' + row['reference_file']
            entry = domains.setdefault(key, {"arxiv_id": row['arxiv_id'], "reference_file": row['reference_file'],
                "flags": row['domain_flags'], "reference_intervals_log10_eV": row['reference_intervals_log10_eV'], "arms": []})
            entry['arms'].append(row['arm'])
    dump(out / "reference_domain_review.json", list(domains.values()))
    dump(out / "provenance.json", {"input_sha256": provenance,
         "analysis_sha256": {str(p.relative_to(HERE)): digest(p) for p in sorted(HERE.rglob('*')) if p.is_file() and p.suffix in ('.py', '.json')}})
    report(out, summary, paired)


def report(out, summary, paired):
    lines = ["# Revised one-way coverage evaluation", "",
             "**Superseded:** [../cohort_coverage/report.md](../cohort_coverage/report.md) retains all members of the original reported cohorts. This older screened-subset report is retained for audit.", "",
             "Coverage is the fraction of the assigned ground-truth mass support recovered by the extraction, measured uniformly in log mass. Prediction support outside the reference is unverified and incurs no penalty. Coupling accuracy is not part of this coverage measurement.", "",
             "This is a reference-screened, conditional mass-support analysis, not certified physical completeness. Reference identity mappings and prior audit-based unresolved decisions are inherited. All masses are interpreted as eV under the archived schema. Closed curves are projected onto the mass axis; this does not certify recovery of their boundary or excluded area. Coupling-conversion problems alone do not prevent measuring mass support.", "",
             "## Reference-domain handling", "",
             "No endpoint is clipped to a prediction. A reference-only screen flags terminal adjacent mass spacing of at least three decades, and LUX is explicitly flagged for its mixed target. Flagged domains are unresolved, not extraction failures; raw stored-range coverage is retained only as a diagnostic. The three-decade threshold is a transparent triage heuristic, not physical validation. Unflagged references can still contain subtler extensions or target errors. Explicit gaps are preserved; undocumented gaps cannot be recovered from saved polylines.", "",
             "## Results", "",
             "The denominator for each threshold fraction is the assessed subset, not all 291 papers. Other cases are reported separately, not assigned zero. A point-only prediction against a finite reference interval has zero interval coverage; a point-only reference has no defined interval-coverage score.", "",
             "| Configuration | Assessed | Other cases | Median coverage | Coverage >=90% |", "|---|---:|---:|---:|---:|"]
    for arm, s in summary.items():
        n, count = s['assessed'], s['threshold_counts']['0.9']
        lines.append(f"| {NAMES[arm]} | {n} | {s['pool']-n} | {100*s['median_reference_coverage']:.1f}% | {count}/{n} ({100*count/n:.1f}%) |")
    lines += ["", "## Same-paper, same-reference subsets", "", "These remain selected, retrospective subsets with provisional reference identities.", "",
              "| Model | Shared N | Agent median | Pipeline median | Agent >=90% | Pipeline >=90% |", "|---|---:|---:|---:|---:|---:|"]
    for model, s in paired.items():
        lines.append(f"| {model} | {s['n']} | {100*s['agent']['median_reference_coverage']:.1f}% | {100*s['pipeline']['median_reference_coverage']:.1f}% | {s['agent']['at_least_90_percent']}/{s['n']} | {s['pipeline']['at_least_90_percent']}/{s['n']} |")
    lines += ["", "## Effect of reference-domain screening", "",
              "For transparency, these one-way diagnostics include the flagged reference domains literally, without treating their endpoints as validated truth. They isolate the effect of withholding flagged ranges; neither table establishes overall physical completeness.", "",
              "| Configuration | Literal stored-range comparisons | Median | Coverage >=90% |", "|---|---:|---:|---:|"]
    for arm, s in summary.items():
        raw = s['unscreened_stored_range_diagnostic']
        lines.append(f"| {NAMES[arm]} | {raw['n']} | {100*raw['median']:.1f}% | {raw['at_least_90_percent']}/{raw['n']} |")
    lines += ["", "## Dispositions", ""]
    for arm, s in summary.items():
        lines.append(f"- {NAMES[arm]}: `{json.dumps(s['status_counts'], sort_keys=True)}`")
    lines += ["", "## Reproduction", "", "Run `python -m evaluation.revision.coverage --benchmark-root PATH` in the straxion environment against the bundled archived inputs. No model calls, manual digitization, or changes to extraction outputs are involved. Earlier two-way coverage outputs are retained for audit and are superseded by this report for coverage interpretation."]
    (out / 'report.md').write_text('\n'.join(lines)+'\n')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--benchmark-root', type=Path, required=True)
    parser.add_argument('--out', type=Path, default=Path('paper/revision/coverage'))
    args = parser.parse_args()
    root, out = args.benchmark_root.resolve(), args.out.resolve()
    if out == root or root in out.parents:
        parser.error('Output must be outside the benchmark input directory')
    run(root, out)
