# AutoAxionLimits Extraction Pipeline — Evaluation Report

## Summary

- **Papers evaluated**: 329
- **Papers with curve comparison**: 261

## Curve-Comparison Coverage

A curve is scored only against a ground-truth curve of the **same coupling**. Papers whose extracted coupling has no matching GT curve are not comparable and are excluded from residual statistics (this is not an extraction failure).

| Status | Papers | Meaning |
|--------|--------|---------|
| compared | 261 | scored against a same-coupling GT curve |
| no_comparable_gt | 14 | extracted coupling has no GT curve in the pool (usually a coupling misclassification) |
| convention_mismatch | 13 | same coupling but the GT curve uses a different convention/units (e.g. f_a [GeV] vs normalized, or d_e vs a large-valued variable) — excluded as a units gap, not extraction error |
| gt_unusable | 1 | GT curve has <2 usable points after boundary filtering |
| no_extracted_points | 2 | pipeline returned no data points |
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
| coupling_type | 98.3% | 291 |
| is_new_limit | 100.0% | 32 |
| is_projection | 100.0% | 32 |
| data_source | 46.9% | 32 |

> **Label provenance**: `is_new_limit`, `is_projection`, and `data_source` are scored against an **independent LLM labeler** (`evaluation/label_ground_truth.py`, model `claude-opus-4-5`) whose sole task is to classify paper properties — a distinct model and prompt from the extractor it grades, so this is a fair cross-model test, not self-agreement. These are **not human gold labels**. A human audit of 15 labeled papers found per-field labeler↔human agreement: is_new_limit 15/15, is_projection 15/15, data_source 14/15 (difficulty is derived mechanically from data_source + point count, not labeled).

### Coupling Type Misclassifications

| arXiv ID | Predicted | Expected |
|----------|-----------|----------|
| 2504.00720 | AxionCPV | ['AxionMass'] |
| 2105.13085 | DarkPhoton | ['VectorBL'] |
| 2301.08736 | DarkPhoton | ['VectorBL'] |
| 2112.07687 | DarkPhoton | ['VectorBL'] |
| 2301.10784 | ScalarNucleon | ['AxionMass'] |

### Coupling-Type Confusion Matrix (multi-type-aware)

Rows = authoritative GT type, columns = predicted type. A prediction is correct iff it is in ANY of the paper's GT types (diagonal). Off-diagonal cells are the confusable clusters. Graded 291, correct 286 (98.3%), skipped 38 (no prediction / no GT type).

| GT ⟍ Pred | AxionCPV | AxionEDM | AxionElectron | AxionMass | AxionNeutron | AxionPhoton | AxionProton | DarkPhoton | MonopoleDipole | ScalarBaryon | ScalarElectron | ScalarNucleon | ScalarPhoton | VectorBL |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| AxionEDM |  | **3** |  |  |  |  |  |  |  |  |  |  |  |  |
| AxionElectron |  |  | **16** |  |  |  |  |  |  |  |  |  |  |  |
| AxionMass | 1 |  |  | **16** |  |  |  |  |  |  |  | 1 |  |  |
| AxionNeutron |  |  |  |  | **16** |  |  |  |  |  |  |  |  |  |
| AxionPhoton |  |  |  |  |  | **140** |  |  |  |  |  |  |  |  |
| AxionProton |  |  |  |  |  |  | **2** |  |  |  |  |  |  |  |
| DarkPhoton |  |  |  |  |  |  |  | **62** |  |  |  |  |  |  |
| MonopoleDipole |  |  |  |  |  |  |  |  | **2** |  |  |  |  |  |
| ScalarBaryon |  |  |  |  |  |  |  |  |  | **1** |  |  |  |  |
| ScalarElectron |  |  |  |  |  |  |  |  |  |  | **3** |  |  |  |
| ScalarNucleon |  |  |  |  |  |  |  |  |  |  |  | **5** |  |  |
| ScalarPhoton |  |  |  |  |  |  |  |  |  |  |  |  | **14** |  |
| VectorBL |  |  |  |  |  |  |  | 3 |  |  |  |  |  | **6** |

Off-diagonal confusions (GT → predicted, richest first):

- VectorBL → DarkPhoton: 3
- AxionMass → AxionCPV: 1
- AxionMass → ScalarNucleon: 1

## Extraction Quality — Interpolation Metric (primary)

Build log-log interpolation from extracted points, evaluate at ground-truth masses.

- **Papers compared**: 261 (259 with mass-range overlap, 2 with zero overlap)

**Coupling-value accuracy** (papers with mass-range overlap):
- **Median residual across papers**: 0.183 dex (IQR 0.079–0.454)
- **Mean residual across papers** (outlier-sensitive): 0.537 dex
- **Mean fraction within 0.3 dex (factor 2; the leaderboard headline is 10%, results/leaderboard.py)**: 62.8%
- **Mean fraction within 0.5 dex (factor 3)**: 74.4%

**Mass-range coverage** (a separate failure mode):
- **Mean interpolation coverage**: 86.2%
- **Zero-overlap papers**: 2/261 (0.8%) — extracted masses miss the GT range entirely (usually 1–2 extracted points or the wrong mass window)

**Reverse pass** (GT interpolated onto the *extracted* masses):
- Mirrors the forward pass. A large forward-vs-reverse gap, or a reverse coverage well below the forward coverage, flags an extraction whose mass *extent* or shape disagrees with the GT (e.g. running past the GT range).
- **Median reverse residual across papers**: 0.181 dex (forward: 0.183 dex)
- **Mean reverse interpolation coverage**: 77.2% (forward: 86.2%)

## Residual by Coupling Type — Micro vs Macro Average (issue #543)

The compared-paper pool is dominated by one coupling type (AxionPhoton), so the per-paper **micro-average** headline is largely that one type's number. The **macro-average** weights each coupling type equally (mean of the per-type medians), exposing how the pipeline does across the *range* of couplings rather than on the most common one.

- **Micro-average median residual** (per paper, 259 papers): 0.183 dex
- **Macro-average median residual** (equal weight per type, 12 types): 0.915 dex
- **Macro − micro gap**: +0.732 dex (macro is worse; a positive gap means the rarer couplings are harder than the AxionPhoton-dominated micro-average implies)

Per-type medians carry a bootstrap 95% CI (1000 resamples). Rows with **N < 5** are flagged small-sample — their median and CI are unstable and should not be read as a reliable per-type score.

| Coupling Type | N | Median Resid. (dex) | 95% CI (dex) | Flag |
|---------------|---|---------------------|--------------|------|
| AxionPhoton | 135 | 0.157 | [0.124, 0.190] |  |
| DarkPhoton | 59 | 0.167 | [0.113, 0.223] |  |
| AxionNeutron | 15 | 0.413 | [0.067, 1.678] |  |
| AxionElectron | 14 | 0.176 | [0.076, 0.913] |  |
| ScalarPhoton | 11 | 0.452 | [0.202, 0.829] |  |
| AxionMass | 10 | 0.460 | [0.151, 4.253] |  |
| VectorBL | 5 | 0.380 | [0.202, 1.647] |  |
| AxionEDM | 3 | 0.042 | [0.031, 1.662] | ⚠ small-sample (N<5) |
| ScalarElectron | 3 | 0.195 | [0.132, 0.531] | ⚠ small-sample (N<5) |
| ScalarNucleon | 2 | 4.719 | [0.011, 9.428] | ⚠ small-sample (N<5) |
| MonopoleDipole | 1 | 0.400 | [0.400, 0.400] | ⚠ small-sample (N<5) |
| AxionProton | 1 | 3.415 | [3.415, 3.415] | ⚠ small-sample (N<5) |

