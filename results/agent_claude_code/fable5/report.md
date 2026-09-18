# AutoAxionLimits Extraction Pipeline — Evaluation Report

## Summary

- **Papers evaluated**: 329
- **Papers with curve comparison**: 281

## Curve-Comparison Coverage

A curve is scored only against a ground-truth curve of the **same coupling**. Papers whose extracted coupling has no matching GT curve are not comparable and are excluded from residual statistics (this is not an extraction failure).

| Status | Papers | Meaning |
|--------|--------|---------|
| compared | 281 | scored against a same-coupling GT curve |
| no_comparable_gt | 7 | extracted coupling has no GT curve in the pool (usually a coupling misclassification) |
| gt_unusable | 2 | GT curve has <2 usable points after boundary filtering |
| no_extracted_points | 1 | pipeline returned no data points |
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
| coupling_type | 99.7% | 291 |
| is_new_limit | 100.0% | 32 |
| is_projection | 100.0% | 32 |
| data_source | 18.8% | 32 |

> **Label provenance**: `is_new_limit`, `is_projection`, and `data_source` are scored against an **independent LLM labeler** (`evaluation/label_ground_truth.py`, model `claude-opus-4-5`) whose sole task is to classify paper properties — a distinct model and prompt from the extractor it grades, so this is a fair cross-model test, not self-agreement. These are **not human gold labels**. A human audit of 15 labeled papers found per-field labeler↔human agreement: is_new_limit 15/15, is_projection 15/15, data_source 14/15 (difficulty is derived mechanically from data_source + point count, not labeled).

### Coupling Type Misclassifications

| arXiv ID | Predicted | Expected |
|----------|-----------|----------|
| 1906.11844 | AxionProton | ['AxionNeutron'] |

### Coupling-Type Confusion Matrix (multi-type-aware)

Rows = authoritative GT type, columns = predicted type. A prediction is correct iff it is in ANY of the paper's GT types (diagonal). Off-diagonal cells are the confusable clusters. Graded 291, correct 290 (99.7%), skipped 38 (no prediction / no GT type).

| GT ⟍ Pred | AxionEDM | AxionElectron | AxionMass | AxionNeutron | AxionPhoton | AxionProton | DarkPhoton | MonopoleDipole | ScalarBaryon | ScalarElectron | ScalarNucleon | ScalarPhoton | VectorBL |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| AxionEDM | **4** |  |  |  |  |  |  |  |  |  |  |  |  |
| AxionElectron |  | **16** |  |  |  |  |  |  |  |  |  |  |  |
| AxionMass |  |  | **19** |  |  |  |  |  |  |  |  |  |  |
| AxionNeutron |  |  |  | **14** |  | 1 |  |  |  |  |  |  |  |
| AxionPhoton |  |  |  |  | **139** |  |  |  |  |  |  |  |  |
| AxionProton |  |  |  |  |  | **3** |  |  |  |  |  |  |  |
| DarkPhoton |  |  |  |  |  |  | **60** |  |  |  |  |  |  |
| MonopoleDipole |  |  |  |  |  |  |  | **3** |  |  |  |  |  |
| ScalarBaryon |  |  |  |  |  |  |  |  | **1** |  |  |  |  |
| ScalarElectron |  |  |  |  |  |  |  |  |  | **2** |  |  |  |
| ScalarNucleon |  |  |  |  |  |  |  |  |  |  | **5** |  |  |
| ScalarPhoton |  |  |  |  |  |  |  |  |  |  |  | **14** |  |
| VectorBL |  |  |  |  |  |  |  |  |  |  |  |  | **10** |

Off-diagonal confusions (GT → predicted, richest first):

- AxionNeutron → AxionProton: 1

## Extraction Quality — Interpolation Metric (primary)

Build log-log interpolation from extracted points, evaluate at ground-truth masses.

- **Papers compared**: 281 (281 with mass-range overlap, 0 with zero overlap)

**Coupling-value accuracy** (papers with mass-range overlap):
- **Median residual across papers**: 0.024 dex (IQR 0.009–0.093)
- **Mean residual across papers** (outlier-sensitive): 0.102 dex
- **Mean fraction within 0.3 dex (factor 2; the leaderboard headline is 10%, results/leaderboard.py)**: 89.7%
- **Mean fraction within 0.5 dex (factor 3)**: 93.7%

**Mass-range coverage** (a separate failure mode):
- **Mean interpolation coverage**: 92.5%
- **Zero-overlap papers**: 0/281 (0.0%) — extracted masses miss the GT range entirely (usually 1–2 extracted points or the wrong mass window)

**Reverse pass** (GT interpolated onto the *extracted* masses):
- Mirrors the forward pass. A large forward-vs-reverse gap, or a reverse coverage well below the forward coverage, flags an extraction whose mass *extent* or shape disagrees with the GT (e.g. running past the GT range).
- **Median reverse residual across papers**: 0.027 dex (forward: 0.024 dex)
- **Mean reverse interpolation coverage**: 90.3% (forward: 92.5%)

## Residual by Coupling Type — Micro vs Macro Average (issue #543)

The compared-paper pool is dominated by one coupling type (AxionPhoton), so the per-paper **micro-average** headline is largely that one type's number. The **macro-average** weights each coupling type equally (mean of the per-type medians), exposing how the pipeline does across the *range* of couplings rather than on the most common one.

- **Micro-average median residual** (per paper, 281 papers): 0.024 dex
- **Macro-average median residual** (equal weight per type, 13 types): 0.035 dex
- **Macro − micro gap**: +0.011 dex (macro is worse; a positive gap means the rarer couplings are harder than the AxionPhoton-dominated micro-average implies)

Per-type medians carry a bootstrap 95% CI (1000 resamples). Rows with **N < 5** are flagged small-sample — their median and CI are unstable and should not be read as a reliable per-type score.

| Coupling Type | N | Median Resid. (dex) | 95% CI (dex) | Flag |
|---------------|---|---------------------|--------------|------|
| AxionPhoton | 138 | 0.019 | [0.013, 0.025] |  |
| DarkPhoton | 58 | 0.047 | [0.020, 0.076] |  |
| AxionMass | 18 | 0.022 | [0.013, 0.061] |  |
| AxionElectron | 16 | 0.018 | [0.006, 0.054] |  |
| AxionNeutron | 14 | 0.025 | [0.013, 0.042] |  |
| ScalarPhoton | 14 | 0.066 | [0.049, 0.204] |  |
| VectorBL | 9 | 0.111 | [0.010, 0.285] |  |
| AxionEDM | 4 | 0.049 | [0.003, 0.440] | ⚠ small-sample (N<5) |
| MonopoleDipole | 3 | 0.040 | [0.005, 0.188] | ⚠ small-sample (N<5) |
| ScalarNucleon | 2 | 0.010 | [0.009, 0.011] | ⚠ small-sample (N<5) |
| AxionProton | 2 | 0.009 | [0.004, 0.015] | ⚠ small-sample (N<5) |
| ScalarElectron | 2 | 0.037 | [0.023, 0.050] | ⚠ small-sample (N<5) |
| ScalarBaryon | 1 | 0.002 | [0.002, 0.002] | ⚠ small-sample (N<5) |

## Shape & Mass-Range Agreement — Symmetric Metrics (complementary)

These are symmetric, 2-D complements to the (asymmetric, vertical-only) interpolation residual. **Area-between-curves** integrates |Δ log10 coupling| over the overlapping log-mass range and normalises by the overlap width (a single shape+offset number, in dex; a pure mass shift inflates it even when the vertical residual looks fine). **Mass-range Jaccard** is the Jaccard index of the extracted vs GT log-mass intervals (1.0 = identical extent; small = over-/under-claimed mass range), reported separately from interpolation coverage.

