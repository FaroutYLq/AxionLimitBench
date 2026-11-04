#!/usr/bin/env python3
"""Freeze the 100-paper repeatability sample.

Population: the frozen AxionLimitBench measured-limit pool restricted to papers
whose reference can grade an extraction (manifest.json: in_measured_pool AND
scorable). Eligibility depends only on reference availability -- never on any
previous extraction's success or residual.

Sampling: uniform without replacement, Python random.Random(20261103).sample
over the SORTED id list (string sort), n = 100.
"""
import hashlib, json, random, sys, time
from pathlib import Path

FROZEN = Path("/private/tmp/axionlimitbench-revision-source")
SEED = 20261103
N = 100
OUT = Path(__file__).resolve().parent

man = json.loads((FROZEN / "data/manifest.json").read_text())
pool = sorted(p["arxiv_id"] for p in man["papers"] if p["in_measured_pool"] and p["scorable"])
assert len(pool) == man["n_scorable"] == 292, len(pool)
measured = json.loads((FROZEN / "data/measured_pool_ids.json").read_text())
assert set(pool) <= set(measured)
rng = random.Random(SEED)
sample = rng.sample(pool, N)          # order of draw kept as the processing order
assert len(set(sample)) == N
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
out = {
    "protocol": "uniform sample without replacement, random.Random(seed).sample(sorted_pool, n)",
    "seed": SEED, "n": N,
    "population": "manifest.json papers with in_measured_pool and scorable (reference-scorable measured-limit pool)",
    "population_size": len(pool),
    "population_sha256": hashlib.sha256(json.dumps(pool).encode()).hexdigest(),
    "manifest_sha256": sha(FROZEN / "data/manifest.json"),
    "measured_pool_ids_sha256": sha(FROZEN / "data/measured_pool_ids.json"),
    "frozen_source": str(FROZEN), "frozen_commit": "ac1542965b7c6b254238312a4d735d90c5a3a472",
    "python": sys.version.split()[0],
    "frozen_at": time.strftime("%Y-%m-%dT%H:%M:%S%z"),
    "ids_in_draw_order": sample,
    "ids_sorted": sorted(sample),
}
(OUT / "selected_ids.json").write_text(json.dumps(out, indent=1))
(OUT / "population_ids.json").write_text(json.dumps(pool, indent=1))
print(len(pool), len(sample), sample[:5])
