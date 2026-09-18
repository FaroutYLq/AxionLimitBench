# AutoAxionLimits Extraction Pipeline — Evaluation Report

## Summary

- **Papers evaluated**: 328
- **Papers with curve comparison**: 246

## Curve-Comparison Coverage

A curve is scored only against a ground-truth curve of the **same coupling**. Papers whose extracted coupling has no matching GT curve are not comparable and are excluded from residual statistics (this is not an extraction failure).

| Status | Papers | Meaning |
|--------|--------|---------|
| compared | 246 | scored against a same-coupling GT curve |
| no_comparable_gt | 27 | extracted coupling has no GT curve in the pool (usually a coupling misclassification) |
| convention_mismatch | 11 | same coupling but the GT curve uses a different convention/units (e.g. f_a [GeV] vs normalized, or d_e vs a large-valued variable) — excluded as a units gap, not extraction error |
| gt_unusable | 1 | GT curve has <2 usable points after boundary filtering |
| no_extracted_points | 4 | pipeline returned no data points |
| no_prediction | 1 | pipeline returned no coupling type |
| excluded_gt | 38 | every GT entry for this paper is excluded with a documented reason (see Excluded GT Entries below) — not scored |

## Excluded GT Entries (42)

These ground-truth entries cannot grade any extraction (documented, reversible — see `evaluation/ground_truth/EXCLUSIONS.md`). They are skipped by all scoring but listed here so exclusions stay visible.

| arXiv ID | Repo file | Coupling | Reason |
|----------|-----------|----------|--------|
| 2201.02042 | limit_data/ScalarPhoton/CsCav.txt | ScalarPhoton | Reference matches neither curve of the paper's exclusion figure |
| 2201.02042 | limit_data/ScalarElectron/CsCav.txt | ScalarElectron | Reference matches neither curve of the paper's exclusion figure |
| 1505.07455 | limit_data/AxionMass/Berkowitz15.txt | AxionMass | AxionMass prediction-band file: both columns are masses (m_lo, m_hi) — there is no coupling column, so no extraction can match it; the extractor's refusal (0 points) is correct behavior for these papers. |
| 2312.13723 | limit_data/ScalarElectron/Cavities.txt | ScalarElectron | Reference digitised from a superseded arXiv version |
| 1202.5851 | limit_data/AxionMass/Kawasaki12.txt | AxionMass | AxionMass prediction-band file: both columns are masses (m_lo, m_hi) — there is no coupling column, so no extraction can match it; the extractor's refusal (0 points) is correct behavior for these papers. |
| 1609.00667 | limit_data/AxionPhoton/NuSTAR.txt | AxionPhoton | Paper publishes sterile-neutrino limits only (sin^2(2theta) vs mass, decay rate Gamma vs mass) from the NuSTAR X-ray line search; it never quotes an axion-photon coupling. The repo AxionPhoton/NuSTAR.txt g_agamma curve is the maintainer's derived conversion of the same X-ray line flux limit to decaying-ALP DM, so the GT demands a quantity that is not extractable from the paper. |
| 2110.10262 | limit_data/AxionPhoton/ADMX_Sidecar_JTWPA.txt | AxionPhoton | Reference follows a figure mass axis inconsistent with the paper's stated scan |
| 2007.04990 | limit_data/AxionMass/Gorghetto20.txt | AxionMass | AxionMass prediction-band file: both columns are masses (m_lo, m_hi) — there is no coupling column, so no extraction can match it; the extractor's refusal (0 points) is correct behavior for these papers. |
| 2007.04990 | limit_data/AxionMass/GorghettoDW_6.txt | AxionMass | AxionMass prediction-band file: both columns are masses (m_lo, m_hi) — there is no coupling column, so no extraction can match it; the extractor's refusal (0 points) is correct behavior for these papers. |
| 2410.02218 | limit_data/AxionEDM/ONIX.txt | AxionEDM | Reference has a mis-set log-axis calibration |
| 2410.02218 | limit_data/fa/ONIX.txt | AxionMass | Reference has a mis-set log-axis calibration |
| 1708.02111 | limit_data/AxionElectron/WDhint.txt | AxionElectron | Reference is a 1-sigma hint band, not an exclusion limit |
| 2412.08699 | limit_data/AxionMass/Benabou24.txt | AxionMass | AxionMass prediction-band file: both columns are masses (m_lo, m_hi) — there is no coupling column, so no extraction can match it; the extractor's refusal (0 points) is correct behavior for these papers. |
| 2412.08699 | limit_data/AxionMass/Benabou24_DW.txt | AxionMass | AxionMass prediction-band file: both columns are masses (m_lo, m_hi) — there is no coupling column, so no extraction can match it; the extractor's refusal (0 points) is correct behavior for these papers. |
| 1512.06746 | limit_data/AxionMass/Bonati16.txt | AxionMass | QCD-axion mass prediction band (m_lo, m_hi), no coupling column |
| 1606.07494 | limit_data/AxionMass/Borsanyi16.txt | AxionMass | QCD-axion mass prediction band (m_lo, m_hi), no coupling column |
| 1906.00967 | limit_data/AxionMass/Buschmann20.txt | AxionMass | AxionMass prediction-band file: both columns are masses (m_lo, m_hi) — there is no coupling column, so no extraction can match it; the extractor's refusal (0 points) is correct behavior for these papers. |
| 2108.05368 | limit_data/AxionMass/Buschmann21.txt | AxionMass | AxionMass prediction-band file: both columns are masses (m_lo, m_hi) — there is no coupling column, so no extraction can match it; the extractor's refusal (0 points) is correct behavior for these papers. |
| 1705.00676 | limit_data/AxionMass/Dine17.txt | AxionMass | AxionMass prediction-band file: both columns are masses (m_lo, m_hi) — there is no coupling column, so no extraction can match it; the extractor's refusal (0 points) is correct behavior for these papers. |
| 1509.00026 | limit_data/AxionMass/Fleury15.txt | AxionMass | AxionMass prediction-band file: both columns are masses (m_lo, m_hi) — there is no coupling column, so no extraction can match it; the extractor's refusal (0 points) is correct behavior for these papers. |
| 1708.07521 | limit_data/AxionMass/Klaer17.txt | AxionMass | QCD-axion mass prediction band (m_lo, m_hi), no coupling column |
| 1606.03145 | limit_data/AxionMass/Petreczky16.txt | AxionMass | AxionMass prediction-band file: both columns are masses (m_lo, m_hi) — there is no coupling column, so no extraction can match it; the extractor's refusal (0 points) is correct behavior for these papers. |
| 2401.17253 | limit_data/AxionMass/Saikawa24.txt | AxionMass | QCD-axion mass prediction band (m_lo, m_hi), no coupling column |
| 1412.0789 | limit_data/AxionMass/SaikawaDW_6_10.txt | AxionMass | QCD-axion mass window stored as a single reference point |
| 2206.11598 | limit_data/AxionMass/VISHnu.txt | AxionMass | AxionMass prediction-band file: both columns are masses (m_lo, m_hi) — there is no coupling column, so no extraction can match it; the extractor's refusal (0 points) is correct behavior for these papers. |
| 1902.04644 | limit_data/AxionNeutron/CASPEr_ZULF.txt | AxionNeutron | Reference file belongs to a different paper |
| 2112.03439 | limit_data/AxionPhoton/BreakthroughListen.txt | AxionPhoton | Paper reports decay-rate/annihilation limits only (lambda [s^-1], <sigma v>); the GT g_agamma value is the repo maintainer's derived physics conversion and never appears in the paper, so it is not extractable. |
| hep-ex/0702006 | limit_data/AxionPhoton/CAST_highm.txt | AxionPhoton | Reference mixes later buffer-gas results into this paper's curve |
| 2209.06299 | limit_data/AxionPhoton/INTEGRAL.txt | AxionPhoton | Reference digitised from a superseded arXiv version |
| 1912.07751 | limit_data/AxionPhoton/UPLOAD.txt | AxionPhoton | Reference digitised from a superseded arXiv version |
| 2102.02207 | limit_data/AxionPhoton/XMM-Newton.txt | AxionPhoton | Paper publishes decaying-DM limits via the sterile-neutrino mixing angle sin^2(2theta) vs m_chi (5-16 keV) from XMM-Newton blank-sky observations; it never quotes an axion-photon coupling. The repo AxionPhoton/XMM-Newton.txt g_agamma curve is the maintainer's derived conversion, so the GT demands a quantity that is not extractable from the paper. |
| 2412.09595 | limit_data/AxionProton/SuperKamiokande.txt | AxionProton | Reference digitised from a superseded arXiv version |
| 2101.02805 | limit_data/DarkPhoton/DarkEfield.txt | DarkPhoton | Reference encodes a projected curve, not the measured limit |
| 2207.05767 | limit_data/DarkPhoton/FAST.txt | DarkPhoton | Reference digitised from a superseded arXiv version |
| 2402.17140 | limit_data/DarkPhoton/JWST.txt | DarkPhoton | Reference digitised from a superseded arXiv version |
| 2208.03183 | limit_data/DarkPhoton/SQMS.txt | DarkPhoton | Reference resonance placed at the wrong mass |
| 2205.06817 | limit_data/ScalarElectron/IPTA.txt | ScalarElectron | Reference is a projection from mock data ingested as a measured limit |
| 2005.14694 | limit_data/ScalarPhoton/BACON.txt | ScalarPhoton | Published-version-only content: the d_e ultralight-DM limit (repo BACON.txt) exists only in the published Nature 591, 564 (2021) figure; no arXiv version of the paper contains it, so it is unreachable from the benchmark's input PDF. |
| 2011.08693 | limit_data/fa/BlackHoleSpins_Mehta.txt | AxionMass | GT digitizes private-communication data: BlackHoleSpins_Mehta.txt's own header says the 178-point BHSR compilation came via 'private communication'; it is not published in the paper PDF. |
| 2404.00616 | limit_data/fa/I2Ca.txt | AxionMass | Reference is a projected constraint stored outside Projections/ |
| 1003.0964 | — | DarkPhoton | Wrong GT mapping: LSW_UWA.txt is arXiv:1410.5244's limit (per the file header). This paper's own limit (chi = 2.9e-5 at 37.9 ueV, stated to lie 'within already established limits') has no repo data file, so there is nothing valid to grade against. |
| 2312.11608 | limit_data/AxionPhoton/GammaRayDecayCompilation.txt | AxionPhoton | GammaRayDecayCompilation.txt is a compilation of PRE-EXISTING gamma-ray decay limits (HEAO-1/COMPTEL/EGRET/Fermi) shown as background in this paper's figure — not the paper's own result. The paper's headline (HERA 21-cm projection) is keyed separately. |

