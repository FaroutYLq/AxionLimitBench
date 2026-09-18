"""Build the leaderboard from every scored run under results/<system>/<run>/metrics.json.

    python3 results/leaderboard.py            # writes results/LEADERBOARD.md + leaderboard.json

Headline metric (success rate): fraction of *scorable* papers whose extracted
curve has a median residual <= log10(1.1) = 0.041 dex (within 10%) against the
ground truth; "within 2x" (0.3 dex) is reported alongside. The scorable
pool is the measured-limits pool minus papers whose ground truth can grade
nothing (all entries excluded, or the GT file itself is unusable). Everything
else the system does wrong counts as a miss: abstaining, a wrong coupling
type (no comparable ground truth), a convention the scorer cannot reconcile,
zero mass overlap, or a residual above the threshold.
"""
from __future__ import annotations

import json
import math
import statistics
from pathlib import Path

ROOT = Path(__file__).resolve().parent
TAU = math.log10(1.1)   # 10%: the headline success tolerance
TAU2X = 0.3             # factor of two, reported alongside
CATASTROPHIC = 3.0
UNGRADEABLE = {"excluded_gt", "gt_unusable", None}


def summarise(run_dir: Path) -> dict | None:
    mp = run_dir / "metrics.json"
    if not mp.exists():
        return None
    m = json.loads(mp.read_text())
    run = json.loads((run_dir / "run.json").read_text()) if (run_dir / "run.json").exists() else {}
    pp = m.get("per_paper") or []
    pool_n = (m.get("pool") or {}).get("n_pool_papers") or len(pp)
    missing = (m.get("pool") or {}).get("missing") or []
    errors = (m.get("pool") or {}).get("errors") or []
    def cstatus(p):
        return p.get("comparison_status") if p.get("comparison_status") is not None else (
            "excluded_gt" if p.get("status") == "excluded_gt" else None)
    ungradeable = [p for p in pp if cstatus(p) in UNGRADEABLE]
    scorable = pool_n - len(ungradeable)
    compared, zero_overlap = [], 0
    for p in pp:
        if cstatus(p) != "compared":
            continue
        im = p.get("interp_metrics") or {}
        r = im.get("median_residual_dex")
        try:
            r = float(r)
        except (TypeError, ValueError):
            r = float("nan")
        if not math.isfinite(r):
            zero_overlap += 1  # compared but no mass overlap: a miss, not a residual
            continue
        compared.append((p["arxiv_id"], float(r)))
    within = sum(1 for _, r in compared if r <= TAU)
    within2x = sum(1 for _, r in compared if r <= TAU2X)
    cat = sum(1 for _, r in compared if r > CATASTROPHIC)
    cls = (m.get("classification") or {}).get("coupling_type") or {}
    status = {}
    for p in pp:
        status[str(cstatus(p))] = status.get(str(cstatus(p)), 0) + 1
    # cost / effort from snapshots' meta (agent runs only)
    costs, turns, leaks, timeouts = [], [], 0, 0
    for sp in run_dir.glob("*.json"):
        if sp.name in ("metrics.json", "metrics_summary.json", "run.json", "metadata_cache.json"):
            continue
        try:
            meta = json.loads(sp.read_text()).get("meta") or {}
        except Exception:
            continue
        if meta.get("total_cost_usd") is not None:
            costs.append(float(meta["total_cost_usd"]))
        if meta.get("num_turns") is not None:
            turns.append(int(meta["num_turns"]))
        leaks += bool(meta.get("leak_suspect"))
        timeouts += bool(meta.get("timed_out"))
    return {
        "system": run.get("system") or run_dir.parent.name,
        "run": run_dir.name,
        "model": run.get("model"),
        "pool_papers": pool_n,
        "scorable": scorable,
        "snapshots_missing": len(missing),
        "snapshots_error": len(errors),
        "compared": len(compared),
        "zero_overlap": zero_overlap,
        "ungradeable": len(ungradeable),
        "coverage": len(compared) / scorable if scorable else None,
        "success_rate_10pct": within / scorable if scorable else None,
        "within_10pct_n": within,
        "within_2x": within2x / scorable if scorable else None,
        "within_2x_n": within2x,
        "conditional_median_dex": statistics.median(r for _, r in compared) if compared else None,
        "catastrophic_gt3dex": cat,
        "catastrophic_rate_of_compared": cat / len(compared) if compared else None,
        "coupling_type_accuracy": cls.get("accuracy"),
        "status_counts": status,
        "cost_usd_total": sum(costs) if costs else None,
        "cost_usd_median_per_paper": statistics.median(costs) if costs else None,
        "turns_median": statistics.median(turns) if turns else None,
        "leak_suspects": leaks,
        "timeouts": timeouts,
        "notes": run.get("transport_notes") or run.get("harness"),
    }


def main() -> None:
    rows = []
    for mp in sorted(ROOT.glob("*/*/metrics.json")):
        if mp.parent.name.endswith("_smoke"):
            continue  # smoke tests are not leaderboard entries
        s = summarise(mp.parent)
        if s:
            rows.append(s)
    rows.sort(key=lambda r: -(r["success_rate_10pct"] or 0))
    (ROOT / "leaderboard.json").write_text(json.dumps(rows, indent=1))

    def f(x, p=3):
        return "-" if x is None else (f"{x:.{p}f}" if isinstance(x, float) else str(x))

    lines = [
        "# AxionLimitBench leaderboard",
        "",
        "Success rate = fraction of scorable papers whose curve is within 10% (0.041 dex) of the reference; abstentions, wrong coupling type, "
        f"convention gaps and zero-overlap curves all count as misses. Within 2x = the same at 0.3 dex. Catastrophic = median residual > {CATASTROPHIC} dex "
        "among compared papers. The pipeline's measured run-to-run noise is about +/-0.04 dex on the conditional median.",
        "",
        "| system | run | model | scorable | compared | coverage | **success rate (10%)** | within 2x | cond. median [dex] | catastrophic | ct acc. | median $/paper | median turns |",
        "|---|---|---|---|---|---|---|---|---|---|---|---|---|",
    ]
    for r in rows:
        lines.append(
            f"| {r['system']} | {r['run']} | {r['model']} | {r['scorable']} | {r['compared']} | "
            f"{f(r['coverage'])} | **{f(r['success_rate_10pct'])}** ({r['within_10pct_n']}) | {f(r['within_2x'])} ({r['within_2x_n']}) | "
            f"{f(r['conditional_median_dex'])} | {r['catastrophic_gt3dex']} | {f(r['coupling_type_accuracy'])} | "
            f"{f(r['cost_usd_median_per_paper'], 2)} | {f(r['turns_median'], 0)} |")
    lines += ["", "## Status counts", ""]
    for r in rows:
        lines.append(f"- **{r['system']}/{r['run']}**: {json.dumps(r['status_counts'])}; snapshots missing {r['snapshots_missing']}, "
                     f"error {r['snapshots_error']}, leak suspects {r['leak_suspects']}, timeouts {r['timeouts']}")
    (ROOT / "LEADERBOARD.md").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
