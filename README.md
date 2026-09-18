# AxionLimitBench

*Can AI curate a dark matter constraint repository?*

A benchmark for extracting experimental exclusion limits from particle-physics
papers. Given a paper that bounds an axion, dark-photon or other light-boson
coupling, a system must decide whether the paper reports a new measured limit,
identify the coupling, and return the excluded-region boundary as a curve in a
canonical (mass, coupling) plane. Each answer is graded against the curve the
maintainer of the [AxionLimits](https://github.com/cajohare/AxionLimits)
compilation committed for that paper.

- **292 graded papers**, 13 coupling types. Papers whose reference cannot grade
  any extraction (prediction bands, published-only data, superseded versions)
  are excluded with recorded evidence (`data/EXCLUSIONS.md`).
- The task card every system sees: [`docs/TASK.md`](docs/TASK.md).
  Prediction format: [`schema/prediction.schema.json`](schema/prediction.schema.json).
- Frozen scorer, one-command rescore, and every baseline's raw predictions are
  in the repo, so any number here can be reproduced offline.
- Paper: *AxionLimitBench: can AI curate a dark matter constraint repository?*
  (ML4PS 2026, submitted). Companion paper on the pipeline baseline:
  [arXiv:2606.21658](https://arxiv.org/abs/2606.21658).

## Leaderboard

Success rate = fraction of the 292 papers whose curve is within 10% (0.041 dex)
of the reference; abstentions, wrong coupling types, unconvertible declarations
and zero-overlap curves all count as misses. Compared = fraction with a gradable
curve. Conditional median and catastrophic fraction (>3 dex) are over compared
papers. Agent cost is the CLI's nominal API-equivalent charge; pipeline cost the
companion paper's list-price estimate.

| system | model | success rate | compared | cond. median [dex] | catastrophic | type acc. | $/paper |
|---|---|---|---|---|---|---|---|
| generic agent (Claude Code, 7 tools, task card only) | claude-fable-5 | **56%** | 97% | 0.02 | 0.0% | 100% | 1.48 |
| generic agent | claude-opus-4-8 | 47% | 93% | 0.04 | 0.7% | 98% | 0.99 |
| AutoAxionLimits pipeline | claude-fable-5 | 19% | 90% | 0.16 | 3.8% | 98% | 0.88 |
| AutoAxionLimits pipeline | claude-opus-4-8 | 14% | 89% | 0.18 | 3.5% | 98% | 0.44 |
| generic agent | claude-haiku-4-5 | 9% | 75% | 0.38 | 7.3% | 86% | 0.28 |
| AutoAxionLimits pipeline | claude-haiku-4-5 | 5% | 77% | 0.62 | 17.6% | 93% | 0.09 |

Full table with counts, status breakdowns and the factor-of-two fraction:
[`results/LEADERBOARD.md`](results/LEADERBOARD.md). Every agent session's
transcript was kept and audited for access to compilations, HEPData or INSPIRE
(`baselines/agent_claude_code/audit_leaks.py`; none found).

## Quickstart: evaluate your own system

```bash
git clone https://github.com/FaroutYLq/AxionLimitBench && cd AxionLimitBench
pip install -r requirements.txt
python3 data/fetch_pdfs.py --out ~/axlb_pdfs          # PDFs are not redistributed; ~20 min from arXiv
```

1. Read [`docs/TASK.md`](docs/TASK.md). Give your system the PDF (and, if you
   like, the paper's own arXiv e-print) and nothing else: no compilations,
   HEPData, INSPIRE or web search.
2. For each arXiv id in `data/measured_pool_ids.json`, write
   `results/<your_system>/<run>/<id>.json` in the prediction schema
   (`/` in an id becomes `_`). Add a `run.json` with model, date and any caps.
3. Validate, score, rebuild the leaderboard:

```bash
python3 -m scorer.validate --snapshots results/<your_system>/<run>
python3 -m scorer.score    --snapshots results/<your_system>/<run> --report
python3 results/leaderboard.py
```

`scorer.validate` warns about `coupling_convention` labels the scorer will not
recognise (they count as misses), so fix those before scoring.

## Metrics

Headline: success rate at 10%. Secondary: compared fraction, conditional median
residual over compared papers, catastrophic fraction (>3 dex), coupling-type
accuracy, cost and turns. The fraction within a factor of two (0.3 dex) is kept
in the full leaderboard; the per-paper failure audits were done at that
tolerance. On references re-digitised from tables a perfect extraction sits
about 0.03 dex from the reference, so residuals near that level measure the
reference's own digitisation.

## Budget policy

The benchmark imposes **no cost, token, turn or wall-clock cap**. Any cap a
submitter applies is a property of their run and must be recorded in
`run.json` (the reference agent runs used a 10-dollar per-paper cap and a
30-minute wall clock).

## Layout

```
data/            manifest.json, papers.json (labels), ground_truth/*.txt, fetch_pdfs.py,
                 measured_pool_ids.json, EXCLUSIONS.md, PLANE_AUDIT.md, PINNED.md
docs/TASK.md     the task card
schema/          prediction JSON schema
scorer/          frozen scorer (vendored from AutoAxionLimits), validate.py, score.py, tests/
baselines/       agent_claude_code/run_agent.py (reference agent), audit_leaks.py
results/         per-system snapshots, metrics, leaderboard, failure audits
hf/              Hugging Face dataset card and upload script
```

## Reproducing the reference agent runs

```bash
python3 baselines/agent_claude_code/run_agent.py --outdir results/agent_claude_code/<run> --model <model> --workers 3
```

Needs the Claude Code CLI on PATH (subscription login or `ANTHROPIC_API_KEY`).
Each paper runs in a throwaway directory with seven tools; the task card is
appended to the system prompt; transcripts are kept as `<id>.events.jsonl`.

## Known limitations

- Reference curves are single hand digitisations: residuals below ~0.1 dex are
  not meaningful. The compilation records neither the arXiv version nor the
  scenario its curator chose, so some references contradict the paper a system
  reads today; those found so far are excluded with evidence.
- The reference files are public on GitHub and so plausibly in training data;
  the agent transcripts show each curve being derived from the paper, and no
  session accessed a secondary source.
- Noisy or banded limits: the scorer evaluates at every reference vertex, so a
  smoothed trace of a spiky limit pays the reference's own scatter, and the
  task card does not say which edge or statistic the compilation records.
- The compilation's own planes are inconsistent in places (its B-L axis mixes
  ε and g across files); every correction is documented in
  `data/PLANE_AUDIT.md`.

## Mirrors and versions

The full agent transcripts (`*.events.jsonl`, about 3 GB) are too large for git
and are published with everything else in the Hugging Face dataset mirror:
https://huggingface.co/datasets/FaroutYLq/AxionLimitBench. Releases are tagged
here and archived on Zenodo: https://doi.org/10.5281/zenodo.22838233 (concept DOI, latest version;
v0.1.1 is https://doi.org/10.5281/zenodo.22838234).

## Licence and citation

MIT (see `LICENSE`, `CITATION.cff`). Reference curves are from
cajohare/AxionLimits (MIT, Ciaran O'Hare).