## Classification Accuracy

| Field | Accuracy | N |
|-------|----------|---|
| coupling_type | 93.1% | 290 |
| is_new_limit | 100.0% | 32 |
| is_projection | 100.0% | 32 |
| data_source | 25.0% | 32 |

> **Label provenance**: `is_new_limit`, `is_projection`, and `data_source` are scored against an **independent LLM labeler** (`evaluation/label_ground_truth.py`, model `claude-opus-4-5`) whose sole task is to classify paper properties — a distinct model and prompt from the extractor it grades, so this is a fair cross-model test, not self-agreement. These are **not human gold labels**. A human audit of 15 labeled papers found per-field labeler↔human agreement: is_new_limit 15/15, is_projection 15/15, data_source 14/15 (difficulty is derived mechanically from data_source + point count, not labeled).

### Coupling Type Misclassifications

| arXiv ID | Predicted | Expected |
|----------|-----------|----------|
| 2504.00720 | AxionPhoton | ['AxionMass'] |
| 1607.07327 | ScalarBaryon | ['ScalarElectron', 'ScalarPhoton'] |
| 2401.18076 | ScalarBaryon | ['ScalarElectron', 'ScalarPhoton'] |
| 1207.2442 | ScalarBaryon | ['VectorBL'] |
| 2306.01048 | AxionNeutron | ['AxionProton'] |
| 2111.09892 | AxionMass | ['AxionNeutron', 'AxionProton'] |
| 1907.11485 | AxionPhoton | ['AxionElectron', 'DarkPhoton'] |
| 2207.11330 | AxionPhoton | ['AxionElectron'] |
| hep-ph/0611223 | ScalarBaryon | ['AxionNeutron', 'AxionProton'] |
| 1907.12628 | AxionElectron | ['DarkPhoton'] |
| 2410.02858 | None | ['DarkPhoton'] |
| 1807.04512 | ScalarBaryon | ['ScalarElectron', 'ScalarPhoton'] |
| 2306.16219 | ScalarNucleon | ['ScalarElectron'] |
| 2105.13085 | DarkPhoton | ['VectorBL'] |
| 2301.08736 | DarkPhoton | ['VectorBL'] |
| 2112.07687 | DarkPhoton | ['VectorBL'] |
| 2011.11646 | AxionNeutron | ['AxionMass'] |
| 2410.21590 | AxionNeutron | ['AxionMass'] |
| 1708.08464 | AxionNeutron | ['AxionMass'] |
| 2211.02661 | AxionNeutron | ['AxionMass'] |

### Coupling-Type Confusion Matrix (multi-type-aware)

Rows = authoritative GT type, columns = predicted type. A prediction is correct iff it is in ANY of the paper's GT types (diagonal). Off-diagonal cells are the confusable clusters. Graded 289, correct 270 (93.4%), skipped 39 (no prediction / no GT type).

| GT ⟍ Pred | AxionEDM | AxionElectron | AxionMass | AxionNeutron | AxionPhoton | AxionProton | DarkPhoton | MonopoleDipole | ScalarBaryon | ScalarElectron | ScalarNucleon | ScalarPhoton | VectorBL |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| AxionEDM | **5** |  |  |  |  |  |  |  |  |  |  |  |  |
| AxionElectron |  | **14** |  |  | 2 |  |  |  |  |  |  |  |  |
| AxionMass |  |  | **11** | 4 | 1 |  |  |  |  |  |  |  |  |
| AxionNeutron |  |  | 1 | **14** |  |  |  |  | 1 |  |  |  |  |
| AxionPhoton |  |  |  |  | **142** |  |  |  |  |  |  |  |  |
| AxionProton |  |  | 1 | 1 |  | **1** |  |  | 1 |  |  |  |  |
| DarkPhoton |  | 1 |  |  | 1 |  | **54** |  |  |  |  |  |  |
| MonopoleDipole |  |  |  |  |  |  |  | **3** |  |  |  |  |  |
| ScalarBaryon |  |  |  |  |  |  |  |  | **2** |  |  |  |  |
| ScalarElectron |  |  |  |  |  |  |  |  | 3 | **4** | 1 |  |  |
| ScalarNucleon |  |  |  |  |  |  |  |  |  |  | **5** |  |  |
| ScalarPhoton |  |  |  |  |  |  |  |  | 3 |  |  | **8** |  |
| VectorBL |  |  |  |  |  |  | 3 |  | 1 |  |  |  | **7** |

Off-diagonal confusions (GT → predicted, richest first):

- AxionMass → AxionNeutron: 4
- ScalarElectron → ScalarBaryon: 3
- ScalarPhoton → ScalarBaryon: 3
- VectorBL → DarkPhoton: 3
- AxionElectron → AxionPhoton: 2
- AxionMass → AxionPhoton: 1
- AxionNeutron → AxionMass: 1
- AxionNeutron → ScalarBaryon: 1
- AxionProton → AxionMass: 1
- AxionProton → AxionNeutron: 1
- AxionProton → ScalarBaryon: 1
- DarkPhoton → AxionElectron: 1
- DarkPhoton → AxionPhoton: 1
- ScalarElectron → ScalarNucleon: 1
- VectorBL → ScalarBaryon: 1

## Extraction Quality — Interpolation Metric (primary)

Build log-log interpolation from extracted points, evaluate at ground-truth masses.

- **Papers compared**: 246 (222 with mass-range overlap, 24 with zero overlap)

**Coupling-value accuracy** (papers with mass-range overlap):
- **Median residual across papers**: 0.616 dex (IQR 0.263–2.069)
- **Mean residual across papers** (outlier-sensitive): 1.833 dex
- **Mean fraction within 0.3 dex (factor 2; the leaderboard headline is 10%, results/leaderboard.py)**: 31.2%
- **Mean fraction within 0.5 dex (factor 3)**: 42.1%

**Mass-range coverage** (a separate failure mode):
- **Mean interpolation coverage**: 76.4%
- **Zero-overlap papers**: 24/246 (9.8%) — extracted masses miss the GT range entirely (usually 1–2 extracted points or the wrong mass window)

**Reverse pass** (GT interpolated onto the *extracted* masses):
- Mirrors the forward pass. A large forward-vs-reverse gap, or a reverse coverage well below the forward coverage, flags an extraction whose mass *extent* or shape disagrees with the GT (e.g. running past the GT range).
- **Median reverse residual across papers**: 0.653 dex (forward: 0.616 dex)
- **Mean reverse interpolation coverage**: 60.3% (forward: 76.4%)

## Residual by Coupling Type — Micro vs Macro Average (issue #543)

The compared-paper pool is dominated by one coupling type (AxionPhoton), so the per-paper **micro-average** headline is largely that one type's number. The **macro-average** weights each coupling type equally (mean of the per-type medians), exposing how the pipeline does across the *range* of couplings rather than on the most common one.

- **Micro-average median residual** (per paper, 222 papers): 0.616 dex
- **Macro-average median residual** (equal weight per type, 12 types): 2.509 dex
- **Macro − micro gap**: +1.893 dex (macro is worse; a positive gap means the rarer couplings are harder than the AxionPhoton-dominated micro-average implies)

Per-type medians carry a bootstrap 95% CI (1000 resamples). Rows with **N < 5** are flagged small-sample — their median and CI are unstable and should not be read as a reliable per-type score.

| Coupling Type | N | Median Resid. (dex) | 95% CI (dex) | Flag |
|---------------|---|---------------------|--------------|------|
| AxionPhoton | 121 | 0.480 | [0.415, 0.623] |  |
| DarkPhoton | 52 | 0.659 | [0.508, 1.773] |  |
| AxionNeutron | 12 | 1.562 | [0.231, 2.309] |  |
| AxionElectron | 9 | 0.561 | [0.090, 1.451] |  |
| ScalarPhoton | 7 | 5.970 | [3.285, 20.395] |  |
| VectorBL | 6 | 1.516 | [0.212, 5.377] |  |
| AxionEDM | 4 | 3.378 | [0.129, 19.995] | ⚠ small-sample (N<5) |
| AxionMass | 4 | 7.828 | [3.136, 9.977] | ⚠ small-sample (N<5) |
| ScalarElectron | 3 | 2.499 | [0.309, 7.581] | ⚠ small-sample (N<5) |
| ScalarNucleon | 2 | 3.181 | [2.060, 4.303] | ⚠ small-sample (N<5) |
| ScalarBaryon | 1 | 2.410 | [2.410, 2.410] | ⚠ small-sample (N<5) |
| MonopoleDipole | 1 | 0.063 | [0.063, 0.063] | ⚠ small-sample (N<5) |

