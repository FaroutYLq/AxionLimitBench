# AutoAxionLimits Extraction Pipeline — Evaluation Report

## Summary

- **Papers evaluated**: 329
- **Papers with curve comparison**: 265

## Curve-Comparison Coverage

A curve is scored only against a ground-truth curve of the **same coupling**. Papers whose extracted coupling has no matching GT curve are not comparable and are excluded from residual statistics (this is not an extraction failure).

| Status | Papers | Meaning |
|--------|--------|---------|
| compared | 265 | scored against a same-coupling GT curve |
| no_comparable_gt | 14 | extracted coupling has no GT curve in the pool (usually a coupling misclassification) |
| convention_mismatch | 9 | same coupling but the GT curve uses a different convention/units (e.g. f_a [GeV] vs normalized, or d_e vs a large-valued variable) — excluded as a units gap, not extraction error |
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
| data_source | 56.2% | 32 |

> **Label provenance**: `is_new_limit`, `is_projection`, and `data_source` are scored against an **independent LLM labeler** (`evaluation/label_ground_truth.py`, model `claude-opus-4-5`) whose sole task is to classify paper properties — a distinct model and prompt from the extractor it grades, so this is a fair cross-model test, not self-agreement. These are **not human gold labels**. A human audit of 15 labeled papers found per-field labeler↔human agreement: is_new_limit 15/15, is_projection 15/15, data_source 14/15 (difficulty is derived mechanically from data_source + point count, not labeled).

### Coupling Type Misclassifications

| arXiv ID | Predicted | Expected |
|----------|-----------|----------|
| hep-ph/0611223 | AxionPhoton | ['AxionNeutron', 'AxionProton'] |
| 2302.04565 | ScalarNucleon | ['ScalarPhoton'] |
| 2105.13085 | DarkPhoton | ['VectorBL'] |
| 2301.08736 | DarkPhoton | ['VectorBL'] |
| 2112.07687 | DarkPhoton | ['VectorBL'] |

### Coupling-Type Confusion Matrix (multi-type-aware)

Rows = authoritative GT type, columns = predicted type. A prediction is correct iff it is in ANY of the paper's GT types (diagonal). Off-diagonal cells are the confusable clusters. Graded 291, correct 286 (98.3%), skipped 38 (no prediction / no GT type).

| GT ⟍ Pred | AxionEDM | AxionElectron | AxionMass | AxionNeutron | AxionPhoton | AxionProton | DarkPhoton | MonopoleDipole | ScalarBaryon | ScalarElectron | ScalarNucleon | ScalarPhoton | VectorBL |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| AxionEDM | **3** |  |  |  |  |  |  |  |  |  |  |  |  |
| AxionElectron |  | **16** |  |  |  |  |  |  |  |  |  |  |  |
| AxionMass |  |  | **18** |  |  |  |  |  |  |  |  |  |  |
| AxionNeutron |  |  |  | **15** | 1 |  |  |  |  |  |  |  |  |
| AxionPhoton |  |  |  |  | **139** |  |  |  |  |  |  |  |  |
| AxionProton |  |  |  |  | 1 | **2** |  |  |  |  |  |  |  |
| DarkPhoton |  |  |  |  |  |  | **63** |  |  |  |  |  |  |
| MonopoleDipole |  |  |  |  |  |  |  | **2** |  |  |  |  |  |
| ScalarBaryon |  |  |  |  |  |  |  |  | **1** |  |  |  |  |
| ScalarElectron |  |  |  |  |  |  |  |  |  | **2** |  |  |  |
| ScalarNucleon |  |  |  |  |  |  |  |  |  |  | **5** |  |  |
| ScalarPhoton |  |  |  |  |  |  |  |  |  |  | 1 | **14** |  |
| VectorBL |  |  |  |  |  |  | 3 |  |  |  |  |  | **6** |

Off-diagonal confusions (GT → predicted, richest first):

- VectorBL → DarkPhoton: 3
- AxionNeutron → AxionPhoton: 1
- AxionProton → AxionPhoton: 1
- ScalarPhoton → ScalarNucleon: 1

## Extraction Quality — Interpolation Metric (primary)

Build log-log interpolation from extracted points, evaluate at ground-truth masses.

- **Papers compared**: 265 (261 with mass-range overlap, 4 with zero overlap)

**Coupling-value accuracy** (papers with mass-range overlap):
- **Median residual across papers**: 0.160 dex (IQR 0.050–0.435)
- **Mean residual across papers** (outlier-sensitive): 0.683 dex
- **Mean fraction within 0.3 dex (factor 2; the leaderboard headline is 10%, results/leaderboard.py)**: 65.4%
- **Mean fraction within 0.5 dex (factor 3)**: 75.9%

**Mass-range coverage** (a separate failure mode):
- **Mean interpolation coverage**: 88.6%
- **Zero-overlap papers**: 4/265 (1.5%) — extracted masses miss the GT range entirely (usually 1–2 extracted points or the wrong mass window)

**Reverse pass** (GT interpolated onto the *extracted* masses):
- Mirrors the forward pass. A large forward-vs-reverse gap, or a reverse coverage well below the forward coverage, flags an extraction whose mass *extent* or shape disagrees with the GT (e.g. running past the GT range).
- **Median reverse residual across papers**: 0.162 dex (forward: 0.160 dex)
- **Mean reverse interpolation coverage**: 79.1% (forward: 88.6%)

## Residual by Coupling Type — Micro vs Macro Average (issue #543)

The compared-paper pool is dominated by one coupling type (AxionPhoton), so the per-paper **micro-average** headline is largely that one type's number. The **macro-average** weights each coupling type equally (mean of the per-type medians), exposing how the pipeline does across the *range* of couplings rather than on the most common one.

- **Micro-average median residual** (per paper, 261 papers): 0.160 dex
- **Macro-average median residual** (equal weight per type, 12 types): 0.895 dex
- **Macro − micro gap**: +0.735 dex (macro is worse; a positive gap means the rarer couplings are harder than the AxionPhoton-dominated micro-average implies)

Per-type medians carry a bootstrap 95% CI (1000 resamples). Rows with **N < 5** are flagged small-sample — their median and CI are unstable and should not be read as a reliable per-type score.

| Coupling Type | N | Median Resid. (dex) | 95% CI (dex) | Flag |
|---------------|---|---------------------|--------------|------|
| AxionPhoton | 134 | 0.131 | [0.104, 0.153] |  |
| DarkPhoton | 58 | 0.163 | [0.094, 0.207] |  |
| AxionNeutron | 14 | 0.339 | [0.045, 1.041] |  |
| AxionElectron | 14 | 0.115 | [0.047, 0.324] |  |
| ScalarPhoton | 13 | 0.448 | [0.298, 1.192] |  |
| AxionMass | 12 | 1.015 | [0.348, 10.593] |  |
| VectorBL | 6 | 0.617 | [0.196, 8.011] |  |
| AxionEDM | 3 | 0.129 | [0.031, 0.267] | ⚠ small-sample (N<5) |
| MonopoleDipole | 2 | 0.117 | [0.034, 0.200] | ⚠ small-sample (N<5) |
| ScalarNucleon | 2 | 6.996 | [2.294, 11.699] | ⚠ small-sample (N<5) |
| ScalarElectron | 2 | 0.655 | [0.058, 1.251] | ⚠ small-sample (N<5) |
| AxionProton | 1 | 0.015 | [0.015, 0.015] | ⚠ small-sample (N<5) |

