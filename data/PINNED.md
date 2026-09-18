# Pinned provenance (AxionLimitBench the initial ingestion.0)

- Ground truth: `AutoAxionLimits` `evaluation/ground_truth/` at commit `73682236` (origin/master, 2026-09-09).
  `papers.json`, `data/*.txt`, `EXCLUSIONS.md` and `PHASE4_convention_audit.md` are copied verbatim.
- Curves originate from `cajohare/AxionLimits` `limit_data/` (MIT licence), ingested with the
  header-declared unit conversions documented in `evaluation/ground_truth.py` of AutoAxionLimits
  (lambda[m] -> eV on fifth-force files; per-file y/x scale factors for COBEFIRAS_Cyr and Xenon1T).
- Measured-limits pool (329 papers) = one representative entry per arXiv id, projection-only papers dropped.
- Scorable pool (312 papers) = measured pool minus papers whose every ground-truth entry is excluded
  (see EXCLUSIONS.md: prediction-band files, published-only/private data).
- Four entries had no file under `evaluation/ground_truth/data/` in AutoAxionLimits (the original scorer
  fell back to the repo's `limit_data/` at scoring time). They were ingested here with the same
  `_ingest_reference_file` rule so the benchmark is self-contained: 2305.00890 (DarkPhoton/AMAILS.txt),
  2503.14582 (AxionPhoton/JWST_Saha.txt), 1609.00667 (AxionPhoton/NuSTAR.txt), 2007.04899
  (VectorB-L/Projections/OptomechanicalMembranes.txt, projection pool only). Verified: rescoring the
  Fable-5 harness snapshots with the vendored scorer reproduces the committed metrics bit-for-bit
  (micro 0.16648 dex, 267 compared, ct 0.98077, identical status counts).
