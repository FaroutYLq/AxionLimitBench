#!/usr/bin/env python3
"""Render REPORT.md from analysis/out/summary.json (+ per_paper.json)."""
import json, sys
from pathlib import Path

EXP = Path(__file__).resolve().parents[1]
out = Path(sys.argv[1]) if len(sys.argv) > 1 else EXP / "analysis" / "out"
S = json.loads((out / "summary.json").read_text())
P = json.loads((out / "per_paper.json").read_text())
byid = {p["arxiv_id"]: p for p in P}
f3 = lambda x: "n/a" if x is None else f"{x:.3f}"
pct = lambda x: "n/a" if x is None else f"{100*x:.0f}%"
q = S["paired_abs_delta_residual_dex"]; h = S["histogram_abs_delta_residual_dex"]
am = S["aggregate_medians"]; rs = S["reference_selection"]; fx = rs["fixed_reference"]; dc = S["direct_curve_comparison"]
pv = S["provenance"]; rm = S.get("run_meta") or {}
n = S["sample"]["n_selected"]
L = []
w = L.append
w("# Fable 5 agent repeatability: 100 papers, two fresh sessions each\n")
w(f"Generated from `analysis/out/summary.json`. Protocol: `protocol/PROTOCOL.md`; IDs: `protocol/selected_ids.json` (sha256 {S['sample']['selected_ids_sha256'][:16]}…).\n")
w("## Setup\n")
w(f"- Sample: {n} papers drawn uniformly without replacement (seed {S['sample']['seed']}) from the {S['sample']['population_size']}-paper reference-scorable measured-limit pool of AxionLimitBench at commit {S['scorer']['commit'][:12]}.")
w(f"- Agent: frozen benchmark driver `run_agent.py` v{list(pv['driver_version'])[0]} (imported unmodified), task card sha256 {list(pv['task_card_sha256'])[0][:16]}…, identical in all sessions.")
w(f"- Configuration: model requested {dict(pv['models_requested'])}; billed {dict(pv['models_billed'])}; init-event model {dict(pv['init_model'])}; effort {dict(pv['effort'])}; transport {dict(pv['transport'])}; Claude Code {dict(pv['claude_code_version'])}; permission mode {dict(pv['permission_mode'])}; tools {dict(pv['tools'])}; timeout {rm.get('config',{}).get('timeout_s')} s; cap ${rm.get('config',{}).get('max_budget_usd')} per session; {rm.get('config',{}).get('workers')} workers; queue {rm.get('queue_order')}.")
w(f"- Timing: started {rm.get('started_at')}, finished {rm.get('finished_at')}; sessions completed {rm.get('sessions_completed')} of {rm.get('n_sessions_planned')}; CLI-reported cost repeat1 ${pv['total_cost_usd'].get('repeat1',0):.2f}, repeat2 ${pv['total_cost_usd'].get('repeat2',0):.2f}.")
w(f"- Driver retry attempts (meta.attempt index): {dict(pv['attempt_index'])}; CLI result subtypes {dict(pv['cli_subtype'])}; timed out {dict(pv['timed_out'])}; leak-audit flags {dict(pv['leak_suspect'])}; snapshot status {dict(pv['status'])}.")
w(f"- Scorer: frozen `scorer/score.py` (measured-limits pool) run separately per repeat; score = per-paper median residual (dex) of a compared paper.\n")
w("## Coverage and outcome transitions\n")
w("| | repeat1 | repeat2 |\n|---|---|---|")
w(f"| attempted (snapshot present) | {S['attempted']['repeat1']} | {S['attempted']['repeat2']} |")
w(f"| finite residual score | {S['finite']['repeat1']} | {S['finite']['repeat2']} |")
w(f"| finite in both (common cohort) | {S['common_finite']} | |")
w(f"| finite in this repeat only | {len(S['finite_only_repeat1'])} {S['finite_only_repeat1']} | {len(S['finite_only_repeat2'])} {S['finite_only_repeat2']} |")
w(f"| finite in neither | {len(S['finite_in_neither'])} {S['finite_in_neither']} | |\n")
w("Outcome counts per repeat: " + "; ".join(f"{r}: {S['outcome_counts'][r]}" for r in ("repeat1", "repeat2")) + "\n")
w("Transitions (repeat1 → repeat2):\n")
w("| repeat1 | repeat2 | n |\n|---|---|---|")
for t in S["outcome_transitions_repeat1_to_repeat2"]:
    w(f"| {t['repeat1']} | {t['repeat2']} | {t['n']} |")