## Shape & Mass-Range Agreement — Symmetric Metrics (complementary)

These are symmetric, 2-D complements to the (asymmetric, vertical-only) interpolation residual. **Area-between-curves** integrates |Δ log10 coupling| over the overlapping log-mass range and normalises by the overlap width (a single shape+offset number, in dex; a pure mass shift inflates it even when the vertical residual looks fine). **Mass-range Jaccard** is the Jaccard index of the extracted vs GT log-mass intervals (1.0 = identical extent; small = over-/under-claimed mass range), reported separately from interpolation coverage.

- **Papers scored**: 237 (210 with mass overlap for area)
- **Median area-between-curves**: 0.764 dex (mean 1.760 dex)
- **Median mass-range Jaccard**: 0.580 (mean 0.532)

## Per-Paper Results

| arXiv ID | Coupling | Conf. | Interp. Cov. | Med. Resid. | Rev. Resid. | Area (dex) | Mass Jaccard | ≤0.3 dex | Points |
|----------|----------|-------|--------------|-------------|-------------|------------|--------------|----------|--------|
| 2208.07293 | ✓ | 0.50 | 100.0% | 0.129 | 0.129 | 0.129 | 0.052 | 100.0% | 2/2 |
| 2212.04413 | ✓ | 0.45 | 100.0% | 7.581 | ∞ | 7.769 | 0.992 | 0.0% | 2/73 |
| 2410.19902 | ✓ | 0.85 | 0.0% | ∞ | ∞ | ∞ | 0.000 | 0.0% | 37/2 |
| 1907.03767 | ✓ | 0.75 | 86.3% | 4.366 | 3.408 | 2.911 | 0.808 | 0.0% | 10/182 |
| 2209.06216 | ✓ | 0.85 | 27.6% | 0.157 | 0.083 | 0.760 | 0.181 | 78.6% | 2/2771 |
| 2005.14184 | ✓ | 0.92 | 99.7% | 0.561 | 0.443 | 0.500 | 0.998 | 25.2% | 11/891 |
| 2504.00720 | ✗ (AxionPhoton) | 0.65 | no_comparable_gt | — | — | — | — | — | — |
| 2408.02668 | ✓ | 0.92 | 100.0% | 0.437 | 0.734 | 1.760 | 0.481 | 40.4% | 20/413 |
| 1905.13650 | ✓ | 0.72 | 100.0% | 1.547 | 0.562 | 0.948 | 0.568 | 3.3% | 33/243 |
| 2110.03679 | ✓ | 0.85 | 99.2% | 0.649 | 0.638 | 0.708 | 0.250 | 0.0% | 31/129 |
| 2303.07370 | ✓ | 0.65 | 100.0% | 3.301 | 2.840 | 3.351 | 0.900 | 4.7% | 6/107 |
| 2309.16600 | ✓ | 0.85 | 41.5% | 0.231 | 0.200 | 0.240 | 0.167 | 76.9% | 23/188 |
| 2504.16044 | ✓ | 0.92 | gt_unusable | — | — | — | — | — | — |
| 2312.06746 | ✓ | 0.85 | 60.8% | 0.324 | 0.334 | 0.444 | 0.754 | 47.1% | 5/171 |
| 1310.8098 | ✓ | 0.85 | 71.1% | 2.072 | 1.977 | 2.281 | 0.179 | 3.1% | 86/135 |
| 2408.02368 | ✓ | 0.95 | 100.0% | 0.176 | 0.007 | 0.175 | 0.999 | 87.8% | 3/647 |
| 2011.07100 | ✓ | 0.92 | 0.0% | ∞ | ∞ | ∞ | 0.000 | 0.0% | 4/79 |
| 2302.09096 | ✓ | 0.85 | 0.0% | ∞ | ∞ | ∞ | 0.000 | 0.0% | 38/41 |
| 1410.7267 | ✓ | 0.85 | 0.0% | ∞ | ∞ | ∞ | 0.000 | 0.0% | 54/74 |
| 1712.00483 | ✓ | 0.92 | 41.2% | 2.410 | 1.397 | 2.264 | 0.025 | 0.0% | 2/119 |
| 1607.07327 | ✗ (ScalarBaryon) | 0.50 | no_comparable_gt | — | — | — | — | — | — |
| 1611.05852 | ✓ | 0.75 | no_comparable_gt | — | — | — | — | — | — |
| 2111.06883 | ✓ | 0.50 | no_comparable_gt | — | — | — | — | — | — |
| 0802.2350 | ✓ | 0.85 | 100.0% | 4.303 | 3.529 | 3.874 | 0.183 | 0.0% | 61/24 |
| 2009.04517 | ✓ | 0.65 | 100.0% | 1.576 | 1.576 | 1.362 | 0.240 | 0.0% | 3/29 |
| 2010.08107 | ✓ | 0.50 | convention_mismatch | — | — | — | — | — | — |
| 2201.02042 | — | — | EXCLUDED | — | — | — | — | — | — |
| 2403.03004 | ✓ | 0.92 | 81.4% | 2.424 | 2.289 | 2.318 | 0.579 | 0.0% | 30/414 |
| 2205.03617 | ✓ | 0.50 | no_comparable_gt | — | — | — | — | — | — |
| 2310.06017 | ✓ | 0.75 | 46.9% | 4.304 | 5.518 | 4.241 | 0.461 | 0.0% | 2/113 |
| 2102.08764 | ✓ | 0.92 | 100.0% | 0.000 | 0.000 | 0.000 | 0.892 | 100.0% | 2/2 |
| 2308.14656 | ✓ | 0.92 | 98.7% | 0.213 | 0.330 | 0.182 | 0.980 | 89.2% | 2/75 |
| 2207.03102 | ✓ | 0.85 | 100.0% | 0.593 | 0.593 | 0.768 | 0.360 | 24.0% | 25/2 |
| 1505.07455 | — | — | EXCLUDED | — | — | — | — | — | — |
| 2105.04603 | ✓ | 0.85 | 85.9% | 3.738 | 3.722 | 3.929 | 0.836 | 0.0% | 30/707 |
| 2303.11792 | ✓ | 0.92 | 90.0% | 0.141 | 0.128 | 0.144 | 0.748 | 100.0% | 2/20 |
| 1607.06083 | ✓ | 0.75 | 0.0% | ∞ | ∞ | ∞ | 0.000 | 0.0% | 12/113 |
| 2108.04746 | ✓ | 0.85 | 100.0% | 22.529 | 22.310 | 22.338 | 0.481 | 0.0% | 61/283 |
| 2208.12670 | ✓ | 0.95 | 100.0% | 0.000 | ∞ | — | — | 100.0% | 2/1 |
| 1806.05120 | ✓ | 0.92 | 97.9% | 0.192 | 0.211 | 0.215 | 0.973 | 81.5% | 2/94 |
| 2101.01241 | ✓ | 0.92 | 100.0% | 19.995 | ∞ | — | — | 0.0% | 2/1 |
| 2404.14476 | ✓ | 0.88 | 98.0% | 0.975 | 1.197 | 1.146 | 0.238 | 24.0% | 31/51 |
| 2504.12377 | ✓ | 0.85 | 100.0% | 0.707 | 0.457 | 0.475 | 0.625 | 0.0% | 25/15 |
| 2408.15227 | ✓ | 0.92 | 94.8% | 0.327 | 0.327 | 0.306 | 0.906 | 37.6% | 65/230 |
| 2209.09917 | ✓ | 0.85 | 80.0% | 0.376 | 0.387 | 0.369 | 0.750 | 50.0% | 10/5 |
| 2406.00387 | ✓ | 0.85 | 100.0% | 0.458 | 0.596 | 1.102 | 0.764 | 28.7% | 25/108 |
| 1207.3275 | ✓ | 0.85 | 100.0% | 0.643 | 0.708 | 0.659 | 0.015 | 0.0% | 37/9 |
| 2205.01079 | ✓ | 0.65 | 78.6% | 0.523 | 0.523 | 0.623 | 0.898 | 27.3% | 5/14 |
| 2212.02403 | ✓ | 0.92 | 100.0% | 1.703 | 1.273 | 1.218 | 0.790 | 4.8% | 51/42 |
| 1903.12190 | ✓ | 0.85 | 66.7% | 5.811 | 4.796 | 5.382 | 0.618 | 0.0% | 14/3 |
| 2305.00890 | ✓ | 0.92 | 100.0% | 0.547 | ∞ | 2.773 | 0.996 | 31.0% | 2/4991 |
| 1708.06367 | ✓ | 0.50 | 94.4% | 0.906 | 0.992 | 0.931 | 0.963 | 0.0% | 2/36 |
| 2312.13723 | — | — | EXCLUDED | — | — | — | — | — | — |
| 2410.10363 | ✓ | 0.75 | 0.0% | ∞ | ∞ | ∞ | 0.000 | 0.0% | 6/288 |
| 1202.5851 | — | — | EXCLUDED | — | — | — | — | — | — |
| 2208.06519 | ✓ | 0.92 | 100.0% | 1.978 | ∞ | — | — | 0.0% | 34/1 |
| 2401.16747 | ✓ | 0.75 | 97.0% | 1.373 | 1.591 | 1.410 | 0.999 | 0.0% | 21/66 |
| 2401.18076 | ✗ (ScalarBaryon) | 0.75 | no_comparable_gt | — | — | — | — | — | — |
| 2503.13653 | ✓ | 0.75 | 26.4% | 3.625 | 3.166 | 5.245 | 0.450 | 0.0% | 4/53 |
| 2308.06339 | ✓ | 0.75 | 96.1% | 0.517 | 0.539 | 0.560 | 0.997 | 13.7% | 14/76 |
| 2109.11734 | ✓ | 0.92 | 75.0% | 0.106 | 0.320 | 0.117 | 0.879 | 66.7% | 6/12 |
| 2308.09077 | ✓ | 0.75 | 75.9% | 2.860 | 2.865 | 2.856 | 0.222 | 0.0% | 30/54 |
| 2110.06096 | ✓ | 0.75 | 97.5% | 0.410 | 0.432 | 0.392 | 0.970 | 8.1% | 6/242 |
| 2205.03679 | ✓ | 0.85 | 100.0% | 0.152 | 0.176 | 0.170 | 0.976 | 90.0% | 19/1525 |
| 2202.08858 | ✓ | 0.85 | 99.5% | 3.994 | 4.118 | 4.219 | 0.883 | 0.0% | 30/203 |
| 2503.14582 | ✓ | 0.75 | 100.0% | 0.480 | 0.464 | 0.434 | 0.997 | 14.4% | 4/196912 |
| 1207.2442 | ✗ (ScalarBaryon) | 0.75 | no_comparable_gt | — | — | — | — | — | — |
| 1609.00667 | — | — | EXCLUDED | — | — | — | — | — | — |
| 2407.03828 | ✓ | 0.92 | 99.1% | 0.159 | 0.235 | 0.727 | 0.296 | 57.4% | 30/116 |
| 1810.04602 | ✓ | 0.50 | no_extracted_points | — | — | — | — | — | — |
| 2110.10262 | — | — | EXCLUDED | — | — | — | — | — | — |
| 2306.05934 | ✓ | 0.92 | 99.7% | 0.325 | 0.110 | 0.227 | 0.997 | 46.1% | 2/2636 |
| 2306.01048 | ✗ (AxionNeutron) | 0.85 | no_comparable_gt | — | — | — | — | — | — |
| 2008.08773 | ✓ | 0.85 | 97.0% | 2.499 | 2.829 | 2.028 | 0.528 | 0.5% | 4393/629 |
| 2007.04990 | — | — | EXCLUDED | — | — | — | — | — | — |
| 2207.11968 | ✓ | 0.75 | 100.0% | 1.177 | ∞ | 1.228 | 0.299 | 0.0% | 5/128 |
| 0807.2926 | ✓ | 0.75 | 0.0% | ∞ | ∞ | ∞ | 0.000 | 0.0% | 30/18 |
| 1508.02463 | ✓ | 0.75 | 66.7% | 0.063 | 1.288 | 0.353 | 0.148 | 62.2% | 2/111 |
| 0809.4700 | ✓ | 0.85 | 57.1% | 0.166 | 0.244 | 0.166 | 0.037 | 60.0% | 7/35 |
| 2006.07055 | ✓ | 0.75 | 100.0% | 20.395 | ∞ | 20.151 | 0.177 | 0.0% | 46/146 |
| 2004.02733 | ✓ | 0.25 | 100.0% | 2.622 | 2.622 | 2.622 | 0.605 | 0.0% | 19/33 |
| 2111.09892 | ✗ (AxionMass) | 0.50 | no_comparable_gt | — | — | — | — | — | — |
| 1401.6460 | ✓ | 0.75 | convention_mismatch | — | — | — | — | — | — |
| 2204.01454 | ✓ | 0.85 | 100.0% | 5.851 | 5.741 | 6.093 | 0.359 | 0.0% | 64/42 |
| 2410.02218 | — | — | EXCLUDED | — | — | — | — | — | — |
| 1808.02340 | ✓ | 0.75 | 0.0% | ∞ | ∞ | ∞ | 0.000 | 0.0% | 22/265 |
| 2311.16364 | ✓ | 0.85 | 100.0% | 0.471 | 0.516 | 0.511 | 0.615 | 32.2% | 92/121 |
| 1704.02297 | ✓ | 0.95 | 96.6% | 0.338 | 0.586 | 0.366 | 0.085 | 35.7% | 2/58 |
| 1707.07921 | ✓ | 0.92 | 100.0% | 1.451 | 1.451 | 0.754 | 0.452 | 25.0% | 4/30 |
| 1806.00310 | ✓ | 0.75 | 0.0% | ∞ | ∞ | ∞ | 0.000 | 0.0% | 30/8 |
| 2007.03694 | ✓ | 0.92 | 100.0% | 0.090 | 0.090 | ∞ | 0.000 | 100.0% | 1/2 |
| 1911.11905 | ✓ | 0.85 | 24.2% | 0.945 | 0.933 | 0.917 | 0.264 | 0.0% | 15/256 |
| 1902.04246 | ✓ | 0.30 | convention_mismatch | — | — | — | — | — | — |
| 1708.02111 | — | — | EXCLUDED | — | — | — | — | — | — |
| 2006.09721 | ✓ | 0.85 | 0.0% | ∞ | ∞ | ∞ | 0.000 | 0.0% | 99/148 |
| 1907.11485 | ✗ (AxionPhoton) | 0.72 | no_comparable_gt | — | — | — | — | — | — |
| 2112.12116 | ✓ | 0.65 | 100.0% | 4.605 | 4.611 | 4.684 | 0.496 | 0.0% | 8/100 |
| 2006.12431 | ✓ | 0.75 | 0.0% | ∞ | ∞ | ∞ | 0.000 | 0.0% | 10/90 |
| 2207.11330 | ✗ (AxionPhoton) | 0.75 | no_comparable_gt | — | — | — | — | — | — |
| 2412.08699 | — | — | EXCLUDED | — | — | — | — | — | — |
| 1512.06746 | — | — | EXCLUDED | — | — | — | — | — | — |
| 1606.07494 | — | — | EXCLUDED | — | — | — | — | — | — |
| 1906.00967 | — | — | EXCLUDED | — | — | — | — | — | — |
| 2108.05368 | — | — | EXCLUDED | — | — | — | — | — | — |
| 1705.00676 | — | — | EXCLUDED | — | — | — | — | — | — |
| 1509.00026 | — | — | EXCLUDED | — | — | — | — | — | — |
| 2402.00741 | ✓ | 0.25 | no_extracted_points | — | — | — | — | — | — |
| 1708.07521 | — | — | EXCLUDED | — | — | — | — | — | — |
| 1606.03145 | — | — | EXCLUDED | — | — | — | — | — | — |
| 2401.17253 | — | — | EXCLUDED | — | — | — | — | — | — |
| 1412.0789 | — | — | EXCLUDED | — | — | — | — | — | — |
| 2206.11598 | — | — | EXCLUDED | — | — | — | — | — | — |
| 1902.04644 | — | — | EXCLUDED | — | — | — | — | — | — |
| 2306.08039 | ✓ | 0.92 | 0.0% | ∞ | ∞ | ∞ | 0.000 | 0.0% | 12/1158 |
| 2102.01448 | ✓ | 0.92 | 100.0% | 2.305 | 1.930 | 2.064 | 0.882 | 0.0% | 18/70 |
| 2209.03289 | ✓ | 0.92 | 0.0% | ∞ | ∞ | ∞ | 0.000 | 0.0% | 79/110 |
| 2209.13588 | ✓ | 0.65 | 45.7% | 0.231 | 0.245 | 0.278 | 0.463 | 62.9% | 20/230 |
| 1906.11844 | ✓ | 0.85 | 50.0% | 0.180 | 0.180 | 0.180 | 0.120 | 100.0% | 2/2 |
| hep-ph/0611223 | ✗ (ScalarBaryon) | 0.50 | no_comparable_gt | — | — | — | — | — | — |
| 1810.12257 | ✓ | 0.95 | 100.0% | 0.304 | ∞ | 0.348 | 0.997 | 49.6% | 2/3214 |
| 2102.06722 | ✓ | 0.85 | 100.0% | 4.943 | 4.912 | 4.924 | 0.932 | 0.0% | 18/391 |
| 2404.12517 | ✓ | 0.75 | 100.0% | 0.666 | 0.293 | 0.643 | 0.024 | 32.0% | 47/284 |
| 0910.5914 | ✓ | 0.75 | 7.4% | 0.597 | 0.603 | 0.613 | 0.106 | 0.0% | 2/27 |
| 1804.05750 | ✓ | 0.85 | 100.0% | 1.361 | 1.309 | 1.152 | 0.844 | 8.3% | 30/145 |
| 1910.08638 | ✓ | 0.92 | 100.0% | 1.319 | 1.319 | 1.294 | 0.313 | 0.0% | 51/82 |
| 2504.07279 | ✓ | 0.92 | 89.3% | 0.424 | 0.373 | 0.396 | 0.934 | 6.7% | 2/234 |
| 1911.05772 | ✓ | 0.75 | 100.0% | 0.391 | 0.460 | 0.529 | 0.992 | 40.9% | 6/22 |
| 1901.00920 | ✓ | 0.85 | 99.1% | 1.248 | 1.069 | 1.345 | 1.000 | 0.0% | 6/117 |
| 1004.1313 | ✓ | 0.85 | 18.0% | 1.166 | 1.244 | 1.358 | 0.171 | 0.0% | 3/228 |
| 2008.05355 | ✓ | 0.30 | convention_mismatch | — | — | — | — | — | — |
| 2302.10206 | ✓ | 0.92 | 87.5% | 0.210 | 0.568 | 0.404 | 0.707 | 85.7% | 2/8 |
| 2101.11290 | ✓ | 0.85 | 50.0% | 0.018 | 0.021 | 0.028 | 0.010 | 100.0% | 9/2 |
| 2002.08370 | ✓ | 0.65 | 0.0% | ∞ | ∞ | ∞ | 0.000 | 0.0% | 12/36 |
| 2211.12699 | ✓ | 0.92 | 0.0% | ∞ | ∞ | ∞ | 0.000 | 0.0% | 3/75 |
| 2108.03316 | ✓ | 0.92 | 100.0% | 1.215 | 1.245 | 1.196 | 0.935 | 9.0% | 8/321 |
| 1709.00009 | ✓ | 0.75 | 0.0% | ∞ | ∞ | ∞ | 0.000 | 0.0% | 12/37 |
| 2007.13071 | ✓ | 0.92 | 0.0% | ∞ | ∞ | ∞ | 0.000 | 0.0% | 19/318 |
| 2009.09059 | ✓ | 0.82 | 82.5% | 0.501 | 0.473 | 0.458 | 0.285 | 28.7% | 32/114 |
| 2112.03439 | — | — | EXCLUDED | — | — | — | — | — | — |
| 2001.05102 | ✓ | 0.85 | 88.3% | 0.312 | 0.311 | 0.312 | 0.826 | 42.6% | 41/77 |
| 2008.10141 | ✓ | 0.75 | 89.5% | 2.038 | 2.015 | 2.058 | 0.896 | 0.0% | 17/220 |
| 2012.10764 | ✓ | 0.92 | 100.0% | 1.615 | 1.662 | 1.549 | 0.996 | 0.0% | 4/125 |
| 2206.08845 | ✓ | 0.75 | 99.1% | 1.784 | 1.805 | 1.783 | 0.953 | 0.0% | 6/2959 |
| 2207.13597 | ✓ | 0.92 | 93.9% | 1.548 | 1.550 | 1.548 | 0.969 | 0.0% | 2/49 |
| 2210.10961 | ✓ | 0.92 | 94.8% | 0.415 | 0.375 | 0.474 | 0.964 | 41.6% | 41/251 |
| 2312.11003 | ✓ | 0.50 | 91.2% | 1.919 | 1.915 | 1.919 | 0.945 | 0.0% | 2/181 |
| 2403.13390 | ✓ | 0.92 | 98.6% | 0.111 | 0.101 | 0.116 | 0.982 | 100.0% | 2/70 |
| 2402.12892 | ✓ | 0.75 | 100.0% | 0.586 | 0.591 | 0.628 | 0.966 | 1.4% | 8/362 |
| 2211.02902 | ✓ | 0.85 | 100.0% | 0.262 | 0.276 | 0.246 | 0.988 | 71.0% | 30/169 |
| 1705.02290 | ✓ | 0.85 | 99.8% | 4.693 | 5.277 | 5.409 | 0.292 | 0.0% | 20/436 |
| hep-ex/0702006 | — | — | EXCLUDED | — | — | — | — | — | — |
| 1704.05189 | ✓ | 0.85 | 100.0% | 0.441 | 0.425 | 0.350 | 0.657 | 21.3% | 51/61 |
| 2411.13701 | ✓ | 0.85 | 63.5% | 9.883 | 10.051 | 9.347 | 0.449 | 0.0% | 452/170 |
| 2109.03261 | ✓ | 0.92 | 79.3% | 0.271 | 0.451 | 0.563 | 0.417 | 56.5% | 24/29 |
| 1304.0989 | ✓ | 0.92 | 55.2% | 0.065 | 0.113 | 0.079 | 0.037 | 100.0% | 3/29 |
| 1703.07354 | ✓ | 0.75 | 63.6% | 0.419 | 0.534 | 0.495 | 0.228 | 39.3% | 34/44 |
| 1907.05475 | ✓ | 0.92 | 94.1% | 0.274 | 0.274 | 0.234 | 0.430 | 68.8% | 39/17 |
| 2104.12772 | ✓ | 0.92 | 15.6% | 0.011 | 0.019 | 0.013 | 0.039 | 100.0% | 2/64 |
| 2407.10618 | ✓ | 0.75 | 100.0% | 0.864 | 1.955 | 1.274 | 0.998 | 12.3% | 12/2612 |
| 2303.03594 | ✓ | 0.92 | 25.8% | 0.459 | 0.352 | 0.450 | 0.385 | 8.7% | 2/89 |
| 2311.05476 | ✓ | 0.75 | 65.3% | 12.556 | 12.495 | 12.467 | 0.582 | 0.0% | 8/121 |
| 2201.09890 | ✓ | 0.92 | 49.2% | 0.817 | 1.878 | 0.999 | 0.447 | 27.2% | 2/590 |
| 1110.2895 | ✓ | 0.65 | 100.0% | 6.237 | 6.569 | 6.583 | 0.085 | 0.0% | 8/16 |
| 2412.02232 | ✓ | 0.92 | 88.7% | 1.317 | 2.156 | 0.931 | 0.889 | 0.0% | 4/124 |
| 2504.07559 | ✓ | 0.92 | 58.1% | 0.531 | 1.040 | 0.621 | 0.580 | 23.5% | 2/198 |
| 2404.17333 | ✓ | 0.92 | 20.0% | 0.124 | 0.137 | 0.461 | 0.052 | 80.0% | 5/25 |
| 2405.08059 | ✓ | 0.65 | 100.0% | 0.623 | 0.554 | 0.583 | 0.299 | 22.5% | 25/40 |
| 2211.03414 | ✓ | 0.85 | 0.0% | ∞ | ∞ | ∞ | 0.000 | 0.0% | 31/109 |
| 1603.06978 | ✓ | 0.35 | 100.0% | 0.266 | 0.221 | 0.575 | 0.407 | 54.0% | 30/287 |
| 2305.10327 | ✓ | 0.75 | 100.0% | 0.293 | ∞ | 1.239 | 0.964 | 51.0% | 2/49 |
| 2305.01002 | ✓ | 0.85 | 0.0% | ∞ | ∞ | ∞ | 0.000 | 0.0% | 7/38 |
| 2208.13794 | ✓ | 0.85 | 94.4% | 0.258 | 0.700 | 0.314 | 0.719 | 58.3% | 2/89 |
| 2501.17119 | ✓ | 0.92 | 100.0% | 0.053 | 0.053 | 0.054 | 0.674 | 100.0% | 58/799 |
| 1406.6053 | ✓ | 0.95 | 100.0% | 0.017 | 0.017 | ∞ | 0.000 | 100.0% | 1/27 |
| 2110.14406 | ✓ | 0.75 | 100.0% | 2.394 | ∞ | — | — | 0.0% | 32/1 |
| 2203.04332 | ✓ | 0.92 | 59.5% | 0.029 | 0.137 | 0.033 | 0.182 | 100.0% | 2/148 |
| 1610.02580 | ✓ | 0.85 | 54.5% | 0.025 | 0.025 | 0.039 | 0.511 | 100.0% | 46/121 |
| 2008.01853 | ✓ | 0.50 | convention_mismatch | — | — | — | — | — | — |
| 2409.08998 | ✓ | 0.50 | convention_mismatch | — | — | — | — | — | — |
| 1311.3148 | ✓ | 0.92 | 59.1% | 0.161 | 0.120 | 0.169 | 0.778 | 100.0% | 2/22 |
| 2301.06560 | ✓ | 0.75 | 68.0% | 0.286 | 0.580 | 0.457 | 0.813 | 54.5% | 5/97 |
| 2412.02543 | ✓ | 0.85 | 99.0% | 0.198 | 0.934 | 0.194 | 0.990 | 63.3% | 2/99 |
| 2209.06299 | — | — | EXCLUDED | — | — | — | — | — | — |
| 2310.15395 | ✓ | 0.92 | 91.6% | 0.106 | 0.109 | 0.119 | 0.906 | 93.8% | 5/262 |
| 2503.11753 | ✓ | 0.75 | 95.9% | 1.162 | 1.155 | 1.227 | 0.963 | 0.0% | 15/1844 |
| 1509.00476 | ✓ | 0.50 | no_extracted_points | — | — | — | — | — | — |
| 2307.01365 | ✓ | 0.85 | 0.0% | ∞ | ∞ | ∞ | 0.000 | 0.0% | 15/94 |
| 2111.08025 | ✓ | 0.75 | 75.3% | 1.417 | 1.213 | 1.346 | 0.779 | 0.0% | 5/93 |
| 2412.03660 | ✓ | 0.85 | 67.0% | 1.768 | 1.623 | 1.538 | 0.661 | 9.1% | 8/115 |
| 2409.11777 | ✓ | 0.92 | 100.0% | 0.182 | 0.429 | 0.392 | 0.997 | 75.6% | 4/86 |
| 2401.07798 | ✓ | 0.92 | 100.0% | 1.151 | 1.329 | 0.874 | 0.424 | 0.0% | 5/38 |
| 1811.10997 | ✓ | 0.85 | 27.1% | 0.707 | 0.712 | 0.677 | 0.177 | 0.0% | 31/144 |
| 2203.04319 | ✓ | 0.85 | 100.0% | 0.422 | 0.373 | 0.470 | 0.678 | 26.5% | 39/132 |
| 2307.03878 | ✓ | 0.85 | 39.5% | 0.842 | 0.852 | 0.987 | 0.630 | 6.7% | 316/76 |
| 2110.13636 | ✓ | 0.85 | 93.5% | 0.012 | 0.013 | 0.026 | 0.992 | 91.4% | 60/62 |
| 2008.09464 | ✓ | 0.85 | 100.0% | 0.480 | 0.382 | 0.576 | 0.633 | 36.0% | 30/50 |
| 2202.08274 | ✓ | 0.85 | 100.0% | 0.436 | 0.332 | 0.440 | 0.780 | 35.4% | 31/257 |
| 2203.12152 | ✓ | 0.75 | 95.1% | 0.386 | 0.402 | 0.398 | 0.841 | 20.5% | 18/123 |
| 2310.00904 | ✓ | 0.92 | 0.0% | ∞ | ∞ | ∞ | 0.000 | 0.0% | 35/53 |
| 2407.18586 | ✓ | 0.92 | 100.0% | 0.043 | ∞ | 0.046 | 0.990 | 99.2% | 2/265 |
| 1706.00209 | ✓ | 0.95 | 100.0% | 0.000 | ∞ | — | — | 100.0% | 1/1 |
| 1506.08082 | ✓ | 0.85 | 91.7% | 0.706 | 0.852 | 0.815 | 0.026 | 0.0% | 20/12 |
| 2303.08410 | ✓ | 0.85 | 100.0% | 2.144 | 2.052 | 2.116 | 0.338 | 0.0% | 37/192 |
| 2403.02096 | ✓ | 0.85 | 100.0% | 0.398 | 0.380 | 0.342 | 0.971 | 35.0% | 25/838 |
| 2412.02229 | ✓ | 0.85 | 32.5% | 1.291 | 0.778 | 0.984 | 0.398 | 10.3% | 52/120 |
| 1510.08052 | ✓ | 0.85 | 96.6% | 0.684 | 0.729 | 1.175 | 0.065 | 14.1% | 32/88 |
| 2409.10514 | ✓ | 0.85 | 77.6% | 0.371 | 0.327 | 0.361 | 0.665 | 40.5% | 30/156 |
| 1903.03586 | ✓ | 0.50 | no_extracted_points | — | — | — | — | — | — |
| 1903.06547 | ✓ | 0.85 | 100.0% | 0.686 | ∞ | — | — | 0.0% | 25/1 |
| 2012.09498 | ✓ | 0.95 | 100.0% | 0.079 | ∞ | — | — | 100.0% | 1/1 |
| 2304.07505 | ✓ | 0.92 | 75.0% | 0.519 | 0.669 | 0.489 | 0.718 | 20.8% | 2/32 |
| 2402.19063 | ✓ | 0.85 | 100.0% | 0.419 | 0.417 | 0.373 | 0.998 | 32.9% | 51/149 |
| 2104.13798 | ✓ | 0.92 | 50.0% | 1.052 | 1.037 | 1.040 | 0.000 | 0.0% | 51/2 |
| 2403.07790 | ✓ | 0.95 | 99.8% | 0.203 | 0.579 | 0.207 | 0.992 | 79.7% | 2/420 |
| 2409.01805 | ✓ | 0.92 | 100.0% | 2.843 | 0.121 | 3.407 | 0.503 | 11.0% | 3/91 |
| 2003.03348 | ✓ | 0.92 | 0.0% | ∞ | ∞ | ∞ | 0.000 | 0.0% | 12/857 |
| 2303.11395 | ✓ | 0.65 | 100.0% | 0.712 | 0.705 | 0.777 | 0.707 | 8.1% | 30/37 |
| 2304.01060 | ✓ | 0.65 | 96.1% | 2.523 | 1.302 | 1.129 | 0.621 | 2.0% | 30/51 |
| 2212.09764 | ✓ | 0.75 | 97.0% | 0.493 | 0.277 | 0.384 | 0.077 | 37.5% | 12/33 |
| 2405.19393 | ✓ | 0.85 | 94.5% | 0.275 | 0.384 | 0.367 | 0.874 | 53.8% | 10/55 |
| 2306.11575 | ✓ | 0.75 | 94.2% | 0.201 | 0.396 | 0.257 | 0.274 | 74.9% | 9/415 |
| 2006.06722 | ✓ | 0.92 | 30.3% | 0.005 | 0.010 | 0.007 | 0.033 | 100.0% | 2/76 |
| 2203.16567 | ✓ | 0.92 | 100.0% | 1.216 | 0.983 | 0.880 | 0.762 | 13.0% | 6/115 |
| 2008.13662 | ✓ | 0.85 | 98.4% | 0.225 | 0.201 | 0.242 | 0.740 | 74.6% | 10/64 |
| 2205.05700 | ✓ | 0.92 | 100.0% | 0.713 | 0.863 | 0.849 | 0.982 | 21.3% | 6/122 |
| 2303.06968 | ✓ | 0.75 | 100.0% | 1.698 | 1.251 | 1.591 | 0.973 | 0.0% | 12/174 |
| 1501.01639 | ✓ | 0.85 | 11.1% | 1.460 | 1.742 | 1.682 | 0.307 | 0.0% | 30/18 |
| 2307.11216 | ✓ | 0.85 | 100.0% | 0.185 | 0.197 | 0.219 | 0.767 | 73.3% | 32/60 |
| 2112.09620 | ✓ | 0.92 | 100.0% | 0.295 | 0.020 | 0.279 | 0.924 | 53.0% | 4/83 |
| 2408.16045 | ✓ | 0.85 | 84.7% | 5.517 | 5.527 | 5.505 | 0.842 | 0.0% | 30/124 |
| 2205.05574 | ✓ | 0.85 | 68.9% | 0.057 | 0.061 | 0.076 | 0.802 | 100.0% | 16/508 |
| 2307.07403 | ✓ | 0.85 | 95.3% | 0.302 | 0.342 | 0.307 | 0.970 | 49.1% | 7/555 |
| astro-ph/0611502 | ✓ | 0.85 | 97.8% | 8.710 | 8.505 | 8.540 | 0.980 | 0.0% | 18/91 |
| 2301.06778 | ✓ | 0.92 | 98.8% | 0.198 | 0.399 | 0.179 | 0.948 | 89.4% | 2/86 |
| 1912.07751 | — | — | EXCLUDED | — | — | — | — | — | — |
| 2402.07976 | ✓ | 0.85 | 97.6% | 0.444 | 0.281 | 0.397 | 0.940 | 19.7% | 10/10796 |
| 2102.00379 | ✓ | 0.72 | 57.7% | 0.482 | 0.400 | 2.959 | 0.544 | 13.3% | 4/26 |
| 2102.02207 | — | — | EXCLUDED | — | — | — | — | — | — |
| 2503.04726 | ✓ | 0.65 | 94.5% | 0.879 | 0.863 | 0.821 | 0.917 | 0.0% | 25/16611 |
| 2008.03305 | ✓ | 0.65 | 99.1% | 0.147 | 0.145 | 0.382 | 0.182 | 70.2% | 30/115 |
| 2412.09595 | — | — | EXCLUDED | — | — | — | — | — | — |
| 2008.02209 | ✓ | 0.75 | 44.4% | 7.579 | 5.379 | 2.867 | 0.181 | 0.0% | 12/99 |
| 2407.16628 | ✓ | 0.75 | 100.0% | 2.335 | 2.348 | 2.052 | 0.798 | 5.0% | 22/101 |
| 0801.1527 | ✓ | 0.85 | 77.1% | 2.299 | 2.253 | 3.265 | 0.830 | 3.0% | 9/175 |
| 2002.05165 | ✓ | 0.75 | 89.7% | 3.072 | 3.011 | 3.148 | 0.483 | 5.1% | 10/671 |
| 2409.12940 | ✓ | 0.75 | 81.6% | 0.435 | 0.551 | 0.528 | 0.551 | 40.1% | 19/174 |
| 2409.12115 | ✓ | 0.75 | 98.8% | 2.302 | 2.111 | 1.936 | 0.999 | 0.0% | 15/80 |
| 1201.5902 | ✓ | 0.65 | no_comparable_gt | — | — | — | — | — | — |
| 1911.05086 | ✓ | 0.90 | 100.0% | 0.000 | 0.000 | 0.000 | 1.000 | 100.0% | 401/401 |
| 2003.13698 | ✓ | 0.90 | 100.0% | 0.000 | 0.000 | 0.000 | 1.000 | 100.0% | 393/393 |
| 0810.5501 | ✓ | 0.85 | 100.0% | 0.051 | 0.228 | 0.216 | 0.855 | 71.4% | 4/112 |
| 2002.01796 | ✓ | 0.85 | no_comparable_gt | — | — | — | — | — | — |
| 1907.12628 | ✗ (AxionElectron) | 0.82 | no_comparable_gt | — | — | — | — | — | — |
| 1906.08814 | ✓ | 0.92 | 100.0% | 0.000 | 0.000 | ∞ | 0.000 | 100.0% | 1/2 |
| 2101.02805 | — | — | EXCLUDED | — | — | — | — | — | — |
| 2405.20444 | ✓ | 0.92 | 99.8% | 0.647 | 0.910 | 0.581 | 0.459 | 9.8% | 17/493 |
| 2301.11512 | ✓ | 0.85 | 100.0% | 0.061 | 0.060 | 0.075 | 0.828 | 56.2% | 21/16 |
| 2207.05767 | — | — | EXCLUDED | — | — | — | — | — | — |
| 2003.13144 | ✓ | 0.85 | 86.4% | 0.960 | 1.021 | 0.968 | 0.718 | 0.0% | 21/22 |
| 2310.13891 | ✓ | 0.75 | 100.0% | 0.113 | 0.094 | 0.117 | 0.039 | 100.0% | 22/87 |
| 2304.12907 | ✓ | 0.85 | 86.5% | 6.450 | 9.003 | 7.071 | 0.242 | 3.7% | 43/126 |
| 2211.00022 | ✓ | 0.85 | 97.2% | 0.586 | 0.362 | 1.787 | 0.970 | 37.4% | 537/143 |
| 2406.19445 | ✓ | 0.92 | 43.4% | 2.765 | 3.060 | 2.617 | 0.202 | 0.0% | 12/99 |
| 2402.17140 | — | — | EXCLUDED | — | — | — | — | — | — |
| 2110.01582 | ✓ | 0.85 | 100.0% | 3.535 | 3.779 | 3.451 | 0.045 | 0.0% | 26/26 |
| 2301.03622 | ✓ | 0.75 | 100.0% | 0.109 | 0.111 | 0.124 | 0.539 | 90.3% | 26/401 |
| 1410.5244 | ✓ | 0.85 | 100.0% | 0.107 | 0.095 | 0.075 | 0.599 | 90.5% | 197/21 |
| 2410.02858 | ✗ (None) | 0.00 | no_prediction | — | — | — | — | — | — |
| 2110.10497 | ✓ | 0.92 | 23.6% | 1.184 | 1.016 | 1.004 | 0.248 | 5.9% | 5/72 |
| 2012.05427 | ✓ | 0.85 | 100.0% | 0.577 | 3.943 | 4.443 | 0.633 | 26.9% | 29/26 |
| 2204.03818 | ✓ | 0.75 | 100.0% | 0.566 | ∞ | 0.598 | 0.011 | 1.4% | 24/3689 |
| 2405.12285 | ✓ | 0.85 | 100.0% | 0.908 | 0.789 | 0.927 | 0.945 | 5.5% | 30/91 |
| 2406.02546 | ✓ | 0.92 | 95.5% | 0.550 | 1.313 | 0.660 | 0.902 | 23.8% | 3/22 |
| 2209.03419 | ✓ | 0.75 | 100.0% | 0.467 | 0.472 | 0.458 | 0.119 | 3.4% | 79/325 |
| 2212.01971 | ✓ | 0.85 | 29.0% | 0.247 | 0.290 | 0.287 | 0.321 | 65.8% | 7/131 |
| 2305.09711 | ✓ | 0.92 | 0.0% | ∞ | ∞ | ∞ | 0.000 | 0.0% | 47/57500 |
| 1502.04490 | ✓ | 0.85 | 71.5% | 2.221 | 2.954 | 2.781 | 0.653 | 8.0% | 9/123 |
| 1905.05579 | ✓ | 0.92 | 98.1% | 0.106 | 0.242 | 0.132 | 0.950 | 92.2% | 2/104 |
| 1301.6557 | ✓ | 0.75 | 99.2% | 1.143 | 1.573 | 1.648 | 0.895 | 1.6% | 37/123 |
| 2208.03183 | — | — | EXCLUDED | — | — | — | — | — | — |
| 2008.12231 | ✓ | 0.65 | 100.0% | 6.775 | ∞ | — | — | 0.0% | 48/1 |
| 2308.08337 | ✓ | 0.75 | 100.0% | 6.463 | ∞ | — | — | 0.0% | 30/1 |
| 1008.3536 | ✓ | 0.65 | 40.0% | 2.876 | 2.427 | 2.773 | 0.237 | 0.0% | 5/100 |
| 2106.00022 | ✓ | 0.85 | 84.5% | 0.670 | 0.564 | 0.690 | 0.912 | 0.0% | 36/58 |
| 1804.10777 | ✓ | 0.75 | 66.7% | 3.522 | 1.815 | 2.190 | 0.863 | 0.0% | 7/3 |
| 1504.00118 | ✓ | 0.75 | 100.0% | 5.182 | ∞ | 5.579 | 0.020 | 0.0% | 38/12 |
| 2006.02828 | ✓ | 0.85 | 100.0% | 1.015 | ∞ | 1.037 | 0.000 | 0.0% | 27/6 |
| 1907.12449 | ✓ | 0.85 | 99.6% | 4.102 | 0.251 | 3.309 | 0.817 | 2.2% | 8/555 |
| 1903.05101 | ✓ | 0.65 | 100.0% | 4.072 | 4.095 | 4.070 | 0.848 | 0.0% | 7/53 |
| 2006.13929 | ✓ | 0.75 | 99.0% | 1.568 | 0.997 | 1.230 | 0.689 | 15.5% | 10/98 |
| 1807.04512 | ✗ (ScalarBaryon) | 0.50 | no_comparable_gt | — | — | — | — | — | — |
| hep-ph/0307284 | ✓ | 0.75 | no_comparable_gt | — | — | — | — | — | — |
| 2103.03783 | ✓ | 0.75 | 13.0% | 5.970 | 6.423 | 5.997 | 0.049 | 0.0% | 7/69 |
| 2205.06817 | — | — | EXCLUDED | — | — | — | — | — | — |
| 2306.16219 | ✗ (ScalarNucleon) | 0.65 | no_comparable_gt | — | — | — | — | — | — |
| 2303.00778 | ✓ | 0.75 | 100.0% | 2.060 | 2.060 | 2.073 | 0.176 | 0.0% | 19/2 |
| 2212.05721 | ✓ | 0.85 | 31.8% | 0.309 | 0.405 | 0.291 | 0.577 | 49.1% | 5/333 |
| 2005.14694 | — | — | EXCLUDED | — | — | — | — | — | — |
| 1503.06886 | ✓ | 0.85 | 100.0% | 3.285 | 2.555 | 2.071 | 0.990 | 4.6% | 6/1006 |
| 1902.02788 | ✓ | 0.50 | convention_mismatch | — | — | — | — | — | — |
| 2301.03433 | ✓ | 0.85 | 100.0% | 11.069 | 11.379 | 10.357 | 0.974 | 0.0% | 2965/172 |
| 2302.04565 | ✓ | 0.75 | 100.0% | 4.085 | 3.239 | 3.221 | 0.317 | 0.0% | 13/848 |
| 1604.08514 | ✓ | 0.50 | 87.5% | 0.746 | 1.057 | 0.896 | 0.892 | 6.1% | 3/505 |
| quant-ph/0106045 | ✓ | 0.30 | no_comparable_gt | — | — | — | — | — | — |
| 2109.08822 | ✓ | 0.92 | 65.6% | 0.411 | 0.849 | 1.026 | 0.740 | 33.3% | 44/32 |
| 2105.13085 | ✗ (DarkPhoton) | 0.30 | no_comparable_gt | — | — | — | — | — | — |
| 2301.08736 | ✗ (DarkPhoton) | 0.65 | no_comparable_gt | — | — | — | — | — | — |
| 2403.02381 | ✓ | 0.85 | 99.9% | 0.014 | 0.008 | 0.330 | 0.466 | 63.9% | 1318/1001 |
| 2409.03814 | ✓ | 0.92 | 51.6% | 0.609 | 0.684 | 0.594 | 0.508 | 16.4% | 2/308 |
| 2112.07687 | ✗ (DarkPhoton) | 0.30 | no_comparable_gt | — | — | — | — | — | — |
| 2302.00685 | ✓ | 0.65 | 0.0% | ∞ | ∞ | ∞ | 0.000 | 0.0% | 5/11 |
| 2011.11646 | ✗ (AxionNeutron) | 0.72 | no_comparable_gt | — | — | — | — | — | — |
| 2406.10337 | ✓ | 0.35 | 23.5% | 8.936 | 9.012 | 9.013 | 0.043 | 0.0% | 4/51 |
| 2011.08693 | — | — | EXCLUDED | — | — | — | — | — | — |
| 2012.12790 | ✓ | 0.65 | convention_mismatch | — | — | — | — | — | — |
| 2412.03655 | ✓ | 0.65 | convention_mismatch | — | — | — | — | — | — |
| 2105.13963 | ✓ | 0.85 | convention_mismatch | — | — | — | — | — | — |
| 2404.00616 | — | — | EXCLUDED | — | — | — | — | — | — |
| 2412.20932 | ✓ | 0.75 | 50.0% | 9.977 | 2.996 | 6.487 | 0.996 | 0.0% | 2/2 |
| 2408.07740 | ✓ | 0.65 | 100.0% | 3.136 | ∞ | 4.259 | 0.051 | 0.0% | 2/18 |
| 2410.21590 | ✗ (AxionNeutron) | 0.65 | no_comparable_gt | — | — | — | — | — | — |
| 2205.01637 | ✓ | 0.85 | no_comparable_gt | — | — | — | — | — | — |
| 1708.08464 | ✗ (AxionNeutron) | 0.65 | no_comparable_gt | — | — | — | — | — | — |
| 2303.09865 | ✓ | 0.65 | 100.0% | 6.719 | 3.352 | 3.451 | 0.210 | 0.0% | 79/2 |
| 2211.02661 | ✗ (AxionNeutron) | 0.65 | no_comparable_gt | — | — | — | — | — | — |
| 2301.10784 | ✓ | 0.45 | convention_mismatch | — | — | — | — | — | — |
| 1003.0964 | — | — | EXCLUDED | — | — | — | — | — | — |
| 2312.11608 | — | — | EXCLUDED | — | — | — | — | — | — |

