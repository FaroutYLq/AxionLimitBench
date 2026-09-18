# Failure-anatomy rubric (AxionLimitBench agent arm, Fable 5)

You are auditing why a generic tool-using agent MISSED on a paper of the AxionLimitBench benchmark.
"Miss" = its extracted limit curve was not within 0.3 dex (factor 2) of the AxionLimits curator's curve,
or it was not compared at all (wrong coupling type, abstained, convention gap). Work case by case, to the
depth of a referee: open the actual sources, quote numbers, decide who is right.

## Where things are (all read-only; never modify them)
- Bench repo: this repository
  - agent snapshot:      results/agent_claude_code/fable5/<id>.json   (id with "/" -> "_")
  - agent transcript:    results/agent_claude_code/fable5/<id>.events.jsonl  (stream-json; assistant tool_use blocks show every command; user blocks hold tool results)
  - pipeline snapshot:   results/aal_harness/fable5/<id>.json          (the domain pipeline on the same model, for contrast)
  - scorer per-paper:    results/agent_claude_code/fable5/metrics.json  (per_paper[] has comparison_status, interp_metrics, gt_file, coupling_type_expected)
  - ground truth entry:  data/papers.json (papers[] by arxiv_id; may have several entries = several curves)
  - ground truth curve:  data/ground_truth/<ground_truth_data_file>   (2 cols: mass [eV], coupling; sentinel rows y>=1e19 are fill walls, ignore)
  - task card the agent saw: docs/TASK.md (canonical plane + exact declaration label per coupling type)
  - scorer conventions:  scorer/conventions.py (what declarations it accepts/converts; ScalarPhoton/Electron "d_e_large" etc. are GT files stored in a non-canonical plane)
- Paper PDFs: ~/.cache/aal_pdf_cache/<id>.pdf  (use the Read tool with the `pages` parameter to look at specific pages/figures)
- The arXiv e-print (LaTeX + figure files) can be fetched: curl -sL https://arxiv.org/e-print/<id> -o /tmp/x.tar.gz (it is a tar.gz or a bare PDF/tex). Use a scratch dir under /private/tmp.
- Upstream curator repo for provenance of a GT file: the AutoAxionLimits checkout/limit_data/<...> (header comments often say which figure/scenario was digitised).

## For EACH paper produce
1. what_agent_did: 2-4 sentences from the transcript (which figure/file, which curve/scenario, conversions, points, declaration).
2. what_curator_has: which figure/scenario/plane the GT file encodes (from its header, its value range, the paper).
3. discrepancy: the concrete numbers (e.g. "agent 3.1e-3 GeV^-1 at 10 neV vs GT 1.1e-6": factor, direction, mass window overlap).
4. root_cause: ONE primary class from
   - digitisation      (axis calibration, wrong curve/panel/line style, inset vs main, log/linear mix-up, units on axis)
   - scenario          (agent chose a different but legitimate curve: other benchmark, prior, polarisation, mass regime, expected vs observed)
   - identification    (wrong coupling type; or abstained on a paper that does carry a measured limit)
   - convention        (right physics, plane/units/declaration mismatch; incl. squared vs linear, d_n vs g_d, 2m_N factors, rho_DM rescale)
   - ground_truth      (curator file is stale/erratum, different plane than declared, coarse, wrong, or encodes a scenario the task card would not pick)
   - scorer            (mass-window/zero-overlap artifact, best-match multi-GT choice, GT_point_reference, threshold edge 0.30-0.33)
   - task_card         (the miss follows directly from a task-card rule, e.g. theory predictions declared out of scope)
   - ambiguous         (paper genuinely underdetermines the answer)
   plus a secondary class if relevant.
5. who_is_right: agent | curator | both_defensible | neither | undetermined  (with the decisive evidence).
6. harness_catchable: could a deterministic guard (corroboration vs a quoted text anchor, axis sanity, unit-plane screen, range check) have caught it? yes/no + which.
7. severity: catastrophic (>3 dex) | large (1-3) | moderate (0.3-1) | not_compared.
8. lesson: one sentence, benchmark-facing (what AxionLimitBench of the task card / GT / scorer should change, or what the agent should have done).

Be quantitative and skeptical of BOTH sides: the curator's files are hand digitisations and sometimes stale; the agent's notes are self-reports. Verify against the PDF/e-print whenever the transcript alone does not settle it. Do not skip papers; if a source is unreachable, say so and give your best-supported verdict.

## Output
Write a JSON list (one object per paper, keys exactly: arxiv_id, what_agent_did, what_curator_has, discrepancy, root_cause, secondary_cause, who_is_right, evidence, harness_catchable, severity, lesson) to the OUT path given to you, then reply with a compact markdown table (arxiv_id | root_cause | who_is_right | severity | one-line lesson) and 3-5 sentences of cross-case synthesis.