w("")
w("## Paired |Δ| of per-paper median residual (common finite cohort)\n")
w(f"n = {q['n']} papers. Median {f3(q.get('median'))} dex; Q1 {f3(q.get('q1'))}; Q3 {f3(q.get('q3'))}; p90 {f3(q.get('p90'))}; max {f3(q.get('max'))} dex. "
  f"Fraction below 0.01 dex: {pct(q.get('frac_lt_0.01'))} ({q.get('n_lt_0.01')}/{q['n']}); below 0.03 dex: {pct(q.get('frac_lt_0.03'))} ({q.get('n_lt_0.03')}/{q['n']}); below 0.1 dex: {pct(q.get('frac_lt_0.1'))} ({q.get('n_lt_0.1')}/{q['n']}).\n")
w(f"Histogram (`hist_abs_delta.png`), denominator = {h['denominator']} papers finite in both repeats:\n")
labels = ["<0.01", "0.01–0.03", "0.03–0.1", "0.1–0.3", "0.3–1", "1–3", ">3"]
w("| bin (dex) | " + " | ".join(labels) + " |\n|---|" + "---|" * len(labels))
w("| papers | " + " | ".join(str(c) for c in h["bin_counts"]) + " |\n")
big = sorted([p for p in P if p["abs_delta_dex"] is not None and p["abs_delta_dex"] >= 0.1], key=lambda p: -p["abs_delta_dex"])
if big:
    w(f"Papers with |Δ| ≥ 0.1 dex ({len(big)}):\n")
    w("| arXiv | repeat1 | repeat2 | |Δ| | ref1 | ref2 | source1 | source2 | type1 | type2 |\n|---|---|---|---|---|---|---|---|---|---|")
    for p in big:
        w(f"| {p['arxiv_id']} | {f3(p['repeat1_residual_dex'])} | {f3(p['repeat2_residual_dex'])} | {f3(p['abs_delta_dex'])} | {str(p['repeat1_gt_file']).replace('limit_data/','')} | {str(p['repeat2_gt_file']).replace('limit_data/','')} | {p['repeat1_data_source']} | {p['repeat2_data_source']} | {p['repeat1_coupling_type']} | {p['repeat2_coupling_type']} |")
    w("")
w("## Aggregate medians\n")
w("| cohort | repeat1 | repeat2 |\n|---|---|---|")
w(f"| own finite cohort | {f3(am['repeat1']['own_finite_cohort']['median_residual_dex'])} (n={am['repeat1']['own_finite_cohort']['n']}) | {f3(am['repeat2']['own_finite_cohort']['median_residual_dex'])} (n={am['repeat2']['own_finite_cohort']['n']}) |")
w(f"| common finite cohort (n={am['repeat1']['common_finite_cohort']['n']}) | {f3(am['repeat1']['common_finite_cohort']['median_residual_dex'])} | {f3(am['repeat2']['common_finite_cohort']['median_residual_dex'])} |\n")
w("## Reference selection vs extraction variation\n")
w(f"- Best-match reference (scorer rule #739) changed between repeats on {rs['n_reference_changed']} of {rs['n_common']} common-cohort papers ({rs['n_multi_candidate_papers_in_common']} of them have more than one candidate reference curve). IDs: {rs['reference_changed_ids']}.")
if rs['n_reference_changed']:
    w(f"  |Δ| on reference-changed papers: median {f3(rs['abs_delta_on_reference_changed'].get('median'))}, max {f3(rs['abs_delta_on_reference_changed'].get('max'))}; on unchanged: median {f3(rs['abs_delta_on_reference_unchanged'].get('median'))}, max {f3(rs['abs_delta_on_reference_unchanged'].get('max'))}.")
