# Revised PDU evaluation and agent repeatability supplement

Reproducibility files supporting the revised evaluation in *Towards LLM-Powered
Automation of a Dark Matter Constraint Repository*.

This supplement preserves the frozen AxionLimitBench source at
`ac1542965b7c6b254238312a4d735d90c5a3a472` and adds the revised coverage and joint
success analyses, outcome audits, numerical table and figure scripts, and the
100-paper Fable 5 agent repeatability study. It does not change the original
AxionLimitBench leaderboard or introduce a new production extraction method.

Download both archives and extract them into the same directory:

- `pdu-revision-2026-11-04-analysis.tar.gz`: frozen inputs, software, predictions,
  analysis outputs, protocols, and figures.
- `pdu-revision-2026-11-04-transcripts.tar.gz`: all 200 new agent event transcripts.
- `SHA256SUMS`: checksums of both archives.

The included README explains offline reproduction. The coverage results,
outcome table, numerical results table, and repeatability statistics were
recomputed and matched the saved outputs. All Python figures and the TikZ
architecture diagram were regenerated. No new model calls were made during
packaging or verification.

Existing benchmark and agent setup:

- Source: https://github.com/FaroutYLq/AxionLimitBench
- Benchmark v0.1.1: https://doi.org/10.5281/zenodo.22838234
- Companion manuscript (accepted to ML4PS 2026): https://doi.org/10.5281/zenodo.22880507
- Earlier benchmark transcripts: https://huggingface.co/datasets/FaroutYLq/AxionLimitBench

Coverage-qualified percentages are conditional on eligible finite comparisons.
They differ from the original benchmark leaderboard's success definition.
The repeatability study measures repeated extraction on a frozen sample, not
prospective generalization or a measured reduction in manual curation time.