- **Papers scored**: 272 (272 with mass overlap for area)
- **Median area-between-curves**: 0.052 dex (mean 0.175 dex)
- **Median mass-range Jaccard**: 0.984 (mean 0.802)

## Per-Paper Results

| arXiv ID | Coupling | Conf. | Interp. Cov. | Med. Resid. | Rev. Resid. | Area (dex) | Mass Jaccard | ≤0.3 dex | Points |
|----------|----------|-------|--------------|-------------|-------------|------------|--------------|----------|--------|
| 2208.07293 | ✓ | 0.85 | 100.0% | 0.076 | 0.076 | 0.080 | 0.045 | 100.0% | 90/2 |
| 2212.04413 | ✓ | 0.85 | 99.1% | 0.008 | 0.006 | 0.012 | 0.995 | 100.0% | 80/107 |
| 2410.19902 | ✓ | 0.65 | 100.0% | 0.021 | 0.021 | 0.021 | 0.636 | 100.0% | 2/2 |
| 1907.03767 | ✓ | 0.85 | 98.4% | 0.019 | 0.014 | 0.065 | 0.994 | 92.2% | 98/182 |
| 2209.06216 | ✓ | 0.85 | 98.4% | 0.018 | 0.013 | 0.565 | 0.969 | 91.1% | 71/2771 |
| 2005.14184 | ✓ | 0.92 | 99.7% | 0.058 | 0.053 | 0.055 | 0.998 | 96.8% | 93/891 |
| 2504.00720 | ✓ | 0.85 | 97.1% | 0.013 | 0.020 | 0.198 | 0.997 | 95.6% | 95/70 |
| 2408.02668 | ✓ | 0.90 | 99.8% | 0.167 | 0.197 | 0.209 | 0.956 | 79.1% | 83/413 |
| 1905.13650 | ✓ | 0.70 | 100.0% | 1.392 | 1.310 | 0.997 | 0.699 | 3.3% | 46/243 |
| 2110.03679 | ✓ | 0.93 | 98.4% | 0.121 | 0.165 | 0.088 | 0.266 | 87.4% | 29/129 |
| 2303.07370 | ✓ | 0.90 | 99.1% | 0.046 | 0.046 | 0.047 | 0.941 | 100.0% | 27/107 |
| 2309.16600 | ✓ | 0.85 | 97.3% | 0.018 | 0.037 | 0.025 | 0.991 | 100.0% | 100/188 |
| 2504.16044 | ✓ | 0.70 | gt_unusable | — | — | — | — | — | — |
| 2312.06746 | ✓ | 0.92 | 100.0% | 0.002 | 0.002 | 0.028 | 0.995 | 100.0% | 70/171 |
| 1310.8098 | ✓ | 0.92 | 97.0% | 0.008 | 0.008 | 0.008 | 0.324 | 100.0% | 59/135 |
| 2408.02368 | ✓ | 0.92 | 100.0% | 0.020 | 0.021 | 0.025 | 0.996 | 100.0% | 100/647 |
| 2011.07100 | ✓ | 0.85 | 97.5% | 0.188 | 0.196 | 0.195 | 0.334 | 100.0% | 60/79 |
| 2302.09096 | ✓ | 0.90 | 100.0% | 0.040 | 0.005 | 0.100 | 0.499 | 97.6% | 60/41 |
| 1410.7267 | ✓ | 0.92 | 100.0% | 0.009 | 0.009 | 0.014 | 0.994 | 100.0% | 60/74 |
| 1712.00483 | ✓ | 0.85 | 97.0% | 0.324 | 0.336 | 0.382 | 0.650 | 46.9% | 42/33 |
| 1607.07327 | ✓ | 0.90 | 100.0% | 0.002 | 0.005 | 0.004 | 0.984 | 100.0% | 60/35 |
| 1611.05852 | ✓ | 0.75 | no_comparable_gt | — | — | — | — | — | — |
| 2111.06883 | ✓ | 0.85 | no_comparable_gt | — | — | — | — | — | — |
| 0802.2350 | ✓ | 0.92 | 70.8% | 0.011 | 0.010 | 0.012 | 0.679 | 100.0% | 35/24 |
| 2009.04517 | ✓ | 0.70 | 93.1% | 0.006 | 0.005 | 0.006 | 0.073 | 100.0% | 26/29 |
| 2010.08107 | ✓ | 0.85 | 99.5% | 0.065 | 0.044 | 0.095 | 0.988 | 93.2% | 86/208 |
| 2201.02042 | — | — | EXCLUDED | — | — | — | — | — | — |
| 2403.03004 | ✓ | 0.75 | 98.8% | 0.192 | 0.124 | 0.171 | 0.998 | 77.3% | 85/414 |
| 2205.03617 | ✓ | 0.60 | no_comparable_gt | — | — | — | — | — | — |
| 2310.06017 | ✓ | 0.90 | 99.1% | 0.010 | 0.010 | 0.012 | 0.997 | 100.0% | 50/113 |
| 2102.08764 | ✓ | 0.90 | 100.0% | 0.000 | 0.000 | 0.000 | 0.892 | 100.0% | 2/2 |
| 2308.14656 | ✓ | 0.85 | 97.3% | 0.005 | 0.005 | 0.006 | 0.994 | 100.0% | 82/75 |
| 2207.03102 | ✓ | 0.95 | 100.0% | 0.000 | 0.000 | 0.000 | 0.360 | 100.0% | 2/2 |
| 1505.07455 | — | — | EXCLUDED | — | — | — | — | — | — |
| 2105.04603 | ✓ | 0.60 | 97.7% | 0.164 | 0.169 | 0.168 | 0.978 | 97.5% | 99/707 |
| 2303.11792 | ✓ | 0.90 | 95.0% | 0.136 | 0.136 | 0.133 | 0.889 | 100.0% | 76/20 |
| 1607.06083 | ✓ | 0.65 | 50.0% | 0.000 | 0.000 | 0.000 | 0.522 | 100.0% | 72/2 |
| 2108.04746 | ✓ | 0.85 | 98.2% | 0.066 | 0.055 | 0.108 | 0.997 | 82.4% | 200/283 |
| 2208.12670 | ✓ | 0.95 | 100.0% | 0.001 | ∞ | — | — | 100.0% | 189/1 |
| 1806.05120 | ✓ | 0.92 | 98.9% | 0.109 | 0.069 | 0.113 | 0.994 | 93.5% | 38/94 |
| 2101.01241 | ✓ | 0.90 | 100.0% | 0.003 | ∞ | — | — | 100.0% | 86/1 |
| 2404.14476 | ✓ | 0.95 | 96.1% | 0.002 | 0.001 | 0.002 | 0.190 | 100.0% | 95/51 |
| 2504.12377 | ✓ | 0.90 | 100.0% | 0.003 | 0.003 | 0.003 | 0.584 | 100.0% | 34/15 |
| 2408.15227 | ✓ | 0.90 | 99.1% | 0.028 | 0.032 | 0.038 | 0.984 | 100.0% | 100/230 |
| 2209.09917 | ✓ | 0.92 | 100.0% | 0.034 | 0.034 | 0.035 | 1.000 | 100.0% | 5/5 |
| 2406.00387 | ✓ | 0.85 | 99.1% | 0.002 | 0.000 | 0.318 | 1.000 | 100.0% | 80/108 |
| 1207.3275 | ✓ | 0.90 | 100.0% | 0.023 | 0.020 | 0.022 | 0.044 | 100.0% | 28/9 |
| 2205.01079 | ✓ | 0.90 | 100.0% | 0.012 | 0.012 | 0.011 | 1.000 | 100.0% | 14/14 |
| 2212.02403 | ✓ | 0.90 | 90.5% | 0.040 | 0.035 | 0.044 | 0.967 | 100.0% | 95/42 |
| 1903.12190 | ✓ | 0.90 | 66.7% | 0.120 | 0.118 | 0.129 | 0.914 | 100.0% | 27/3 |
| 2305.00890 | ✓ | 0.90 | 100.0% | 0.008 | 0.001 | 0.048 | 0.997 | 98.2% | 93/4991 |
| 1708.06367 | ✓ | 0.90 | 100.0% | 0.023 | 0.025 | 0.042 | 0.947 | 100.0% | 90/36 |
| 2312.13723 | — | — | EXCLUDED | — | — | — | — | — | — |
| 2410.10363 | ✓ | 0.75 | 100.0% | 0.001 | 0.001 | 0.278 | 0.995 | 100.0% | 59/288 |
| 1202.5851 | — | — | EXCLUDED | — | — | — | — | — | — |
| 2208.06519 | ✓ | 0.92 | 100.0% | 0.093 | ∞ | — | — | 100.0% | 52/1 |
| 2401.16747 | ✓ | 0.90 | 97.0% | 0.009 | 0.023 | 0.029 | 0.999 | 100.0% | 100/66 |
| 2401.18076 | ✓ | 0.90 | 100.0% | 0.035 | 0.036 | 0.040 | 0.974 | 100.0% | 62/29 |
| 2503.13653 | ✓ | 0.55 | 96.2% | 0.522 | 0.508 | 1.682 | 0.561 | 0.0% | 71/53 |
| 2308.06339 | ✓ | 0.90 | 96.1% | 0.017 | 0.017 | 0.030 | 0.997 | 100.0% | 126/76 |
| 2109.11734 | ✓ | 0.90 | 91.7% | 0.024 | 0.007 | 0.133 | 0.998 | 81.8% | 12/12 |
| 2308.09077 | ✓ | 0.90 | 98.1% | 0.170 | 0.172 | 0.169 | 0.993 | 100.0% | 99/54 |
| 2110.06096 | ✓ | 0.90 | 98.8% | 0.019 | 0.013 | 0.020 | 0.989 | 100.0% | 109/242 |
| 2205.03679 | ✓ | 0.90 | 99.8% | 0.128 | 0.145 | 0.148 | 0.999 | 95.7% | 90/1525 |
| 2202.08858 | ✓ | 0.88 | 99.0% | 0.054 | 0.076 | 0.087 | 0.996 | 95.5% | 62/203 |
| 2503.14582 | ✓ | 0.92 | 100.0% | 0.365 | 0.348 | 0.416 | 0.996 | 36.5% | 47/196912 |
| 1207.2442 | ✓ | 0.90 | 78.0% | 0.006 | 0.004 | 0.031 | 0.735 | 94.9% | 75/50 |
| 1609.00667 | — | — | EXCLUDED | — | — | — | — | — | — |
| 2407.03828 | ✓ | 0.92 | 99.1% | 0.022 | 0.026 | 0.024 | 0.296 | 100.0% | 70/116 |
| 1810.04602 | ✓ | 0.92 | 96.4% | 0.017 | 0.065 | 0.030 | 0.880 | 96.2% | 39/55 |
| 2110.10262 | — | — | EXCLUDED | — | — | — | — | — | — |
| 2306.05934 | ✓ | 0.90 | 99.1% | 0.045 | 0.029 | 0.041 | 0.987 | 100.0% | 80/2636 |
| 2306.01048 | ✓ | 0.80 | 97.2% | 0.004 | 0.003 | 1.091 | 0.324 | 100.0% | 17/36 |
| 2008.08773 | ✓ | 0.90 | 97.8% | 0.084 | 0.058 | 0.101 | 0.905 | 96.8% | 78/543 |
| 2007.04990 | — | — | EXCLUDED | — | — | — | — | — | — |
| 2207.11968 | ✓ | 0.90 | 98.4% | 0.010 | 0.012 | 0.015 | 0.999 | 100.0% | 43/128 |
| 0807.2926 | ✓ | 0.90 | 22.2% | 0.025 | 0.025 | 0.027 | 0.921 | 100.0% | 10/18 |
| 1508.02463 | ✓ | 0.90 | 97.3% | 0.005 | 0.004 | 0.012 | 0.213 | 100.0% | 61/111 |
| 0809.4700 | ✓ | 0.90 | 97.1% | 0.008 | 0.008 | 0.013 | 0.165 | 91.2% | 33/35 |
| 2006.07055 | ✓ | 0.80 | 99.3% | 0.058 | 0.044 | 0.088 | 0.991 | 81.4% | 161/146 |
| 2004.02733 | ✓ | 0.85 | 100.0% | 0.039 | 0.039 | 0.034 | 0.958 | 100.0% | 17/33 |
| 2111.09892 | ✓ | 0.82 | 50.0% | 0.000 | 0.000 | 0.000 | 0.591 | 100.0% | 9/2 |
| 1401.6460 | ✓ | 0.85 | 75.0% | 0.440 | 0.439 | 0.522 | 0.956 | 0.0% | 45/4 |
| 2204.01454 | ✓ | 0.85 | 100.0% | 0.062 | 0.058 | 0.074 | 0.980 | 100.0% | 57/42 |
| 2410.02218 | — | — | EXCLUDED | — | — | — | — | — | — |
| 1808.02340 | ✓ | 0.90 | 100.0% | 0.040 | 0.039 | 0.036 | 0.984 | 100.0% | 110/265 |
| 2311.16364 | ✓ | 0.90 | 98.3% | 0.051 | 0.093 | 0.076 | 0.990 | 88.2% | 90/121 |
| 1704.02297 | ✓ | 0.80 | 1.7% | 0.000 | 0.000 | 0.000 | 0.352 | 100.0% | 2/58 |
| 1707.07921 | ✓ | 0.90 | 53.3% | 0.363 | 0.311 | 0.391 | 0.080 | 37.5% | 70/30 |
| 1806.00310 | ✓ | 0.85 | 100.0% | 0.185 | 0.185 | 0.170 | 0.001 | 97.8% | 90/8 |
| 2007.03694 | ✓ | 0.90 | 50.0% | 0.000 | 0.000 | 0.000 | 0.441 | 100.0% | 2/2 |
| 1911.11905 | ✓ | 0.95 | 100.0% | 0.078 | 0.069 | 0.068 | 0.988 | 91.8% | 98/256 |
| 1902.04246 | ✓ | 0.90 | 100.0% | 0.010 | 0.014 | 0.017 | 0.738 | 100.0% | 100/61 |
| 1708.02111 | — | — | EXCLUDED | — | — | — | — | — | — |
| 2006.09721 | ✓ | 0.93 | 99.3% | 0.022 | 0.027 | 0.024 | 0.862 | 100.0% | 98/148 |
| 1907.11485 | ✓ | 0.97 | 100.0% | 0.006 | 0.006 | 0.008 | 0.991 | 100.0% | 78/111 |
| 2112.12116 | ✓ | 0.85 | 98.8% | 0.013 | 0.014 | 0.012 | 0.991 | 100.0% | 49/81 |
| 2006.12431 | ✓ | 0.92 | 100.0% | 0.005 | 0.008 | 0.007 | 0.992 | 100.0% | 41/90 |
| 2207.11330 | ✓ | 0.90 | 99.2% | 0.014 | 0.023 | 0.013 | 0.990 | 100.0% | 71/118 |
| 2412.08699 | — | — | EXCLUDED | — | — | — | — | — | — |
| 1512.06746 | — | — | EXCLUDED | — | — | — | — | — | — |
| 1606.07494 | — | — | EXCLUDED | — | — | — | — | — | — |
| 1906.00967 | — | — | EXCLUDED | — | — | — | — | — | — |
| 2108.05368 | — | — | EXCLUDED | — | — | — | — | — | — |
| 1705.00676 | — | — | EXCLUDED | — | — | — | — | — | — |
| 1509.00026 | — | — | EXCLUDED | — | — | — | — | — | — |
| 2402.00741 | ✓ | 0.50 | gt_unusable | — | — | — | — | — | — |
| 1708.07521 | — | — | EXCLUDED | — | — | — | — | — | — |
| 1606.03145 | — | — | EXCLUDED | — | — | — | — | — | — |
| 2401.17253 | — | — | EXCLUDED | — | — | — | — | — | — |
| 1412.0789 | — | — | EXCLUDED | — | — | — | — | — | — |
| 2206.11598 | — | — | EXCLUDED | — | — | — | — | — | — |
| 1902.04644 | — | — | EXCLUDED | — | — | — | — | — | — |
| 2306.08039 | ✓ | 0.75 | 98.9% | 0.011 | 0.010 | 0.018 | 0.989 | 99.7% | 96/1158 |
| 2102.01448 | ✓ | 0.55 | 98.6% | 0.042 | 0.045 | 0.063 | 0.958 | 100.0% | 90/70 |
| 2209.03289 | ✓ | 0.75 | 98.2% | 0.030 | 0.032 | 0.034 | 0.990 | 100.0% | 90/110 |
| 2209.13588 | ✓ | 0.80 | 99.4% | 0.015 | 0.006 | 0.011 | 0.994 | 100.0% | 100/350 |
| 1906.11844 | ✗ (AxionProton) | 0.85 | no_comparable_gt | — | — | — | — | — | — |
| hep-ph/0611223 | ✓ | 0.85 | 96.9% | 0.020 | 0.020 | 0.019 | 0.127 | 100.0% | 16/32 |
| 1810.12257 | ✓ | 0.95 | 100.0% | 0.094 | 0.081 | 0.091 | 0.998 | 97.8% | 100/3214 |
| 2102.06722 | ✓ | 0.90 | 98.2% | 0.010 | 0.006 | 0.013 | 0.990 | 100.0% | 100/391 |
| 2404.12517 | ✓ | 0.90 | 97.9% | 0.304 | 0.228 | 0.205 | 0.991 | 48.6% | 75/284 |
| 0910.5914 | ✓ | 0.90 | 100.0% | 0.205 | 0.205 | 0.209 | 0.090 | 100.0% | 54/27 |
| 1804.05750 | ✓ | 0.92 | 97.9% | 0.071 | 0.074 | 0.074 | 0.927 | 100.0% | 100/145 |
| 1910.08638 | ✓ | 0.90 | 100.0% | 0.020 | 0.019 | 0.021 | 0.302 | 100.0% | 99/82 |
| 2504.07279 | ✓ | 0.85 | 98.7% | 0.280 | 0.280 | 0.306 | 0.988 | 61.0% | 68/234 |
| 1911.05772 | ✓ | 0.85 | 95.5% | 0.080 | 0.080 | 0.446 | 0.999 | 71.4% | 70/22 |
| 1901.00920 | ✓ | 0.90 | 97.4% | 0.018 | 0.013 | 0.105 | 0.999 | 93.9% | 74/117 |
| 1004.1313 | ✓ | 0.90 | 99.1% | 0.010 | 0.005 | 0.007 | 0.088 | 100.0% | 50/228 |
| 2008.05355 | ✓ | 0.93 | 98.0% | 0.018 | 0.020 | 0.016 | 0.971 | 100.0% | 73/49 |
| 2302.10206 | ✓ | 0.75 | 100.0% | 0.822 | 0.918 | 0.748 | 0.716 | 0.0% | 38/8 |
| 2101.11290 | ✓ | 0.90 | 50.0% | 0.010 | 0.056 | 0.064 | 0.010 | 100.0% | 89/2 |
| 2002.08370 | ✓ | 0.75 | 63.9% | 0.804 | 1.009 | 0.936 | 0.490 | 26.1% | 34/36 |
| 2211.12699 | ✓ | 0.97 | 98.7% | 0.276 | 0.341 | 0.273 | 0.965 | 55.4% | 654/75 |
| 2108.03316 | ✓ | 0.92 | 99.7% | 0.100 | 0.066 | 0.084 | 0.999 | 99.7% | 70/321 |
| 1709.00009 | ✓ | 0.85 | 100.0% | 0.012 | 0.015 | 0.620 | 0.940 | 100.0% | 95/37 |
| 2007.13071 | ✓ | 0.97 | 98.1% | 0.015 | 0.013 | 0.017 | 0.985 | 100.0% | 434/318 |
| 2009.09059 | ✓ | 0.80 | 97.4% | 0.010 | 0.147 | 0.026 | 0.369 | 100.0% | 51/114 |
| 2112.03439 | — | — | EXCLUDED | — | — | — | — | — | — |
| 2001.05102 | ✓ | 0.92 | 96.1% | 0.048 | 0.049 | 0.048 | 0.989 | 100.0% | 90/77 |
| 2008.10141 | ✓ | 0.90 | 98.6% | 0.018 | 0.018 | 0.018 | 0.987 | 100.0% | 90/220 |
| 2012.10764 | ✓ | 0.85 | 98.4% | 0.015 | 0.015 | 0.019 | 0.998 | 100.0% | 88/125 |
| 2206.08845 | ✓ | 0.90 | 98.2% | 0.177 | 0.178 | 0.178 | 0.983 | 99.6% | 120/2959 |
| 2207.13597 | ✓ | 0.90 | 95.9% | 0.013 | 0.012 | 0.012 | 0.991 | 100.0% | 90/49 |
| 2210.10961 | ✓ | 0.90 | 97.6% | 0.003 | 0.002 | 0.007 | 0.992 | 100.0% | 109/251 |
| 2312.11003 | ✓ | 0.90 | 100.0% | 0.009 | 0.009 | 0.015 | 0.990 | 100.0% | 110/181 |
| 2403.13390 | ✓ | 0.90 | 97.1% | 0.008 | 0.006 | 0.013 | 0.992 | 100.0% | 99/70 |
| 2402.12892 | ✓ | 0.85 | 99.4% | 0.023 | 0.018 | 0.053 | 0.993 | 95.8% | 98/362 |
| 2211.02902 | ✓ | 0.85 | 100.0% | 0.031 | 0.027 | 0.038 | 0.998 | 99.4% | 100/169 |
| 1705.02290 | ✓ | 0.95 | 46.6% | 0.066 | 0.066 | 0.070 | 0.100 | 100.0% | 78/436 |
| hep-ex/0702006 | — | — | EXCLUDED | — | — | — | — | — | — |
| 1704.05189 | ✓ | 0.85 | 96.7% | 0.014 | 0.010 | 0.273 | 0.979 | 98.3% | 88/61 |
| 2411.13701 | ✓ | 0.85 | 96.5% | 0.005 | 0.005 | 0.011 | 0.982 | 99.4% | 70/170 |
| 2109.03261 | ✓ | 0.92 | 89.7% | 0.014 | 0.007 | 0.076 | 0.426 | 100.0% | 18/29 |
| 1304.0989 | ✓ | 0.95 | 65.5% | 0.008 | 0.006 | 0.008 | 0.092 | 100.0% | 34/29 |
| 1703.07354 | ✓ | 0.90 | 65.9% | 0.097 | 0.060 | 0.176 | 0.234 | 69.0% | 80/44 |
| 1907.05475 | ✓ | 0.92 | 64.7% | 0.095 | 0.242 | 0.088 | 0.494 | 72.7% | 45/17 |
| 2104.12772 | ✓ | 0.90 | 98.4% | 0.013 | 0.009 | 0.009 | 0.495 | 100.0% | 51/64 |
| 2407.10618 | ✓ | 0.90 | 100.0% | 0.197 | 0.213 | 0.174 | 0.999 | 70.5% | 152/2612 |
| 2303.03594 | ✓ | 0.90 | 100.0% | 0.097 | 0.083 | 0.114 | 0.993 | 94.4% | 78/89 |
| 2311.05476 | ✓ | 0.85 | 98.3% | 0.005 | 0.005 | 0.006 | 0.990 | 100.0% | 97/121 |
| 2201.09890 | ✓ | 0.88 | 98.5% | 0.009 | 0.007 | 1.418 | 0.532 | 100.0% | 30/199 |
| 1110.2895 | ✓ | 0.60 | 100.0% | 0.440 | 0.204 | 2.014 | 0.115 | 43.8% | 59/16 |
| 2412.02232 | ✓ | 0.80 | 89.5% | 0.090 | 0.083 | 0.129 | 0.898 | 83.8% | 84/124 |
| 2504.07559 | ✓ | 0.92 | 96.5% | 0.023 | 0.018 | 0.031 | 0.994 | 96.9% | 87/198 |
| 2404.17333 | ✓ | 0.85 | 96.0% | 0.009 | 0.002 | 0.028 | 0.191 | 95.8% | 43/25 |
| 2405.08059 | ✓ | 0.90 | 95.0% | 0.020 | 0.015 | 0.021 | 0.992 | 100.0% | 79/40 |
| 2211.03414 | ✓ | 0.90 | 99.1% | 0.006 | 0.006 | 0.008 | 0.988 | 100.0% | 71/109 |
| 1603.06978 | ✓ | 0.90 | 99.3% | 0.001 | 0.001 | 0.187 | 0.997 | 100.0% | 80/287 |
| 2305.10327 | ✓ | 0.80 | 98.0% | 0.007 | 0.009 | 0.334 | 0.979 | 100.0% | 38/49 |
| 2305.01002 | ✓ | 0.90 | 97.4% | 0.004 | 0.004 | 0.482 | 0.998 | 100.0% | 14/38 |
| 2208.13794 | ✓ | 0.85 | 100.0% | 0.033 | 0.033 | 0.055 | 0.374 | 100.0% | 41/89 |
| 2501.17119 | ✓ | 0.90 | 97.2% | 0.013 | 0.011 | 0.012 | 0.986 | 100.0% | 100/799 |
| 1406.6053 | ✓ | 0.90 | 7.4% | 0.003 | 0.017 | 0.004 | 0.744 | 100.0% | 2/27 |
| 2110.14406 | ✓ | 0.90 | 100.0% | 0.011 | ∞ | — | — | 100.0% | 84/1 |
| 2203.04332 | ✓ | 0.92 | 99.3% | 0.006 | 0.005 | 0.005 | 0.337 | 100.0% | 53/148 |
| 1610.02580 | ✓ | 0.92 | 54.5% | 0.052 | 0.054 | 0.055 | 0.515 | 100.0% | 152/121 |
| 2008.01853 | ✓ | 0.90 | 46.8% | 0.146 | 0.145 | 0.747 | 0.191 | 94.2% | 105/111 |
| 2409.08998 | ✓ | 0.85 | 96.9% | 0.044 | 0.048 | 1.117 | 0.986 | 98.1% | 100/324 |
| 1311.3148 | ✓ | 0.88 | 100.0% | 0.008 | 0.005 | 0.029 | 0.717 | 100.0% | 42/22 |
| 2301.06560 | ✓ | 0.90 | 68.0% | 0.000 | 0.000 | 0.000 | 0.813 | 100.0% | 60/97 |
| 2412.02543 | ✓ | 0.93 | 99.0% | 0.040 | 0.037 | 0.037 | 0.993 | 100.0% | 100/99 |
| 2209.06299 | — | — | EXCLUDED | — | — | — | — | — | — |
| 2310.15395 | ✓ | 0.90 | 99.6% | 0.082 | 0.049 | 0.079 | 0.997 | 98.9% | 100/262 |
| 2503.11753 | ✓ | 0.85 | 99.9% | 0.041 | 0.012 | 0.070 | 1.000 | 96.6% | 411/1844 |
| 1509.00476 | ✓ | 0.60 | 81.0% | 0.791 | 0.686 | 0.909 | 0.838 | 0.0% | 23/21 |
| 2307.01365 | ✓ | 0.92 | 100.0% | 0.249 | 0.253 | 0.270 | 0.909 | 64.9% | 194/94 |
| 2111.08025 | ✓ | 0.90 | 98.9% | 0.010 | 0.011 | 0.011 | 0.993 | 100.0% | 69/93 |
| 2412.03660 | ✓ | 0.93 | 100.0% | 0.001 | 0.002 | 0.002 | 0.996 | 100.0% | 20/115 |
| 2409.11777 | ✓ | 0.90 | 97.7% | 0.047 | 0.046 | 0.046 | 0.999 | 100.0% | 80/86 |
| 2401.07798 | ✓ | 0.85 | 94.7% | 0.007 | 0.007 | 0.153 | 0.781 | 100.0% | 53/38 |
| 1811.10997 | ✓ | 0.92 | 99.3% | 0.011 | 0.007 | 0.016 | 0.997 | 100.0% | 61/144 |
| 2203.04319 | ✓ | 0.92 | 100.0% | 0.004 | 0.004 | 0.004 | 0.994 | 100.0% | 48/132 |
| 2307.03878 | ✓ | 0.90 | 97.4% | 0.006 | 0.006 | 0.154 | 0.999 | 100.0% | 58/76 |
| 2110.13636 | ✓ | 0.90 | 96.8% | 0.002 | 0.002 | 0.029 | 0.995 | 100.0% | 61/62 |
| 2008.09464 | ✓ | 0.90 | 96.0% | 0.006 | 0.006 | 0.032 | 0.998 | 100.0% | 80/50 |
| 2202.08274 | ✓ | 0.88 | 99.2% | 0.046 | 0.018 | 0.053 | 0.991 | 94.1% | 100/257 |
| 2203.12152 | ✓ | 0.92 | 99.2% | 0.025 | 0.019 | 0.070 | 0.984 | 97.5% | 108/123 |
| 2310.00904 | ✓ | 0.95 | 100.0% | 0.025 | 0.022 | 0.023 | 0.979 | 100.0% | 95/53 |
| 2407.18586 | ✓ | 0.92 | 97.4% | 0.012 | 0.009 | 0.013 | 0.997 | 100.0% | 105/265 |
| 1706.00209 | ✓ | 0.75 | 100.0% | 0.000 | ∞ | — | — | 100.0% | 29/1 |
| 1506.08082 | ✓ | 0.95 | 91.7% | 0.010 | 0.012 | 0.015 | 0.036 | 90.9% | 86/12 |
| 2303.08410 | ✓ | 0.85 | 100.0% | 0.102 | 0.064 | 0.087 | 0.999 | 95.3% | 82/192 |
| 2403.02096 | ✓ | 0.90 | 100.0% | 0.130 | 0.051 | 0.100 | 0.998 | 68.3% | 66/838 |
| 2412.02229 | ✓ | 0.93 | 99.2% | 0.011 | 0.013 | 0.013 | 0.993 | 100.0% | 51/120 |
| 1510.08052 | ✓ | 0.70 | 96.6% | 0.007 | 0.016 | 0.360 | 0.065 | 85.9% | 100/88 |
| 2409.10514 | ✓ | 0.93 | 100.0% | 0.002 | 0.001 | 0.002 | 0.949 | 100.0% | 70/156 |
| 1903.03586 | ✓ | 0.90 | 85.7% | 0.005 | 0.035 | 0.029 | 0.959 | 100.0% | 32/7 |
| 1903.06547 | ✓ | 0.95 | 100.0% | 0.000 | ∞ | — | — | 100.0% | 2/1 |
| 2012.09498 | ✓ | 0.90 | 100.0% | 0.048 | ∞ | — | — | 100.0% | 1041/1 |
| 2304.07505 | ✓ | 0.92 | 75.0% | 0.262 | 0.211 | 0.228 | 0.716 | 58.3% | 32/32 |
| 2402.19063 | ✓ | 0.92 | 100.0% | 0.114 | 0.109 | 0.145 | 0.998 | 75.2% | 149/149 |
| 2104.13798 | ✓ | 0.90 | 100.0% | 0.087 | 0.353 | 0.373 | 0.988 | 100.0% | 94/2 |
| 2403.07790 | ✓ | 0.95 | 99.8% | 0.020 | 0.018 | 0.020 | 0.996 | 100.0% | 95/420 |
| 2409.01805 | ✓ | 0.90 | 94.5% | 0.129 | 0.130 | 0.137 | 0.957 | 100.0% | 53/91 |
| 2003.03348 | ✓ | 0.92 | 99.9% | 0.003 | 0.002 | 0.017 | 0.999 | 98.9% | 100/857 |
| 2303.11395 | ✓ | 0.85 | 94.6% | 0.003 | 0.003 | 0.138 | 0.800 | 100.0% | 44/37 |
| 2304.01060 | ✓ | 0.90 | 94.1% | 0.024 | 0.023 | 0.569 | 0.979 | 100.0% | 71/51 |
| 2212.09764 | ✓ | 0.90 | 97.0% | 0.001 | 0.002 | 0.002 | 0.136 | 100.0% | 50/33 |
| 2405.19393 | ✓ | 0.90 | 100.0% | 0.099 | 0.102 | 0.108 | 0.986 | 100.0% | 48/55 |
| 2306.11575 | ✓ | 0.85 | 95.7% | 0.010 | 0.011 | 0.018 | 0.914 | 100.0% | 21/415 |
| 2006.06722 | ✓ | 0.92 | 98.7% | 0.003 | 0.001 | 0.003 | 0.110 | 100.0% | 11/76 |
| 2203.16567 | ✓ | 0.92 | 98.3% | 0.059 | 0.031 | 0.041 | 0.994 | 100.0% | 100/115 |
| 2008.13662 | ✓ | 0.92 | 98.4% | 0.110 | 0.069 | 0.095 | 0.986 | 82.5% | 51/64 |
| 2205.05700 | ✓ | 0.80 | 99.2% | 0.014 | 0.009 | 0.015 | 0.995 | 100.0% | 80/122 |
| 2303.06968 | ✓ | 0.85 | 99.4% | 0.187 | 0.123 | 0.234 | 0.999 | 59.0% | 75/174 |
| 1501.01639 | ✓ | 0.85 | 50.0% | 0.003 | 0.003 | 0.003 | 0.612 | 100.0% | 40/2 |
| 2307.11216 | ✓ | 0.92 | 100.0% | 0.128 | 0.132 | 0.125 | 0.897 | 100.0% | 85/60 |
| 2112.09620 | ✓ | 0.92 | 98.8% | 0.007 | 0.006 | 0.007 | 0.998 | 100.0% | 80/83 |
| 2408.16045 | ✓ | 0.92 | 100.0% | 0.010 | 0.009 | 0.011 | 0.999 | 100.0% | 80/124 |
| 2205.05574 | ✓ | 0.90 | 98.8% | 0.009 | 0.003 | 0.007 | 0.984 | 100.0% | 102/508 |
| 2307.07403 | ✓ | 0.85 | 96.8% | 0.178 | 0.094 | 0.158 | 0.995 | 69.1% | 97/555 |
| astro-ph/0611502 | ✓ | 0.90 | 97.8% | 0.212 | 0.217 | 0.201 | 0.999 | 97.8% | 88/91 |
| 2301.06778 | ✓ | 0.90 | 95.3% | 0.029 | 0.030 | 0.030 | 0.990 | 100.0% | 80/86 |
| 1912.07751 | — | — | EXCLUDED | — | — | — | — | — | — |
| 2402.07976 | ✓ | 0.50 | 99.0% | 0.467 | 0.454 | 0.409 | 0.990 | 8.5% | 100/10796 |
| 2102.00379 | ✓ | 0.85 | 100.0% | 0.045 | 0.044 | 1.262 | 0.999 | 100.0% | 41/26 |
| 2102.02207 | — | — | EXCLUDED | — | — | — | — | — | — |
| 2503.04726 | ✓ | 0.80 | 97.0% | 0.143 | 0.146 | 0.164 | 0.978 | 90.0% | 97/16611 |
| 2008.03305 | ✓ | 0.93 | 99.1% | 0.003 | 0.002 | 0.005 | 0.190 | 100.0% | 19/115 |
| 2412.09595 | — | — | EXCLUDED | — | — | — | — | — | — |
| 2008.02209 | ✓ | 0.85 | 97.1% | 0.048 | 0.047 | 0.049 | 0.978 | 100.0% | 78/69 |
| 2407.16628 | ✓ | 0.70 | 100.0% | 2.053 | 2.058 | 2.037 | 0.989 | 0.0% | 55/101 |
| 0801.1527 | ✓ | 0.85 | 98.9% | 0.106 | 0.103 | 0.127 | 0.985 | 94.2% | 68/175 |
| 2002.05165 | ✓ | 0.90 | 83.2% | 0.043 | 0.043 | 0.045 | 0.482 | 99.6% | 67/671 |
| 2409.12940 | ✓ | 0.90 | 99.4% | 0.018 | 0.017 | 0.017 | 1.000 | 100.0% | 51/174 |
| 2409.12115 | ✓ | 0.90 | 98.8% | 0.033 | 0.034 | 0.127 | 0.998 | 100.0% | 60/80 |
| 1201.5902 | ✓ | 0.90 | 99.1% | 0.069 | 0.060 | 0.098 | 0.992 | 73.9% | 98/228 |
| 1911.05086 | ✓ | 0.95 | 100.0% | 0.000 | 0.000 | 0.017 | 1.000 | 97.3% | 100/401 |
| 2003.13698 | ✓ | 0.90 | 98.7% | 0.000 | 0.000 | 0.011 | 0.990 | 99.5% | 115/393 |
| 0810.5501 | ✓ | 0.92 | 96.4% | 0.003 | 0.005 | 0.004 | 0.996 | 100.0% | 46/112 |
| 2002.01796 | ✓ | 0.85 | no_comparable_gt | — | — | — | — | — | — |
| 1907.12628 | ✓ | 0.92 | 98.6% | 0.031 | 0.031 | 0.037 | 0.989 | 100.0% | 97/73 |
| 1906.08814 | ✓ | 0.92 | 100.0% | 0.000 | 0.160 | 0.166 | 0.668 | 100.0% | 62/2 |
| 2101.02805 | — | — | EXCLUDED | — | — | — | — | — | — |
| 2405.20444 | ✓ | 0.85 | 100.0% | 0.062 | 0.028 | 0.052 | 0.989 | 98.8% | 105/493 |
| 2301.11512 | ✓ | 0.93 | 93.8% | 0.007 | 0.003 | 0.005 | 0.999 | 100.0% | 62/16 |
| 2207.05767 | — | — | EXCLUDED | — | — | — | — | — | — |
| 2003.13144 | ✓ | 0.97 | 86.4% | 0.086 | 0.058 | 0.117 | 0.802 | 84.2% | 15/22 |
| 2310.13891 | ✓ | 0.90 | 98.9% | 0.014 | 0.015 | 0.015 | 0.998 | 100.0% | 82/87 |
| 2304.12907 | ✓ | 0.85 | 99.2% | 0.011 | 0.011 | 0.012 | 0.249 | 100.0% | 57/126 |
| 2211.00022 | ✓ | 0.75 | 56.6% | 0.018 | 0.014 | 0.023 | 0.544 | 100.0% | 56/143 |
| 2406.19445 | ✓ | 0.93 | 49.5% | 0.000 | 0.000 | 0.000 | 0.235 | 100.0% | 50/99 |
| 2402.17140 | — | — | EXCLUDED | — | — | — | — | — | — |
| 2110.01582 | ✓ | 0.90 | 100.0% | 0.199 | 0.185 | 0.150 | 0.880 | 80.8% | 64/26 |
| 2301.03622 | ✓ | 0.90 | 98.3% | 0.243 | 0.274 | 0.264 | 0.996 | 61.7% | 100/401 |
| 1007.3766 | ✓ | 0.95 | 30.4% | 0.087 | 0.113 | 0.104 | 0.228 | 80.6% | 22/102 |
| 1410.5244 | ✓ | 0.85 | 90.5% | 0.085 | 0.026 | 0.035 | 0.974 | 100.0% | 20/21 |
| 2410.02858 | ✓ | 0.90 | 66.7% | 0.002 | 0.001 | 0.002 | 0.790 | 100.0% | 4/6 |
| 2110.10497 | ✓ | 0.60 | 100.0% | 0.453 | 0.259 | 0.319 | 0.992 | 36.1% | 95/72 |
| 2012.05427 | ✓ | 0.85 | 61.5% | 1.115 | 0.693 | 0.943 | 0.834 | 0.0% | 100/26 |
| 2204.03818 | ✓ | 0.90 | 99.9% | 0.007 | 0.003 | 0.023 | 1.000 | 99.5% | 100/3689 |
| 2405.12285 | ✓ | 0.92 | 98.9% | 0.060 | 0.064 | 0.107 | 0.995 | 95.6% | 100/91 |
| 2406.02546 | ✓ | 0.90 | 86.4% | 0.082 | 0.068 | 0.139 | 0.964 | 84.2% | 60/22 |
| 2209.03419 | ✓ | 0.92 | 98.2% | 0.083 | 0.049 | 0.064 | 0.992 | 99.7% | 80/325 |
| 2212.01971 | ✓ | 0.85 | 98.5% | 0.562 | 0.560 | 0.593 | 0.983 | 1.6% | 147/131 |
| 2305.09711 | ✓ | 0.90 | 99.7% | 0.082 | 0.077 | 0.099 | 0.993 | 99.0% | 112/57500 |
| 1502.04490 | ✓ | 0.93 | 73.2% | 0.156 | 0.162 | 0.155 | 0.671 | 87.8% | 60/123 |
| 1905.05579 | ✓ | 0.92 | 99.0% | 0.107 | 0.102 | 0.146 | 0.976 | 89.3% | 100/104 |
| 1301.6557 | ✓ | 0.90 | 95.9% | 0.115 | 0.070 | 0.105 | 0.839 | 99.2% | 92/123 |
| 2208.03183 | — | — | EXCLUDED | — | — | — | — | — | — |
| 2008.12231 | ✓ | 0.75 | 100.0% | 0.000 | ∞ | — | — | 100.0% | 35/1 |
| 2308.08337 | ✓ | 0.85 | 100.0% | 0.000 | ∞ | — | — | 100.0% | 2/1 |
| 1008.3536 | ✓ | 0.85 | 100.0% | 0.116 | 0.095 | 0.251 | 0.666 | 75.0% | 69/100 |
| 2106.00022 | ✓ | 0.85 | 93.1% | 0.070 | 0.072 | 0.071 | 0.991 | 100.0% | 100/58 |
| 1804.10777 | ✓ | 0.92 | 66.7% | 0.064 | 0.027 | 0.057 | 0.996 | 100.0% | 30/3 |
| 1504.00118 | ✓ | 0.92 | 66.7% | 0.100 | 0.076 | 0.077 | 0.751 | 100.0% | 13/12 |
| 2006.02828 | ✓ | 0.95 | 83.3% | 0.051 | 0.060 | 0.072 | 0.992 | 100.0% | 100/6 |
| 1907.12449 | ✓ | 0.80 | 99.3% | 0.010 | 0.010 | 0.029 | 0.761 | 97.8% | 99/555 |
| 1903.05101 | ✓ | 0.90 | 96.2% | 0.030 | 0.032 | 0.030 | 0.943 | 100.0% | 40/53 |
| 2006.13929 | ✓ | 0.92 | 98.0% | 0.021 | 0.007 | 0.023 | 0.747 | 95.8% | 66/98 |
| 1807.04512 | ✓ | 0.85 | 19.4% | 0.485 | 0.566 | 0.610 | 0.544 | 14.3% | 50/36 |
| hep-ph/0307284 | ✓ | 0.75 | no_comparable_gt | — | — | — | — | — | — |
| 2103.03783 | ✓ | 0.90 | 100.0% | 0.049 | 0.049 | 0.052 | 0.992 | 100.0% | 100/69 |
| 2205.06817 | — | — | EXCLUDED | — | — | — | — | — | — |
| 2306.16219 | ✓ | 0.85 | 98.0% | 0.050 | 0.048 | 0.056 | 0.983 | 93.0% | 88/102 |
| 2303.00778 | ✓ | 0.75 | 100.0% | 0.002 | 0.002 | 0.002 | 0.176 | 100.0% | 7/2 |
| 2212.05721 | ✓ | 0.90 | 100.0% | 0.023 | 0.008 | 0.018 | 0.996 | 100.0% | 120/333 |
| 2005.14694 | — | — | EXCLUDED | — | — | — | — | — | — |
| 1503.06886 | ✓ | 0.90 | 99.1% | 0.049 | 0.022 | 0.040 | 0.980 | 99.4% | 96/1006 |
| 1902.02788 | ✓ | 0.75 | 100.0% | 0.362 | 0.192 | 0.474 | 0.568 | 46.9% | 100/130 |
| 2301.03433 | ✓ | 0.90 | 98.8% | 0.083 | 0.058 | 0.069 | 0.971 | 100.0% | 91/172 |
| 2302.04565 | ✓ | 0.85 | 98.6% | 0.927 | 0.611 | 0.712 | 0.995 | 11.6% | 92/848 |
| 1604.08514 | ✓ | 0.90 | 99.0% | 0.065 | 0.028 | 0.050 | 0.995 | 100.0% | 100/505 |
| quant-ph/0106045 | ✓ | 0.65 | no_comparable_gt | — | — | — | — | — | — |
| 2109.08822 | ✓ | 0.85 | 93.8% | 0.302 | 0.309 | 0.306 | 0.986 | 40.0% | 80/32 |
| 2105.13085 | ✓ | 0.85 | 98.7% | 0.111 | 0.153 | 0.145 | 0.992 | 97.4% | 100/236 |
| 2301.08736 | ✓ | 0.50 | 98.8% | 0.904 | 0.882 | 1.195 | 0.994 | 0.0% | 72/165 |
| 2403.02381 | ✓ | 0.90 | no_extracted_points | — | — | — | — | — | — |
| 2409.03814 | ✓ | 0.92 | 51.3% | 0.284 | 0.329 | 0.293 | 0.504 | 53.2% | 85/308 |
| 2112.07687 | ✓ | 0.85 | 100.0% | 0.023 | 0.027 | 0.029 | 0.991 | 85.0% | 99/167 |
| 2302.00685 | ✓ | 0.75 | 100.0% | 1.888 | 3.089 | 3.257 | 0.397 | 9.1% | 94/11 |
| 2011.11646 | ✓ | 0.85 | 100.0% | 0.032 | 0.034 | 0.033 | 0.996 | 98.0% | 48/49 |
| 2406.10337 | ✓ | 0.60 | 39.2% | 0.016 | 7.074 | 1.015 | 0.118 | 60.0% | 48/51 |
| 2011.08693 | — | — | EXCLUDED | — | — | — | — | — | — |
| 2012.12790 | ✓ | 0.85 | 99.5% | 0.024 | 0.008 | 0.022 | 0.997 | 99.0% | 68/209 |
| 2412.03655 | ✓ | 0.80 | 100.0% | 0.016 | 0.016 | 0.041 | 0.994 | 98.7% | 82/545 |
| 2105.13963 | ✓ | 0.85 | 95.0% | 0.004 | 0.005 | 0.364 | 0.533 | 100.0% | 72/20 |
| 2404.00616 | — | — | EXCLUDED | — | — | — | — | — | — |
| 2412.20932 | ✓ | 0.90 | 50.0% | 0.012 | 0.014 | 0.014 | 0.995 | 100.0% | 20/2 |
| 2408.07740 | ✓ | 0.75 | 100.0% | 0.002 | 0.002 | 0.014 | 0.082 | 100.0% | 38/18 |
| 2410.21590 | ✓ | 0.85 | 94.1% | 0.061 | 0.040 | 1.000 | 0.763 | 100.0% | 46/34 |
| 2205.01637 | ✓ | 0.65 | 90.0% | 0.038 | 0.040 | 0.121 | 0.250 | 100.0% | 9/10 |
| 1708.08464 | ✓ | 0.75 | 66.7% | 0.279 | 0.444 | 0.304 | 0.553 | 50.0% | 37/3 |
| 2303.09865 | ✓ | 0.90 | 100.0% | 0.005 | 0.005 | 0.007 | 0.995 | 100.0% | 100/2 |
| 2211.02661 | ✓ | 0.85 | 99.4% | 0.119 | 0.119 | 0.121 | 0.269 | 100.0% | 51/167 |
| 2301.10784 | ✓ | 0.92 | 97.2% | 0.128 | 0.133 | 0.132 | 0.985 | 100.0% | 80/107 |
| 1003.0964 | — | — | EXCLUDED | — | — | — | — | — | — |
| 2312.11608 | — | — | EXCLUDED | — | — | — | — | — | — |

