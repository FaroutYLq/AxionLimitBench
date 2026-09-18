# AutoAxionLimits Extraction Pipeline — Evaluation Report

## Summary

- **Papers evaluated**: 329
- **Papers with curve comparison**: 275

## Curve-Comparison Coverage

A curve is scored only against a ground-truth curve of the **same coupling**. Papers whose extracted coupling has no matching GT curve are not comparable and are excluded from residual statistics (this is not an extraction failure).

| Status | Papers | Meaning |
|--------|--------|---------|
| compared | 275 | scored against a same-coupling GT curve |
| no_comparable_gt | 8 | extracted coupling has no GT curve in the pool (usually a coupling misclassification) |
| gt_unusable | 1 | GT curve has <2 usable points after boundary filtering |
| no_extracted_points | 4 | pipeline returned no data points |
| no_prediction | 3 | pipeline returned no coupling type |
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
| is_new_limit | 93.8% | 32 |
| is_projection | 100.0% | 32 |
| data_source | 25.0% | 32 |

> **Label provenance**: `is_new_limit`, `is_projection`, and `data_source` are scored against an **independent LLM labeler** (`evaluation/label_ground_truth.py`, model `claude-opus-4-5`) whose sole task is to classify paper properties — a distinct model and prompt from the extractor it grades, so this is a fair cross-model test, not self-agreement. These are **not human gold labels**. A human audit of 15 labeled papers found per-field labeler↔human agreement: is_new_limit 15/15, is_projection 15/15, data_source 14/15 (difficulty is derived mechanically from data_source + point count, not labeled).

### Coupling Type Misclassifications

| arXiv ID | Predicted | Expected |
|----------|-----------|----------|
| 1905.13650 | None | ['AxionNeutron'] |
| 2402.00741 | None | ['AxionMass'] |
| 1906.11844 | AxionProton | ['AxionNeutron'] |
| 2105.13085 | DarkPhoton | ['VectorBL'] |
| 1708.08464 | None | ['AxionMass'] |

### Coupling-Type Confusion Matrix (multi-type-aware)

Rows = authoritative GT type, columns = predicted type. A prediction is correct iff it is in ANY of the paper's GT types (diagonal). Off-diagonal cells are the confusable clusters. Graded 288, correct 286 (99.3%), skipped 41 (no prediction / no GT type).

| GT ⟍ Pred | AxionEDM | AxionElectron | AxionMass | AxionNeutron | AxionPhoton | AxionProton | DarkPhoton | MonopoleDipole | ScalarBaryon | ScalarElectron | ScalarNucleon | ScalarPhoton | VectorBL |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| AxionEDM | **5** |  |  |  |  |  |  |  |  |  |  |  |  |
| AxionElectron |  | **16** |  |  |  |  |  |  |  |  |  |  |  |
| AxionMass |  |  | **15** |  |  |  |  |  |  |  |  |  |  |
| AxionNeutron |  |  |  | **13** |  | 1 |  |  |  |  |  |  |  |
| AxionPhoton |  |  |  |  | **139** |  |  |  |  |  |  |  |  |
| AxionProton |  |  |  |  |  | **3** |  |  |  |  |  |  |  |
| DarkPhoton |  |  |  |  |  |  | **59** |  |  |  |  |  |  |
| MonopoleDipole |  |  |  |  |  |  |  | **3** |  |  |  |  |  |
| ScalarBaryon |  |  |  |  |  |  |  |  | **1** |  |  |  |  |
| ScalarElectron |  |  |  |  |  |  |  |  |  | **2** |  |  |  |
| ScalarNucleon |  |  |  |  |  |  |  |  |  |  | **4** |  |  |
| ScalarPhoton |  |  |  |  |  |  |  |  |  |  |  | **16** |  |
| VectorBL |  |  |  |  |  |  | 1 |  |  |  |  |  | **10** |

Off-diagonal confusions (GT → predicted, richest first):

- AxionNeutron → AxionProton: 1
- VectorBL → DarkPhoton: 1

## Extraction Quality — Interpolation Metric (primary)

Build log-log interpolation from extracted points, evaluate at ground-truth masses.

- **Papers compared**: 275 (271 with mass-range overlap, 4 with zero overlap)

**Coupling-value accuracy** (papers with mass-range overlap):
- **Median residual across papers**: 0.041 dex (IQR 0.012–0.135)
- **Mean residual across papers** (outlier-sensitive): 0.185 dex
- **Mean fraction within 0.3 dex (factor 2; the leaderboard headline is 10%, results/leaderboard.py)**: 85.3%
- **Mean fraction within 0.5 dex (factor 3)**: 91.8%

**Mass-range coverage** (a separate failure mode):
- **Mean interpolation coverage**: 89.1%
- **Zero-overlap papers**: 4/275 (1.5%) — extracted masses miss the GT range entirely (usually 1–2 extracted points or the wrong mass window)

**Reverse pass** (GT interpolated onto the *extracted* masses):
- Mirrors the forward pass. A large forward-vs-reverse gap, or a reverse coverage well below the forward coverage, flags an extraction whose mass *extent* or shape disagrees with the GT (e.g. running past the GT range).
- **Median reverse residual across papers**: 0.039 dex (forward: 0.041 dex)
- **Mean reverse interpolation coverage**: 88.7% (forward: 89.1%)

## Residual by Coupling Type — Micro vs Macro Average (issue #543)

The compared-paper pool is dominated by one coupling type (AxionPhoton), so the per-paper **micro-average** headline is largely that one type's number. The **macro-average** weights each coupling type equally (mean of the per-type medians), exposing how the pipeline does across the *range* of couplings rather than on the most common one.

- **Micro-average median residual** (per paper, 271 papers): 0.041 dex
- **Macro-average median residual** (equal weight per type, 13 types): 0.063 dex
- **Macro − micro gap**: +0.022 dex (macro is worse; a positive gap means the rarer couplings are harder than the AxionPhoton-dominated micro-average implies)

Per-type medians carry a bootstrap 95% CI (1000 resamples). Rows with **N < 5** are flagged small-sample — their median and CI are unstable and should not be read as a reliable per-type score.

| Coupling Type | N | Median Resid. (dex) | 95% CI (dex) | Flag |
|---------------|---|---------------------|--------------|------|
| AxionPhoton | 134 | 0.024 | [0.017, 0.050] |  |
| DarkPhoton | 55 | 0.051 | [0.038, 0.086] |  |
| ScalarPhoton | 16 | 0.095 | [0.056, 0.231] |  |
| AxionElectron | 16 | 0.033 | [0.008, 0.056] |  |
| AxionMass | 15 | 0.147 | [0.026, 0.342] |  |
| AxionNeutron | 12 | 0.054 | [0.019, 0.217] |  |
| VectorBL | 8 | 0.257 | [0.102, 0.503] |  |
| AxionEDM | 5 | 0.053 | [0.019, 0.393] |  |
| MonopoleDipole | 3 | 0.016 | [0.005, 0.017] | ⚠ small-sample (N<5) |
| ScalarNucleon | 2 | 0.008 | [0.005, 0.011] | ⚠ small-sample (N<5) |
| AxionProton | 2 | 0.018 | [0.002, 0.033] | ⚠ small-sample (N<5) |
| ScalarElectron | 2 | 0.029 | [0.029, 0.030] | ⚠ small-sample (N<5) |
| ScalarBaryon | 1 | 0.030 | [0.030, 0.030] | ⚠ small-sample (N<5) |

## Shape & Mass-Range Agreement — Symmetric Metrics (complementary)