## Shape & Mass-Range Agreement — Symmetric Metrics (complementary)

These are symmetric, 2-D complements to the (asymmetric, vertical-only) interpolation residual. **Area-between-curves** integrates |Δ log10 coupling| over the overlapping log-mass range and normalises by the overlap width (a single shape+offset number, in dex; a pure mass shift inflates it even when the vertical residual looks fine). **Mass-range Jaccard** is the Jaccard index of the extracted vs GT log-mass intervals (1.0 = identical extent; small = over-/under-claimed mass range), reported separately from interpolation coverage.

- **Papers scored**: 252 (247 with mass overlap for area)
- **Median area-between-curves**: 0.231 dex (mean 0.607 dex)
- **Median mass-range Jaccard**: 0.879 (mean 0.721)

## Per-Paper Results

| arXiv ID | Coupling | Conf. | Interp. Cov. | Med. Resid. | Rev. Resid. | Area (dex) | Mass Jaccard | ≤0.3 dex | Points |
|----------|----------|-------|--------------|-------------|-------------|------------|--------------|----------|--------|
| 2208.07293 | ✓ | 0.75 | 100.0% | 0.042 | 0.042 | 0.040 | 0.045 | 100.0% | 30/2 |
| 2212.04413 | ✓ | 0.40 | 71.1% | 0.128 | 0.137 | 0.132 | 0.733 | 100.0% | 4/97 |
| 2410.19902 | ✓ | 0.72 | 100.0% | 0.342 | 0.342 | 0.397 | 0.636 | 17.2% | 29/2 |
| 1907.03767 | ✓ | 0.60 | 89.0% | 0.413 | 0.415 | 0.533 | 0.773 | 35.8% | 31/182 |
| 2209.06216 | ✓ | 0.45 | 100.0% | 0.596 | 0.582 | 0.636 | 0.844 | 36.2% | 33/2771 |
| 2005.14184 | ✓ | 0.60 | 99.7% | 0.275 | 0.212 | 0.222 | 0.998 | 56.1% | 8/891 |
| 2504.00720 | ✗ (AxionCPV) | 0.50 | no_comparable_gt | — | — | — | — | — | — |
| 2408.02668 | ✓ | 0.55 | 98.1% | 0.877 | 0.852 | 0.821 | 0.991 | 13.3% | 12/413 |
| 1905.13650 | ✓ | 0.60 | 100.0% | 1.213 | 1.238 | 1.169 | 0.682 | 0.8% | 26/243 |
| 2110.03679 | ✓ | 0.85 | 97.7% | 0.036 | 0.036 | 0.059 | 0.265 | 100.0% | 26/129 |
| 2303.07370 | ✓ | 0.45 | 57.0% | 0.163 | 0.161 | 0.170 | 0.556 | 95.1% | 7/107 |
| 2309.16600 | ✓ | 0.78 | 97.3% | 0.067 | 0.061 | 0.080 | 0.989 | 98.4% | 36/188 |
| 2504.16044 | ✓ | 0.85 | gt_unusable | — | — | — | — | — | — |
| 2312.06746 | ✓ | 0.72 | 0.6% | 0.030 | 0.048 | 0.042 | 0.011 | 100.0% | 2/171 |
| 1310.8098 | ✓ | 0.72 | 100.0% | 1.205 | 0.831 | 1.167 | 0.271 | 14.0% | 32/43 |
| 2408.02368 | ✓ | 0.85 | 100.0% | 0.176 | 0.007 | 0.175 | 0.999 | 87.8% | 3/647 |
| 2011.07100 | ✓ | 0.60 | 70.9% | 0.400 | 0.464 | 0.592 | 0.287 | 33.9% | 24/79 |
| 2302.09096 | ✓ | 0.50 | convention_mismatch | — | — | — | — | — | — |
| 1410.7267 | ✓ | 0.35 | 82.4% | 9.428 | 9.384 | 9.426 | 0.840 | 0.0% | 5/74 |
| 1712.00483 | ✓ | 0.55 | 63.6% | 0.829 | 0.755 | 1.071 | 0.430 | 19.0% | 2/33 |
| 1607.07327 | ✓ | 0.55 | 100.0% | 0.195 | ∞ | 0.237 | 0.965 | 65.7% | 2/35 |
| 1611.05852 | ✓ | 0.85 | no_comparable_gt | — | — | — | — | — | — |
| 2111.06883 | ✓ | 0.30 | no_comparable_gt | — | — | — | — | — | — |
| 0802.2350 | ✓ | 0.30 | 70.8% | 0.011 | 0.027 | 0.014 | 0.680 | 100.0% | 6/24 |
| 2009.04517 | ✓ | 0.55 | 96.6% | 7.537 | 7.825 | 8.613 | 0.223 | 0.0% | 28/29 |
| 2010.08107 | ✓ | 0.55 | 99.5% | 1.887 | 1.504 | 2.219 | 0.988 | 0.0% | 2/208 |
| 2201.02042 | — | — | EXCLUDED | — | — | — | — | — | — |
| 2403.03004 | ✓ | 0.80 | 100.0% | 0.727 | 0.720 | 0.739 | 0.980 | 6.8% | 31/414 |
| 2205.03617 | ✓ | 0.42 | no_comparable_gt | — | — | — | — | — | — |
| 2310.06017 | ✓ | 0.80 | 100.0% | 1.647 | 1.016 | 1.708 | 0.860 | 8.8% | 32/113 |
| 2102.08764 | ✓ | 0.92 | 100.0% | 0.000 | 0.000 | 0.000 | 0.892 | 100.0% | 2/2 |
| 2308.14656 | ✓ | 0.60 | 100.0% | 0.214 | ∞ | 0.184 | 0.993 | 84.0% | 2/75 |
| 2207.03102 | ✓ | 0.90 | 100.0% | 0.000 | 0.000 | 0.000 | 0.240 | 100.0% | 2/2 |
| 1505.07455 | — | — | EXCLUDED | — | — | — | — | — | — |
| 2105.04603 | ✓ | 0.50 | 98.3% | 3.553 | 3.565 | 3.447 | 0.984 | 0.0% | 5/707 |
| 2303.11792 | ✓ | 0.90 | 90.0% | 0.141 | 0.128 | 0.144 | 0.748 | 100.0% | 2/20 |
| 1607.06083 | ✓ | 0.40 | 37.2% | 0.414 | 0.442 | 0.409 | 0.365 | 16.7% | 5/113 |
| 2108.04746 | ✓ | 0.40 | 97.2% | 0.452 | 0.399 | 0.545 | 0.986 | 38.5% | 31/283 |
| 2208.12670 | ✓ | 0.80 | 100.0% | 0.011 | ∞ | — | — | 100.0% | 25/1 |
| 1806.05120 | ✓ | 0.75 | 97.9% | 0.192 | 0.211 | 0.215 | 0.973 | 81.5% | 2/94 |
| 2101.01241 | ✓ | 0.82 | 100.0% | 0.031 | ∞ | — | — | 100.0% | 2/1 |
| 2404.14476 | ✓ | 0.80 | 96.1% | 0.493 | 0.339 | 0.241 | 0.190 | 32.7% | 28/51 |
| 2504.12377 | ✓ | 0.85 | 100.0% | 0.177 | 0.027 | 0.027 | 0.581 | 100.0% | 28/15 |
| 2408.15227 | ✓ | 0.60 | 100.0% | 0.054 | 0.063 | 0.055 | 0.517 | 100.0% | 30/230 |
| 2209.09917 | ✓ | 0.50 | 80.0% | 0.512 | 0.323 | 0.352 | 0.750 | 25.0% | 5/5 |
| 2406.00387 | ✓ | 0.85 | 99.1% | 0.477 | 0.347 | 0.088 | 0.991 | 38.3% | 101/108 |
| 1207.3275 | ✓ | 0.72 | 100.0% | 0.064 | 0.046 | 0.069 | 0.045 | 77.8% | 22/9 |
| 2205.01079 | ✓ | 0.50 | 78.6% | 0.123 | 0.109 | 0.231 | 0.898 | 72.7% | 5/14 |
| 2212.02403 | ✓ | 0.50 | 100.0% | 1.882 | 1.043 | 1.206 | 0.980 | 2.4% | 4/42 |
| 1903.12190 | ✓ | 0.40 | 66.7% | 3.799 | 2.398 | 3.338 | 0.623 | 0.0% | 6/3 |
| 2305.00890 | ✓ | 0.85 | 100.0% | 0.065 | 0.880 | 0.987 | 0.996 | 79.1% | 31/4991 |
| 1708.06367 | ✓ | 0.30 | convention_mismatch | — | — | — | — | — | — |
| 2312.13723 | — | — | EXCLUDED | — | — | — | — | — | — |
| 2410.10363 | ✓ | 0.40 | 100.0% | 0.293 | ∞ | 0.740 | 0.943 | 51.0% | 2/288 |
| 1202.5851 | — | — | EXCLUDED | — | — | — | — | — | — |
| 2208.06519 | ✓ | 0.90 | 100.0% | 0.097 | ∞ | — | — | 100.0% | 1/1 |
| 2401.16747 | ✓ | 0.55 | 97.0% | 0.272 | 0.213 | 0.256 | 0.999 | 56.2% | 33/66 |
| 2401.18076 | ✓ | 0.55 | 82.8% | 1.137 | 1.073 | 1.008 | 0.729 | 4.2% | 31/29 |
| 2503.13653 | ✓ | 0.42 | 88.7% | 4.333 | 4.171 | 2.395 | 0.437 | 0.0% | 7/53 |
| 2308.06339 | ✓ | 0.30 | 96.1% | 0.139 | 0.081 | 0.162 | 0.997 | 86.3% | 6/76 |
| 2109.11734 | ✓ | 0.90 | 83.3% | 0.144 | 0.004 | 0.084 | 0.820 | 100.0% | 6/12 |
| 2308.09077 | ✓ | 0.70 | 83.3% | 0.182 | 0.261 | 0.194 | 0.923 | 100.0% | 2/54 |
| 2110.06096 | ✓ | 0.68 | 100.0% | 0.063 | 0.062 | 0.067 | 0.516 | 100.0% | 37/242 |
| 2205.03679 | ✓ | 0.75 | 100.0% | 0.223 | ∞ | 0.249 | 0.976 | 68.9% | 2/1525 |
| 2202.08858 | ✓ | 0.70 | 100.0% | 1.272 | 1.264 | 1.279 | 0.914 | 0.0% | 26/203 |
| 2503.14582 | ✓ | 0.60 | 100.0% | 0.184 | 0.124 | 0.207 | 0.997 | 75.4% | 7/196912 |
| 1207.2442 | ✓ | 0.50 | convention_mismatch | — | — | — | — | — | — |
| 1609.00667 | — | — | EXCLUDED | — | — | — | — | — | — |
| 2407.03828 | ✓ | 0.85 | 99.1% | 0.022 | 0.068 | 0.051 | 0.296 | 100.0% | 36/116 |
| 1810.04602 | ✓ | 0.78 | 96.4% | 0.520 | 0.513 | 0.481 | 0.912 | 9.4% | 28/55 |
| 2110.10262 | — | — | EXCLUDED | — | — | — | — | — | — |
| 2306.05934 | ✓ | 0.82 | 100.0% | 0.123 | 0.166 | 0.110 | 0.999 | 98.1% | 3/2636 |
| 2306.01048 | ✓ | 0.78 | 27.8% | 3.415 | 3.808 | 0.674 | 0.289 | 0.0% | 33/36 |
| 2008.08773 | ✓ | 0.50 | convention_mismatch | — | — | — | — | — | — |
| 2007.04990 | — | — | EXCLUDED | — | — | — | — | — | — |
| 2207.11968 | ✓ | 0.82 | 96.9% | 0.132 | 0.146 | 0.176 | 0.977 | 86.3% | 32/128 |
| 0807.2926 | ✓ | 0.50 | 16.7% | 0.026 | 0.045 | 0.030 | 0.368 | 100.0% | 2/18 |
| 1508.02463 | ✓ | 0.60 | 90.7% | 0.040 | 0.058 | 0.030 | 0.176 | 100.0% | 29/43 |
| 0809.4700 | ✓ | 0.60 | 97.1% | 0.026 | 0.076 | 0.024 | 0.167 | 94.1% | 5/35 |
| 2006.07055 | ✓ | 0.42 | convention_mismatch | — | — | — | — | — | — |
| 2004.02733 | ✓ | 0.60 | 97.0% | 0.167 | 0.055 | 0.040 | 0.966 | 96.9% | 27/33 |
| 2111.09892 | ✓ | 0.50 | 100.0% | 0.000 | ∞ | 0.000 | 0.793 | 100.0% | 2/2 |
| 1401.6460 | ✓ | 0.50 | 50.0% | 1.662 | 2.013 | 1.660 | 0.863 | 0.0% | 26/4 |
| 2204.01454 | ✓ | 0.50 | 97.6% | 0.264 | 0.197 | 0.478 | 0.988 | 51.2% | 31/42 |
| 2410.02218 | — | — | EXCLUDED | — | — | — | — | — | — |
| 1808.02340 | ✓ | 0.60 | 1.1% | 0.913 | 0.813 | 0.898 | 0.011 | 0.0% | 2/265 |
| 2311.16364 | ✓ | 0.55 | 100.0% | 1.131 | 1.360 | 1.380 | 0.989 | 8.3% | 31/121 |
| 1704.02297 | ✓ | 0.85 | 96.6% | 0.107 | 0.116 | 0.121 | 0.085 | 96.4% | 34/58 |
| 1707.07921 | ✓ | 0.75 | 46.7% | 1.444 | 0.997 | 1.094 | 0.353 | 0.0% | 30/30 |
| 1806.00310 | ✓ | 0.85 | 100.0% | 0.045 | 0.045 | 0.045 | 0.005 | 100.0% | 2/8 |
| 2007.03694 | ✓ | 0.90 | 50.0% | 0.000 | 0.000 | 0.000 | 0.412 | 100.0% | 2/2 |
| 1911.11905 | ✓ | 0.50 | 100.0% | 1.063 | 1.078 | 1.023 | 0.994 | 7.2% | 34/250 |
| 1902.04246 | ✓ | 0.60 | 91.8% | 0.220 | 0.112 | 0.208 | 0.779 | 100.0% | 2/61 |
| 1708.02111 | — | — | EXCLUDED | — | — | — | — | — | — |
| 2006.09721 | ✓ | 0.85 | 0.0% | ∞ | ∞ | ∞ | 0.000 | 0.0% | 99/148 |
| 1907.11485 | ✓ | 0.90 | 100.0% | 0.000 | 0.000 | 0.000 | 1.000 | 100.0% | 78/78 |
| 2112.12116 | ✓ | 0.72 | 95.1% | 0.335 | 0.307 | 0.389 | 0.946 | 49.4% | 30/81 |
| 2006.12431 | ✓ | 0.70 | 98.9% | 0.107 | 0.115 | 0.113 | 0.956 | 94.4% | 29/90 |
| 2207.11330 | ✓ | 0.50 | 99.2% | 0.695 | 0.739 | 0.726 | 0.993 | 0.0% | 10/118 |
| 2412.08699 | — | — | EXCLUDED | — | — | — | — | — | — |
| 1512.06746 | — | — | EXCLUDED | — | — | — | — | — | — |
| 1606.07494 | — | — | EXCLUDED | — | — | — | — | — | — |
| 1906.00967 | — | — | EXCLUDED | — | — | — | — | — | — |
| 2108.05368 | — | — | EXCLUDED | — | — | — | — | — | — |
| 1705.00676 | — | — | EXCLUDED | — | — | — | — | — | — |
| 1509.00026 | — | — | EXCLUDED | — | — | — | — | — | — |
| 2402.00741 | ✓ | 0.20 | no_extracted_points | — | — | — | — | — | — |
| 1708.07521 | — | — | EXCLUDED | — | — | — | — | — | — |
| 1606.03145 | — | — | EXCLUDED | — | — | — | — | — | — |
| 2401.17253 | — | — | EXCLUDED | — | — | — | — | — | — |
| 1412.0789 | — | — | EXCLUDED | — | — | — | — | — | — |
| 2206.11598 | — | — | EXCLUDED | — | — | — | — | — | — |
| 1902.04644 | — | — | EXCLUDED | — | — | — | — | — | — |
| 2306.08039 | ✓ | 0.60 | 99.9% | 0.094 | 0.123 | 0.129 | 1.000 | 87.7% | 30/1158 |
| 2102.01448 | ✓ | 0.60 | 100.0% | 1.678 | 1.369 | 1.584 | 0.882 | 0.0% | 4/70 |
| 2209.03289 | ✓ | 0.75 | 100.0% | 0.052 | 0.061 | 0.058 | 0.998 | 100.0% | 29/110 |
| 2209.13588 | ✓ | 0.40 | 99.6% | 1.013 | 0.920 | 1.007 | 0.998 | 0.0% | 7/230 |
| 1906.11844 | ✓ | 0.50 | convention_mismatch | — | — | — | — | — | — |
| hep-ph/0611223 | ✓ | 0.40 | 43.8% | 0.025 | 0.037 | 0.024 | 0.084 | 100.0% | 2/32 |
| 1810.12257 | ✓ | 0.70 | 100.0% | 0.200 | 0.162 | 0.256 | 0.997 | 69.5% | 6/3214 |
| 2102.06722 | ✓ | 0.80 | 98.7% | 0.153 | 0.140 | 0.210 | 0.991 | 69.7% | 8/391 |
| 2404.12517 | ✓ | 0.72 | 79.9% | 0.305 | 0.110 | 0.175 | 0.918 | 48.5% | 5/284 |
| 0910.5914 | ✓ | 0.60 | 100.0% | 0.102 | 0.102 | 0.101 | 0.079 | 100.0% | 22/27 |
| 1804.05750 | ✓ | 0.80 | 100.0% | 0.121 | 0.087 | 0.117 | 0.847 | 93.8% | 4/145 |
| 1910.08638 | ✓ | 0.80 | 100.0% | 0.059 | 0.050 | 0.057 | 0.354 | 100.0% | 27/172 |
| 2504.07279 | ✓ | 0.55 | 89.3% | 0.444 | 0.484 | 0.462 | 0.934 | 0.0% | 2/234 |
| 1911.05772 | ✓ | 0.45 | 100.0% | 0.278 | 0.121 | 0.457 | 0.992 | 50.0% | 6/22 |
| 1901.00920 | ✓ | 0.60 | 99.1% | 0.848 | 0.171 | 0.565 | 1.000 | 32.8% | 9/117 |
| 1004.1313 | ✓ | 0.82 | 54.4% | 0.166 | 0.016 | 0.061 | 0.072 | 73.4% | 29/228 |
| 2008.05355 | ✓ | 0.60 | 98.0% | 0.168 | 0.190 | 0.204 | 0.971 | 77.1% | 3/49 |
| 2302.10206 | ✓ | 0.40 | 100.0% | 1.064 | 1.728 | 1.989 | 0.146 | 0.0% | 7/14 |
| 2101.11290 | ✓ | 0.55 | 50.0% | 0.041 | 0.041 | 0.049 | 0.010 | 100.0% | 28/2 |
| 2002.08370 | ✓ | 0.40 | 88.9% | 1.604 | 2.402 | 2.839 | 0.779 | 18.8% | 6/36 |
| 2211.12699 | ✓ | 0.72 | 100.0% | 0.079 | 0.057 | 0.094 | 0.931 | 93.3% | 31/75 |
| 2108.03316 | ✓ | 0.80 | 93.5% | 0.100 | 0.084 | 0.086 | 0.848 | 99.7% | 33/321 |
| 1709.00009 | ✓ | 0.45 | 70.3% | 2.339 | 2.630 | 1.382 | 0.176 | 0.0% | 6/37 |
| 2007.13071 | ✓ | 0.60 | 99.4% | 0.245 | 0.041 | 0.266 | 0.968 | 56.0% | 2/318 |
| 2009.09059 | ✓ | 0.85 | 82.5% | 0.561 | 0.626 | 0.574 | 0.305 | 0.0% | 29/114 |
| 2112.03439 | — | — | EXCLUDED | — | — | — | — | — | — |
| 2001.05102 | ✓ | 0.80 | 97.4% | 0.043 | 0.042 | 0.042 | 0.982 | 100.0% | 35/77 |
| 2008.10141 | ✓ | 0.80 | 98.6% | 0.021 | 0.022 | 0.021 | 0.966 | 100.0% | 2/220 |
| 2012.10764 | ✓ | 0.55 | 100.0% | 0.543 | 0.489 | 0.269 | 0.996 | 30.4% | 5/125 |
| 2206.08845 | ✓ | 0.72 | 99.1% | 0.107 | 0.093 | 0.112 | 0.953 | 99.9% | 6/2959 |
| 2207.13597 | ✓ | 0.70 | 93.9% | 0.020 | 0.021 | 0.021 | 0.969 | 100.0% | 3/49 |
| 2210.10961 | ✓ | 0.85 | 94.8% | 0.009 | 0.026 | 0.014 | 0.964 | 100.0% | 2/251 |
| 2312.11003 | ✓ | 0.80 | 91.2% | 0.016 | 0.020 | 0.019 | 0.945 | 100.0% | 2/181 |
| 2403.13390 | ✓ | 0.82 | 98.6% | 0.012 | 0.008 | 0.017 | 0.982 | 100.0% | 2/70 |
| 2402.12892 | ✓ | 0.40 | 100.0% | 0.066 | ∞ | 0.170 | 0.966 | 81.5% | 2/362 |
| 2211.02902 | ✓ | 0.80 | 100.0% | 0.142 | 0.154 | 0.149 | 0.988 | 97.6% | 29/169 |
| 1705.02290 | ✓ | 0.92 | 36.2% | 0.066 | 0.034 | 0.062 | 0.077 | 100.0% | 2/436 |
| hep-ex/0702006 | — | — | EXCLUDED | — | — | — | — | — | — |
| 1704.05189 | ✓ | 0.45 | 68.9% | 0.936 | 0.729 | 0.439 | 0.588 | 0.0% | 27/61 |
| 2411.13701 | ✓ | 0.40 | 72.9% | 0.234 | 0.463 | 0.390 | 0.841 | 53.2% | 4/170 |
| 2109.03261 | ✓ | 0.80 | 82.8% | 0.172 | 0.172 | 0.178 | 0.422 | 87.5% | 24/29 |
| 1304.0989 | ✓ | 0.80 | 96.6% | 0.133 | 0.088 | 0.055 | 0.140 | 100.0% | 7/29 |
| 1703.07354 | ✓ | 0.82 | 63.6% | 0.023 | 0.033 | 0.133 | 0.228 | 71.4% | 34/44 |
| 1907.05475 | ✓ | 0.85 | 58.8% | 0.067 | 0.057 | 0.053 | 0.479 | 80.0% | 30/17 |
| 2104.12772 | ✓ | 0.82 | 21.9% | 0.006 | 0.020 | 0.007 | 0.318 | 100.0% | 2/64 |
| 2407.10618 | ✓ | 0.50 | 100.0% | 2.481 | 2.293 | 2.124 | 0.935 | 7.3% | 36/2612 |
| 2303.03594 | ✓ | 0.85 | 25.8% | 0.459 | 0.352 | 0.450 | 0.385 | 8.7% | 2/89 |
| 2311.05476 | ✓ | 0.30 | convention_mismatch | — | — | — | — | — | — |
| 2201.09890 | ✓ | 0.50 | 95.2% | 0.114 | 0.472 | 1.258 | 0.044 | 75.0% | 7/21 |
| 1110.2895 | ✓ | 0.15 | convention_mismatch | — | — | — | — | — | — |
| 2412.02232 | ✓ | 0.60 | 88.7% | 0.911 | 1.356 | 0.908 | 0.889 | 14.5% | 4/124 |
| 2504.07559 | ✓ | 0.80 | 60.1% | 0.398 | 0.274 | 0.348 | 0.557 | 38.7% | 26/198 |
| 2404.17333 | ✓ | 0.92 | 20.0% | 0.124 | 0.137 | 0.461 | 0.052 | 80.0% | 5/25 |
| 2405.08059 | ✓ | 0.55 | 87.5% | 0.138 | 0.321 | 0.245 | 0.892 | 62.9% | 2/40 |
| 2211.03414 | ✓ | 0.80 | 83.5% | 0.081 | 0.104 | 0.107 | 0.856 | 96.7% | 25/109 |
| 1603.06978 | ✓ | 0.83 | 62.4% | 0.051 | 0.052 | 0.273 | 0.787 | 90.5% | 4/287 |
| 2305.10327 | ✓ | 0.70 | 85.7% | 0.132 | 0.197 | 0.600 | 0.612 | 90.5% | 5/49 |
| 2305.01002 | ✓ | 0.50 | 47.4% | 0.342 | 0.389 | 0.287 | 0.151 | 44.4% | 7/38 |
| 2208.13794 | ✓ | 0.55 | 94.4% | 0.335 | 0.369 | 0.322 | 0.719 | 44.0% | 4/89 |
| 2501.17119 | ✓ | 0.85 | 100.0% | 0.037 | 0.038 | 0.036 | 0.992 | 100.0% | 39/799 |
| 1406.6053 | ✓ | 0.90 | 3.7% | 0.003 | 0.010 | 0.004 | 0.793 | 100.0% | 2/27 |
| 2110.14406 | ✓ | 0.90 | 100.0% | 0.000 | ∞ | — | — | 100.0% | 1/1 |
| 2203.04332 | ✓ | 0.85 | 99.3% | 0.010 | 0.014 | 0.013 | 0.338 | 100.0% | 35/148 |
| 1610.02580 | ✓ | 0.90 | 57.0% | 0.044 | 0.049 | 0.061 | 0.523 | 97.1% | 46/121 |
| 2008.01853 | ✓ | 0.75 | 46.8% | 0.132 | 1.126 | 0.732 | 0.191 | 94.2% | 4/111 |
| 2409.08998 | ✓ | 0.82 | 97.2% | 0.138 | 0.145 | 1.197 | 0.989 | 98.1% | 4/324 |
| 1311.3148 | ✓ | 0.85 | 59.1% | 0.027 | 0.120 | 0.030 | 0.778 | 100.0% | 2/22 |
| 2301.06560 | ✓ | 0.45 | 84.5% | 0.244 | 0.089 | 0.199 | 0.901 | 59.8% | 6/97 |
| 2412.02543 | ✓ | 0.70 | 99.0% | 0.184 | 0.225 | 0.209 | 0.990 | 72.4% | 10/99 |
| 2209.06299 | — | — | EXCLUDED | — | — | — | — | — | — |
| 2310.15395 | ✓ | 0.70 | 66.8% | 0.122 | 0.046 | 0.141 | 0.661 | 89.7% | 2/262 |
| 2503.11753 | ✓ | 0.68 | 95.9% | 0.378 | 0.395 | 0.406 | 0.963 | 35.2% | 24/1844 |
| 1509.00476 | ✓ | 0.40 | 90.5% | 1.016 | 1.048 | 1.166 | 0.725 | 0.0% | 5/21 |
| 2307.01365 | ✓ | 0.82 | 98.9% | 0.321 | 0.281 | 0.329 | 0.925 | 47.3% | 33/94 |
| 2111.08025 | ✓ | 0.55 | 80.6% | 0.696 | 0.711 | 0.696 | 0.576 | 14.7% | 6/93 |
| 2412.03660 | ✓ | 0.78 | 67.0% | 0.224 | 0.265 | 0.582 | 0.661 | 61.0% | 5/115 |
| 2409.11777 | ✓ | 0.80 | 100.0% | 0.067 | 0.108 | 0.144 | 0.997 | 100.0% | 6/86 |
| 2401.07798 | ✓ | 0.60 | 92.1% | 0.190 | 0.587 | 0.649 | 0.364 | 54.3% | 24/38 |
| 1811.10997 | ✓ | 0.70 | 97.9% | 0.309 | 0.287 | 0.284 | 0.975 | 46.8% | 6/144 |
| 2203.04319 | ✓ | 0.82 | 87.9% | 0.062 | 0.145 | 0.095 | 0.941 | 83.6% | 28/132 |
| 2307.03878 | ✓ | 0.85 | no_comparable_gt | — | — | — | — | — | — |
| 2110.13636 | ✓ | 0.85 | 93.5% | 0.012 | 0.013 | 0.026 | 0.992 | 91.4% | 60/62 |
| 2008.09464 | ✓ | 0.85 | 96.0% | 0.023 | 0.023 | 0.040 | 0.992 | 97.9% | 73/50 |
| 2202.08274 | ✓ | 0.80 | 100.0% | 0.162 | 0.089 | 0.219 | 0.780 | 72.0% | 34/257 |
| 2203.12152 | ✓ | 0.80 | 98.4% | 0.747 | 0.654 | 0.661 | 0.976 | 3.3% | 31/123 |
| 2310.00904 | ✓ | 0.72 | 100.0% | 0.183 | 0.179 | 0.179 | 0.979 | 100.0% | 28/53 |
| 2407.18586 | ✓ | 0.85 | 97.4% | 0.052 | 0.045 | 0.064 | 0.990 | 94.6% | 34/265 |
| 1706.00209 | ✓ | 0.82 | 100.0% | 0.000 | ∞ | — | — | 100.0% | 1/1 |
| 1506.08082 | ✓ | 0.80 | 91.7% | 0.984 | 1.027 | 1.028 | 0.037 | 0.0% | 35/12 |
| 2303.08410 | ✓ | 0.90 | 100.0% | 0.117 | 0.065 | 0.100 | 0.973 | 92.7% | 18/192 |
| 2403.02096 | ✓ | 0.85 | 73.3% | 0.119 | 0.106 | 0.097 | 0.849 | 88.1% | 9/838 |
| 2412.02229 | ✓ | 0.75 | 97.5% | 0.409 | 0.495 | 0.448 | 0.965 | 35.0% | 40/120 |
| 1510.08052 | ✓ | 0.60 | 96.6% | 0.345 | 0.350 | 0.340 | 0.065 | 40.0% | 7/88 |
| 2409.10514 | ✓ | 0.82 | 89.7% | 0.231 | 0.193 | 0.191 | 0.943 | 57.9% | 25/156 |
| 1903.03586 | ✓ | 0.55 | 57.1% | 0.397 | 0.237 | 0.296 | 0.825 | 25.0% | 9/7 |
| 1903.06547 | ✓ | 0.92 | 100.0% | 0.000 | ∞ | — | — | 100.0% | 1/1 |
| 2012.09498 | ✓ | 0.90 | 100.0% | 0.079 | ∞ | — | — | 100.0% | 2/1 |
| 2304.07505 | ✓ | 0.85 | 75.0% | 0.519 | 0.669 | 0.489 | 0.718 | 20.8% | 2/32 |
| 2402.19063 | ✓ | 0.80 | 100.0% | 0.271 | 0.263 | 0.237 | 0.932 | 55.7% | 40/149 |
| 2104.13798 | ✓ | 0.90 | 100.0% | 0.000 | 0.000 | 0.000 | 1.000 | 100.0% | 2/2 |
| 2403.07790 | ✓ | 0.85 | 99.8% | 0.095 | 0.036 | 0.109 | 0.992 | 98.1% | 3/420 |
| 2409.01805 | ✓ | 0.78 | 68.1% | 0.301 | 0.207 | 0.395 | 0.583 | 50.0% | 25/91 |
| 2003.03348 | ✓ | 0.85 | 99.1% | 0.090 | 0.074 | 0.096 | 0.991 | 94.8% | 37/857 |
| 2303.11395 | ✓ | 0.45 | 97.3% | 0.207 | 0.536 | 0.538 | 0.815 | 58.3% | 5/37 |
| 2304.01060 | ✓ | 0.42 | 94.1% | 0.100 | 0.128 | 0.757 | 0.902 | 83.3% | 4/51 |
| 2212.09764 | ✓ | 0.55 | 97.0% | 0.084 | 0.117 | 0.155 | 0.078 | 100.0% | 12/33 |
| 2405.19393 | ✓ | 0.50 | 96.4% | 0.500 | 0.595 | 0.767 | 0.903 | 22.6% | 28/55 |
| 2306.11575 | ✓ | 0.72 | 100.0% | 0.408 | 0.371 | 0.350 | 0.997 | 32.8% | 6/415 |
| 2006.06722 | ✓ | 0.80 | 98.7% | 0.028 | 0.086 | 0.075 | 0.106 | 100.0% | 24/76 |
| 2203.16567 | ✓ | 0.85 | 100.0% | 0.079 | 0.038 | 0.058 | 0.982 | 100.0% | 5/115 |
| 2008.13662 | ✓ | 0.60 | 98.4% | 0.193 | 0.100 | 0.205 | 0.986 | 76.2% | 7/64 |
| 2205.05700 | ✓ | 0.55 | 100.0% | 0.606 | 0.312 | 0.596 | 0.982 | 34.4% | 6/122 |
| 2303.06968 | ✓ | 0.60 | 90.8% | 0.339 | 0.345 | 0.417 | 0.877 | 43.7% | 31/174 |
| 1501.01639 | ✓ | 0.55 | 5.6% | 0.257 | 0.258 | 0.257 | 0.675 | 100.0% | 2/18 |
| 2307.11216 | ✓ | 0.80 | 96.7% | 0.083 | 0.101 | 0.122 | 0.914 | 100.0% | 33/60 |
| 2112.09620 | ✓ | 0.70 | 100.0% | 0.478 | 0.025 | 0.409 | 0.924 | 36.1% | 5/83 |
| 2408.16045 | ✓ | 0.85 | 99.2% | 0.096 | 0.124 | 0.146 | 0.976 | 80.5% | 8801/124 |
| 2205.05574 | ✓ | 0.85 | 99.2% | 0.023 | 0.007 | 0.025 | 0.977 | 100.0% | 31/508 |
| 2307.07403 | ✓ | 0.60 | 95.3% | 0.456 | 0.548 | 0.481 | 0.970 | 30.6% | 7/555 |
| astro-ph/0611502 | ✓ | 0.30 | 97.8% | 0.157 | 0.181 | 0.150 | 0.992 | 98.9% | 7/91 |
| 2301.06778 | ✓ | 0.85 | 98.8% | 0.198 | 0.399 | 0.179 | 0.948 | 89.4% | 2/86 |
| 1912.07751 | — | — | EXCLUDED | — | — | — | — | — | — |
| 2402.07976 | ✓ | 0.70 | 97.6% | 0.449 | 0.279 | 0.407 | 0.940 | 12.6% | 5/10796 |
| 2102.00379 | ✓ | 0.50 | 76.9% | 0.384 | 0.339 | 1.625 | 0.979 | 35.0% | 30/26 |
| 2102.02207 | — | — | EXCLUDED | — | — | — | — | — | — |
| 2503.04726 | ✓ | 0.50 | 94.5% | 0.227 | 0.152 | 0.245 | 0.917 | 59.1% | 7/16611 |
| 2008.03305 | ✓ | 0.80 | 99.1% | 0.098 | 0.105 | 0.118 | 0.190 | 100.0% | 28/115 |
| 2412.09595 | — | — | EXCLUDED | — | — | — | — | — | — |
| 2008.02209 | ✓ | 0.60 | 97.1% | 0.049 | 0.049 | 0.073 | 0.934 | 97.0% | 15/69 |
| 2407.16628 | ✓ | 0.85 | 100.0% | 0.124 | 0.122 | 0.182 | 0.949 | 76.2% | 28/101 |
| 0801.1527 | ✓ | 0.42 | 66.3% | 1.756 | 2.314 | 1.658 | 0.764 | 12.9% | 9/175 |
| 2002.05165 | ✓ | 0.85 | 81.4% | 0.180 | 0.181 | 0.205 | 0.482 | 91.0% | 359/671 |
| 2409.12940 | ✓ | 0.80 | 100.0% | 0.112 | 0.168 | 0.303 | 0.922 | 75.9% | 49/174 |
| 2409.12115 | ✓ | 0.85 | 98.8% | 1.216 | 1.221 | 1.085 | 0.983 | 7.6% | 120/80 |
| 1201.5902 | ✓ | 0.45 | no_comparable_gt | — | — | — | — | — | — |
| 1911.05086 | ✓ | 0.90 | 100.0% | 0.000 | 0.000 | 0.000 | 1.000 | 100.0% | 401/401 |
| 2003.13698 | ✓ | 0.90 | 100.0% | 0.000 | 0.000 | 0.000 | 1.000 | 100.0% | 393/393 |
| 0810.5501 | ✓ | 0.70 | 90.2% | 0.046 | 0.025 | 0.074 | 0.978 | 89.1% | 5/112 |
| 2002.01796 | ✓ | 0.85 | no_comparable_gt | — | — | — | — | — | — |
| 1907.12628 | ✓ | 0.72 | 100.0% | 0.236 | 0.236 | 0.227 | 0.970 | 71.2% | 29/73 |
| 1906.08814 | ✓ | 0.80 | 100.0% | 0.000 | 0.000 | ∞ | 0.000 | 100.0% | 1/2 |
| 2101.02805 | — | — | EXCLUDED | — | — | — | — | — | — |
| 2405.20444 | ✓ | 0.60 | 99.6% | 0.409 | 0.825 | 0.369 | 0.986 | 36.0% | 2/493 |
| 2301.11512 | ✓ | 0.85 | 100.0% | 0.061 | 0.060 | 0.075 | 0.828 | 56.2% | 21/16 |
| 2207.05767 | — | — | EXCLUDED | — | — | — | — | — | — |
| 2003.13144 | ✓ | 0.85 | 86.4% | 0.112 | 0.102 | 0.151 | 0.802 | 73.7% | 24/22 |
| 2310.13891 | ✓ | 0.80 | 100.0% | 0.026 | ∞ | 0.026 | 0.925 | 100.0% | 2/87 |
| 2304.12907 | ✓ | 0.45 | convention_mismatch | — | — | — | — | — | — |
| 2211.00022 | ✓ | 0.68 | 100.0% | 0.276 | 0.312 | 0.388 | 0.955 | 53.1% | 33/143 |
| 2406.19445 | ✓ | 0.70 | 49.5% | 0.586 | 0.455 | 0.593 | 0.233 | 34.7% | 24/99 |
| 2402.17140 | — | — | EXCLUDED | — | — | — | — | — | — |
| 2110.01582 | ✓ | 0.70 | 46.2% | 0.109 | 0.088 | 0.147 | 0.787 | 100.0% | 5/26 |
| 2301.03622 | ✓ | 0.68 | 100.0% | 0.362 | 0.421 | 0.371 | 0.987 | 38.4% | 5/401 |
| 1007.3766 | ✓ | 0.85 | 100.0% | 0.283 | 0.283 | ∞ | 0.000 | 100.0% | 1/102 |
| 1410.5244 | ✓ | 0.85 | 100.0% | 0.107 | 0.095 | 0.075 | 0.599 | 90.5% | 197/21 |
| 2410.02858 | ✓ | 0.50 | 50.0% | 0.167 | 0.119 | 0.112 | 0.789 | 66.7% | 4/6 |
| 2110.10497 | ✓ | 0.70 | 100.0% | 0.113 | 0.113 | ∞ | 0.000 | 100.0% | 1/72 |
| 2012.05427 | ✓ | 0.80 | 92.3% | 4.189 | 4.113 | 7.141 | 0.570 | 0.0% | 29/26 |
| 2204.03818 | ✓ | 0.85 | 100.0% | 0.082 | 0.095 | 0.118 | 0.966 | 94.1% | 37/3689 |
| 2405.12285 | ✓ | 0.60 | 91.2% | 0.209 | 0.236 | 0.193 | 0.850 | 66.3% | 6/91 |
| 2406.02546 | ✓ | 0.82 | 95.5% | 0.441 | 0.274 | 0.571 | 0.902 | 42.9% | 6/22 |
| 2209.03419 | ✓ | 0.70 | 98.2% | 0.109 | 0.178 | 0.105 | 0.993 | 93.7% | 2/325 |
| 2212.01971 | ✓ | 0.50 | 97.7% | 0.199 | 0.194 | 0.167 | 0.976 | 75.8% | 3/131 |
| 2305.09711 | ✓ | 0.83 | 100.0% | 0.268 | ∞ | 0.279 | 0.951 | 63.4% | 2/57500 |
| 1502.04490 | ✓ | 0.60 | 70.7% | 0.724 | 1.058 | 1.041 | 0.687 | 25.3% | 8/123 |
| 1905.05579 | ✓ | 0.80 | 98.1% | 0.106 | 0.242 | 0.132 | 0.950 | 92.2% | 2/104 |
| 1301.6557 | ✓ | 0.80 | 81.3% | 0.143 | 0.124 | 0.140 | 0.841 | 78.0% | 29/123 |
| 2208.03183 | — | — | EXCLUDED | — | — | — | — | — | — |
| 2008.12231 | ✓ | 0.90 | 100.0% | 0.000 | ∞ | — | — | 100.0% | 1/1 |
| 2308.08337 | ✓ | 0.90 | 100.0% | 0.000 | ∞ | — | — | 100.0% | 1/1 |
| 1008.3536 | ✓ | 0.80 | 100.0% | 1.369 | 1.210 | 1.446 | 0.493 | 14.0% | 23/100 |
| 2106.00022 | ✓ | 0.85 | 87.9% | 0.582 | 0.585 | 0.597 | 0.937 | 11.8% | 29/58 |
| 1804.10777 | ✓ | 0.75 | 66.7% | 0.972 | 0.587 | 0.580 | 0.863 | 0.0% | 26/3 |
| 1504.00118 | ✓ | 0.82 | 66.7% | 0.147 | 0.055 | 0.118 | 0.766 | 75.0% | 3/12 |
| 2006.02828 | ✓ | 0.85 | 100.0% | 0.159 | ∞ | 0.167 | 0.952 | 100.0% | 2/6 |
| 1907.12449 | ✓ | 0.55 | 31.0% | 0.465 | 0.306 | 0.421 | 0.308 | 22.7% | 8/555 |
| 1903.05101 | ✓ | 0.78 | 77.4% | 0.115 | 0.099 | 0.129 | 0.662 | 100.0% | 27/53 |
| 2006.13929 | ✓ | 0.70 | 99.0% | 0.358 | 0.348 | 0.511 | 0.908 | 40.2% | 30/98 |
| 1807.04512 | ✓ | 0.32 | 44.4% | 0.367 | 0.509 | 0.804 | 0.603 | 50.0% | 32/36 |
| hep-ph/0307284 | ✓ | 0.30 | no_comparable_gt | — | — | — | — | — | — |
| 2103.03783 | ✓ | 0.45 | 100.0% | 0.787 | 0.810 | 0.824 | 0.941 | 13.0% | 31/69 |
| 2205.06817 | — | — | EXCLUDED | — | — | — | — | — | — |
| 2306.16219 | ✓ | 0.40 | 100.0% | 0.531 | 0.446 | 0.624 | 0.996 | 37.3% | 29/102 |
| 2303.00778 | ✓ | 0.50 | convention_mismatch | — | — | — | — | — | — |
| 2212.05721 | ✓ | 0.60 | 31.8% | 0.132 | 0.083 | 0.189 | 0.541 | 83.0% | 4/333 |
| 2005.14694 | — | — | EXCLUDED | — | — | — | — | — | — |
| 1503.06886 | ✓ | 0.72 | 100.0% | 0.150 | 0.161 | 0.236 | 0.990 | 86.6% | 10/1006 |
| 1902.02788 | ✓ | 0.30 | 0.0% | ∞ | ∞ | ∞ | 0.000 | 0.0% | 2/130 |
| 2301.03433 | ✓ | 0.50 | 86.0% | 0.202 | 0.219 | 0.231 | 0.666 | 84.5% | 8/172 |
| 2302.04565 | ✓ | 0.70 | 80.0% | 0.347 | 0.162 | 0.252 | 0.877 | 44.4% | 43/848 |
| 1604.08514 | ✓ | 0.55 | 87.5% | 0.621 | 0.668 | 0.811 | 0.892 | 12.4% | 5/505 |
| quant-ph/0106045 | ✓ | 0.55 | no_comparable_gt | — | — | — | — | — | — |
| 2109.08822 | ✓ | 0.72 | 96.9% | 0.380 | 0.372 | 0.349 | 0.996 | 19.4% | 6/32 |
| 2105.13085 | ✗ (DarkPhoton) | 0.30 | no_comparable_gt | — | — | — | — | — | — |
| 2301.08736 | ✗ (DarkPhoton) | 0.62 | no_comparable_gt | — | — | — | — | — | — |
| 2403.02381 | ✓ | 0.80 | 66.6% | 0.202 | 0.039 | 0.068 | 0.333 | 63.3% | 24/1001 |
| 2409.03814 | ✓ | 0.80 | 51.6% | 0.344 | 0.323 | 0.352 | 0.508 | 43.4% | 28/308 |
| 2112.07687 | ✗ (DarkPhoton) | 0.30 | no_comparable_gt | — | — | — | — | — | — |
| 2302.00685 | ✓ | 0.50 | 100.0% | 1.192 | 2.195 | 2.217 | 0.423 | 27.3% | 33/11 |
| 2011.11646 | ✓ | 0.35 | 100.0% | 7.314 | 8.037 | 8.458 | 0.794 | 0.0% | 24/49 |
| 2406.10337 | ✓ | 0.35 | convention_mismatch | — | — | — | — | — | — |
| 2011.08693 | — | — | EXCLUDED | — | — | — | — | — | — |
| 2012.12790 | ✓ | 0.35 | 94.3% | 11.470 | 10.899 | 11.280 | 0.937 | 0.0% | 5/209 |
| 2412.03655 | ✓ | 0.70 | 99.6% | 0.578 | 0.709 | 0.767 | 0.855 | 6.8% | 28/545 |
| 2105.13963 | ✓ | 0.40 | convention_mismatch | — | — | — | — | — | — |
| 2404.00616 | — | — | EXCLUDED | — | — | — | — | — | — |
| 2412.20932 | ✓ | 0.50 | 50.0% | 0.002 | 0.014 | 0.006 | 0.996 | 100.0% | 2/2 |
| 2408.07740 | ✓ | 0.40 | 100.0% | 0.848 | 0.453 | 1.670 | 0.064 | 11.1% | 31/18 |
| 2410.21590 | ✓ | 0.35 | convention_mismatch | — | — | — | — | — | — |
| 2205.01637 | ✓ | 0.55 | no_comparable_gt | — | — | — | — | — | — |
| 1708.08464 | ✓ | 0.20 | no_extracted_points | — | — | — | — | — | — |
| 2303.09865 | ✓ | 0.55 | 100.0% | 0.004 | 0.004 | 0.004 | 0.991 | 100.0% | 24/2 |
| 2211.02661 | ✓ | 0.30 | 100.0% | 0.299 | 0.301 | 0.291 | 0.529 | 58.1% | 2/167 |
| 2301.10784 | ✗ (ScalarNucleon) | 0.40 | no_comparable_gt | — | — | — | — | — | — |
| 1003.0964 | — | — | EXCLUDED | — | — | — | — | — | — |
| 2312.11608 | — | — | EXCLUDED | — | — | — | — | — | — |

