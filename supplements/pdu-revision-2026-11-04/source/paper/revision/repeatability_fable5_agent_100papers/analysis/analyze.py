#!/usr/bin/env python3
"""Score and compare the two fresh Fable 5 agent repeats (paired repeatability).

Usage (conda straxion):
    python analysis/analyze.py [--runs-dir runs] [--out analysis/out]

Steps
1. Score each repeat's snapshot directory with the frozen scorer
   (scorer/score.py, measured-limits pool) -> scoring/<repeat>/metrics.json.
2. Re-score both repeats against a COMMON FIXED reference chosen by a
   score-independent rule (largest ground_truth_num_points among the paper's
   non-excluded entries; tie -> smallest gt file name).
3. Pair per-paper median residuals, report |delta| statistics, transitions,
   reference changes, aggregate medians, direct curve-vs-curve agreement,
   histogram, session provenance table, and the archived benchmark snapshot as
   a supplementary column.
No extraction happens here; no network access.
"""
from __future__ import annotations
import argparse, csv, hashlib, json, os, subprocess, sys, tempfile
from collections import Counter
from pathlib import Path

FROZEN = Path(os.environ.get("AXLB_BENCHMARK_ROOT", str(Path(__file__).resolve().parents[4] / "benchmark")))
EXP = Path(__file__).resolve().parents[1]
REPEATS = ("repeat1", "repeat2")
BINS = [0, 0.01, 0.03, 0.1, 0.3, 1, 3, float("inf")]
THRESH = (0.01, 0.03, 0.1)