These are symmetric, 2-D complements to the (asymmetric, vertical-only) interpolation residual. **Area-between-curves** integrates |Δ log10 coupling| over the overlapping log-mass range and normalises by the overlap width (a single shape+offset number, in dex; a pure mass shift inflates it even when the vertical residual looks fine). **Mass-range Jaccard** is the Jaccard index of the extracted vs GT log-mass intervals (1.0 = identical extent; small = over-/under-claimed mass range), reported separately from interpolation coverage.

- **Papers scored**: 266 (262 with mass overlap for area)
- **Median area-between-curves**: 0.075 dex (mean 0.256 dex)
- **Median mass-range Jaccard**: 0.965 (mean 0.771)

## Per-Paper Results

| arXiv ID | Coupling | Conf. | Interp. Cov. | Med. Resid. | Rev. Resid. | Area (dex) | Mass Jaccard | ≤0.3 dex | Points |
|----------|----------|-------|--------------|-------------|-------------|------------|--------------|----------|--------|
| 2208.07293 | ✓ | 0.65 | 100.0% | 0.068 | 0.068 | 0.071 | 0.044 | 100.0% | 50/2 |
| 2212.04413 | ✓ | 0.50 | 100.0% | 2.149 | 2.164 | 2.356 | 0.991 | 0.0% | 36/97 |
| 2410.19902 | ✓ | 0.85 | 100.0% | 0.342 | 0.342 | 0.342 | 0.636 | 0.0% | 2/2 |
| 1907.03767 | ✓ | 0.75 | 96.2% | 0.303 | 0.296 | 0.427 | 0.936 | 49.7% | 41/182 |
| 2209.06216 | ✓ | 0.72 | 99.1% | 0.014 | 0.010 | 0.343 | 0.985 | 97.7% | 60/2771 |
| 2005.14184 | ✓ | 0.85 | 99.7% | 0.056 | 0.041 | 0.053 | 0.998 | 96.8% | 89/891 |
| 2504.00720 | ✓ | 0.80 | 97.1% | 0.066 | 0.056 | 0.216 | 0.997 | 63.2% | 60/70 |
| 2408.02668 | ✓ | 0.80 | 100.0% | 0.189 | 0.262 | 0.214 | 0.993 | 74.6% | 53/413 |
| 1905.13650 | ✗ (None) | 0.90 | no_prediction | — | — | — | — | — | — |
| 2110.03679 | ✓ | 0.90 | 99.2% | 0.117 | 0.176 | 0.088 | 0.264 | 88.3% | 27/129 |
| 2303.07370 | ✓ | 0.85 | 98.1% | 0.026 | 0.027 | 0.027 | 0.994 | 100.0% | 25/107 |
| 2309.16600 | ✓ | 0.78 | 94.7% | 0.030 | 0.018 | 0.032 | 0.974 | 100.0% | 45/188 |
| 2504.16044 | ✓ | 0.80 | gt_unusable | — | — | — | — | — | — |
| 2312.06746 | ✓ | 0.85 | 94.2% | 0.050 | 0.049 | 0.079 | 0.982 | 88.2% | 44/171 |
| 1310.8098 | ✓ | 0.85 | 60.7% | 0.004 | 0.004 | 0.005 | 0.171 | 100.0% | 58/135 |
| 2408.02368 | ✓ | 0.85 | 0.0% | ∞ | ∞ | ∞ | 0.000 | 0.0% | 60/647 |
| 2011.07100 | ✓ | 0.80 | 97.5% | 0.017 | 0.011 | 0.021 | 0.335 | 100.0% | 20/79 |
| 2302.09096 | ✓ | 0.80 | 100.0% | 0.016 | 0.005 | 0.094 | 0.499 | 97.6% | 42/41 |
| 1410.7267 | ✓ | 0.80 | 94.6% | 0.005 | 0.009 | 0.009 | 0.976 | 100.0% | 16/74 |
| 1712.00483 | ✓ | 0.80 | 97.0% | 0.354 | 0.355 | 0.386 | 0.651 | 43.8% | 15/33 |
| 1607.07327 | ✓ | 0.80 | 97.1% | 0.034 | 0.039 | 0.038 | 0.955 | 100.0% | 22/35 |
| 1611.05852 | ✓ | 0.72 | no_comparable_gt | — | — | — | — | — | — |
| 2111.06883 | ✓ | 0.40 | 97.2% | 0.056 | 0.058 | 0.098 | 0.982 | 93.0% | 41/176 |
| 0802.2350 | ✓ | 0.90 | 70.8% | 0.011 | 0.025 | 0.012 | 0.679 | 100.0% | 6/24 |
| 2009.04517 | ✓ | 0.90 | no_extracted_points | — | — | — | — | — | — |
| 2010.08107 | ✓ | 0.72 | 99.0% | 0.069 | 0.057 | 0.102 | 0.986 | 93.2% | 58/208 |
| 2201.02042 | — | — | EXCLUDED | — | — | — | — | — | — |
| 2403.03004 | ✓ | 0.55 | 98.3% | 0.302 | 0.328 | 0.297 | 0.986 | 49.6% | 45/414 |
| 2205.03617 | ✓ | 0.40 | no_comparable_gt | — | — | — | — | — | — |
| 2310.06017 | ✓ | 0.55 | 99.1% | 0.278 | 0.280 | 0.281 | 0.997 | 91.1% | 32/113 |
| 2102.08764 | ✓ | 0.95 | 100.0% | 0.000 | 0.000 | 0.000 | 0.892 | 100.0% | 2/2 |
| 2308.14656 | ✓ | 0.80 | 0.0% | ∞ | ∞ | ∞ | 0.000 | 0.0% | 41/75 |
| 2207.03102 | ✓ | 0.90 | 100.0% | 0.000 | 0.000 | 0.000 | 0.240 | 100.0% | 2/2 |
| 1505.07455 | — | — | EXCLUDED | — | — | — | — | — | — |
| 2105.04603 | ✓ | 0.80 | 99.9% | 0.156 | 0.156 | 0.154 | 1.000 | 96.9% | 70/707 |
| 2303.11792 | ✓ | 0.80 | 95.0% | 0.137 | 0.134 | 0.134 | 0.890 | 100.0% | 59/20 |
| 1607.06083 | ✓ | 0.55 | 0.0% | ∞ | ∞ | ∞ | 0.000 | 0.0% | 51/113 |
| 2108.04746 | ✓ | 0.62 | 96.5% | 0.231 | 0.154 | 0.221 | 0.990 | 59.3% | 64/283 |
| 2208.12670 | ✓ | 0.88 | 100.0% | 0.000 | ∞ | — | — | 100.0% | 95/1 |
| 1806.05120 | ✓ | 0.85 | 98.9% | 0.108 | 0.068 | 0.112 | 0.994 | 93.5% | 38/94 |
| 2101.01241 | ✓ | 0.83 | 100.0% | 0.035 | ∞ | — | — | 100.0% | 33/1 |
| 2404.14476 | ✓ | 0.85 | 96.1% | 0.023 | 0.025 | 0.025 | 0.190 | 100.0% | 35/51 |
| 2504.12377 | ✓ | 0.85 | 100.0% | 0.003 | 0.003 | 0.003 | 0.581 | 100.0% | 16/15 |
| 2408.15227 | ✓ | 0.72 | 98.3% | 0.109 | 0.093 | 0.099 | 0.984 | 100.0% | 54/230 |
| 2209.09917 | ✓ | 0.85 | 100.0% | 0.000 | 0.000 | 0.001 | 1.000 | 100.0% | 5/5 |
| 2406.00387 | ✓ | 0.82 | 100.0% | 0.005 | 0.007 | 0.327 | 0.996 | 100.0% | 46/108 |
| 1207.3275 | ✓ | 0.85 | 100.0% | 0.026 | 0.019 | 0.022 | 0.058 | 100.0% | 27/9 |
| 2205.01079 | ✓ | 0.50 | 100.0% | 0.012 | 0.012 | 0.011 | 1.000 | 100.0% | 14/14 |
| 2212.02403 | ✓ | 0.78 | 90.5% | 0.040 | 0.038 | 0.038 | 0.967 | 97.4% | 61/42 |
| 1903.12190 | ✓ | 0.82 | 33.3% | 0.161 | 0.160 | 0.160 | 0.772 | 100.0% | 70/3 |
| 2305.00890 | ✓ | 0.80 | 90.5% | 0.052 | 0.058 | 0.074 | 0.972 | 97.1% | 55/4991 |
| 1708.06367 | ✓ | 0.60 | 97.2% | 0.019 | 0.020 | 0.027 | 0.947 | 100.0% | 34/36 |
| 2312.13723 | — | — | EXCLUDED | — | — | — | — | — | — |
| 2410.10363 | ✓ | 0.40 | 13.9% | 0.874 | 0.860 | 1.050 | 0.053 | 0.0% | 35/288 |
| 1202.5851 | — | — | EXCLUDED | — | — | — | — | — | — |
| 2208.06519 | ✓ | 0.85 | 100.0% | 0.093 | ∞ | — | — | 100.0% | 50/1 |
| 2401.16747 | ✓ | 0.80 | 97.0% | 0.007 | 0.021 | 0.026 | 0.995 | 100.0% | 123/66 |
| 2401.18076 | ✓ | 0.80 | 100.0% | 0.204 | 0.199 | 0.192 | 0.973 | 100.0% | 40/29 |
| 2503.13653 | ✓ | 0.80 | 94.3% | 0.006 | 0.008 | 1.480 | 0.571 | 100.0% | 94/53 |
| 2308.06339 | ✓ | 0.60 | 96.1% | 0.019 | 0.016 | 0.029 | 0.997 | 100.0% | 45/76 |
| 2109.11734 | ✓ | 0.72 | 91.7% | 0.024 | 0.007 | 0.133 | 0.998 | 81.8% | 12/12 |
| 2308.09077 | ✓ | 0.80 | 96.3% | 0.171 | 0.171 | 0.172 | 0.990 | 100.0% | 55/54 |
| 2110.06096 | ✓ | 0.72 | 95.5% | 0.047 | 0.048 | 0.058 | 0.980 | 100.0% | 80/242 |
| 2205.03679 | ✓ | 0.75 | 97.8% | 0.057 | 0.035 | 0.042 | 0.975 | 100.0% | 45/1525 |
| 2202.08858 | ✓ | 0.80 | 99.0% | 0.041 | 0.021 | 0.091 | 0.997 | 92.0% | 50/203 |
| 2503.14582 | ✓ | 0.85 | 99.9% | 0.363 | 0.348 | 0.383 | 0.996 | 36.9% | 45/196912 |
| 1207.2442 | ✓ | 0.78 | 80.0% | 0.102 | 0.121 | 0.125 | 0.685 | 85.0% | 25/50 |
| 1609.00667 | — | — | EXCLUDED | — | — | — | — | — | — |
| 2407.03828 | ✓ | 0.85 | 90.5% | 0.038 | 0.039 | 0.039 | 0.279 | 100.0% | 26/116 |
| 1810.04602 | ✓ | 0.85 | 96.4% | 0.011 | 0.007 | 0.012 | 0.880 | 96.2% | 10/55 |
| 2110.10262 | — | — | EXCLUDED | — | — | — | — | — | — |
| 2306.05934 | ✓ | 0.72 | 100.0% | 0.048 | 0.058 | 0.062 | 0.991 | 100.0% | 29/2636 |
| 2306.01048 | ✓ | 0.70 | 97.2% | 0.002 | 0.002 | 3.353 | 0.324 | 100.0% | 19/36 |
| 2008.08773 | ✓ | 0.75 | 96.5% | 0.095 | 0.080 | 0.097 | 0.925 | 94.5% | 59/543 |
| 2007.04990 | — | — | EXCLUDED | — | — | — | — | — | — |
| 2207.11968 | ✓ | 0.85 | 98.4% | 0.008 | 0.008 | 0.013 | 0.999 | 99.2% | 64/128 |
| 0807.2926 | ✓ | 0.85 | 16.7% | 0.026 | 0.045 | 0.030 | 0.430 | 100.0% | 2/18 |
| 1508.02463 | ✓ | 0.85 | 97.3% | 0.005 | 0.004 | 0.012 | 0.213 | 100.0% | 46/111 |
| 0809.4700 | ✓ | 0.75 | 82.9% | 0.011 | 0.155 | 0.037 | 0.167 | 89.7% | 11/35 |
| 2006.07055 | ✓ | 0.60 | 100.0% | 0.095 | 0.039 | 0.126 | 0.995 | 77.4% | 75/146 |
| 2004.02733 | ✓ | 0.70 | 97.0% | 0.246 | 0.002 | 0.040 | 0.966 | 65.6% | 2/33 |
| 2111.09892 | ✓ | 0.60 | 100.0% | 0.000 | 0.000 | 0.000 | 0.297 | 100.0% | 2/2 |
| 1401.6460 | ✓ | 0.75 | 75.0% | 0.393 | 0.393 | 0.357 | 0.750 | 33.3% | 25/4 |
| 2204.01454 | ✓ | 0.80 | 100.0% | 0.147 | 0.143 | 0.148 | 0.986 | 97.6% | 29/42 |
| 2410.02218 | — | — | EXCLUDED | — | — | — | — | — | — |
| 1808.02340 | ✓ | 0.60 | 96.2% | 0.170 | 0.130 | 0.203 | 0.966 | 70.6% | 70/265 |
| 2311.16364 | ✓ | 0.60 | 98.3% | 0.059 | 0.088 | 0.077 | 0.990 | 88.2% | 87/121 |
| 1704.02297 | ✓ | 0.80 | 93.1% | 0.010 | 0.009 | 0.012 | 0.083 | 100.0% | 45/58 |
| 1707.07921 | ✓ | 0.78 | 50.0% | 0.288 | 0.382 | 0.387 | 0.080 | 53.3% | 22/30 |
| 1806.00310 | ✓ | 0.80 | 100.0% | 0.167 | 0.167 | 0.156 | 0.001 | 97.5% | 40/8 |
| 2007.03694 | ✓ | 0.85 | 50.0% | 0.000 | 0.000 | 0.000 | 0.382 | 100.0% | 2/2 |
| 1911.11905 | ✓ | 0.90 | 100.0% | 0.056 | 0.052 | 0.060 | 0.992 | 94.5% | 90/256 |
| 1902.04246 | ✓ | 0.80 | 100.0% | 0.031 | 0.025 | 0.034 | 0.743 | 100.0% | 80/61 |
| 1708.02111 | — | — | EXCLUDED | — | — | — | — | — | — |
| 2006.09721 | ✓ | 0.80 | 99.3% | 0.035 | 0.026 | 0.034 | 0.862 | 100.0% | 91/148 |
| 1907.11485 | ✓ | 0.90 | 100.0% | 0.006 | 0.006 | 0.008 | 0.991 | 100.0% | 78/111 |
| 2112.12116 | ✓ | 0.72 | 100.0% | 0.002 | 0.002 | 0.009 | 1.000 | 100.0% | 34/100 |
| 2006.12431 | ✓ | 0.80 | 98.9% | 0.005 | 0.005 | 0.008 | 0.992 | 100.0% | 55/90 |
| 2207.11330 | ✓ | 0.75 | 99.2% | 0.015 | 0.022 | 0.014 | 0.990 | 100.0% | 71/118 |
| 2412.08699 | — | — | EXCLUDED | — | — | — | — | — | — |
| 1512.06746 | — | — | EXCLUDED | — | — | — | — | — | — |
| 1606.07494 | — | — | EXCLUDED | — | — | — | — | — | — |
| 1906.00967 | — | — | EXCLUDED | — | — | — | — | — | — |
| 2108.05368 | — | — | EXCLUDED | — | — | — | — | — | — |
| 1705.00676 | — | — | EXCLUDED | — | — | — | — | — | — |
| 1509.00026 | — | — | EXCLUDED | — | — | — | — | — | — |
| 2402.00741 | ✗ (None) | 0.90 | no_prediction | — | — | — | — | — | — |
| 1708.07521 | — | — | EXCLUDED | — | — | — | — | — | — |
| 1606.03145 | — | — | EXCLUDED | — | — | — | — | — | — |
| 2401.17253 | — | — | EXCLUDED | — | — | — | — | — | — |
| 1412.0789 | — | — | EXCLUDED | — | — | — | — | — | — |
| 2206.11598 | — | — | EXCLUDED | — | — | — | — | — | — |
| 1902.04644 | — | — | EXCLUDED | — | — | — | — | — | — |
| 2306.08039 | ✓ | 0.78 | 97.7% | 0.016 | 0.013 | 0.029 | 0.977 | 99.6% | 44/1158 |
| 2102.01448 | ✓ | 0.50 | 97.1% | 0.360 | 0.358 | 0.399 | 0.960 | 14.7% | 45/70 |
| 2209.03289 | ✓ | 0.80 | 32.7% | 0.067 | 0.189 | 0.099 | 0.334 | 97.2% | 2/110 |
| 2209.13588 | ✓ | 0.72 | 97.7% | 0.033 | 0.028 | 0.033 | 0.983 | 100.0% | 45/350 |
| 1906.11844 | ✗ (AxionProton) | 0.55 | no_comparable_gt | — | — | — | — | — | — |
| hep-ph/0611223 | ✓ | 0.72 | 93.8% | 0.019 | 0.017 | 0.018 | 0.124 | 100.0% | 34/32 |
| 1810.12257 | ✓ | 0.82 | 99.0% | 0.080 | 0.059 | 0.072 | 0.991 | 99.9% | 100/3214 |
| 2102.06722 | ✓ | 0.85 | 96.9% | 0.013 | 0.007 | 0.018 | 0.976 | 100.0% | 70/391 |
| 2404.12517 | ✓ | 0.80 | 95.4% | 0.307 | 0.205 | 0.200 | 0.986 | 46.9% | 36/284 |
| 0910.5914 | ✓ | 0.82 | 3.7% | 0.301 | 0.206 | 0.240 | 0.095 | 0.0% | 19/27 |
| 1804.05750 | ✓ | 0.85 | 97.9% | 0.081 | 0.074 | 0.075 | 0.926 | 100.0% | 80/145 |
| 1910.08638 | ✓ | 0.85 | 100.0% | 0.016 | 0.008 | 0.020 | 0.307 | 97.6% | 63/82 |
| 2504.07279 | ✓ | 0.60 | 88.0% | 0.066 | 0.060 | 0.107 | 0.831 | 84.5% | 52/234 |
| 1911.05772 | ✓ | 0.75 | 95.5% | 0.122 | 0.097 | 0.455 | 0.999 | 71.4% | 48/22 |
| 1901.00920 | ✓ | 0.85 | 98.3% | 0.027 | 0.012 | 0.100 | 1.000 | 92.2% | 66/117 |
| 1004.1313 | ✓ | 0.85 | 99.1% | 0.018 | 0.003 | 0.014 | 0.088 | 100.0% | 30/228 |
| 2008.05355 | ✓ | 0.90 | 98.0% | 0.017 | 0.019 | 0.016 | 0.971 | 100.0% | 73/49 |
| 2302.10206 | ✓ | 0.72 | 100.0% | 0.806 | 0.913 | 1.151 | 0.733 | 12.5% | 45/8 |
| 2101.11290 | ✓ | 0.78 | 50.0% | 0.083 | 0.061 | 0.062 | 0.010 | 100.0% | 70/2 |
| 2002.08370 | ✓ | 0.72 | 80.6% | 0.013 | 0.013 | 0.016 | 0.624 | 96.6% | 66/36 |
| 2211.12699 | ✓ | 0.95 | 98.7% | 0.276 | 0.341 | 0.273 | 0.965 | 55.4% | 654/75 |
| 2108.03316 | ✓ | 0.80 | 99.7% | 0.100 | 0.085 | 0.085 | 0.999 | 99.7% | 50/321 |
| 1709.00009 | ✓ | 0.50 | 100.0% | 1.067 | 0.848 | 3.311 | 0.907 | 16.2% | 23/37 |
| 2007.13071 | ✓ | 0.97 | 98.1% | 0.029 | 0.013 | 0.029 | 0.985 | 100.0% | 78/318 |
| 2009.09059 | ✓ | 0.85 | 33.3% | 0.096 | 0.221 | 0.092 | 0.109 | 100.0% | 16/114 |
| 2112.03439 | — | — | EXCLUDED | — | — | — | — | — | — |
| 2001.05102 | ✓ | 0.85 | 96.1% | 0.048 | 0.049 | 0.048 | 0.984 | 100.0% | 60/77 |
| 2008.10141 | ✓ | 0.75 | 98.6% | 0.018 | 0.012 | 0.020 | 0.966 | 100.0% | 10/220 |
| 2012.10764 | ✓ | 0.80 | 94.4% | 0.014 | 0.010 | 0.031 | 0.976 | 95.8% | 49/125 |
| 2206.08845 | ✓ | 0.85 | 98.6% | 0.176 | 0.177 | 0.174 | 0.987 | 99.9% | 100/2959 |
| 2207.13597 | ✓ | 0.85 | 91.8% | 0.012 | 0.014 | 0.012 | 0.975 | 100.0% | 45/49 |
| 2210.10961 | ✓ | 0.85 | 94.8% | 0.003 | 0.003 | 0.005 | 0.964 | 100.0% | 100/251 |
| 2312.11003 | ✓ | 0.85 | 90.1% | 0.008 | 0.008 | 0.010 | 0.934 | 100.0% | 79/181 |
| 2403.13390 | ✓ | 0.85 | 98.6% | 0.012 | 0.010 | 0.017 | 0.982 | 100.0% | 5/70 |
| 2402.12892 | ✓ | 0.75 | 98.9% | 0.024 | 0.014 | 0.065 | 0.993 | 93.0% | 99/362 |
| 2211.02902 | ✓ | 0.75 | 99.4% | 0.054 | 0.044 | 0.061 | 0.988 | 98.8% | 100/169 |
| 1705.02290 | ✓ | 0.90 | 47.2% | 0.067 | 0.063 | 0.070 | 0.100 | 100.0% | 19/436 |
| hep-ex/0702006 | — | — | EXCLUDED | — | — | — | — | — | — |
| 1704.05189 | ✓ | 0.85 | no_extracted_points | — | — | — | — | — | — |
| 2411.13701 | ✓ | 0.72 | 96.5% | 0.006 | 0.005 | 0.013 | 0.982 | 98.8% | 54/170 |
| 2109.03261 | ✓ | 0.85 | 96.6% | 0.016 | 0.005 | 0.075 | 0.426 | 100.0% | 18/29 |
| 1304.0989 | ✓ | 0.90 | 65.5% | 0.008 | 0.006 | 0.008 | 0.092 | 100.0% | 34/29 |
| 1703.07354 | ✓ | 0.85 | 63.6% | 0.082 | 0.080 | 0.156 | 0.227 | 71.4% | 60/44 |
| 1907.05475 | ✓ | 0.80 | 64.7% | 0.095 | 0.268 | 0.085 | 0.469 | 72.7% | 35/17 |
| 2104.12772 | ✓ | 0.85 | 98.4% | 0.003 | 0.003 | 0.007 | 0.497 | 100.0% | 23/64 |
| 2407.10618 | ✓ | 0.70 | 96.4% | 0.271 | 0.285 | 0.265 | 0.982 | 93.1% | 77/2612 |
| 2303.03594 | ✓ | 0.80 | 95.5% | 0.143 | 0.141 | 0.168 | 0.949 | 82.4% | 36/89 |
| 2311.05476 | ✓ | 0.75 | 96.7% | 0.003 | 0.002 | 0.005 | 0.992 | 100.0% | 59/121 |
| 2201.09890 | ✓ | 0.80 | 99.5% | 0.010 | 0.011 | 0.278 | 0.530 | 99.0% | 18/199 |
| 1110.2895 | ✓ | 0.40 | 15.0% | 8.945 | 9.221 | 8.400 | 0.688 | 0.0% | 37/40 |
| 2412.02232 | ✓ | 0.50 | 77.4% | 0.292 | 0.229 | 0.427 | 0.794 | 50.0% | 34/124 |
| 2504.07559 | ✓ | 0.85 | 64.6% | 0.107 | 0.061 | 0.089 | 0.572 | 93.0% | 54/198 |
| 2404.17333 | ✓ | 0.80 | 96.0% | 0.194 | 0.123 | 0.231 | 0.191 | 62.5% | 6/25 |
| 2405.08059 | ✓ | 0.95 | no_extracted_points | — | — | — | — | — | — |
| 2211.03414 | ✓ | 0.82 | 99.1% | 0.010 | 0.010 | 0.014 | 0.991 | 100.0% | 50/109 |
| 1603.06978 | ✓ | 0.85 | 99.0% | 0.004 | 0.000 | 0.187 | 1.000 | 100.0% | 24/287 |
| 2305.10327 | ✓ | 0.83 | 98.0% | 0.005 | 0.006 | 0.353 | 0.979 | 100.0% | 80/49 |
| 2305.01002 | ✓ | 0.78 | 94.7% | 0.005 | 0.008 | 0.294 | 0.976 | 100.0% | 8/38 |
| 2208.13794 | ✓ | 0.80 | 100.0% | 0.429 | 0.411 | 0.428 | 0.404 | 0.0% | 27/89 |
| 2501.17119 | ✓ | 0.85 | 98.2% | 0.012 | 0.010 | 0.013 | 0.996 | 100.0% | 80/799 |
| 1406.6053 | ✓ | 0.90 | 3.7% | 0.003 | 0.010 | 0.004 | 0.793 | 100.0% | 2/27 |
| 2110.14406 | ✓ | 0.85 | 100.0% | 0.003 | ∞ | — | — | 100.0% | 32/1 |
| 2203.04332 | ✓ | 0.85 | 99.3% | 0.006 | 0.004 | 0.005 | 0.337 | 100.0% | 45/148 |
| 1610.02580 | ✓ | 0.85 | 54.5% | 0.064 | 0.066 | 0.077 | 0.517 | 95.5% | 25/121 |
| 2008.01853 | ✓ | 0.80 | 48.6% | 0.151 | 0.148 | 0.743 | 0.192 | 92.6% | 60/111 |
| 2409.08998 | ✓ | 0.78 | 98.5% | 0.086 | 0.092 | 1.182 | 0.894 | 97.5% | 91/324 |
| 1311.3148 | ✓ | 0.82 | 100.0% | 0.009 | 0.006 | 0.030 | 0.716 | 100.0% | 42/22 |
| 2301.06560 | ✓ | 0.80 | 68.0% | 0.003 | 0.003 | 0.002 | 0.813 | 100.0% | 20/97 |
| 2412.02543 | ✓ | 0.85 | 99.0% | 0.053 | 0.041 | 0.049 | 0.992 | 100.0% | 50/99 |
| 2209.06299 | — | — | EXCLUDED | — | — | — | — | — | — |
| 2310.15395 | ✓ | 0.82 | 98.5% | 0.115 | 0.122 | 0.137 | 0.991 | 92.6% | 84/262 |
| 2503.11753 | ✓ | 0.80 | 95.0% | 0.214 | 0.005 | 0.251 | 0.953 | 69.6% | 45/1844 |
| 1509.00476 | ✓ | 0.60 | 95.2% | 0.019 | 0.035 | 0.025 | 0.983 | 90.0% | 11/21 |
| 2307.01365 | ✓ | 0.82 | 100.0% | 0.285 | 0.272 | 0.296 | 0.909 | 52.1% | 42/94 |
| 2111.08025 | ✓ | 0.83 | 93.5% | 0.034 | 0.033 | 0.033 | 0.983 | 100.0% | 49/93 |
| 2412.03660 | ✓ | 0.85 | 100.0% | 0.012 | 0.012 | 0.012 | 0.996 | 100.0% | 20/115 |
| 2409.11777 | ✓ | 0.82 | 100.0% | 0.098 | 0.100 | 0.041 | 0.999 | 100.0% | 90/86 |
| 2401.07798 | ✓ | 0.60 | 100.0% | 0.012 | 0.007 | 0.164 | 0.786 | 97.4% | 45/38 |
| 1811.10997 | ✓ | 0.85 | 99.3% | 0.006 | 0.010 | 0.008 | 0.997 | 100.0% | 66/144 |
| 2203.04319 | ✓ | 0.85 | 97.0% | 0.006 | 0.030 | 0.021 | 0.982 | 100.0% | 17/132 |
| 2307.03878 | ✓ | 0.72 | 94.7% | 0.008 | 0.009 | 0.190 | 0.996 | 100.0% | 54/76 |
| 2110.13636 | ✓ | 0.80 | 90.3% | 0.011 | 0.013 | 0.037 | 0.956 | 100.0% | 25/62 |
| 2008.09464 | ✓ | 0.80 | 96.0% | 0.006 | 0.006 | 0.026 | 0.998 | 100.0% | 73/50 |
| 2202.08274 | ✓ | 0.75 | 87.2% | 0.228 | 0.147 | 0.251 | 0.885 | 61.2% | 68/257 |
| 2203.12152 | ✓ | 0.85 | 98.4% | 0.034 | 0.028 | 0.060 | 0.979 | 97.5% | 89/123 |
| 2310.00904 | ✓ | 0.90 | 100.0% | 0.012 | 0.013 | 0.014 | 0.979 | 100.0% | 70/53 |
| 2407.18586 | ✓ | 0.85 | 97.7% | 0.014 | 0.011 | 0.017 | 0.997 | 100.0% | 70/265 |
| 1706.00209 | ✓ | 0.85 | 100.0% | 0.000 | ∞ | — | — | 100.0% | 2/1 |
| 1506.08082 | ✓ | 0.85 | 91.7% | 0.061 | 0.024 | 0.024 | 0.036 | 90.9% | 70/12 |
| 2303.08410 | ✓ | 0.90 | 99.5% | 0.117 | 0.061 | 0.100 | 0.993 | 92.7% | 9/192 |
| 2403.02096 | ✓ | 0.85 | 100.0% | 0.130 | 0.044 | 0.100 | 0.998 | 68.4% | 45/838 |
| 2412.02229 | ✓ | 0.80 | 99.2% | 0.009 | 0.013 | 0.012 | 0.994 | 100.0% | 51/120 |
| 1510.08052 | ✓ | 0.85 | 96.6% | 0.008 | 0.006 | 0.362 | 0.065 | 85.9% | 24/88 |
| 2409.10514 | ✓ | 0.85 | 100.0% | 0.057 | 0.022 | 0.096 | 0.892 | 73.7% | 43/156 |
| 1903.03586 | ✓ | 0.72 | 0.0% | ∞ | ∞ | ∞ | 0.000 | 0.0% | 32/7 |
| 1903.06547 | ✓ | 0.95 | 100.0% | 0.000 | ∞ | — | — | 100.0% | 2/1 |
| 2012.09498 | ✓ | 0.85 | 100.0% | 0.241 | ∞ | — | — | 100.0% | 70/1 |
| 2304.07505 | ✓ | 0.90 | 75.0% | 0.262 | 0.206 | 0.228 | 0.716 | 54.2% | 32/32 |
| 2402.19063 | ✓ | 0.85 | 98.0% | 0.231 | 0.233 | 0.233 | 0.984 | 60.3% | 49/149 |
| 2104.13798 | ✓ | 0.85 | 100.0% | 0.000 | 0.000 | 0.000 | 1.000 | 100.0% | 2/2 |
| 2403.07790 | ✓ | 0.90 | 99.8% | 0.021 | 0.017 | 0.025 | 0.996 | 100.0% | 90/420 |
| 2409.01805 | ✓ | 0.83 | 94.5% | 0.132 | 0.128 | 0.137 | 0.958 | 100.0% | 37/91 |
| 2003.03348 | ✓ | 0.85 | 97.8% | 0.024 | 0.023 | 0.048 | 0.979 | 96.8% | 45/857 |
| 2303.11395 | ✓ | 0.78 | 94.6% | 0.003 | 0.003 | 0.136 | 0.800 | 100.0% | 44/37 |
| 2304.01060 | ✓ | 0.78 | 98.0% | 0.018 | 0.021 | 0.565 | 0.976 | 100.0% | 34/51 |
| 2212.09764 | ✓ | 0.85 | 97.0% | 0.002 | 0.002 | 0.002 | 0.136 | 100.0% | 35/33 |
| 2405.19393 | ✓ | 0.78 | 98.2% | 0.263 | 0.291 | 0.206 | 0.918 | 53.7% | 43/55 |
| 2306.11575 | ✓ | 0.85 | 96.1% | 0.008 | 0.008 | 0.008 | 0.930 | 100.0% | 30/415 |
| 2006.06722 | ✓ | 0.85 | 97.4% | 0.002 | 0.000 | 0.003 | 0.110 | 100.0% | 11/76 |
| 2203.16567 | ✓ | 0.85 | 100.0% | 0.083 | 0.061 | 0.064 | 0.993 | 100.0% | 30/115 |
| 2008.13662 | ✓ | 0.82 | 100.0% | 0.011 | 0.017 | 0.017 | 0.987 | 100.0% | 51/64 |
| 2205.05700 | ✓ | 0.62 | 73.0% | 0.015 | 0.011 | 0.019 | 0.798 | 100.0% | 35/122 |
| 2303.06968 | ✓ | 0.85 | 99.4% | 0.192 | 0.127 | 0.222 | 0.999 | 58.4% | 34/174 |
| 1501.01639 | ✓ | 0.75 | 50.0% | 0.003 | 0.003 | 0.003 | 0.612 | 100.0% | 12/2 |
| 2307.11216 | ✓ | 0.80 | 100.0% | 0.127 | 0.132 | 0.123 | 0.920 | 100.0% | 42/60 |
| 2112.09620 | ✓ | 0.82 | 98.8% | 0.007 | 0.006 | 0.007 | 0.998 | 100.0% | 80/83 |
| 2408.16045 | ✓ | 0.78 | 100.0% | 0.026 | 0.024 | 0.028 | 0.999 | 100.0% | 45/124 |
| 2205.05574 | ✓ | 0.80 | 98.4% | 0.015 | 0.009 | 0.023 | 0.984 | 100.0% | 90/508 |
| 2307.07403 | ✓ | 0.72 | 93.9% | 0.189 | 0.073 | 0.165 | 0.967 | 67.8% | 97/555 |
| astro-ph/0611502 | ✓ | 0.68 | 97.8% | 0.157 | 0.181 | 0.150 | 0.992 | 98.9% | 7/91 |
| 2301.06778 | ✓ | 0.82 | 96.5% | 0.066 | 0.064 | 0.091 | 0.925 | 92.8% | 54/86 |
| 1912.07751 | — | — | EXCLUDED | — | — | — | — | — | — |
| 2402.07976 | ✓ | 0.55 | 98.8% | 0.024 | 0.024 | 0.166 | 0.988 | 81.0% | 90/10796 |
| 2102.00379 | ✓ | 0.78 | 100.0% | 0.066 | 0.065 | 1.269 | 0.999 | 100.0% | 42/26 |
| 2102.02207 | — | — | EXCLUDED | — | — | — | — | — | — |
| 2503.04726 | ✓ | 0.70 | 97.0% | 0.175 | 0.160 | 0.187 | 0.981 | 87.1% | 85/16611 |
| 2008.03305 | ✓ | 0.85 | 99.1% | 0.017 | 0.015 | 0.019 | 0.190 | 100.0% | 19/115 |
| 2412.09595 | — | — | EXCLUDED | — | — | — | — | — | — |
| 2008.02209 | ✓ | 0.60 | 83.3% | 0.038 | 0.041 | 0.043 | 0.909 | 100.0% | 24/12 |
| 2407.16628 | ✓ | 0.78 | 100.0% | 2.197 | 2.217 | 2.205 | 0.992 | 0.0% | 50/101 |
| 0801.1527 | ✓ | 0.80 | 79.4% | 1.090 | 1.292 | 1.292 | 0.840 | 9.4% | 21/175 |
| 2002.05165 | ✓ | 0.80 | 83.2% | 0.012 | 0.023 | 0.022 | 0.482 | 99.6% | 62/671 |
| 2409.12940 | ✓ | 0.80 | 96.6% | 0.480 | 0.230 | 0.384 | 0.798 | 42.9% | 65/174 |
| 2409.12115 | ✓ | 0.82 | 96.2% | 0.082 | 0.076 | 0.159 | 0.967 | 87.0% | 45/80 |
| 1201.5902 | ✓ | 0.50 | 99.1% | 0.126 | 0.080 | 0.129 | 0.984 | 69.0% | 72/228 |
| 1911.05086 | ✓ | 0.90 | 60.1% | 0.005 | 0.000 | 0.006 | 0.600 | 100.0% | 41/401 |
| 2003.13698 | ✓ | 0.85 | 99.7% | 0.000 | 0.000 | 0.038 | 1.000 | 96.9% | 67/393 |
| 0810.5501 | ✓ | 0.82 | 90.2% | 0.022 | 0.031 | 0.022 | 0.972 | 100.0% | 44/112 |
| 2002.01796 | ✓ | 0.72 | no_comparable_gt | — | — | — | — | — | — |
| 1907.12628 | ✓ | 0.85 | 98.6% | 0.031 | 0.030 | 0.032 | 0.990 | 100.0% | 40/73 |
| 1906.08814 | ✓ | 0.85 | 100.0% | 0.000 | 0.176 | 0.167 | 0.688 | 100.0% | 34/2 |
| 2101.02805 | — | — | EXCLUDED | — | — | — | — | — | — |
| 2405.20444 | ✓ | 0.80 | 99.8% | 0.066 | 0.038 | 0.059 | 0.993 | 95.9% | 80/493 |
| 2301.11512 | ✓ | 0.90 | 93.8% | 0.008 | 0.009 | 0.007 | 0.994 | 100.0% | 19/16 |
| 2207.05767 | — | — | EXCLUDED | — | — | — | — | — | — |
| 2003.13144 | ✓ | 0.97 | 86.4% | 0.086 | 0.058 | 0.117 | 0.802 | 84.2% | 15/22 |
| 2310.13891 | ✓ | 0.85 | 98.9% | 0.038 | 0.039 | 0.039 | 0.998 | 100.0% | 45/87 |
| 2304.12907 | ✓ | 0.80 | 92.1% | 0.010 | 0.010 | 0.011 | 0.248 | 100.0% | 55/126 |
| 2211.00022 | ✓ | 0.80 | 94.4% | 0.040 | 0.024 | 0.217 | 0.950 | 80.0% | 59/143 |
| 2406.19445 | ✓ | 0.85 | 49.5% | 0.004 | 0.003 | 0.005 | 0.235 | 100.0% | 40/99 |
| 2402.17140 | — | — | EXCLUDED | — | — | — | — | — | — |
| 2110.01582 | ✓ | 0.90 | 76.9% | 0.188 | 0.181 | 0.146 | 0.963 | 95.0% | 55/26 |
| 2301.03622 | ✓ | 0.85 | 98.3% | 0.274 | 0.266 | 0.291 | 0.997 | 53.0% | 85/401 |
| 1007.3766 | ✓ | 0.90 | 30.4% | 0.087 | 0.113 | 0.104 | 0.228 | 80.6% | 22/102 |
| 1410.5244 | ✓ | 0.82 | 95.2% | 0.050 | 0.019 | 0.032 | 0.977 | 100.0% | 55/21 |
| 2410.02858 | ✓ | 0.82 | 66.7% | 0.002 | 0.001 | 0.002 | 0.790 | 100.0% | 4/6 |
| 2110.10497 | ✓ | 0.83 | 100.0% | 0.340 | 0.320 | 0.381 | 0.991 | 48.6% | 95/72 |
| 2012.05427 | ✓ | 0.60 | no_comparable_gt | — | — | — | — | — | — |
| 2204.03818 | ✓ | 0.85 | 98.9% | 0.021 | 0.021 | 0.048 | 0.989 | 97.8% | 93/3689 |
| 2405.12285 | ✓ | 0.82 | 98.9% | 0.049 | 0.050 | 0.107 | 0.997 | 94.4% | 124/91 |
| 2406.02546 | ✓ | 0.82 | 90.9% | 0.094 | 0.072 | 0.178 | 0.918 | 75.0% | 45/22 |
| 2209.03419 | ✓ | 0.80 | 96.0% | 0.086 | 0.056 | 0.060 | 0.967 | 99.7% | 40/325 |
| 2212.01971 | ✓ | 0.80 | 97.7% | 0.560 | 0.560 | 0.541 | 0.983 | 3.1% | 67/131 |
| 2305.09711 | ✓ | 0.80 | 99.4% | 0.098 | 0.087 | 0.117 | 0.989 | 97.0% | 50/57500 |
| 1502.04490 | ✓ | 0.80 | 71.5% | 0.171 | 0.148 | 0.166 | 0.651 | 87.5% | 21/123 |
| 1905.05579 | ✓ | 0.85 | 99.0% | 0.084 | 0.150 | 0.130 | 0.962 | 93.2% | 68/104 |
| 1301.6557 | ✓ | 0.70 | 59.3% | 0.369 | 0.060 | 0.367 | 0.591 | 19.2% | 2/123 |
| 2208.03183 | — | — | EXCLUDED | — | — | — | — | — | — |
| 2008.12231 | ✓ | 0.78 | 100.0% | 0.000 | ∞ | — | — | 100.0% | 21/1 |
| 2308.08337 | ✓ | 0.90 | 100.0% | 0.000 | ∞ | — | — | 100.0% | 1/1 |
| 1008.3536 | ✓ | 0.60 | 75.0% | 0.499 | 0.417 | 0.517 | 0.469 | 29.3% | 45/100 |
| 2106.00022 | ✓ | 0.85 | 82.8% | 0.164 | 0.163 | 0.161 | 0.910 | 100.0% | 41/58 |
| 1804.10777 | ✓ | 0.85 | 66.7% | 0.071 | 0.062 | 0.105 | 0.996 | 100.0% | 30/3 |
| 1504.00118 | ✓ | 0.85 | 66.7% | 0.099 | 0.066 | 0.076 | 0.746 | 100.0% | 31/12 |
| 2006.02828 | ✓ | 0.95 | 83.3% | 0.051 | 0.060 | 0.072 | 0.992 | 100.0% | 100/6 |
| 1907.12449 | ✓ | 0.72 | 98.6% | 0.008 | 0.008 | 0.023 | 0.874 | 99.1% | 75/555 |
| 1903.05101 | ✓ | 0.85 | 96.2% | 0.030 | 0.032 | 0.030 | 0.944 | 100.0% | 18/53 |
| 2006.13929 | ✓ | 0.85 | 99.0% | 0.010 | 0.012 | 0.013 | 0.753 | 96.9% | 53/98 |
| 1807.04512 | ✓ | 0.70 | 88.9% | 0.014 | 0.577 | 1.141 | 0.800 | 87.5% | 70/36 |
| hep-ph/0307284 | ✓ | 0.50 | no_comparable_gt | — | — | — | — | — | — |
| 2103.03783 | ✓ | 0.70 | 97.1% | 0.106 | 0.060 | 0.145 | 0.975 | 68.7% | 36/69 |
| 2205.06817 | — | — | EXCLUDED | — | — | — | — | — | — |
| 2306.16219 | ✓ | 0.78 | 98.0% | 0.030 | 0.048 | 0.042 | 0.983 | 95.0% | 88/102 |
| 2303.00778 | ✓ | 0.80 | 100.0% | 0.030 | 0.030 | 0.030 | 0.097 | 100.0% | 2/2 |
| 2212.05721 | ✓ | 0.82 | 100.0% | 0.029 | 0.021 | 0.034 | 0.993 | 100.0% | 48/333 |
| 2005.14694 | — | — | EXCLUDED | — | — | — | — | — | — |
| 1503.06886 | ✓ | 0.80 | 99.8% | 0.050 | 0.028 | 0.041 | 0.999 | 99.3% | 36/1006 |
| 1902.02788 | ✓ | 0.55 | 100.0% | 0.328 | 0.212 | 0.472 | 0.562 | 46.9% | 40/130 |
| 2301.03433 | ✓ | 0.80 | 92.4% | 0.019 | 0.016 | 0.023 | 0.922 | 100.0% | 42/172 |
| 2302.04565 | ✓ | 0.60 | 96.2% | 0.892 | 0.579 | 0.718 | 0.933 | 12.3% | 39/848 |
| 1604.08514 | ✓ | 0.85 | 97.8% | 0.064 | 0.032 | 0.052 | 0.983 | 100.0% | 45/505 |
| quant-ph/0106045 | ✓ | 0.55 | no_comparable_gt | — | — | — | — | — | — |
| 2109.08822 | ✓ | 0.80 | 93.8% | 0.503 | 0.521 | 0.522 | 0.972 | 0.0% | 60/32 |
| 2105.13085 | ✗ (DarkPhoton) | 0.45 | no_comparable_gt | — | — | — | — | — | — |
| 2301.08736 | ✓ | 0.40 | 98.8% | 1.040 | 1.040 | 1.592 | 0.993 | 0.0% | 50/165 |
| 2403.02381 | ✓ | 0.90 | no_extracted_points | — | — | — | — | — | — |
| 2409.03814 | ✓ | 0.80 | 49.4% | 0.236 | 0.230 | 0.257 | 0.491 | 61.2% | 45/308 |
| 2112.07687 | ✓ | 0.72 | 100.0% | 0.123 | 0.064 | 0.177 | 0.991 | 69.5% | 67/167 |
| 2302.00685 | ✓ | 0.70 | 100.0% | 1.882 | 3.268 | 3.252 | 0.398 | 9.1% | 45/11 |
| 2011.11646 | ✓ | 0.55 | 89.8% | 0.026 | 0.035 | 0.030 | 0.814 | 100.0% | 13/49 |
| 2406.10337 | ✓ | 0.55 | 60.8% | 5.035 | 5.146 | 0.639 | 0.160 | 0.0% | 72/51 |
| 2011.08693 | — | — | EXCLUDED | — | — | — | — | — | — |
| 2012.12790 | ✓ | 0.50 | 97.1% | 0.037 | 0.009 | 0.068 | 0.987 | 88.2% | 32/209 |
| 2412.03655 | ✓ | 0.68 | 99.1% | 0.016 | 0.017 | 0.031 | 0.991 | 98.9% | 40/545 |
| 2105.13963 | ✓ | 0.65 | 95.0% | 1.774 | 1.789 | 0.382 | 0.530 | 5.3% | 57/20 |
| 2404.00616 | — | — | EXCLUDED | — | — | — | — | — | — |
| 2412.20932 | ✓ | 0.80 | 50.0% | 0.002 | 0.007 | 0.006 | 0.996 | 100.0% | 12/2 |
| 2408.07740 | ✓ | 0.72 | 83.3% | 0.692 | 0.215 | 0.925 | 0.383 | 20.0% | 18/18 |
| 2410.21590 | ✓ | 0.55 | 76.5% | 0.046 | 0.011 | 0.897 | 0.771 | 100.0% | 12/34 |
| 2205.01637 | ✓ | 0.80 | 90.0% | 0.053 | 0.053 | 0.104 | 0.250 | 100.0% | 9/10 |
| 1708.08464 | ✗ (None) | 0.85 | no_prediction | — | — | — | — | — | — |
| 2303.09865 | ✓ | 0.85 | 100.0% | 0.005 | 0.005 | 0.005 | 0.991 | 100.0% | 12/2 |
| 2211.02661 | ✓ | 0.55 | 99.4% | 0.190 | 0.211 | 3.235 | 0.268 | 98.8% | 33/167 |
| 2301.10784 | ✓ | 0.72 | 96.3% | 0.224 | 0.236 | 0.215 | 0.968 | 100.0% | 47/107 |
| 1003.0964 | — | — | EXCLUDED | — | — | — | — | — | — |
| 2312.11608 | — | — | EXCLUDED | — | — | — | — | — | — |