## Shape & Mass-Range Agreement — Symmetric Metrics (complementary)

These are symmetric, 2-D complements to the (asymmetric, vertical-only) interpolation residual. **Area-between-curves** integrates |Δ log10 coupling| over the overlapping log-mass range and normalises by the overlap width (a single shape+offset number, in dex; a pure mass shift inflates it even when the vertical residual looks fine). **Mass-range Jaccard** is the Jaccard index of the extracted vs GT log-mass intervals (1.0 = identical extent; small = over-/under-claimed mass range), reported separately from interpolation coverage.

- **Papers scored**: 256 (246 with mass overlap for area)
- **Median area-between-curves**: 0.200 dex (mean 0.777 dex)
- **Median mass-range Jaccard**: 0.917 (mean 0.737)

## Per-Paper Results

| arXiv ID | Coupling | Conf. | Interp. Cov. | Med. Resid. | Rev. Resid. | Area (dex) | Mass Jaccard | ≤0.3 dex | Points |
|----------|----------|-------|--------------|-------------|-------------|------------|--------------|----------|--------|
| 2208.07293 | ✓ | 0.50 | 100.0% | 0.129 | 0.129 | 0.129 | 0.052 | 100.0% | 2/2 |
| 2212.04413 | ✓ | 0.30 | 100.0% | 0.143 | 0.167 | 0.982 | 0.995 | 63.9% | 37/97 |
| 2410.19902 | ✓ | 0.85 | convention_mismatch | — | — | — | — | — | — |
| 1907.03767 | ✓ | 0.60 | 93.4% | 0.772 | 0.767 | 0.824 | 0.916 | 20.0% | 44/182 |
| 2209.06216 | ✓ | 0.65 | 94.7% | 0.119 | 0.129 | 0.579 | 0.863 | 81.4% | 35/2771 |
| 2005.14184 | ✓ | 0.80 | 99.7% | 0.110 | 0.093 | 0.107 | 0.998 | 94.6% | 42/891 |
| 2504.00720 | ✓ | 0.70 | 97.1% | 2.177 | 0.067 | 0.976 | 0.992 | 2.9% | 2/70 |
| 2408.02668 | ✓ | 0.60 | 98.1% | 1.044 | 0.993 | 0.984 | 0.991 | 9.6% | 44/413 |
| 1905.13650 | ✓ | 0.55 | 100.0% | 1.310 | 0.934 | 0.757 | 0.730 | 7.4% | 32/243 |
| 2110.03679 | ✓ | 0.85 | 98.4% | 0.123 | 0.054 | 0.102 | 0.267 | 74.0% | 36/129 |
| 2303.07370 | ✓ | 0.55 | 97.2% | 0.161 | 0.129 | 0.138 | 0.965 | 97.1% | 6/107 |
| 2309.16600 | ✓ | 0.85 | 100.0% | 0.276 | 0.265 | 0.275 | 0.995 | 60.6% | 50/188 |
| 2504.16044 | ✓ | 0.85 | gt_unusable | — | — | — | — | — | — |
| 2312.06746 | ✓ | 0.90 | 98.2% | 0.045 | 0.049 | 0.105 | 0.988 | 76.2% | 39/171 |
| 1310.8098 | ✓ | 0.75 | 100.0% | 1.118 | 1.051 | 1.151 | 0.314 | 0.0% | 33/43 |
| 2408.02368 | ✓ | 0.80 | 100.0% | 0.176 | 0.007 | 0.175 | 0.999 | 87.8% | 3/647 |
| 2011.07100 | ✓ | 0.80 | 94.9% | 0.200 | 0.199 | 0.208 | 0.334 | 73.3% | 30/79 |
| 2302.09096 | ✓ | 0.85 | 92.7% | 0.034 | 0.035 | 0.114 | 0.494 | 97.4% | 41/41 |
| 1410.7267 | ✓ | 0.60 | 63.5% | 11.699 | 11.517 | 11.714 | 0.485 | 0.0% | 31/74 |
| 1712.00483 | ✓ | 0.55 | 63.6% | 0.829 | 0.755 | 1.040 | 0.323 | 19.0% | 2/33 |
| 1607.07327 | ✓ | 0.50 | convention_mismatch | — | — | — | — | — | — |
| 1611.05852 | ✓ | 0.75 | no_comparable_gt | — | — | — | — | — | — |
| 2111.06883 | ✓ | 0.30 | no_comparable_gt | — | — | — | — | — | — |
| 0802.2350 | ✓ | 0.30 | 66.7% | 2.294 | 1.900 | 1.964 | 0.335 | 0.0% | 6/24 |
| 2009.04517 | ✓ | 0.70 | 96.6% | 3.269 | 5.265 | 5.135 | 0.223 | 0.0% | 41/29 |
| 2010.08107 | ✓ | 0.50 | 99.5% | 1.887 | 1.504 | 2.219 | 0.988 | 0.0% | 2/208 |
| 2201.02042 | — | — | EXCLUDED | — | — | — | — | — | — |
| 2403.03004 | ✓ | 0.70 | 100.0% | 1.609 | 1.630 | 1.652 | 0.996 | 0.0% | 48/414 |
| 2205.03617 | ✓ | 0.50 | no_comparable_gt | — | — | — | — | — | — |
| 2310.06017 | ✓ | 0.55 | 99.1% | 0.934 | 0.975 | 0.798 | 0.995 | 32.1% | 46/113 |
| 2102.08764 | ✓ | 0.90 | 100.0% | 0.000 | 0.000 | 0.000 | 0.892 | 100.0% | 2/2 |
| 2308.14656 | ✓ | 0.70 | 100.0% | 0.214 | ∞ | 0.184 | 0.993 | 84.0% | 2/75 |
| 2207.03102 | ✓ | 0.90 | 100.0% | 0.000 | 0.000 | 0.000 | 0.360 | 100.0% | 2/2 |
| 1505.07455 | — | — | EXCLUDED | — | — | — | — | — | — |
| 2105.04603 | ✓ | 0.50 | 98.3% | 1.447 | 1.046 | 1.249 | 0.984 | 10.5% | 6/707 |
| 2303.11792 | ✓ | 0.80 | 90.0% | 0.141 | 0.128 | 0.144 | 0.748 | 100.0% | 2/20 |
| 1607.06083 | ✓ | 0.65 | 37.2% | 0.430 | 0.424 | 0.434 | 0.365 | 33.3% | 33/113 |
| 2108.04746 | ✓ | 0.55 | 97.9% | 0.448 | 0.350 | 0.555 | 0.997 | 38.6% | 35/283 |
| 2208.12670 | ✓ | 0.75 | 100.0% | 0.001 | ∞ | — | — | 100.0% | 54/1 |
| 1806.05120 | ✓ | 0.75 | 98.9% | 0.087 | 0.089 | 0.098 | 0.983 | 97.8% | 43/94 |
| 2101.01241 | ✓ | 0.50 | 100.0% | 0.031 | ∞ | — | — | 100.0% | 2/1 |
| 2404.14476 | ✓ | 0.80 | 96.1% | 0.136 | 0.047 | 0.086 | 0.190 | 95.9% | 37/51 |
| 2504.12377 | ✓ | 0.80 | 100.0% | 0.503 | 0.044 | 0.061 | 0.608 | 33.3% | 39/15 |
| 2408.15227 | ✓ | 0.75 | 100.0% | 0.166 | 0.191 | 0.179 | 0.905 | 99.1% | 3/230 |
| 2209.09917 | ✓ | 0.60 | 80.0% | 0.336 | 0.314 | 0.505 | 0.750 | 50.0% | 7/5 |
| 2406.00387 | ✓ | 0.85 | 99.1% | 0.477 | 0.347 | 0.088 | 0.991 | 38.3% | 101/108 |
| 1207.3275 | ✓ | 0.80 | 100.0% | 0.065 | 0.040 | 0.054 | 0.043 | 88.9% | 33/9 |
| 2205.01079 | ✓ | 0.55 | 64.3% | 0.381 | 0.388 | 0.300 | 0.774 | 44.4% | 4/14 |
| 2212.02403 | ✓ | 0.55 | 100.0% | 0.401 | 0.229 | 0.270 | 0.980 | 33.3% | 4/42 |
| 1903.12190 | ✓ | 0.50 | 66.7% | 0.624 | 0.657 | 0.638 | 0.667 | 0.0% | 14/3 |
| 2305.00890 | ✓ | 0.85 | 100.0% | 0.048 | 0.172 | 0.170 | 0.996 | 96.6% | 37/4991 |
| 1708.06367 | ✓ | 0.30 | convention_mismatch | — | — | — | — | — | — |
| 2312.13723 | — | — | EXCLUDED | — | — | — | — | — | — |
| 2410.10363 | ✓ | 0.50 | 33.3% | 0.587 | ∞ | ∞ | 0.000 | 0.0% | 3/288 |
| 1202.5851 | — | — | EXCLUDED | — | — | — | — | — | — |
| 2208.06519 | ✓ | 0.90 | 100.0% | 0.097 | ∞ | — | — | 100.0% | 1/1 |
| 2401.16747 | ✓ | 0.50 | convention_mismatch | — | — | — | — | — | — |
| 2401.18076 | ✓ | 0.40 | 100.0% | 1.906 | 2.244 | 2.010 | 0.972 | 0.0% | 7/29 |
| 2503.13653 | ✓ | 0.40 | 96.2% | 0.379 | 0.733 | 2.424 | 0.567 | 43.1% | 7/53 |
| 2308.06339 | ✓ | 0.30 | 96.1% | 0.234 | 0.220 | 0.225 | 0.997 | 60.3% | 6/76 |
| 2109.11734 | ✓ | 0.90 | 83.3% | 0.144 | 0.004 | 0.084 | 0.820 | 100.0% | 6/12 |
| 2308.09077 | ✓ | 0.70 | 83.3% | 0.182 | 0.261 | 0.194 | 0.923 | 100.0% | 2/54 |
| 2110.06096 | ✓ | 0.65 | 100.0% | 0.069 | 0.084 | 0.081 | 0.525 | 99.2% | 53/242 |
| 2205.03679 | ✓ | 0.60 | 100.0% | 0.389 | ∞ | 0.404 | 0.976 | 4.2% | 2/1525 |
| 2202.08858 | ✓ | 0.40 | 95.1% | 5.102 | 5.048 | 5.095 | 0.963 | 0.0% | 6/203 |
| 2503.14582 | ✓ | 0.70 | 100.0% | 0.349 | 0.373 | 0.387 | 0.997 | 40.5% | 43/196912 |
| 1207.2442 | ✓ | 0.65 | 98.0% | 14.412 | 14.291 | 14.072 | 0.782 | 0.0% | 36/50 |
| 1609.00667 | — | — | EXCLUDED | — | — | — | — | — | — |
| 2407.03828 | ✓ | 0.85 | 99.1% | 0.022 | 0.025 | 0.029 | 0.296 | 100.0% | 40/116 |
| 1810.04602 | ✓ | 0.45 | 96.4% | 0.371 | 0.359 | 0.395 | 0.912 | 41.5% | 5/55 |
| 2110.10262 | — | — | EXCLUDED | — | — | — | — | — | — |
| 2306.05934 | ✓ | 0.60 | 100.0% | 0.200 | 0.277 | 0.189 | 0.999 | 67.7% | 3/2636 |
| 2306.01048 | ✓ | 0.70 | 55.6% | 0.015 | 0.015 | 3.510 | 0.286 | 100.0% | 4/36 |
| 2008.08773 | ✓ | 0.50 | 97.6% | 0.688 | 0.576 | 0.564 | 0.930 | 3.8% | 5/543 |
| 2007.04990 | — | — | EXCLUDED | — | — | — | — | — | — |
| 2207.11968 | ✓ | 0.70 | 100.0% | 0.047 | 0.049 | 0.071 | 0.996 | 99.2% | 47/128 |
| 0807.2926 | ✓ | 0.50 | 16.7% | 0.026 | 0.045 | 0.028 | 0.798 | 100.0% | 2/18 |
| 1508.02463 | ✓ | 0.70 | 97.7% | 0.162 | 0.159 | 0.080 | 0.178 | 57.1% | 45/43 |
| 0809.4700 | ✓ | 0.70 | 62.9% | 0.009 | 0.052 | 0.015 | 0.150 | 100.0% | 2/35 |
| 2006.07055 | ✓ | 0.70 | 100.0% | 19.104 | 19.150 | 19.100 | 0.992 | 0.0% | 48/146 |
| 2004.02733 | ✓ | 0.65 | 100.0% | 0.034 | 0.034 | 0.035 | 0.941 | 100.0% | 32/33 |
| 2111.09892 | ✓ | 0.50 | 100.0% | 0.000 | ∞ | 0.000 | 0.793 | 100.0% | 2/2 |
| 1401.6460 | ✓ | 0.30 | 75.0% | 0.267 | 0.277 | 0.276 | 0.941 | 100.0% | 46/4 |
| 2204.01454 | ✓ | 0.60 | 97.6% | 0.470 | 0.162 | 0.428 | 0.988 | 43.9% | 34/42 |
| 2410.02218 | — | — | EXCLUDED | — | — | — | — | — | — |
| 1808.02340 | ✓ | 0.70 | 100.0% | 0.203 | 0.171 | 0.182 | 0.984 | 67.2% | 52/265 |
| 2311.16364 | ✓ | 0.85 | 100.0% | 0.471 | 0.516 | 0.511 | 0.703 | 32.2% | 92/121 |
| 1704.02297 | ✓ | 0.85 | 96.6% | 0.048 | 0.051 | 0.059 | 0.085 | 98.2% | 49/58 |
| 1707.07921 | ✓ | 0.80 | 96.7% | 0.899 | 0.944 | 0.967 | 0.435 | 0.0% | 36/30 |
| 1806.00310 | ✓ | 0.85 | 100.0% | 0.041 | 0.041 | ∞ | 0.000 | 100.0% | 1/8 |
| 2007.03694 | ✓ | 0.85 | 100.0% | 0.000 | 0.000 | 0.000 | 1.000 | 100.0% | 2/2 |
| 1911.11905 | ✓ | 0.50 | 100.0% | 0.030 | 0.030 | ∞ | 0.000 | 100.0% | 1/250 |
| 1902.04246 | ✓ | 0.70 | 91.8% | 0.074 | 0.406 | 0.088 | 0.779 | 98.2% | 2/61 |
| 1708.02111 | — | — | EXCLUDED | — | — | — | — | — | — |
| 2006.09721 | ✓ | 0.85 | 0.0% | ∞ | ∞ | ∞ | 0.000 | 0.0% | 99/148 |
| 1907.11485 | ✓ | 0.90 | 100.0% | 0.000 | 0.000 | 0.000 | 1.000 | 100.0% | 78/78 |
| 2112.12116 | ✓ | 0.50 | 0.0% | ∞ | ∞ | ∞ | 0.000 | 0.0% | 48/100 |
| 2006.12431 | ✓ | 0.50 | 75.6% | 0.121 | 0.125 | 0.113 | 0.798 | 100.0% | 10/90 |
| 2207.11330 | ✓ | 0.50 | 99.2% | 0.324 | 0.359 | 0.328 | 0.993 | 45.3% | 12/118 |
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
| 2306.08039 | ✓ | 0.65 | 94.0% | 0.188 | 0.518 | 0.383 | 0.940 | 70.4% | 6/1158 |
| 2102.01448 | ✓ | 0.75 | 100.0% | 0.045 | 0.051 | 0.065 | 0.882 | 98.6% | 52/70 |
| 2209.03289 | ✓ | 0.80 | 100.0% | 0.047 | 0.050 | 0.059 | 0.998 | 100.0% | 52/110 |
| 2209.13588 | ✓ | 0.55 | 99.6% | 0.509 | 0.988 | 0.809 | 0.998 | 31.0% | 6/230 |
| 1906.11844 | ✓ | 0.50 | convention_mismatch | — | — | — | — | — | — |
| hep-ph/0611223 | ✗ (AxionPhoton) | 0.45 | no_comparable_gt | — | — | — | — | — | — |
| 1810.12257 | ✓ | 0.70 | 100.0% | 0.508 | 0.410 | 0.521 | 0.997 | 28.2% | 4/3214 |
| 2102.06722 | ✓ | 0.70 | 98.7% | 0.297 | 0.200 | 0.312 | 0.991 | 50.5% | 3/391 |
| 2404.12517 | ✓ | 0.75 | 99.6% | 0.321 | 0.179 | 0.191 | 0.998 | 45.6% | 6/284 |
| 0910.5914 | ✓ | 0.60 | 100.0% | 0.228 | 0.228 | 0.238 | 0.088 | 90.0% | 50/27 |
| 1804.05750 | ✓ | 0.85 | 100.0% | 0.063 | 0.047 | 0.066 | 0.915 | 100.0% | 48/145 |
| 1910.08638 | ✓ | 0.85 | 100.0% | 0.069 | 0.063 | 0.066 | 0.303 | 100.0% | 44/82 |
| 2504.07279 | ✓ | 0.60 | 89.3% | 0.433 | 0.443 | 0.448 | 0.934 | 0.0% | 5/234 |
| 1911.05772 | ✓ | 0.60 | 100.0% | 0.331 | 0.252 | 0.513 | 0.992 | 40.9% | 6/22 |
| 1901.00920 | ✓ | 0.60 | 99.1% | 0.451 | 0.241 | 0.319 | 1.000 | 31.0% | 6/117 |
| 1004.1313 | ✓ | 0.60 | 63.2% | 0.130 | 0.089 | 0.036 | 0.131 | 80.6% | 9/228 |
| 2008.05355 | ✓ | 0.70 | 98.0% | 0.383 | 0.361 | 0.333 | 0.971 | 31.2% | 2/49 |
| 2302.10206 | ✓ | 0.70 | 85.7% | 0.714 | 0.478 | 1.449 | 0.113 | 25.0% | 44/14 |
| 2101.11290 | ✓ | 0.60 | 100.0% | 0.097 | 0.079 | 0.084 | 0.010 | 100.0% | 31/2 |
| 2002.08370 | ✓ | 0.85 | 94.4% | 0.155 | 0.127 | 0.438 | 0.755 | 67.6% | 165/36 |
| 2211.12699 | ✓ | 0.60 | 100.0% | 0.098 | 0.095 | 0.103 | 0.963 | 100.0% | 7/75 |
| 2108.03316 | ✓ | 0.85 | 100.0% | 0.098 | 0.108 | 0.083 | 0.950 | 99.7% | 13/321 |
| 1709.00009 | ✓ | 0.50 | 45.9% | 1.799 | 1.577 | 3.773 | 0.792 | 0.0% | 2/37 |
| 2007.13071 | ✓ | 0.60 | 99.4% | 0.245 | 0.125 | 0.266 | 0.968 | 56.0% | 4/318 |
| 2009.09059 | ✓ | 0.75 | 47.4% | 0.574 | 0.647 | 0.604 | 0.161 | 0.0% | 42/114 |
| 2112.03439 | — | — | EXCLUDED | — | — | — | — | — | — |
| 2001.05102 | ✓ | 0.90 | 97.4% | 0.052 | 0.049 | 0.051 | 0.997 | 100.0% | 53/77 |
| 2008.10141 | ✓ | 0.75 | 98.6% | 0.020 | 0.014 | 0.021 | 0.966 | 100.0% | 3/220 |
| 2012.10764 | ✓ | 0.65 | 100.0% | 0.469 | 0.385 | 0.209 | 0.996 | 36.0% | 6/125 |
| 2206.08845 | ✓ | 0.80 | 99.1% | 0.107 | 0.092 | 0.112 | 0.953 | 99.9% | 6/2959 |
| 2207.13597 | ✓ | 0.70 | 93.9% | 0.020 | 0.021 | 0.021 | 0.969 | 100.0% | 3/49 |
| 2210.10961 | ✓ | 0.85 | 94.8% | 0.009 | 0.026 | 0.014 | 0.964 | 100.0% | 2/251 |
| 2312.11003 | ✓ | 0.80 | 91.2% | 0.015 | 0.018 | 0.018 | 0.945 | 100.0% | 2/181 |
| 2403.13390 | ✓ | 0.80 | 98.6% | 0.012 | 0.008 | 0.017 | 0.982 | 100.0% | 2/70 |
| 2402.12892 | ✓ | 0.55 | 100.0% | 0.066 | 0.079 | 0.170 | 0.966 | 81.5% | 5/362 |
| 2211.02902 | ✓ | 0.60 | 100.0% | 0.083 | 0.072 | 0.094 | 0.988 | 99.4% | 7/169 |
| 1705.02290 | ✓ | 0.90 | 99.8% | 0.066 | 0.045 | 0.055 | 0.135 | 99.8% | 41/436 |
| hep-ex/0702006 | — | — | EXCLUDED | — | — | — | — | — | — |
| 1704.05189 | ✓ | 0.55 | 93.4% | 0.014 | 0.043 | 0.508 | 0.925 | 93.0% | 38/61 |
| 2411.13701 | ✓ | 0.60 | 92.9% | 0.968 | 0.981 | 0.985 | 0.972 | 0.0% | 37/170 |
| 2109.03261 | ✓ | 0.65 | 82.8% | 0.134 | 0.108 | 0.070 | 0.420 | 95.8% | 37/29 |
| 1304.0989 | ✓ | 0.75 | 79.3% | 0.103 | 0.090 | 0.021 | 0.265 | 100.0% | 5/29 |
| 1703.07354 | ✓ | 0.70 | 65.9% | 0.068 | 0.071 | 0.158 | 0.234 | 69.0% | 39/44 |
| 1907.05475 | ✓ | 0.85 | 88.2% | 0.031 | 0.022 | 0.027 | 0.494 | 100.0% | 34/17 |
| 2104.12772 | ✓ | 0.70 | 21.9% | 0.006 | 0.020 | 0.007 | 0.318 | 100.0% | 2/64 |
| 2407.10618 | ✓ | 0.60 | 100.0% | 1.039 | 0.720 | 0.835 | 0.992 | 13.9% | 53/2612 |
| 2303.03594 | ✓ | 0.75 | 25.8% | 0.459 | 0.352 | 0.450 | 0.385 | 8.7% | 2/89 |
| 2311.05476 | ✓ | 0.30 | convention_mismatch | — | — | — | — | — | — |
| 2201.09890 | ✓ | 0.70 | 89.9% | 0.088 | 0.133 | 0.361 | 0.520 | 85.5% | 37/199 |
| 1110.2895 | ✓ | 0.50 | 100.0% | 0.833 | 1.541 | 1.485 | 0.411 | 23.8% | 9/42 |
| 2412.02232 | ✓ | 0.85 | 91.1% | 0.104 | 0.113 | 0.162 | 0.913 | 78.8% | 46/124 |
| 2504.07559 | ✓ | 0.65 | 96.5% | 0.326 | 0.228 | 0.291 | 0.978 | 46.1% | 42/198 |
| 2404.17333 | ✓ | 0.92 | 96.0% | 0.194 | 0.123 | 0.231 | 0.191 | 62.5% | 6/25 |
| 2405.08059 | ✓ | 0.75 | 90.0% | 0.254 | 0.184 | 0.248 | 0.883 | 55.6% | 36/40 |
| 2211.03414 | ✓ | 0.70 | 94.5% | 0.077 | 0.078 | 0.116 | 0.974 | 92.2% | 38/109 |
| 1603.06978 | ✓ | 0.70 | 46.7% | 0.040 | 0.032 | 0.287 | 0.640 | 100.0% | 4/287 |
| 2305.10327 | ✓ | 0.60 | 100.0% | 0.293 | ∞ | 1.239 | 0.964 | 51.0% | 2/49 |
| 2305.01002 | ✓ | 0.70 | 97.4% | 0.107 | 0.083 | 0.906 | 0.930 | 100.0% | 33/38 |
| 2208.13794 | ✓ | 0.60 | 100.0% | 1.139 | 1.147 | 1.178 | 0.389 | 0.0% | 32/89 |
| 2501.17119 | ✓ | 0.75 | 98.4% | 0.033 | 0.032 | 0.032 | 0.993 | 100.0% | 56/799 |
| 1406.6053 | ✓ | 0.50 | 100.0% | 0.118 | 0.118 | 0.159 | 0.005 | 72.7% | 44/27 |
| 2110.14406 | ✓ | 0.80 | 100.0% | 0.000 | ∞ | — | — | 100.0% | 2/1 |
| 2203.04332 | ✓ | 0.85 | 89.9% | 0.007 | 0.009 | 0.012 | 0.332 | 100.0% | 48/148 |
| 1610.02580 | ✓ | 0.90 | 54.5% | 0.049 | 0.049 | 0.055 | 0.512 | 98.5% | 64/121 |
| 2008.01853 | ✓ | 0.80 | 46.8% | 0.132 | 1.126 | 0.732 | 0.191 | 94.2% | 4/111 |
| 2409.08998 | ✓ | 0.85 | 97.2% | 0.144 | 0.131 | 1.143 | 0.989 | 97.5% | 4/324 |
| 1311.3148 | ✓ | 0.80 | 59.1% | 0.027 | 0.120 | 0.030 | 0.778 | 100.0% | 2/22 |
| 2301.06560 | ✓ | 0.50 | 100.0% | 0.000 | 0.000 | ∞ | 0.000 | 100.0% | 1/97 |
| 2412.02543 | ✓ | 0.60 | 99.0% | 0.217 | 0.270 | 0.284 | 0.990 | 68.4% | 11/99 |
| 2209.06299 | — | — | EXCLUDED | — | — | — | — | — | — |
| 2310.15395 | ✓ | 0.70 | 66.8% | 0.122 | 0.046 | 0.141 | 0.661 | 89.7% | 2/262 |
| 2503.11753 | ✓ | 0.55 | 95.9% | 0.534 | 0.518 | 0.512 | 0.963 | 11.8% | 11/1844 |
| 1509.00476 | ✓ | 0.50 | 90.5% | 0.751 | 0.719 | 0.994 | 0.904 | 10.5% | 7/21 |
| 2307.01365 | ✓ | 0.80 | 57.4% | 0.126 | 0.249 | 0.113 | 0.564 | 98.1% | 3/94 |
| 2111.08025 | ✓ | 0.50 | 80.6% | 0.435 | 0.490 | 0.388 | 0.790 | 32.0% | 8/93 |
| 2412.03660 | ✓ | 0.55 | 67.0% | 0.534 | 0.599 | 0.616 | 0.661 | 26.0% | 8/115 |
| 2409.11777 | ✓ | 0.70 | 100.0% | 0.141 | 0.085 | 0.249 | 0.997 | 93.0% | 9/86 |
| 2401.07798 | ✓ | 0.60 | 92.1% | 0.068 | 0.088 | 0.340 | 0.918 | 94.3% | 5/38 |
| 1811.10997 | ✓ | 0.85 | 100.0% | 0.022 | 0.015 | 0.024 | 0.988 | 100.0% | 48/144 |
| 2203.04319 | ✓ | 0.85 | 87.9% | 0.008 | 0.033 | 0.038 | 0.941 | 91.4% | 38/132 |
| 2307.03878 | ✓ | 0.85 | no_comparable_gt | — | — | — | — | — | — |
| 2110.13636 | ✓ | 0.85 | 93.5% | 0.012 | 0.013 | 0.026 | 0.992 | 91.4% | 60/62 |
| 2008.09464 | ✓ | 0.85 | 96.0% | 0.023 | 0.023 | 0.040 | 0.992 | 97.9% | 73/50 |
| 2202.08274 | ✓ | 0.75 | 99.6% | 0.162 | 0.106 | 0.176 | 0.944 | 66.8% | 46/257 |
| 2203.12152 | ✓ | 0.85 | 98.4% | 0.036 | 0.032 | 0.137 | 0.980 | 92.6% | 50/123 |
| 2310.00904 | ✓ | 0.85 | 100.0% | 0.018 | 0.017 | 0.019 | 0.971 | 100.0% | 42/53 |
| 2407.18586 | ✓ | 0.85 | 100.0% | 0.038 | 0.038 | 0.041 | 0.993 | 97.0% | 53/265 |
| 1706.00209 | ✓ | 0.85 | 100.0% | 0.000 | ∞ | — | — | 100.0% | 2/1 |
| 1506.08082 | ✓ | 0.85 | 100.0% | 0.006 | 0.006 | ∞ | 0.000 | 100.0% | 1/12 |
| 2303.08410 | ✓ | 0.92 | 99.0% | 0.117 | 0.084 | 0.100 | 1.000 | 92.6% | 35/192 |
| 2403.02096 | ✓ | 0.85 | 100.0% | 0.130 | 0.135 | 0.099 | 0.998 | 68.6% | 10/838 |
| 2412.02229 | ✓ | 0.75 | 100.0% | 0.301 | 0.299 | 0.316 | 0.985 | 49.2% | 55/120 |
| 1510.08052 | ✓ | 0.85 | 96.6% | 0.033 | 0.036 | 0.038 | 0.065 | 100.0% | 33/88 |
| 2409.10514 | ✓ | 0.80 | 100.0% | 0.147 | 0.116 | 0.155 | 0.908 | 75.6% | 38/156 |
| 1903.03586 | ✓ | 0.60 | 100.0% | 0.449 | 0.416 | 0.364 | 0.134 | 42.9% | 45/7 |
| 1903.06547 | ✓ | 0.90 | 100.0% | 0.000 | ∞ | — | — | 100.0% | 2/1 |
| 2012.09498 | ✓ | 0.85 | 100.0% | 0.079 | ∞ | — | — | 100.0% | 2/1 |
| 2304.07505 | ✓ | 0.75 | 71.9% | 0.287 | 0.255 | 0.282 | 0.675 | 52.2% | 40/32 |
| 2402.19063 | ✓ | 0.75 | 100.0% | 0.202 | 0.166 | 0.182 | 0.999 | 72.5% | 57/149 |
| 2104.13798 | ✓ | 0.85 | 100.0% | 0.000 | 0.000 | 0.000 | 1.000 | 100.0% | 2/2 |
| 2403.07790 | ✓ | 0.75 | 99.8% | 0.145 | 0.312 | 0.152 | 0.992 | 85.0% | 3/420 |
| 2409.01805 | ✓ | 0.85 | 86.8% | 0.407 | 0.281 | 0.330 | 0.930 | 40.5% | 30/91 |
| 2003.03348 | ✓ | 0.85 | 99.6% | 0.025 | 0.030 | 0.046 | 0.991 | 97.4% | 48/857 |
| 2303.11395 | ✓ | 0.65 | 94.6% | 0.019 | 0.050 | 0.286 | 0.779 | 100.0% | 44/37 |
| 2304.01060 | ✓ | 0.75 | 98.0% | 0.050 | 0.034 | 0.582 | 0.948 | 82.0% | 36/51 |
| 2212.09764 | ✓ | 0.85 | 97.0% | 0.085 | 0.047 | 0.045 | 0.136 | 100.0% | 35/33 |
| 2405.19393 | ✓ | 0.55 | 96.4% | 0.294 | 0.292 | 0.481 | 0.876 | 52.8% | 6/55 |
| 2306.11575 | ✓ | 0.60 | 100.0% | 0.218 | 0.195 | 0.143 | 0.997 | 74.5% | 7/415 |
| 2006.06722 | ✓ | 0.85 | 98.7% | 0.048 | 0.167 | 0.110 | 0.109 | 100.0% | 37/76 |
| 2203.16567 | ✓ | 0.85 | 100.0% | 0.083 | 0.062 | 0.064 | 0.993 | 100.0% | 9/115 |
| 2008.13662 | ✓ | 0.60 | 98.4% | 0.166 | 0.090 | 0.175 | 0.986 | 77.8% | 9/64 |
| 2205.05700 | ✓ | 0.55 | 100.0% | 0.613 | 0.361 | 0.612 | 0.846 | 35.2% | 7/122 |
| 2303.06968 | ✓ | 0.70 | 86.8% | 0.150 | 0.139 | 0.150 | 0.910 | 78.1% | 44/174 |
| 1501.01639 | ✓ | 0.50 | 50.0% | 0.003 | 0.003 | 0.003 | 0.612 | 100.0% | 7/2 |
| 2307.11216 | ✓ | 0.75 | 95.0% | 0.116 | 0.114 | 0.122 | 0.905 | 100.0% | 54/60 |
| 2112.09620 | ✓ | 0.65 | 100.0% | 0.149 | 0.032 | 0.135 | 0.924 | 80.7% | 7/83 |
| 2408.16045 | ✓ | 0.85 | 99.2% | 0.096 | 0.124 | 0.146 | 0.976 | 80.5% | 8801/124 |
| 2205.05574 | ✓ | 0.85 | 98.8% | 0.022 | 0.009 | 0.027 | 0.985 | 100.0% | 49/508 |
| 2307.07403 | ✓ | 0.65 | 95.3% | 0.456 | 0.548 | 0.481 | 0.970 | 30.6% | 7/555 |
| astro-ph/0611502 | ✓ | 0.30 | 97.8% | 0.157 | 0.181 | 0.150 | 0.992 | 98.9% | 7/91 |
| 2301.06778 | ✓ | 0.75 | 98.8% | 0.198 | 0.399 | 0.179 | 0.948 | 89.4% | 2/86 |
| 1912.07751 | — | — | EXCLUDED | — | — | — | — | — | — |
| 2402.07976 | ✓ | 0.65 | 97.6% | 1.009 | 0.720 | 0.860 | 0.940 | 14.3% | 2/10796 |
| 2102.00379 | ✓ | 0.55 | 88.5% | 0.394 | 0.356 | 1.688 | 0.997 | 34.8% | 37/26 |
| 2102.02207 | — | — | EXCLUDED | — | — | — | — | — | — |
| 2503.04726 | ✓ | 0.50 | 94.5% | 0.200 | 0.201 | 0.185 | 0.917 | 78.0% | 5/16611 |
| 2008.03305 | ✓ | 0.85 | 99.1% | 0.002 | 0.043 | 0.035 | 0.190 | 100.0% | 36/115 |
| 2412.09595 | — | — | EXCLUDED | — | — | — | — | — | — |
| 2008.02209 | ✓ | 0.65 | 82.6% | 0.050 | 0.048 | 0.048 | 0.839 | 100.0% | 13/69 |
| 2407.16628 | ✓ | 0.70 | 100.0% | 1.930 | 1.900 | 1.834 | 0.987 | 0.0% | 50/101 |
| 0801.1527 | ✓ | 0.80 | 93.1% | 0.081 | 0.080 | 0.124 | 0.961 | 94.5% | 44/175 |
| 2002.05165 | ✓ | 0.85 | 81.4% | 0.180 | 0.181 | 0.205 | 0.482 | 91.0% | 359/671 |
| 2409.12940 | ✓ | 0.70 | 90.8% | 0.021 | 0.051 | 0.121 | 0.978 | 94.9% | 55/174 |
| 2409.12115 | ✓ | 0.75 | 98.8% | 0.165 | 0.180 | 0.241 | 0.974 | 87.3% | 41/80 |
| 1201.5902 | ✓ | 0.60 | no_comparable_gt | — | — | — | — | — | — |
| 1911.05086 | ✓ | 0.90 | 100.0% | 0.000 | 0.000 | 0.000 | 1.000 | 100.0% | 401/401 |
| 2003.13698 | ✓ | 0.90 | 100.0% | 0.000 | 0.000 | 0.000 | 1.000 | 100.0% | 393/393 |
| 0810.5501 | ✓ | 0.80 | 95.5% | 0.042 | 0.064 | 0.050 | 0.995 | 100.0% | 44/112 |
| 2002.01796 | ✓ | 0.75 | no_comparable_gt | — | — | — | — | — | — |
| 1907.12628 | ✓ | 0.45 | 100.0% | 1.831 | 1.904 | 1.376 | 0.970 | 20.5% | 9/73 |
| 1906.08814 | ✓ | 0.85 | 100.0% | 0.000 | 0.114 | 0.180 | 0.708 | 100.0% | 32/2 |
| 2101.02805 | — | — | EXCLUDED | — | — | — | — | — | — |
| 2405.20444 | ✓ | 0.60 | 99.6% | 0.409 | 0.825 | 0.369 | 0.986 | 36.0% | 2/493 |
| 2301.11512 | ✓ | 0.85 | 100.0% | 0.061 | 0.060 | 0.075 | 0.828 | 56.2% | 21/16 |
| 2207.05767 | — | — | EXCLUDED | — | — | — | — | — | — |
| 2003.13144 | ✓ | 0.90 | 86.4% | 0.053 | 0.057 | 0.087 | 0.802 | 89.5% | 39/22 |
| 2310.13891 | ✓ | 0.80 | 100.0% | 0.026 | ∞ | 0.026 | 0.925 | 100.0% | 2/87 |
| 2304.12907 | ✓ | 0.50 | convention_mismatch | — | — | — | — | — | — |
| 2211.00022 | ✓ | 0.60 | 28.7% | 0.959 | 0.823 | 0.820 | 0.281 | 26.8% | 3/143 |
| 2406.19445 | ✓ | 0.55 | 50.5% | 0.502 | 0.506 | 0.447 | 0.235 | 18.0% | 6/99 |
| 2402.17140 | — | — | EXCLUDED | — | — | — | — | — | — |
| 2110.01582 | ✓ | 0.60 | 46.2% | 0.092 | 0.143 | 0.170 | 0.787 | 91.7% | 3/26 |
| 2301.03622 | ✓ | 0.80 | 95.3% | 0.293 | 0.257 | 0.304 | 0.960 | 51.0% | 42/401 |
| 1007.3766 | ✓ | 0.70 | 22.5% | 0.645 | 0.513 | 0.647 | 0.155 | 0.0% | 3/102 |
| 1410.5244 | ✓ | 0.60 | 95.2% | 0.482 | 0.097 | 0.128 | 0.933 | 30.0% | 38/21 |
| 2410.02858 | ✓ | 0.50 | 50.0% | 0.120 | 0.131 | 0.150 | 0.789 | 66.7% | 4/6 |
| 2110.10497 | ✓ | 0.70 | 100.0% | 0.113 | 0.113 | ∞ | 0.000 | 100.0% | 1/72 |
| 2012.05427 | ✓ | 0.50 | convention_mismatch | — | — | — | — | — | — |
| 2204.03818 | ✓ | 0.85 | 98.2% | 0.056 | 0.062 | 0.098 | 0.982 | 95.0% | 51/3689 |
| 2405.12285 | ✓ | 0.60 | 91.2% | 0.386 | 0.352 | 0.359 | 0.850 | 33.7% | 7/91 |
| 2406.02546 | ✓ | 0.65 | 95.5% | 3.275 | 3.490 | 3.187 | 0.902 | 0.0% | 6/22 |
| 2209.03419 | ✓ | 0.60 | 98.2% | 0.182 | 0.257 | 0.174 | 0.993 | 82.8% | 2/325 |
| 2212.01971 | ✓ | 0.60 | 97.7% | 0.199 | 0.194 | 0.167 | 0.976 | 75.8% | 3/131 |
| 2305.09711 | ✓ | 0.75 | 85.7% | 0.269 | 0.386 | 0.264 | 0.840 | 63.5% | 2/57500 |
| 1502.04490 | ✓ | 0.85 | 74.0% | 0.177 | 0.196 | 0.171 | 0.679 | 100.0% | 355/123 |
| 1905.05579 | ✓ | 0.75 | 98.1% | 0.706 | 0.844 | 0.752 | 0.950 | 20.6% | 3/104 |
| 1301.6557 | ✓ | 0.85 | 92.7% | 0.160 | 0.141 | 0.146 | 0.954 | 66.7% | 49/123 |
| 2208.03183 | — | — | EXCLUDED | — | — | — | — | — | — |
| 2008.12231 | ✓ | 0.85 | 100.0% | 0.000 | ∞ | — | — | 100.0% | 3/1 |
| 2308.08337 | ✓ | 0.90 | 100.0% | 0.000 | ∞ | — | — | 100.0% | 1/1 |
| 1008.3536 | ✓ | 0.60 | 57.0% | 0.367 | 0.298 | 0.485 | 0.409 | 40.4% | 11/100 |
| 2106.00022 | ✓ | 0.40 | 100.0% | 1.214 | 0.930 | 1.211 | 0.924 | 19.0% | 5/58 |
| 1804.10777 | ✓ | 0.80 | 66.7% | 0.045 | 0.042 | 0.028 | 0.993 | 100.0% | 40/3 |
| 1504.00118 | ✓ | 0.75 | 66.7% | 0.147 | 0.055 | 0.118 | 0.766 | 75.0% | 3/12 |
| 2006.02828 | ✓ | 0.80 | 100.0% | 0.358 | ∞ | 0.336 | 0.952 | 33.3% | 2/6 |
| 1907.12449 | ✓ | 0.60 | 31.0% | 0.465 | 0.306 | 0.421 | 0.308 | 22.7% | 8/555 |
| 1903.05101 | ✓ | 0.45 | 100.0% | 0.160 | 0.138 | 0.157 | 0.675 | 96.2% | 7/53 |
| 2006.13929 | ✓ | 0.55 | 99.0% | 1.574 | 1.712 | 1.688 | 0.908 | 0.0% | 9/98 |
| 1807.04512 | ✓ | 0.50 | 86.1% | 1.192 | 1.409 | 1.849 | 0.799 | 12.9% | 40/36 |
| hep-ph/0307284 | ✓ | 0.30 | no_comparable_gt | — | — | — | — | — | — |
| 2103.03783 | ✓ | 0.55 | 100.0% | 0.388 | 0.376 | 0.414 | 0.980 | 26.1% | 32/69 |
| 2205.06817 | — | — | EXCLUDED | — | — | — | — | — | — |
| 2306.16219 | ✓ | 0.60 | 100.0% | 1.251 | 1.169 | 1.206 | 0.996 | 0.0% | 49/102 |
| 2303.00778 | ✓ | 0.50 | convention_mismatch | — | — | — | — | — | — |
| 2212.05721 | ✓ | 0.75 | 100.0% | 0.058 | 0.065 | 0.059 | 0.995 | 100.0% | 37/333 |
| 2005.14694 | — | — | EXCLUDED | — | — | — | — | — | — |
| 1503.06886 | ✓ | 0.60 | 100.0% | 0.166 | 0.169 | 0.231 | 0.990 | 83.2% | 11/1006 |
| 1902.02788 | ✓ | 0.60 | 98.5% | 0.298 | 0.294 | 0.422 | 0.553 | 58.6% | 45/130 |
| 2301.03433 | ✓ | 0.60 | 100.0% | 0.310 | 0.289 | 0.325 | 0.862 | 44.8% | 11/172 |
| 2302.04565 | ✗ (ScalarNucleon) | 0.50 | no_comparable_gt | — | — | — | — | — | — |
| 1604.08514 | ✓ | 0.50 | 97.6% | 0.098 | 0.074 | 0.263 | 0.943 | 91.1% | 7/505 |
| quant-ph/0106045 | ✓ | 0.60 | no_comparable_gt | — | — | — | — | — | — |
| 2109.08822 | ✓ | 0.85 | 100.0% | 0.301 | 0.317 | 0.369 | 0.980 | 50.0% | 39/32 |
| 2105.13085 | ✗ (DarkPhoton) | 0.30 | no_comparable_gt | — | — | — | — | — | — |
| 2301.08736 | ✗ (DarkPhoton) | 0.55 | no_comparable_gt | — | — | — | — | — | — |
| 2403.02381 | ✓ | 0.70 | 66.6% | 0.112 | 0.641 | 0.537 | 0.333 | 59.7% | 45/1001 |
| 2409.03814 | ✓ | 0.75 | 51.6% | 0.280 | 0.199 | 0.302 | 0.508 | 51.6% | 48/308 |
| 2112.07687 | ✗ (DarkPhoton) | 0.30 | no_comparable_gt | — | — | — | — | — | — |
| 2302.00685 | ✓ | 0.70 | 100.0% | 1.111 | 2.549 | 2.536 | 0.402 | 36.4% | 35/11 |
| 2011.11646 | ✓ | 0.30 | 98.0% | 0.467 | 0.427 | 0.635 | 0.748 | 22.9% | 39/49 |
| 2406.10337 | ✓ | 0.30 | 0.0% | ∞ | ∞ | ∞ | 0.000 | 0.0% | 2/51 |
| 2011.08693 | — | — | EXCLUDED | — | — | — | — | — | — |
| 2012.12790 | ✓ | 0.40 | 100.0% | 11.422 | 10.779 | 11.200 | 0.752 | 0.0% | 6/209 |
| 2412.03655 | ✓ | 0.30 | 94.7% | 0.230 | 0.259 | 0.266 | 0.903 | 72.3% | 37/545 |
| 2105.13963 | ✓ | 0.75 | 95.0% | 11.118 | 11.182 | 11.565 | 0.533 | 0.0% | 35/20 |
| 2404.00616 | — | — | EXCLUDED | — | — | — | — | — | — |
| 2412.20932 | ✓ | 0.30 | 50.0% | 0.001 | 0.001 | 0.002 | 0.996 | 100.0% | 33/2 |
| 2408.07740 | ✓ | 0.65 | 16.7% | 0.918 | 1.119 | 0.942 | 0.051 | 0.0% | 34/18 |
| 2410.21590 | ✓ | 0.50 | 76.5% | 10.547 | 6.018 | 4.505 | 0.771 | 0.0% | 5/34 |
| 2205.01637 | ✓ | 0.80 | no_comparable_gt | — | — | — | — | — | — |
| 1708.08464 | ✓ | 0.25 | no_extracted_points | — | — | — | — | — | — |
| 2303.09865 | ✓ | 0.60 | 100.0% | 0.005 | 0.005 | 0.005 | 0.991 | 100.0% | 35/2 |
| 2211.02661 | ✓ | 0.85 | 0.0% | ∞ | ∞ | ∞ | 0.000 | 0.0% | 36/167 |
| 2301.10784 | ✓ | 0.50 | 100.0% | 10.638 | 10.644 | 10.714 | 0.946 | 0.0% | 37/107 |
| 1003.0964 | — | — | EXCLUDED | — | — | — | — | — | — |
| 2312.11608 | — | — | EXCLUDED | — | — | — | — | — | — |

