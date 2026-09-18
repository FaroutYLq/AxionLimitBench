"""Score a directory of prediction snapshots against the frozen ground truth.

    python -m scorer.score --snapshots results/<system>/<run> [--out DIR] [--full-pool] [--report]

Writes metrics.json, metrics_summary.json (and report.md with --report) into
--out (default: the snapshot directory). The measured-limits pool is the
default; --full-pool also scores projection entries. Snapshots with
status=="error" are skipped (they are not answers); a paper with no snapshot
counts as missing. Both lists are recorded under "pool" in the outputs.
"""
from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--snapshots", required=True)
    ap.add_argument("--out", default=None)
    ap.add_argument("--full-pool", action="store_true")
    ap.add_argument("--report", action="store_true", help="also write report.md")
    args = ap.parse_args()
    snaps = Path(args.snapshots).resolve()
    out = Path(args.out).resolve() if args.out else snaps
    out.mkdir(parents=True, exist_ok=True)
    os.environ["AAL_EXCLUDE_PROJECTIONS"] = "0" if args.full_pool else "1"
    os.environ["AXLB_RESULTS_DIR"] = str(snaps)
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
    import scorer.evaluate as ev  # noqa: E402  (env must be set before import)
    from scorer.ground_truth import load_ground_truth  # noqa: E402

    entries = load_ground_truth()
    if not args.full_pool:
        entries = [e for e in entries if not e.is_projection]
    pool_ids = sorted({e.arxiv_id for e in entries})
    valid_entries, results, missing, errors = [], [], [], []
    seen: set[str] = set()
    for e in entries:
        p = snaps / f"{e.arxiv_id.replace('/', '_')}.json"
        if not p.exists():
            if e.arxiv_id not in seen:
                missing.append(e.arxiv_id)
            seen.add(e.arxiv_id)
            continue
        d = json.loads(p.read_text())
        if d.get("status") == "error" or d.get("error"):
            if e.arxiv_id not in seen:
                errors.append(e.arxiv_id)
            seen.add(e.arxiv_id)
            continue
        seen.add(e.arxiv_id)
        valid_entries.append(e)
        results.append(d)
    m = ev.compute_all_metrics(valid_entries, results)
    m["benchmark_scope"] = "full_pool" if args.full_pool else "measured_limits_only"
    m["pool"] = {"n_pool_papers": len(pool_ids),
                 "n_scored_snapshots": len({e.arxiv_id for e in valid_entries}),
                 "missing": missing, "errors": errors}
    (out / "metrics.json").write_text(json.dumps(m, indent=2, default=str))
    summary = ev.write_metrics_summary(m, out / "metrics_summary.json")
    summary["pool"] = dict(m["pool"], missing=len(missing), errors=len(errors))
    (out / "metrics_summary.json").write_text(json.dumps(summary, indent=2, default=str))
    if args.report:
        ev.generate_report(m, str(out / "report.md"))
    pta = summary.get("per_type_aggregate") or {}
    print(json.dumps({
        "pool_papers": len(pool_ids),
        "snapshots_scored": len({e.arxiv_id for e in valid_entries}),
        "missing": len(missing), "errors": len(errors),
        "compared": pta.get("n_papers_compared"),
        "micro_median_dex": pta.get("micro_median_residual_dex"),
        "macro_median_dex": pta.get("macro_median_residual_dex"),
        "interpolation": summary.get("interpolation"),
        "status_counts": summary.get("status_counts"),
        "ct_accuracy": (summary.get("classification_accuracy") or {}).get("coupling_type"),
    }, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
