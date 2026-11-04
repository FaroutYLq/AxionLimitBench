# PDU revised evaluation: reproducibility supplement

Prepared 4 November 2026. This supplement contains analysis software and research artifacts;
it does not contain the revised manuscript or the referee report.

## What this supplements

The frozen AxionLimitBench source is commit
`ac1542965b7c6b254238312a4d735d90c5a3a472`:
https://github.com/FaroutYLq/AxionLimitBench/tree/ac1542965b7c6b254238312a4d735d90c5a3a472.
The existing benchmark v0.1.1 archive is
https://doi.org/10.5281/zenodo.22838234; it does not contain this supplement.
The agent setup is described in the companion manuscript,
https://doi.org/10.5281/zenodo.22880507 (accepted to ML4PS 2026).
Historical pipeline software is maintained at
https://github.com/FaroutYLq/AutoAxionLimits.

This supplement adds:

- Two mass-range coverage measures and a joint coverage/pointwise-agreement
  success criterion for six saved model/workflow configurations.
- Explicit per-paper exclusions, cohort membership, and reference assignments.
- Agent/pipeline evaluation outcomes, convention-override and guard audits.
- Two fresh Fable 5 agent sessions for each of 100 frozen randomly selected
  papers: 200 predictions, 200 complete event transcripts, protocol, provenance,
  scorer outputs, and paired repeatability analysis.
- Scripts and frozen inputs for the revised numerical tables and figures.

No extraction is performed by the reproduction command. Offline analysis does
not require Claude Code, credentials, a subscription, or input paper PDFs.

## Reproduce

Extract the compact analysis archive and the transcript archive into the same
parent directory. Both populate `pdu-revision-2026-11-04/`. Preserve this layout.
From that directory, verify the files with `shasum -a 256 -c MANIFEST.sha256`.
With Python 3.10 or later and the dependencies in `requirements.txt` installed:

```bash
python reproduce.py --out /absolute/path/to/new-output-directory
```

For the author's local setup, activate `conda activate straxion` first.
The command creates a separate working copy, reruns coverage, the outcome table,
the main numerical table, and repeatability scoring, and compares the results
with the frozen outputs. Read `verification.json` and the per-step logs in the
output directory. The input archive remains unchanged.

To also regenerate the Python figures:

```bash
python reproduce.py --out /another/new-output-directory --figures
```

The showcase plot additionally requires a working LaTeX installation on PATH
for Matplotlib text rendering. The architecture diagram can be rebuilt with
`pdflatex main.tex` in `paper/revision/figures/figure1_architecture_preview/`.
Generated PDF bytes can vary with plotting/LaTeX versions; the numerical inputs
and statistics are the reproducibility targets.

## Layout

- `benchmark/`: frozen benchmark data, predictions, scorer, task card, and driver.
- `evaluation/revision/`: coverage analysis implementation and exclusion policies.
- `paper/revision/ml4ps_coverage/`: adopted coverage and joint-success results.
- `paper/revision/disposition_audit/`: outcomes for all 329 Fable papers per workflow.
- `paper/revision/convention_override_audit/` and `pipeline_guard_note_check/`:
  recorded audit outputs; rule occurrences do not validate the underlying decisions.
- `paper/revision/repeatability_fable5_agent_100papers/`: full repeatability study.
- `paper/revision/figures/`, `paper/revision/tables/`: plotting and table code.
- `evaluation/eval_runs/`: selected historical pipeline repeatability inputs.
- `figure2_background/`: frozen plotting code and constraint files for the showcase.
- `paper/figures/`: reference figure PDFs, without the manuscript.
- `RELEASE.json`: provenance and explicit path-only portability edits.
- `MANIFEST.sha256`: checksums of the release files.

The `paper/` folder here contains reproducibility inputs and figure sources only;
it is not the private manuscript folder. Historical provenance records retain
original paths as evidence. Production/extraction scripts in `benchmark/` and
the study protocol are archival; rerunning those can require network access and
paid model service. They are not called by `reproduce.py`.

## Interpretation

Coverage is computed on the adopted finite-comparison cohorts, excluding
point-only references and ten documented zero-mass cases. Point-only predictions
against extended references remain included and fail coverage. Both coverages
must exceed 90%, and at least 90% of archived comparison points must agree within
0.3 dex with the same reference. These conditional percentages differ from the
original AxionLimitBench leaderboard definition and do not replace it.

The 100-paper repeatability sample came from the manifest's 292-paper pool.
One member of that population is excluded by the main-results scorer, but was
not selected in the sample. Repeated scores measure repeatability, not
generalization to new papers or time saved in manual curation.

The QUALIPHIDE plot is an illustrative case study, separate from the benchmark;
it is not a blinded benchmark result. Reference compilation scope and scenario
choices can differ from the supplied paper. Consult the per-paper records.

The six original benchmark transcript collections remain distributed through
https://huggingface.co/datasets/FaroutYLq/AxionLimitBench. This supplement contains
the 200 new repeatability transcripts, not a duplicate of those earlier logs.

## Attribution

Preserve the included licenses and citations. Benchmark source and data retain
their original notices in `benchmark/LICENSE` and `benchmark/CITATION.cff`.
The showcase background retains the original AxionLimits license and attribution
in `figure2_background/`. Numerical source papers are identified by arXiv ID;
paper PDFs are not redistributed. See the companion benchmark's data provenance
for the underlying curated constraint files.