## Breakdown by Extraction Source

Median residual is over papers with mass-range overlap; zero-overlap papers are listed separately.

| Source | Papers | Compared | Zero-overlap | Med. Resid. | ≤0.3 dex |
|--------|--------|----------|--------------|-------------|----------|
| table | 4 | 4 | 0 | 0.175 dex | 65.3% |
| figure_vision | 130 | 118 | 2 | 0.129 dex | 66.0% |
| text | 141 | 130 | 1 | 0.182 dex | 63.6% |

## Breakdown by Difficulty

> Difficulty is a placeholder label for the repo-sourced pool (nearly all `medium`); this table is informational only.

| Difficulty | Papers | Coupling Acc. | Med. Resid. | ≤0.3 dex |
|------------|--------|---------------|-------------|----------|
| easy | 11 | 100.0% | 0.045 dex | 71.2% |
| medium | 251 | 98.0% | 0.155 dex | 65.9% |
| hard | 29 | 100.0% | 0.214 dex | 59.1% |

## Confidence Calibration

- "Accurate" = median interpolation residual < **0.32 dex** AND interpolation coverage ≥ 50%.
- The **0.32 dex** threshold is the run-to-run LLM extraction *noise floor* (90th-pct per-paper median-residual std across repeated extractions, PR #545) — the binding floor. It is **not** the upstream digitization floor, which is only ~0.034 dex for table/text-sourced papers (PR #558). So a residual gap here is **real extractor overconfidence, not a yardstick artifact**.

### Binned accuracy (pass/fail)

| Bin | N | Mean Conf. | Actual Acc. | Gap |
|-----|---|------------|-------------|-----|
| [0.3–0.5) | 43 | 44.3% | 41.9% | +0.02 |
| [0.6–0.6) | 57 | 58.4% | 38.6% | +0.20 |
| [0.7–0.7) | 49 | 68.4% | 57.1% | +0.11 |
| [0.8–0.8) | 50 | 77.3% | 80.0% | -0.03 |
| [0.8–0.9) | 66 | 86.3% | 92.4% | -0.06 |

> **Interpretation**: Gap > 0 means the pipeline is overconfident; Gap < 0 means underconfident.

### Continuous view: residual distribution per bin

Median (and IQR) of each bin's per-paper median residual, over papers with a finite residual (zero mass-overlap papers excluded from the distribution but still counted in N). If confidence tracked accuracy, the median residual would fall as confidence rises.

| Bin | N | N finite | Median resid. (dex) | IQR (dex) |
|-----|---|----------|---------------------|-----------|
| [0.3–0.5) | 43 | 41 | 0.37 | 0.12–1.21 |
| [0.6–0.6) | 57 | 57 | 0.39 | 0.20–0.53 |
| [0.7–0.7) | 49 | 49 | 0.16 | 0.07–0.51 |
| [0.8–0.8) | 50 | 50 | 0.14 | 0.05–0.28 |
| [0.8–0.9) | 66 | 64 | 0.05 | 0.01–0.10 |

### Continuous view: empirical P(residual < τ) per bin

Fraction of papers in each bin whose median residual is below τ dex (τ = 0.32 is the noise floor used above). A well-calibrated, accurate extractor would show these probabilities rising with confidence.

| Bin | N | P(<0.10) | P(<0.32) | P(<0.50) | P(<1.00) |
|-----|---|----|----|----|----|
| [0.3–0.5) | 43 | 18.6% | 44.2% | 55.8% | 67.4% |
| [0.6–0.6) | 57 | 14.0% | 40.4% | 70.2% | 87.7% |
| [0.7–0.7) | 49 | 30.6% | 61.2% | 73.5% | 81.6% |
| [0.8–0.8) | 50 | 34.0% | 82.0% | 88.0% | 96.0% |
| [0.8–0.9) | 66 | 72.7% | 92.4% | 97.0% | 97.0% |

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