## Breakdown by Extraction Source

Median residual is over papers with mass-range overlap; zero-overlap papers are listed separately.

| Source | Papers | Compared | Zero-overlap | Med. Resid. | ≤0.3 dex |
|--------|--------|----------|--------------|-------------|----------|
| table | 4 | 4 | 0 | 0.134 dex | 94.7% |
| figure_vision | 116 | 105 | 0 | 0.236 dex | 56.8% |
| text | 154 | 140 | 1 | 0.184 dex | 65.2% |

## Breakdown by Difficulty

> Difficulty is a placeholder label for the repo-sourced pool (nearly all `medium`); this table is informational only.

| Difficulty | Papers | Coupling Acc. | Med. Resid. | ≤0.3 dex |
|------------|--------|---------------|-------------|----------|
| easy | 11 | 100.0% | 0.030 dex | 83.3% |
| medium | 251 | 98.0% | 0.192 dex | 61.5% |
| hard | 29 | 100.0% | 0.188 dex | 65.8% |

## Confidence Calibration

- "Accurate" = median interpolation residual < **0.32 dex** AND interpolation coverage ≥ 50%.
- The **0.32 dex** threshold is the run-to-run LLM extraction *noise floor* (90th-pct per-paper median-residual std across repeated extractions, PR #545) — the binding floor. It is **not** the upstream digitization floor, which is only ~0.034 dex for table/text-sourced papers (PR #558). So a residual gap here is **real extractor overconfidence, not a yardstick artifact**.

### Binned accuracy (pass/fail)

| Bin | N | Mean Conf. | Actual Acc. | Gap |
|-----|---|------------|-------------|-----|
| [0.3–0.5) | 55 | 43.3% | 40.0% | +0.03 |
| [0.6–0.6) | 50 | 57.9% | 44.0% | +0.14 |
| [0.7–0.8) | 50 | 72.1% | 56.0% | +0.16 |
| [0.8–0.8) | 49 | 80.7% | 75.5% | +0.05 |
| [0.8–0.9) | 57 | 86.9% | 82.5% | +0.04 |

> **Interpretation**: Gap > 0 means the pipeline is overconfident; Gap < 0 means underconfident.

### Continuous view: residual distribution per bin

Median (and IQR) of each bin's per-paper median residual, over papers with a finite residual (zero mass-overlap papers excluded from the distribution but still counted in N). If confidence tracked accuracy, the median residual would fall as confidence rises.

| Bin | N | N finite | Median resid. (dex) | IQR (dex) |
|-----|---|----------|---------------------|-----------|
| [0.3–0.5) | 55 | 54 | 0.40 | 0.17–1.06 |
| [0.6–0.6) | 50 | 50 | 0.34 | 0.17–0.68 |
| [0.7–0.8) | 50 | 50 | 0.22 | 0.11–0.38 |
| [0.8–0.8) | 49 | 49 | 0.13 | 0.05–0.27 |
| [0.8–0.9) | 57 | 56 | 0.07 | 0.01–0.13 |

### Continuous view: empirical P(residual < τ) per bin

Fraction of papers in each bin whose median residual is below τ dex (τ = 0.32 is the noise floor used above). A well-calibrated, accurate extractor would show these probabilities rising with confidence.

| Bin | N | P(<0.10) | P(<0.32) | P(<0.50) | P(<1.00) |
|-----|---|----|----|----|----|
| [0.3–0.5) | 55 | 10.9% | 43.6% | 52.7% | 67.3% |
| [0.6–0.6) | 50 | 16.0% | 48.0% | 68.0% | 88.0% |
| [0.7–0.8) | 50 | 18.0% | 62.0% | 84.0% | 92.0% |
| [0.8–0.8) | 49 | 38.8% | 77.6% | 87.8% | 93.9% |
| [0.8–0.9) | 57 | 61.4% | 87.7% | 91.2% | 96.5% |

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