def sha256(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def safe_id(a: str) -> str:
    return a.replace("/", "_")


def run_frozen_scorer(snapdir: Path, out: Path, python: str) -> dict:
    out.mkdir(parents=True, exist_ok=True)
    cmd = [python, "-m", "scorer.score", "--snapshots", str(snapdir), "--out", str(out), "--report"]
    env = dict(os.environ)
    env.pop("AXLB_REFERENCE_ROOT", None)
    r = subprocess.run(cmd, cwd=FROZEN, capture_output=True, text=True, env=env)
    (out / "scorer_stdout.txt").write_text(r.stdout + "\n--- stderr ---\n" + r.stderr)
    if r.returncode != 0:
        raise SystemExit(f"scorer failed on {snapdir}:\n{r.stderr[-2000:]}")
    return json.loads((out / "metrics.json").read_text())


def per_paper_index(metrics: dict) -> dict:
    return {p["arxiv_id"]: p for p in metrics["per_paper"]}


def finite_residual(p: dict | None):
    """Per-paper score = interp_metrics.median_residual_dex of a compared paper."""
    if not p or p.get("comparison_status") != "compared":
        return None
    im = p.get("interp_metrics") or {}
    v = im.get("median_residual_dex")
    if v is None:
        return None
    v = float(v)
    return v if v == v and abs(v) != float("inf") else None


def outcome_label(snap: dict | None, p: dict | None) -> str:
    if snap is None:
        return "missing_snapshot"
    if snap.get("status") == "error" or snap.get("error"):
        return "error_stub"
    m = snap.get("meta") or {}
    if m.get("timed_out"):
        return "timeout" + ("_with_result" if snap.get("num_points") else "")
    if not snap.get("is_new_limit") and not snap.get("num_points"):
        if snap.get("is_projection"):
            return "abstain_projection"
        return "abstain_no_limit"
    if p is None:
        return "not_in_pool"
    st = p.get("comparison_status") or p.get("status")
    if st == "compared":
        return "compared_finite" if finite_residual(p) is not None else "compared_infinite"
    return str(st)


def load_snaps(d: Path, ids) -> dict:
    out = {}
    for a in ids:
        f = d / f"{safe_id(a)}.json"
        out[a] = json.loads(f.read_text()) if f.exists() else None
    return out


# ---------------------------------------------------------------- fixed reference
def fixed_reference_rule(entries):
    """Score-independent rule: per paper, the non-excluded entry with the most
    GT points; ties -> lexicographically smallest ground_truth_data_file."""
    by = {}
    for e in entries:
        if e.excluded:
            continue
        by.setdefault(e.arxiv_id, []).append(e)
    chosen = {}
    for a, es in by.items():
        es = sorted(es, key=lambda e: (-(e.ground_truth_num_points or 0), str(e.ground_truth_data_file)))
        chosen[a] = es[0]
    return chosen


def rescore_fixed_reference(ids, snapdirs: dict, out: Path, python: str) -> dict:
    """Run the frozen scorer's compute_all_metrics with each paper restricted
    to its fixed reference entry. Executed in a subprocess so env-dependent
    scorer globals are set before import."""
    code = r'''
import json, os, sys
from pathlib import Path
os.environ["AAL_EXCLUDE_PROJECTIONS"] = "1"
FROZEN = Path(sys.argv[1]); ids = json.loads(Path(sys.argv[2]).read_text()); snapdirs = json.loads(sys.argv[3]); out = Path(sys.argv[4])
sys.path.insert(0, str(FROZEN))
import scorer.evaluate as ev
from scorer.ground_truth import load_ground_truth
entries = [e for e in load_ground_truth() if not e.is_projection and e.arxiv_id in set(ids)]
by = {}
for e in entries:
    if e.excluded: continue
    by.setdefault(e.arxiv_id, []).append(e)
chosen = {a: sorted(es, key=lambda e: (-(e.ground_truth_num_points or 0), str(e.ground_truth_data_file)))[0] for a, es in by.items()}
rule = {a: {"gt_file": e.reference_repo_file, "coupling_type": e.coupling_type, "n_points": e.ground_truth_num_points,
            "n_candidates_in_paper": len(by[a])} for a, e in chosen.items()}
(out / "fixed_reference_rule.json").write_text(json.dumps(rule, indent=1))
res = {}
for name, d in snapdirs.items():
    os.environ["AXLB_RESULTS_DIR"] = d
    ve, rs = [], []
    for a, e in chosen.items():
        p = Path(d) / f"{a.replace('/', '_')}.json"
        if not p.exists(): continue
        s = json.loads(p.read_text())
        if s.get("status") == "error" or s.get("error"): continue
        ve.append(e); rs.append(s)
    m = ev.compute_all_metrics(ve, rs)
    (out / f"fixed_reference_metrics_{name}.json").write_text(json.dumps(m, indent=1, default=str))
    res[name] = {p["arxiv_id"]: p for p in m["per_paper"]}
print(json.dumps({k: len(v) for k, v in res.items()}))
'''
    out.mkdir(parents=True, exist_ok=True)
    idsf = out / "_ids.json"
    idsf.write_text(json.dumps(list(ids)))
    r = subprocess.run([python, "-c", code, str(FROZEN), str(idsf), json.dumps({k: str(v) for k, v in snapdirs.items()}), str(out)],
                       capture_output=True, text=True, cwd=FROZEN)
    if r.returncode != 0:
        raise SystemExit("fixed-reference rescoring failed:\n" + r.stderr[-3000:])
    return {name: json.loads((out / f"fixed_reference_metrics_{name}.json").read_text()) for name in snapdirs}


# ---------------------------------------------------------------- direct curve comparison
def direct_curve_delta(a: dict | None, b: dict | None):
    """Median |log10 g_b/g_a| over the shared mass range, b interpolated (log-log)
    onto a's masses. None if either curve is missing or no overlap."""
    import numpy as np
    if not a or not b:
        return None
    pa, pb = a.get("data_points") or [], b.get("data_points") or []
    if len(pa) < 2 or len(pb) < 2:
        return None
    A = np.array(sorted(pa), float); B = np.array(sorted(pb), float)
    A = A[(A[:, 0] > 0) & (A[:, 1] > 0)]; B = B[(B[:, 0] > 0) & (B[:, 1] > 0)]
    if len(A) < 2 or len(B) < 2:
        return None
    lo, hi = max(A[0, 0], B[0, 0]), min(A[-1, 0], B[-1, 0])
    if not (hi > lo):
        return {"median_abs_log10_ratio": None, "overlap": False}
    xa = A[(A[:, 0] >= lo) & (A[:, 0] <= hi)]
    if len(xa) == 0:
        return {"median_abs_log10_ratio": None, "overlap": False}
    # unique masses for interpolation
    bx, idx = np.unique(np.log10(B[:, 0]), return_index=True)
    by = np.log10(B[:, 1])[idx]
    yb = np.interp(np.log10(xa[:, 0]), bx, by)
    d = np.abs(np.log10(xa[:, 1]) - yb)
    lf = (np.log10(hi) - np.log10(lo)) / max(np.log10(max(A[-1, 0], B[-1, 0])) - np.log10(min(A[0, 0], B[0, 0])), 1e-12)
    return {"median_abs_log10_ratio": float(np.median(d)), "p90_abs_log10_ratio": float(np.percentile(d, 90)),
            "overlap": True, "mass_overlap_fraction_of_union": float(lf), "n_eval": int(len(d))}


# ---------------------------------------------------------------- stats helpers
def quantiles(xs):
    import numpy as np
    if not xs:
        return {"n": 0}
    x = np.array(xs, float)
    return {"n": int(len(x)), "median": float(np.median(x)), "q1": float(np.percentile(x, 25)),
            "q3": float(np.percentile(x, 75)), "p90": float(np.percentile(x, 90)), "max": float(x.max()),
            "mean": float(x.mean()),
            **{f"frac_lt_{t}": float((x < t).mean()) for t in THRESH},
            **{f"n_lt_{t}": int((x < t).sum()) for t in THRESH}}


def histogram(xs):
    import numpy as np
    counts, _ = np.histogram(np.array(xs, float), bins=BINS)
    return {"bin_edges_dex": [b if b != float("inf") else "infinity" for b in BINS],
            "bin_counts": [int(c) for c in counts], "denominator": len(xs),
            "denominator_definition": "papers with a finite residual score in BOTH repeats (common finite cohort)"}


def session_row(a, rep, snap, attempt_rec, init_ev):
    m = (snap or {}).get("meta") or {}
    return {
        "arxiv_id": a, "repeat": rep,
        "status": "error" if (snap or {}).get("status") == "error" else ("ok" if snap else "missing"),
        "error": (snap or {}).get("error"),
        "started_at": (attempt_rec or {}).get("started_at"), "finished_at": m.get("finished_at") or (attempt_rec or {}).get("finished_at"),
        "elapsed_s": (snap or {}).get("elapsed_s"), "duration_api_ms": m.get("duration_api_ms"),
        "model_requested": m.get("model_requested"), "models_billed": ",".join(m.get("models_billed") or []),
        "init_model": (init_ev or {}).get("model"), "claude_code_version": (init_ev or {}).get("claude_code_version"),
        "permission_mode": (init_ev or {}).get("permissionMode"), "tools": ",".join((init_ev or {}).get("tools") or []),
        "effort": m.get("effort"), "transport": m.get("transport"), "attempt": m.get("attempt"),
        "timed_out": m.get("timed_out"), "cli_subtype": m.get("cli_subtype"), "cli_is_error": m.get("cli_is_error"),
        "num_turns": m.get("num_turns"), "total_cost_usd": m.get("total_cost_usd"),
        "input_tokens": (m.get("usage") or {}).get("input_tokens"), "output_tokens": (m.get("usage") or {}).get("output_tokens"),
        "cache_read_input_tokens": (m.get("usage") or {}).get("cache_read_input_tokens"),
        "cache_creation_input_tokens": (m.get("usage") or {}).get("cache_creation_input_tokens"),
        "leak_suspect": m.get("leak_suspect"), "schema_problems": "; ".join(m.get("schema_problems") or []),
        "task_card_sha256": m.get("task_card_sha256"), "driver_version": m.get("driver_version"),
        "coupling_type": (snap or {}).get("coupling_type"), "is_new_limit": (snap or {}).get("is_new_limit"),
        "is_projection": (snap or {}).get("is_projection"), "num_points": (snap or {}).get("num_points"),
        "data_source": (snap or {}).get("data_source"), "extraction_confidence": (snap or {}).get("extraction_confidence"),
        "events_file": m.get("events_file"),
    }


def read_init_event(path: Path):
    if not path.exists():
        return None
    with path.open() as f:
        for line in f:
            try:
                ev = json.loads(line)
            except json.JSONDecodeError:
                continue
            if ev.get("type") == "system" and ev.get("subtype") == "init":
                return ev
    return None


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--runs-dir", default=str(EXP / "runs"))
    ap.add_argument("--out", default=str(EXP / "analysis" / "out"))
    ap.add_argument("--scoring-dir", default=str(EXP / "scoring"))
    ap.add_argument("--archived", default=str(FROZEN / "results" / "agent_claude_code" / "fable5"),
                    help="archived benchmark snapshots (supplementary column)")
    ap.add_argument("--python", default=sys.executable)
    ap.add_argument("--repeat-dirs", nargs=2, default=None, help="override the two snapshot dirs (testing)")
    args = ap.parse_args()
    runs = Path(args.runs_dir); out = Path(args.out); scoring = Path(args.scoring_dir)
    out.mkdir(parents=True, exist_ok=True)
    sel = json.loads((EXP / "protocol" / "selected_ids.json").read_text())
    ids = sel["ids_sorted"]
    snapdirs = {r: (Path(args.repeat_dirs[i]) if args.repeat_dirs else runs / r) for i, r in enumerate(REPEATS)}

    # 1. frozen scorer per repeat (+ archived subset, supplementary)
    metrics = {r: run_frozen_scorer(d, scoring / r, args.python) for r, d in snapdirs.items()}
    arch_dir = scoring / "archived_subset_snapshots"
    arch_dir.mkdir(parents=True, exist_ok=True)
    n_arch = 0
    for a in ids:
        src = Path(args.archived) / f"{safe_id(a)}.json"
        if src.exists():
            (arch_dir / src.name).write_bytes(src.read_bytes()); n_arch += 1
    metrics["archived"] = run_frozen_scorer(arch_dir, scoring / "archived", args.python)
    pp = {k: per_paper_index(m) for k, m in metrics.items()}

    # 2. fixed common reference
    fixed = rescore_fixed_reference(ids, {**snapdirs, "archived": arch_dir}, scoring / "fixed_reference", args.python)
    fpp = {k: {p["arxiv_id"]: p for p in m["per_paper"]} for k, m in fixed.items()}
    rule = json.loads((scoring / "fixed_reference" / "fixed_reference_rule.json").read_text())

    # 3. per-paper table
    snaps = {r: load_snaps(d, ids) for r, d in snapdirs.items()}
    snaps["archived"] = load_snaps(arch_dir, ids)
    attempts = {}
    af = runs / "attempts.jsonl"
    if af.exists():
        for line in af.read_text().splitlines():
            if line.strip():
                rec = json.loads(line); attempts[(rec["arxiv_id"], rec["repeat"])] = rec
    rows = []
    for a in ids:
        row = {"arxiv_id": a}
        for r in REPEATS + ("archived",):
            p = pp[r].get(a); s = snaps[r][a]
            row[f"{r}_outcome"] = outcome_label(s, p)
            row[f"{r}_residual_dex"] = finite_residual(p)
            row[f"{r}_gt_file"] = (p or {}).get("gt_file")
            row[f"{r}_scored_via"] = (p or {}).get("scored_via")
            row[f"{r}_coupling_type"] = (s or {}).get("coupling_type")
            row[f"{r}_num_points"] = (s or {}).get("num_points")
            row[f"{r}_data_source"] = (s or {}).get("data_source")
            row[f"{r}_fixedref_residual_dex"] = finite_residual(fpp[r].get(a))
            row[f"{r}_fixedref_status"] = (fpp[r].get(a) or {}).get("comparison_status")
        row["fixed_reference_gt_file"] = (rule.get(a) or {}).get("gt_file")
        row["n_reference_candidates"] = (rule.get(a) or {}).get("n_candidates_in_paper")
        r1, r2 = row["repeat1_residual_dex"], row["repeat2_residual_dex"]
        row["abs_delta_dex"] = abs(r2 - r1) if (r1 is not None and r2 is not None) else None
        f1, f2 = row["repeat1_fixedref_residual_dex"], row["repeat2_fixedref_residual_dex"]
        row["abs_delta_fixedref_dex"] = abs(f2 - f1) if (f1 is not None and f2 is not None) else None
        row["reference_changed"] = (row["repeat1_gt_file"] != row["repeat2_gt_file"]) if (row["repeat1_gt_file"] and row["repeat2_gt_file"]) else None
        row["coupling_type_changed"] = (row["repeat1_coupling_type"] != row["repeat2_coupling_type"])
        dc = direct_curve_delta(snaps["repeat1"][a], snaps["repeat2"][a])
        row["direct_curve_median_abs_log10_ratio"] = (dc or {}).get("median_abs_log10_ratio")
        row["direct_curve_p90_abs_log10_ratio"] = (dc or {}).get("p90_abs_log10_ratio")
        row["direct_curve_mass_overlap_fraction"] = (dc or {}).get("mass_overlap_fraction_of_union")
        ra = row["archived_residual_dex"]
        row["abs_delta_repeat1_vs_archived_dex"] = abs(r1 - ra) if (r1 is not None and ra is not None) else None
        row["abs_delta_repeat2_vs_archived_dex"] = abs(r2 - ra) if (r2 is not None and ra is not None) else None
        rows.append(row)
    (out / "per_paper.json").write_text(json.dumps(rows, indent=1))
    with (out / "per_paper.csv").open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)

    # 4. summary statistics
    att = {r: [x["arxiv_id"] for x in rows if x[f"{r}_outcome"] not in ("missing_snapshot",)] for r in REPEATS}
    fin = {r: [x["arxiv_id"] for x in rows if x[f"{r}_residual_dex"] is not None] for r in REPEATS}
    common = [a for a in fin["repeat1"] if a in set(fin["repeat2"])]
    only1 = [a for a in fin["repeat1"] if a not in set(fin["repeat2"])]
    only2 = [a for a in fin["repeat2"] if a not in set(fin["repeat1"])]
    neither = [a for a in ids if a not in set(fin["repeat1"]) and a not in set(fin["repeat2"])]
    byid = {x["arxiv_id"]: x for x in rows}
    deltas = [byid[a]["abs_delta_dex"] for a in common]
    import numpy as np
    med = lambda xs: float(np.median(xs)) if xs else None
    cohort_meds = {r: {"own_finite_cohort": {"n": len(fin[r]), "median_residual_dex": med([byid[a][f"{r}_residual_dex"] for a in fin[r]])},
                       "common_finite_cohort": {"n": len(common), "median_residual_dex": med([byid[a][f"{r}_residual_dex"] for a in common])}}
                   for r in REPEATS}
    ref_changed = [a for a in common if byid[a]["reference_changed"]]
    multi = [a for a in common if (byid[a]["n_reference_candidates"] or 1) > 1]
    fcommon = [a for a in ids if byid[a]["abs_delta_fixedref_dex"] is not None]
    fdeltas = [byid[a]["abs_delta_fixedref_dex"] for a in fcommon]
    # decomposition on common cohort: papers where best-match ref differs
    dec = {"n_common": len(common), "n_reference_changed": len(ref_changed), "reference_changed_ids": ref_changed,
           "n_multi_candidate_papers_in_common": len(multi),
           "abs_delta_on_reference_changed": quantiles([byid[a]["abs_delta_dex"] for a in ref_changed]),
           "abs_delta_on_reference_unchanged": quantiles([byid[a]["abs_delta_dex"] for a in common if a not in set(ref_changed)]),
           "fixed_reference": {"rule": "per paper: non-excluded reference entry with the largest ground_truth_num_points; tie -> smallest gt data file name",
                               "n_finite_both": len(fcommon), "abs_delta": quantiles(fdeltas),
                               "ids_finite_both": fcommon,
                               "repeat_medians_on_fixed_common": {r: med([byid[a][f"{r}_fixedref_residual_dex"] for a in fcommon]) for r in REPEATS}}}
    direct = [byid[a]["direct_curve_median_abs_log10_ratio"] for a in ids if byid[a]["direct_curve_median_abs_log10_ratio"] is not None]
    direct_common = [byid[a]["direct_curve_median_abs_log10_ratio"] for a in common if byid[a]["direct_curve_median_abs_log10_ratio"] is not None]
    transitions = Counter((byid[a]["repeat1_outcome"], byid[a]["repeat2_outcome"]) for a in ids)
    # sessions / provenance
    sess = []
    for r in REPEATS:
        for a in ids:
            s = snaps[r][a]
            ev = read_init_event(snapdirs[r] / f"{safe_id(a)}.events.jsonl")
            sess.append(session_row(a, r, s, attempts.get((a, r)), ev))
    with (out / "sessions.csv").open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(sess[0].keys())); w.writeheader(); w.writerows(sess)
    prov = {
        "n_sessions": len(sess),
        "models_requested": Counter(s["model_requested"] for s in sess), "models_billed": Counter(s["models_billed"] for s in sess),
        "init_model": Counter(s["init_model"] for s in sess), "claude_code_version": Counter(s["claude_code_version"] for s in sess),
        "permission_mode": Counter(s["permission_mode"] for s in sess), "tools": Counter(s["tools"] for s in sess),
        "effort": Counter(s["effort"] for s in sess), "transport": Counter(s["transport"] for s in sess),
        "task_card_sha256": Counter(s["task_card_sha256"] for s in sess), "driver_version": Counter(s["driver_version"] for s in sess),
        "attempt_index": Counter(s["attempt"] for s in sess), "cli_subtype": Counter(s["cli_subtype"] for s in sess),
        "timed_out": Counter(s["timed_out"] for s in sess), "leak_suspect": Counter(s["leak_suspect"] for s in sess),
        "status": Counter(s["status"] for s in sess),
        "total_cost_usd": {r: float(sum(s["total_cost_usd"] or 0 for s in sess if s["repeat"] == r)) for r in REPEATS},
        "elapsed_s": {r: quantiles([s["elapsed_s"] for s in sess if s["repeat"] == r and s["elapsed_s"] is not None]) for r in REPEATS},
        "num_turns": {r: quantiles([s["num_turns"] for s in sess if s["repeat"] == r and s["num_turns"] is not None]) for r in REPEATS},
    }
    prov = {k: (dict(v) if isinstance(v, Counter) else v) for k, v in prov.items()}
    archived_pairs = {f"{r}_vs_archived": quantiles([byid[a][f"abs_delta_{r}_vs_archived_dex"] for a in ids if byid[a][f"abs_delta_{r}_vs_archived_dex"] is not None]) for r in REPEATS}
    summary = {
        "experiment": "fable5_agent_repeatability_100papers",
        "sample": {"n_selected": len(ids), "seed": sel["seed"], "population_size": sel["population_size"],
                   "selected_ids_sha256": sha256(EXP / "protocol" / "selected_ids.json")},
        "scorer": {"source": str(FROZEN), "commit": sel["frozen_commit"],
                   "sha256": {f: sha256(FROZEN / f) for f in ("scorer/score.py", "scorer/evaluate.py", "scorer/metrics.py",
                                                              "scorer/conventions.py", "scorer/ground_truth.py", "data/papers.json")}},
        "score_definition": "interp_metrics.median_residual_dex of a 'compared' paper under the frozen scorer (measured-limits pool); nonfinite otherwise",
        "attempted": {r: len(att[r]) for r in REPEATS},
        "finite": {r: len(fin[r]) for r in REPEATS},
        "common_finite": len(common), "finite_only_repeat1": only1, "finite_only_repeat2": only2, "finite_in_neither": neither,
        "outcome_counts": {r: dict(Counter(byid[a][f"{r}_outcome"] for a in ids)) for r in REPEATS},
        "outcome_transitions_repeat1_to_repeat2": [{"repeat1": k[0], "repeat2": k[1], "n": v} for k, v in sorted(transitions.items(), key=lambda kv: -kv[1])],
        "paired_abs_delta_residual_dex": quantiles(deltas),
        "histogram_abs_delta_residual_dex": histogram(deltas),
        "aggregate_medians": cohort_meds,
        "reference_selection": dec,
        "direct_curve_comparison": {"definition": "median |log10(g_repeat2/g_repeat1)| over the shared mass range, repeat2 interpolated log-log onto repeat1 masses; independent of the reference",
                                    "all_pairs_with_curves": quantiles(direct), "common_finite_cohort": quantiles(direct_common),
                                    "n_pairs_no_mass_overlap": sum(1 for a in ids if (snaps["repeat1"][a] or {}).get("num_points") and (snaps["repeat2"][a] or {}).get("num_points") and byid[a]["direct_curve_median_abs_log10_ratio"] is None)},
        "coupling_type_changed_ids": [a for a in ids if byid[a]["coupling_type_changed"]],
        "supplementary_archived_benchmark": {"n_archived_snapshots_for_sample": n_arch, "note": "archived run's prompt/runtime history differs (two task-card passes); supplementary only",
                                             "archived_finite": sum(1 for a in ids if byid[a]["archived_residual_dex"] is not None),
                                             "archived_median_on_common_finite_cohort": med([byid[a]["archived_residual_dex"] for a in common if byid[a]["archived_residual_dex"] is not None]),
                                             **archived_pairs},
        "provenance": prov,
        "run_meta": json.loads((runs / "run.json").read_text()) if (runs / "run.json").exists() else None,
    }
    if summary["run_meta"]:
        summary["run_meta"].pop("pdf_inputs", None)
    (out / "summary.json").write_text(json.dumps(summary, indent=1, default=str))

    # 5. histogram figure
    import matplotlib; matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    h = summary["histogram_abs_delta_residual_dex"]
    labels = ["<0.01", "0.01–0.03", "0.03–0.1", "0.1–0.3", "0.3–1", "1–3", ">3"]
    fig, ax = plt.subplots(figsize=(6.4, 3.6))
    ax.bar(range(len(labels)), h["bin_counts"], color="#4a6fa5")
    for i, c in enumerate(h["bin_counts"]):
        ax.text(i, c + 0.5, str(c), ha="center", va="bottom", fontsize=9)
    ax.set_xticks(range(len(labels))); ax.set_xticklabels(labels)
    ax.set_xlabel("|Δ median residual| between repeats (dex)")
    ax.set_ylabel("papers")
    ax.set_title(f"Fable 5 agent, two fresh sessions per paper\n(n = {h['denominator']} papers finite in both repeats, of {len(ids)} selected)", fontsize=10)
    fig.tight_layout(); fig.savefig(out / "hist_abs_delta.png", dpi=200); fig.savefig(out / "hist_abs_delta.pdf")
    print(json.dumps({k: summary[k] for k in ("attempted", "finite", "common_finite", "paired_abs_delta_residual_dex", "aggregate_medians")}, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
