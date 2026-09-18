# AxionLimitBench leaderboard

Success rate = fraction of scorable papers whose curve is within 10% (0.041 dex) of the reference; abstentions, wrong coupling type, convention gaps and zero-overlap curves all count as misses. Within 2x = the same at 0.3 dex. Catastrophic = median residual > 3.0 dex among compared papers. The pipeline's measured run-to-run noise is about +/-0.04 dex on the conditional median.

| system | run | model | scorable | compared | coverage | **success rate (10%)** | within 2x | cond. median [dex] | catastrophic | ct acc. | median $/paper | median turns |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| agent_claude_code | fable5 | claude-fable-5 | 289 | 281 | 0.972 | **0.564** (163) | 0.896 (259) | 0.024 | 0 | 0.997 | 1.48 | 15 |
| agent_claude_code | opus48 | claude-opus-4-8 | 290 | 271 | 0.934 | **0.469** (136) | 0.831 (241) | 0.041 | 2 | 0.983 | 0.99 | 18 |
| aal_harness | fable5 | claude-fable-5 | 290 | 261 | 0.900 | **0.190** (55) | 0.590 (171) | 0.160 | 10 | 0.983 | - | - |
| aal_harness | opus48 | claude-opus-4-8 | 290 | 259 | 0.893 | **0.145** (42) | 0.566 (164) | 0.183 | 9 | 0.983 | - | - |
| agent_claude_code | haiku45 | claude-haiku-4-5-20251001 | 290 | 218 | 0.752 | **0.090** (26) | 0.334 (97) | 0.376 | 16 | 0.856 | 0.28 | 18 |
| aal_harness | haiku45 | claude-haiku-4-5-20251001 | 290 | 222 | 0.766 | **0.048** (14) | 0.217 (63) | 0.616 | 39 | 0.931 | - | - |

## Status counts

- **agent_claude_code/fable5**: {"compared": 281, "gt_unusable": 2, "no_comparable_gt": 7, "excluded_gt": 38, "no_extracted_points": 1}; snapshots missing 0, error 0, leak suspects 0, timeouts 0
- **agent_claude_code/opus48**: {"compared": 275, "no_prediction": 3, "gt_unusable": 1, "no_comparable_gt": 8, "no_extracted_points": 4, "excluded_gt": 38}; snapshots missing 0, error 0, leak suspects 0, timeouts 0
- **aal_harness/fable5**: {"compared": 265, "convention_mismatch": 9, "gt_unusable": 1, "no_comparable_gt": 14, "excluded_gt": 38, "no_extracted_points": 2}; snapshots missing 0, error 0, leak suspects 0, timeouts 0
- **aal_harness/opus48**: {"compared": 261, "no_comparable_gt": 14, "gt_unusable": 1, "convention_mismatch": 13, "excluded_gt": 38, "no_extracted_points": 2}; snapshots missing 0, error 0, leak suspects 0, timeouts 0
- **agent_claude_code/haiku45**: {"compared": 242, "no_prediction": 36, "gt_unusable": 1, "excluded_gt": 38, "no_extracted_points": 4, "no_comparable_gt": 8}; snapshots missing 0, error 0, leak suspects 1, timeouts 0
- **aal_harness/haiku45**: {"compared": 246, "no_comparable_gt": 27, "gt_unusable": 1, "convention_mismatch": 11, "excluded_gt": 38, "no_extracted_points": 4, "no_prediction": 1}; snapshots missing 1, error 0, leak suspects 0, timeouts 0