## Breakdown by Extraction Source

Median residual is over papers with mass-range overlap; zero-overlap papers are listed separately.

| Source | Papers | Compared | Zero-overlap | Med. Resid. | ≤0.3 dex |
|--------|--------|----------|--------------|-------------|----------|
| table | 3 | 3 | 0 | 0.124 dex | 48.9% |
| figure_vision | 111 | 91 | 10 | 0.684 dex | 23.5% |
| text | 152 | 132 | 13 | 0.531 dex | 36.0% |

## Breakdown by Difficulty

> Difficulty is a placeholder label for the repo-sourced pool (nearly all `medium`); this table is informational only.

| Difficulty | Papers | Coupling Acc. | Med. Resid. | ≤0.3 dex |
|------------|--------|---------------|-------------|----------|
| easy | 11 | 90.9% | 0.649 dex | 30.1% |
| medium | 250 | 92.4% | 0.643 dex | 31.3% |
| hard | 29 | 100.0% | 0.498 dex | 31.0% |

## Confidence Calibration

- "Accurate" = median interpolation residual < **0.32 dex** AND interpolation coverage ≥ 50%.
- The **0.32 dex** threshold is the run-to-run LLM extraction *noise floor* (90th-pct per-paper median-residual std across repeated extractions, PR #545) — the binding floor. It is **not** the upstream digitization floor, which is only ~0.034 dex for table/text-sourced papers (PR #558). So a residual gap here is **real extractor overconfidence, not a yardstick artifact**.

### Binned accuracy (pass/fail)

| Bin | N | Mean Conf. | Actual Acc. | Gap |
|-----|---|------------|-------------|-----|
| [0.2–0.7) | 28 | 59.1% | 10.7% | +0.48 |
| [0.8–0.8) | 55 | 75.1% | 10.9% | +0.64 |
| [0.8–0.8) | 85 | 85.0% | 22.4% | +0.63 |
| [0.9–0.9) | 70 | 91.9% | 34.3% | +0.58 |
| [0.9–0.9) | 8 | 95.0% | 87.5% | +0.07 |

> **Interpretation**: Gap > 0 means the pipeline is overconfident; Gap < 0 means underconfident.

### Continuous view: residual distribution per bin

Median (and IQR) of each bin's per-paper median residual, over papers with a finite residual (zero mass-overlap papers excluded from the distribution but still counted in N). If confidence tracked accuracy, the median residual would fall as confidence rises.

| Bin | N | N finite | Median resid. (dex) | IQR (dex) |
|-----|---|----------|---------------------|-----------|
| [0.2–0.7) | 28 | 26 | 1.75 | 0.65–3.88 |
| [0.8–0.8) | 55 | 48 | 1.28 | 0.48–3.18 |
| [0.8–0.8) | 85 | 78 | 0.65 | 0.28–2.13 |
| [0.9–0.9) | 70 | 62 | 0.42 | 0.13–1.18 |
| [0.9–0.9) | 8 | 8 | 0.13 | 0.01–0.23 |

### Continuous view: empirical P(residual < τ) per bin

Fraction of papers in each bin whose median residual is below τ dex (τ = 0.32 is the noise floor used above). A well-calibrated, accurate extractor would show these probabilities rising with confidence.

| Bin | N | P(<0.10) | P(<0.32) | P(<0.50) | P(<1.00) |
|-----|---|----|----|----|----|
| [0.2–0.7) | 28 | 0.0% | 14.3% | 17.9% | 39.3% |
| [0.8–0.8) | 55 | 1.8% | 10.9% | 25.5% | 38.2% |
| [0.8–0.8) | 85 | 8.2% | 27.1% | 41.2% | 58.8% |
| [0.9–0.9) | 70 | 15.7% | 38.6% | 48.6% | 62.9% |
| [0.9–0.9) | 8 | 50.0% | 87.5% | 100.0% | 100.0% |

## Methodology

### Curve selection (what each extraction is compared against)
- A paper usually produces several repo curves (one per coupling). The single extraction is compared **only** against the GT curve whose coupling matches the extracted coupling type (taken from the data file's `limit_data/<dir>/`).
- Papers whose extracted coupling has no matching GT curve, or whose GT curve has <2 usable points, are reported under Curve-Comparison Coverage and excluded from residual statistics — they do not measure extraction quality.

### Caveats on the residual floor
- The ground truth `g(x_i)` is the **upstream-curated** repo curve (itself digitised and rescaled from the same papers), not the paper's raw numbers, so a perfect extraction still shows a small nonzero residual from the upstream digitisation/convention gap. That gap is now *measured*: only ~0.034 dex for table/text-sourced papers (PR #558, truly-independent gold-vs-repo, N=10) — i.e. the repo GT is faithful, NOT a ~0.5 dex floor. The figure-only digitisation component remains unmeasured. The binding floor for confidence calibration is instead the run-to-run LLM extraction noise floor (~0.32 dex, PR #545).
- `is_new_limit`, `is_projection`, and `data_source` are scored against an **independent LLM labeler** (`label_ground_truth.py`, `claude-opus-4-5`), a distinct model/prompt from the extractor (so not self-agreement), audited against a human reader (see Classification Accuracy). Entries not yet labeled keep placeholder values (`auto_expanded` / `repo_upstream`) and are excluded from these metrics. `difficulty` is derived mechanically (figure-only + few points ⇒ hard; table/text + many points ⇒ easy; else medium) and is informational only.

### Interpolation metric (primary)
1. Filter boundary-closure sentinel points (coupling >= 1e-2) from both extracted and GT data
2. Build `scipy.interpolate.interp1d` from extracted points in log10(mass) → log10(coupling) space
3. Evaluate the interpolation at each ground-truth mass value
4. Compute residual = |log10(g_interpolated) - log10(g_ground_truth)| at each GT point
5. Only GT points inside the extracted mass range are used (no extrapolation)

**Key statistics:**
- **Interpolation coverage**: fraction of GT points inside the extracted mass range
- **Median/P90 residual**: summary of coupling errors in dex (0.3 dex ≈ factor 2)
- **Fraction within threshold**: what % of GT points have residual below 0.1/0.3/0.5/1.0 dex

When multiple extracted points share the same mass, the strongest constraint (lowest coupling) is kept.

### Symmetric / 2-D metrics (complementary)
- **Reverse pass**: the same interpolation, swapped — build the interp from the GT points and evaluate at the *extracted* masses. The forward pass cannot see an extraction that runs past the GT range; the reverse pass surfaces it as a low reverse coverage / large reverse residual.
- **Area-between-curves**: sample both log-log curves on a common grid over their overlapping log-mass range, integrate |Δ log10 coupling| (trapezoid), normalise by the overlap width → mean dex offset. Penalises both vertical offset and horizontal (mass) shift.
- **Mass-range Jaccard**: Jaccard index of the extracted vs GT log-mass intervals (intersection / union). Penalises over- and under-claimed mass extent independently of interpolation density.

### Confidence calibration
- A paper is "accurate" if median residual < **0.32 dex** AND interpolation coverage ≥ 50%.
- The **0.32 dex** threshold is the run-to-run LLM extraction noise floor (90th-pct per-paper median-residual std over repeated extractions, PR #545) — the binding floor. It is deliberately NOT relaxed to the upstream digitization floor, which is only ~0.034 dex for table/text papers (PR #558, truly-independent gold-vs-repo). The original #542 premise — that 0.3 dex sits below a ~0.5 dex digitization floor — is therefore falsified; 0.3 dex was about right, but justified by *noise*, not digitization.
- **Caveat**: the 0.034 dex digitization floor is measured only for table/text sources. For figure-only source papers the upstream figure-digitization error is unmeasured, so this is not a universal floor.
- Coverage ≥ 50% is kept as an orthogonal curve-quality gate: a low residual on only a sliver of the mass range is not a usable extraction.
- Papers binned by extraction_confidence; actual accuracy computed per bin. Perfect calibration: actual accuracy = mean confidence in each bin.
- Two continuous views supplement the pass/fail rate: the per-bin residual *distribution* (median + IQR) and the empirical P(residual < τ) for τ ∈ {0.1, 0.32, 0.5, 1.0} dex — so a bin shows the real residual spread, not just a thresholded rate.