## Breakdown by Extraction Source

Median residual is over papers with mass-range overlap; zero-overlap papers are listed separately.

| Source | Papers | Compared | Zero-overlap | Med. Resid. | ≤0.3 dex |
|--------|--------|----------|--------------|-------------|----------|
| table | 5 | 5 | 0 | 0.086 dex | 85.5% |
| figure_vision | 70 | 68 | 2 | 0.060 dex | 82.6% |
| text | 31 | 28 | 0 | 0.022 dex | 85.6% |

## Breakdown by Difficulty

> Difficulty is a placeholder label for the repo-sourced pool (nearly all `medium`); this table is informational only.

| Difficulty | Papers | Coupling Acc. | Med. Resid. | ≤0.3 dex |
|------------|--------|---------------|-------------|----------|
| easy | 11 | 100.0% | 0.023 dex | 97.6% |
| medium | 251 | 98.0% | 0.040 dex | 84.4% |
| hard | 29 | 100.0% | 0.048 dex | 89.3% |

## Confidence Calibration

- "Accurate" = median interpolation residual < **0.32 dex** AND interpolation coverage ≥ 50%.
- The **0.32 dex** threshold is the run-to-run LLM extraction *noise floor* (90th-pct per-paper median-residual std across repeated extractions, PR #545) — the binding floor. It is **not** the upstream digitization floor, which is only ~0.034 dex for table/text-sourced papers (PR #558). So a residual gap here is **real extractor overconfidence, not a yardstick artifact**.

### Binned accuracy (pass/fail)

| Bin | N | Mean Conf. | Actual Acc. | Gap |
|-----|---|------------|-------------|-----|
| [0.4–0.7) | 46 | 58.2% | 69.6% | -0.11 |
| [0.7–0.8) | 48 | 74.8% | 89.6% | -0.15 |
| [0.8–0.8) | 80 | 80.7% | 83.8% | -0.03 |
| [0.8–0.8) | 76 | 85.0% | 92.1% | -0.07 |
| [0.9–1.0) | 25 | 91.3% | 88.0% | +0.03 |

> **Interpretation**: Gap > 0 means the pipeline is overconfident; Gap < 0 means underconfident.

### Continuous view: residual distribution per bin

Median (and IQR) of each bin's per-paper median residual, over papers with a finite residual (zero mass-overlap papers excluded from the distribution but still counted in N). If confidence tracked accuracy, the median residual would fall as confidence rises.

| Bin | N | N finite | Median resid. (dex) | IQR (dex) |
|-----|---|----------|---------------------|-----------|
| [0.4–0.7) | 46 | 45 | 0.16 | 0.03–0.36 |
| [0.7–0.8) | 48 | 47 | 0.04 | 0.01–0.12 |
| [0.8–0.8) | 80 | 79 | 0.05 | 0.01–0.15 |
| [0.8–0.8) | 76 | 75 | 0.02 | 0.01–0.07 |
| [0.9–1.0) | 25 | 25 | 0.02 | 0.01–0.09 |

### Continuous view: empirical P(residual < τ) per bin

Fraction of papers in each bin whose median residual is below τ dex (τ = 0.32 is the noise floor used above). A well-calibrated, accurate extractor would show these probabilities rising with confidence.

| Bin | N | P(<0.10) | P(<0.32) | P(<0.50) | P(<1.00) |
|-----|---|----|----|----|----|
| [0.4–0.7) | 46 | 43.5% | 69.6% | 78.3% | 82.6% |
| [0.7–0.8) | 48 | 68.8% | 89.6% | 91.7% | 95.8% |
| [0.8–0.8) | 80 | 65.0% | 90.0% | 95.0% | 97.5% |
| [0.8–0.8) | 76 | 84.2% | 96.1% | 98.7% | 98.7% |
| [0.9–1.0) | 25 | 80.0% | 100.0% | 100.0% | 100.0% |

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
