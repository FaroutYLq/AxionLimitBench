# PDU evaluation supplement v0.1.3

This update adds reproduction of the current Table 1 and Figure 3: standalone
pointwise-agreement pass rates, 95% bootstrap intervals for pointwise agreement
and joint success, and the pointwise-agreement threshold distribution.

Pointwise agreement uses all finite comparisons (agents 281/271/218; pipelines
261/259/222). Coverage and joint success use the established curve-eligible
cohorts (272/262/209 and 249/248/208). A pointwise pass requires at least 90% of
compared points within 0.3 dex; joint success also requires both mass-range
coverages above 90%, using the same reference. Intervals resample papers 20,000
times with fixed seeds. These conditional rates do not replace the original
AxionLimitBench leaderboard definition.

No extraction runs, frozen reference choices, coverage policies, or existing
joint-success counts changed. Figure 4 retains its median-residual analysis.
The original 200 repeatability predictions and complete agent event transcripts
are retained. Private manuscript revision conversations, the referee reply,
manuscript backups, and full manuscript-page previews are excluded.

Download both archives and extract them into one directory:

- `pdu-revision-2026-11-04-analysis.tar.gz`: complete frozen inputs, software,
  results, protocols, and figure sources, including this update.
- `pdu-revision-2026-11-04-transcripts.tar.gz`: 200 repeatability agent transcripts
  (identical to v0.1.2).
- `SHA256SUMS`: archive checksums.

Follow the included README to run offline reproduction without model access.
The updated generator is `paper/revision/pointwise_success_20261104/make_outputs.py`.
Earlier residual-table and CDF scripts remain as historical diagnostics.

Agent setup: https://doi.org/10.5281/zenodo.22880507 (accepted to ML4PS 2026).
Previous complete supplement: https://doi.org/10.5281/zenodo.23943063.
Original benchmark: https://doi.org/10.5281/zenodo.22838234.
