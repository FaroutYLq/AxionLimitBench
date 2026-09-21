---
license: mit
pretty_name: AxionLimitBench
language:
- en
tags:
- physics
- dark-matter
- benchmark
- agents
- information-extraction
size_categories:
- n<1K
---

# AxionLimitBench

A benchmark for extracting experimental exclusion limits from particle-physics papers.
Given a paper that bounds an axion, dark-photon or other light-boson coupling, a system
must decide whether the paper reports a new measured limit, identify the coupling, and
return the excluded-region boundary as a curve in a canonical (mass, coupling) plane.
Each answer is graded against the curve the maintainer of the
[AxionLimits](https://github.com/cajohare/AxionLimits) compilation committed for that paper.

- **292 graded papers**, 13 coupling types. Papers whose reference cannot grade any
  extraction (prediction bands, published-only data, superseded versions) are excluded with
  recorded evidence (`data/EXCLUSIONS.md`).
- The [GitHub repository](https://github.com/FaroutYLq/AxionLimitBench) is the canonical home
  of the benchmark (references, task card, prediction schema, frozen scorer, baselines). This
  dataset mirrors it and adds what is too large for git: the full tool transcript of every
  agent session (`results/*/*/<id>.events.jsonl`, about 3 GB).
- Headline metric: **success rate**, the fraction of graded papers whose curve is within 10%
  (0.041 dex) of the reference; abstentions, wrong coupling types and unconvertible declarations
  count as misses.
- Paper: *AxionLimitBench: can AI curate a dark matter constraint repository?* (ML4PS 2026, submitted):
  [10.5281/zenodo.22880507](https://doi.org/10.5281/zenodo.22880507); the PDF is also [`paper.pdf`](https://huggingface.co/datasets/FaroutYLq/AxionLimitBench/blob/main/paper.pdf) in this repository.
- Archived on Zenodo: https://doi.org/10.5281/zenodo.22838233

## Leaderboard

| system | model | success rate | compared | cond. median [dex] | catastrophic | $/paper |
|---|---|---|---|---|---|---|
| generic agent (Claude Code, 7 tools, task card only) | claude-fable-5 | **56%** | 97% | 0.02 | 0.0% | 1.48 |
| generic agent | claude-opus-4-8 | 47% | 93% | 0.04 | 0.7% | 0.99 |
| AutoAxionLimits pipeline | claude-fable-5 | 19% | 90% | 0.16 | 3.8% | 0.88 |
| AutoAxionLimits pipeline | claude-opus-4-8 | 14% | 89% | 0.18 | 3.5% | 0.44 |
| generic agent | claude-haiku-4-5 | 9% | 75% | 0.38 | 7.3% | 0.28 |
| AutoAxionLimits pipeline | claude-haiku-4-5 | 5% | 77% | 0.62 | 17.6% | 0.09 |

## Contents

```
data/            papers.json (labels), ground_truth/*.txt (reference curves), manifest.json,
                 measured_pool_ids.json, EXCLUSIONS.md, PLANE_AUDIT.md, fetch_pdfs.py
docs/TASK.md     the task card every system sees
schema/          prediction JSON schema
scorer/          frozen scorer (python3 -m scorer.score --snapshots DIR)
baselines/       reference agent driver (Claude Code, headless) and leak audit
results/         per-system, per-paper predictions (<id>.json), scores (metrics.json),
                 leaderboard, failure audits, and for agent runs the full session
                 transcripts (<id>.events.jsonl, stream-json)
```

PDFs are not redistributed; `data/fetch_pdfs.py` downloads them from arXiv.

## Evaluate your own system

1. Read `docs/TASK.md`. Give your system the PDF (and, if you like, the paper's own arXiv
   e-print) and nothing else: no compilations, HEPData, INSPIRE or web search.
2. For each id in `data/measured_pool_ids.json`, write `results/<system>/<run>/<id>.json`
   in the prediction schema, plus a `run.json` with model, date and any caps.
3. `python3 -m scorer.validate --snapshots results/<system>/<run>` then
   `python3 -m scorer.score --snapshots results/<system>/<run> --report`.

## Citation

See `CITATION.cff`. Reference curves are from cajohare/AxionLimits (MIT, Ciaran O'Hare).