## Breakdown by Extraction Source

Median residual is over papers with mass-range overlap; zero-overlap papers are listed separately.

| Source | Papers | Compared | Zero-overlap | Med. Resid. | ≤0.3 dex |
|--------|--------|----------|--------------|-------------|----------|
| table | 3 | 3 | 0 | 0.024 dex | 88.7% |
| figure_vision | 68 | 67 | 0 | 0.046 dex | 88.6% |
| text | 16 | 14 | 0 | 0.001 dex | 97.7% |

## Breakdown by Difficulty

> Difficulty is a placeholder label for the repo-sourced pool (nearly all `medium`); this table is informational only.

| Difficulty | Papers | Coupling Acc. | Med. Resid. | ≤0.3 dex |
|------------|--------|---------------|-------------|----------|
| easy | 11 | 100.0% | 0.002 dex | 98.9% |
| medium | 251 | 99.6% | 0.025 dex | 89.1% |
| hard | 29 | 100.0% | 0.025 dex | 91.0% |

## Confidence Calibration

- "Accurate" = median interpolation residual < **0.32 dex** AND interpolation coverage ≥ 50%.
- The **0.32 dex** threshold is the run-to-run LLM extraction *noise floor* (90th-pct per-paper median-residual std across repeated extractions, PR #545) — the binding floor. It is **not** the upstream digitization floor, which is only ~0.034 dex for table/text-sourced papers (PR #558). So a residual gap here is **real extractor overconfidence, not a yardstick artifact**.

### Binned accuracy (pass/fail)

| Bin | N | Mean Conf. | Actual Acc. | Gap |
|-----|---|------------|-------------|-----|
| [0.5–0.8) | 42 | 71.4% | 66.7% | +0.05 |
| [0.8–0.9) | 64 | 85.2% | 90.6% | -0.05 |
| [0.9–0.9) | 100 | 90.0% | 96.0% | -0.06 |
| [0.9–0.9) | 46 | 92.0% | 97.8% | -0.06 |
| [0.9–1.0) | 29 | 94.5% | 89.7% | +0.05 |

> **Interpretation**: Gap > 0 means the pipeline is overconfident; Gap < 0 means underconfident.

### Continuous view: residual distribution per bin

Median (and IQR) of each bin's per-paper median residual, over papers with a finite residual (zero mass-overlap papers excluded from the distribution but still counted in N). If confidence tracked accuracy, the median residual would fall as confidence rises.

| Bin | N | N finite | Median resid. (dex) | IQR (dex) |
|-----|---|----------|---------------------|-----------|
| [0.5–0.8) | 42 | 42 | 0.03 | 0.01–0.42 |
| [0.8–0.9) | 64 | 64 | 0.04 | 0.01–0.10 |
| [0.9–0.9) | 100 | 100 | 0.02 | 0.01–0.08 |
| [0.9–0.9) | 46 | 46 | 0.03 | 0.01–0.10 |
| [0.9–1.0) | 29 | 29 | 0.02 | 0.00–0.07 |

### Continuous view: empirical P(residual < τ) per bin

Fraction of papers in each bin whose median residual is below τ dex (τ = 0.32 is the noise floor used above). A well-calibrated, accurate extractor would show these probabilities rising with confidence.

| Bin | N | P(<0.10) | P(<0.32) | P(<0.50) | P(<1.00) |
|-----|---|----|----|----|----|
| [0.5–0.8) | 42 | 61.9% | 71.4% | 81.0% | 92.9% |
| [0.8–0.9) | 64 | 73.4% | 90.6% | 95.3% | 98.4% |
| [0.9–0.9) | 100 | 83.0% | 99.0% | 100.0% | 100.0% |
| [0.9–0.9) | 46 | 76.1% | 97.8% | 100.0% | 100.0% |
| [0.9–1.0) | 29 | 89.7% | 100.0% | 100.0% | 100.0% |

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