w(f"- Common fixed reference ({fx['rule']}): finite in both for {fx['n_finite_both']} papers; |Δ| median {f3(fx['abs_delta'].get('median'))}, Q3 {f3(fx['abs_delta'].get('q3'))}, p90 {f3(fx['abs_delta'].get('p90'))}, max {f3(fx['abs_delta'].get('max'))}; fraction < 0.03 dex {pct(fx['abs_delta'].get('frac_lt_0.03'))}. Repeat medians on that cohort: {f3(fx['repeat_medians_on_fixed_common']['repeat1'])} / {f3(fx['repeat_medians_on_fixed_common']['repeat2'])}.")
w(f"- Coupling type differed between repeats on {len(S['coupling_type_changed_ids'])} papers: {S['coupling_type_changed_ids']}.\n")
w("## Direct curve-to-curve agreement (independent of any reference)\n")
a, c = dc["all_pairs_with_curves"], dc["common_finite_cohort"]
w(f"{dc['definition']}. All pairs with two curves: n = {a['n']}, median {f3(a.get('median'))} dex, p90 {f3(a.get('p90'))}, max {f3(a.get('max'))}; common finite cohort: n = {c['n']}, median {f3(c.get('median'))}, p90 {f3(c.get('p90'))}, max {f3(c.get('max'))}. Pairs with two curves but no mass overlap: {dc['n_pairs_no_mass_overlap']}. "
  "This is extraction-to-extraction variation; the residual |Δ| above additionally folds in how each curve sits against the reference.\n")
sa = S["supplementary_archived_benchmark"]
w("## Supplementary: archived benchmark snapshots (different prompt/runtime history)\n")
w(f"Archived Fable run has snapshots for {sa['n_archived_snapshots_for_sample']} of the {n} papers, {sa['archived_finite']} finite; its median on the common cohort is {f3(sa['archived_median_on_common_finite_cohort'])} dex. |repeat − archived|: repeat1 median {f3(sa['repeat1_vs_archived'].get('median'))} (p90 {f3(sa['repeat1_vs_archived'].get('p90'))}, n={sa['repeat1_vs_archived']['n']}), repeat2 median {f3(sa['repeat2_vs_archived'].get('median'))} (p90 {f3(sa['repeat2_vs_archived'].get('p90'))}, n={sa['repeat2_vs_archived']['n']}). {sa['note']}.\n")
w("## Caveats\n")
w("- Two fresh runs give a paired repeatability estimate per paper; they do not measure a noise floor for the full 292-paper benchmark median and no standard error for that median is claimed here.")
w("- Timeouts, abstentions and invalid outputs were kept as outcomes; no session was re-run because of its score. Driver-internal retries are only for usage-limit / rate-limit errors and are listed in the attempt index above.")
w("- The subscription's weekly window was at 100% at launch, so sessions were billed to the account's enabled extra-usage pool on the same CLI (OAuth) transport; the archived benchmark ran inside the window. Same model, same CLI version, same transport label.")
w("- Extraction behaviour was not modified in response to these results.\n")
w("## Suggested factual sentences for the paper (not inserted)\n")
w(f"1. \"To measure the repeatability of the generic agent baseline, we drew {n} papers uniformly at random (seed {S['sample']['seed']}) from the {S['sample']['population_size']}-paper reference-scorable pool and ran two fresh, independent sessions per paper with an identical configuration (claude-fable-5, default effort, 1800 s timeout, \\$10 cap, same task card and tool permissions).\"")
w(f"2. \"Both repeats produced a finite score on {S['common_finite']} of the {n} papers ({S['finite']['repeat1']} and {S['finite']['repeat2']} finite individually); the per-paper median residual differed between repeats by a median of {f3(q.get('median'))} dex (Q1–Q3 {f3(q.get('q1'))}–{f3(q.get('q3'))}, p90 {f3(q.get('p90'))}, max {f3(q.get('max'))}), with {pct(q.get('frac_lt_0.03'))} of papers within 0.03 dex and {pct(q.get('frac_lt_0.1'))} within 0.1 dex.\"")
w(f"3. \"The aggregate median residual was {f3(am['repeat1']['own_finite_cohort']['median_residual_dex'])} dex in the first repeat and {f3(am['repeat2']['own_finite_cohort']['median_residual_dex'])} dex in the second ({f3(am['repeat1']['common_finite_cohort']['median_residual_dex'])} and {f3(am['repeat2']['common_finite_cohort']['median_residual_dex'])} dex on the common cohort).\"")
w(f"4. \"The best-matching reference curve changed between repeats on {rs['n_reference_changed']} of {rs['n_common']} common papers; holding the reference fixed by a score-independent rule gives a median |Δ| of {f3(fx['abs_delta'].get('median'))} dex (n = {fx['n_finite_both']}), and the direct curve-to-curve disagreement between repeats has median {f3(c.get('median'))} dex (p90 {f3(c.get('p90'))}) on the same cohort.\"")
w("5. \"With two repeats this characterises paired per-paper repeatability; it is not a standard error on the full-benchmark median.\"")
(out / "REPORT.md").write_text("\n".join(L) + "\n")
print((out / "REPORT.md").read_text()[:1500])
