"""Validate quadrature resolution on identical frozen inputs; no inference."""
import argparse
import contextlib
import io
import json
from pathlib import Path
import tempfile

from . import rescore
from .rescore import HERE, qualifies, run, dump


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--benchmark-root", type=Path, required=True)
    ap.add_argument("--results", type=Path, default=Path("paper/revision/rescored"))
    args = ap.parse_args()
    protocol = json.loads((HERE / "protocol.json").read_text())
    protocol["grid_size"] = 8192
    decisions = json.loads((HERE / "reference_decisions.json").read_text())["papers"]
    baseline = {(r["arm"], r["arxiv_id"]): r for r in json.loads((args.results / "per_paper.json").read_text())}
    with tempfile.TemporaryDirectory(prefix="aal-quadrature-") as tmp:
        out = Path(tmp)
        rescore.compare = rescore.compare_quadrature
        with contextlib.redirect_stdout(io.StringIO()):
            run(args.benchmark_root.resolve(), out, protocol, decisions)
        high = json.loads((out / "per_paper.json").read_text())
    changes = []
    for r in high:
        old = baseline[(r["arm"], r["arxiv_id"])]
        assert r["status"] == old["status"]
        for factor in protocol["tolerances_factors"]:
            before, after = (qualifies(x["comparison"], factor) for x in (old, r))
            if before != after:
                changes.append({"arm": r["arm"], "arxiv_id": r["arxiv_id"],
                                "factor": factor, "baseline_pass": before, "high_resolution_pass": after})
    result = {"baseline_integration": "exact piecewise-linear", "check_grid": 8192, "paper_arm_records": len(high),
              "changed_classifications": changes,
              "note": "Independent quadrature cross-check only; primary exact-integration outputs are unchanged."}
    dump(args.results / "quadrature_check.json", result)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
