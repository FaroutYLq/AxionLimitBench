"""Per-paper diff between two scorings of the same snapshots.

    python3 results/diff_scores.py <old>/metrics.json <new>/metrics.json
"""
import json, math, sys
def load(p):
    m = json.load(open(p)); out = {}
    for x in m["per_paper"]:
        cs = x.get("comparison_status") or ("excluded_gt" if x.get("status") == "excluded_gt" else None)
        r = (x.get("interp_metrics") or {}).get("median_residual_dex")
        try: r = float(r)
        except (TypeError, ValueError): r = None
        if r is not None and not math.isfinite(r): cs, r = "zero_overlap", None
        out[x["arxiv_id"]] = (cs, r)
    return out
a, b = load(sys.argv[1]), load(sys.argv[2])
import math as _m
TAU = float(__import__("os").environ.get("AXLB_TAU", _m.log10(1.1)))   # headline 10%; AXLB_TAU=0.3 for the 2x column
hit = lambda v: v[0] == "compared" and v[1] is not None and v[1] <= TAU
ha, hb = sum(hit(v) for v in a.values()), sum(hit(v) for v in b.values())
print(f"hits: {ha} -> {hb}   (papers {len(a)})")
ch = []
for k in a:
    if k in b and (a[k][0] != b[k][0] or (a[k][1] is not None and b[k][1] is not None and abs(a[k][1] - b[k][1]) > 1e-6) or ((a[k][1] is None) != (b[k][1] is None))):
        ch.append((k, a[k], b[k]))
print(f"papers changed: {len(ch)}")
for k, x, y in sorted(ch, key=lambda t: -(abs((t[1][1] or 0) - (t[2][1] or 0)))):
    f = lambda v: f"{v[0]}" + (f" {v[1]:.3f}" if v[1] is not None else "")
    print(f"  {k:14s} {f(x):28s} -> {f(y)}")
