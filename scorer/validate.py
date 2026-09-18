"""Validate a submission directory before scoring.

    python3 -m scorer.validate --snapshots results/<system>/<run>

Checks every <id>.json against schema/prediction.schema.json (no external
dependency: a small hand-written checker), confirms ids belong to the pool,
lists pool papers without a snapshot, and warns about declarations the frozen
scorer will not recognise for the predicted coupling type. Exit code 1 on any
schema error so it can gate a CI job.
"""
from __future__ import annotations

import argparse
import json
import math
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TYPES = {"AxionPhoton", "AxionElectron", "AxionNeutron", "AxionProton", "AxionEDM", "AxionMass", "AxionCPV",
         "DarkPhoton", "VectorBL", "ScalarPhoton", "ScalarElectron", "ScalarNucleon", "ScalarBaryon", "MonopoleDipole"}
SOURCES = {"table", "text", "figure_vision", "figure_vector", "ancillary_file", "none", "unknown", None}


def check(d: dict) -> list[str]:
    errs: list[str] = []
    for k in ("arxiv_id", "coupling_type", "is_new_limit", "is_projection", "data_points"):
        if k not in d:
            errs.append(f"missing required key {k}")
    if errs:
        return errs
    if d["coupling_type"] is not None and d["coupling_type"] not in TYPES:
        errs.append(f"coupling_type {d['coupling_type']!r} not in the 14 known types")
    for k in ("is_new_limit", "is_projection"):
        if not isinstance(d[k], bool):
            errs.append(f"{k} must be boolean")
    pts = d["data_points"]
    if not isinstance(pts, list):
        errs.append("data_points must be a list")
    else:
        for i, p in enumerate(pts):
            if not (isinstance(p, (list, tuple)) and len(p) == 2):
                errs.append(f"data_points[{i}] must be [mass_eV, coupling]"); break
            try:
                m, g = float(p[0]), float(p[1])
            except (TypeError, ValueError):
                errs.append(f"data_points[{i}] not numeric"); break
            if not (math.isfinite(m) and math.isfinite(g) and m > 0 and g > 0):
                errs.append(f"data_points[{i}] must be positive finite ({m}, {g})"); break
    if d.get("data_source", None) not in SOURCES:
        errs.append(f"data_source {d.get('data_source')!r} not recognised")
    ec = d.get("extraction_confidence")
    if ec is not None and not (0 <= float(ec) <= 1):
        errs.append("extraction_confidence outside [0,1]")
    return errs


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--snapshots", required=True)
    ap.add_argument("--full-pool", action="store_true")
    args = ap.parse_args()
    snaps = Path(args.snapshots)
    pool = ([p["arxiv_id"] for p in json.loads((ROOT / "data/manifest.json").read_text())["papers"]]
            if args.full_pool else json.loads((ROOT / "data/measured_pool_ids.json").read_text()))
    poolset = set(pool)
    sys.path.insert(0, str(ROOT))
    from scorer.conventions import classify_reported_convention, UNCONVERTIBLE  # noqa: E402

    n_ok = n_err = 0
    seen: set[str] = set()
    conv_warn: list[str] = []
    for f in sorted(snaps.glob("*.json")):
        if f.name in ("run.json", "metrics.json", "metrics_summary.json", "metadata_cache.json") or f.name.endswith("_failure_audit.json"):
            continue
        try:
            d = json.loads(f.read_text())
        except json.JSONDecodeError as e:
            print(f"ERROR {f.name}: not JSON ({e})"); n_err += 1; continue
        if d.get("status") == "error" or d.get("error"):
            print(f"note  {f.name}: error stub (will be skipped by the scorer, counts as missing)"); continue
        errs = check(d)
        aid = d.get("arxiv_id")
        if aid not in poolset:
            errs.append(f"arxiv_id {aid!r} is not in the pool")
        if aid in seen:
            errs.append(f"duplicate arxiv_id {aid}")
        seen.add(aid)
        if errs:
            n_err += 1
            for e in errs:
                print(f"ERROR {f.name}: {e}")
        else:
            n_ok += 1
        ct, decl = d.get("coupling_type"), d.get("coupling_convention")
        if ct and decl and d.get("data_points") and classify_reported_convention(ct, decl) == UNCONVERTIBLE:
            conv_warn.append(f"{aid}: {decl!r} for {ct} will be scored as a convention gap (see docs/TASK.md labels)")
    missing = [i for i in pool if i not in seen]
    print(f"\nvalid {n_ok} | invalid {n_err} | pool papers without a snapshot {len(missing)}")
    if missing[:10]:
        print("  missing e.g.:", ", ".join(missing[:10]), "..." if len(missing) > 10 else "")
    if conv_warn:
        print(f"\n{len(conv_warn)} declaration(s) the scorer will not accept:")
        for w in conv_warn:
            print("  ", w)
    return 1 if n_err else 0


if __name__ == "__main__":
    sys.exit(main())
