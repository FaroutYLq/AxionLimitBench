# AutoAxionLimits Extraction Pipeline — Evaluation Report

## Summary

- **Papers evaluated**: 329
- **Papers with curve comparison**: 242

## Curve-Comparison Coverage

A curve is scored only against a ground-truth curve of the **same coupling**. Papers whose extracted coupling has no matching GT curve are not comparable and are excluded from residual statistics (this is not an extraction failure).

| Status | Papers | Meaning |
|--------|--------|---------|
| compared | 242 | scored against a same-coupling GT curve |
| no_comparable_gt | 8 | extracted coupling has no GT curve in the pool (usually a coupling misclassification) |
| gt_unusable | 1 | GT curve has <2 usable points after boundary filtering |
| no_extracted_points | 4 | pipeline returned no data points |
| no_prediction | 36 | pipeline returned no coupling type |
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
| coupling_type | 85.6% | 291 |
| is_new_limit | 78.1% | 32 |
| is_projection | 100.0% | 32 |
| data_source | 53.1% | 32 |

> **Label provenance**: `is_new_limit`, `is_projection`, and `data_source` are scored against an **independent LLM labeler** (`evaluation/label_ground_truth.py`, model `claude-opus-4-5`) whose sole task is to classify paper properties — a distinct model and prompt from the extractor it grades, so this is a fair cross-model test, not self-agreement. These are **not human gold labels**. A human audit of 15 labeled papers found per-field labeler↔human agreement: is_new_limit 15/15, is_projection 15/15, data_source 14/15 (difficulty is derived mechanically from data_source + point count, not labeled).

### Coupling Type Misclassifications

| arXiv ID | Predicted | Expected |
|----------|-----------|----------|
| 2209.06216 | None | ['AxionElectron', 'AxionPhoton'] |
| 1905.13650 | None | ['AxionNeutron'] |
| 2302.09096 | None | ['MonopoleDipole'] |
| 1611.05852 | None | ['DarkPhoton', 'ScalarElectron', 'ScalarNucleon', 'VectorBL'] |
| 2111.06883 | None | ['ScalarBaryon', 'ScalarElectron', 'ScalarNucleon', 'ScalarPhoton'] |
| 2009.04517 | None | ['AxionNeutron', 'AxionProton', 'ScalarNucleon'] |
| 2205.03617 | None | ['DarkPhoton', 'VectorBL'] |
| 2105.04603 | None | ['AxionNeutron', 'AxionProton'] |
| 1607.06083 | None | ['AxionPhoton'] |
| 2108.04746 | None | ['ScalarElectron', 'ScalarPhoton'] |
| 1903.12190 | None | ['DarkPhoton'] |
| 2410.10363 | None | ['AxionPhoton'] |
| 1207.2442 | None | ['VectorBL'] |
| 2112.12116 | None | ['AxionElectron', 'DarkPhoton'] |
| 2402.00741 | None | ['AxionMass'] |
| 1906.11844 | AxionProton | ['AxionNeutron'] |
| hep-ph/0611223 | AxionPhoton | ['AxionNeutron', 'AxionProton'] |
| 2002.08370 | None | ['AxionPhoton'] |
| 1709.00009 | None | ['AxionPhoton'] |
| 1704.05189 | None | ['AxionPhoton'] |
| 1110.2895 | None | ['AxionPhoton'] |
| 2405.08059 | None | ['AxionPhoton'] |
| 2503.04726 | None | ['AxionPhoton'] |
| 0801.1527 | None | ['DarkPhoton'] |
| 1201.5902 | None | ['AxionPhoton', 'DarkPhoton'] |
| 1911.05086 | None | ['DarkPhoton'] |
| 2301.03622 | AxionPhoton | ['DarkPhoton'] |
| 2212.01971 | AxionPhoton | ['DarkPhoton'] |
| 1807.04512 | None | ['ScalarElectron', 'ScalarPhoton'] |
| hep-ph/0307284 | None | ['ScalarBaryon', 'ScalarElectron', 'ScalarNucleon', 'ScalarPhoton'] |
| 2306.16219 | None | ['ScalarElectron'] |
| 2303.00778 | None | ['ScalarBaryon', 'ScalarElectron', 'ScalarNucleon'] |
| 1902.02788 | None | ['ScalarPhoton'] |
| 2302.04565 | None | ['ScalarPhoton'] |
| quant-ph/0106045 | None | ['ScalarNucleon', 'VectorBL'] |
| 2105.13085 | DarkPhoton | ['VectorBL'] |
| 2301.08736 | None | ['VectorBL'] |
| 2403.02381 | None | ['VectorBL'] |
| 2112.07687 | DarkPhoton | ['VectorBL'] |
| 2011.11646 | None | ['AxionMass'] |
| 2408.07740 | None | ['AxionMass'] |
| 1708.08464 | None | ['AxionMass'] |

### Coupling-Type Confusion Matrix (multi-type-aware)

Rows = authoritative GT type, columns = predicted type. A prediction is correct iff it is in ANY of the paper's GT types (diagonal). Off-diagonal cells are the confusable clusters. Graded 255, correct 249 (97.6%), skipped 74 (no prediction / no GT type).

| GT ⟍ Pred | AxionEDM | AxionElectron | AxionMass | AxionNeutron | AxionPhoton | AxionProton | DarkPhoton | MonopoleDipole | ScalarBaryon | ScalarElectron | ScalarNucleon | ScalarPhoton | VectorBL |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| AxionEDM | **4** |  |  |  |  |  |  |  |  |  |  |  |  |
| AxionElectron |  | **15** |  |  |  |  |  |  |  |  |  |  |  |
| AxionMass |  |  | **12** |  |  |  |  |  |  |  |  |  |  |
| AxionNeutron |  |  |  | **10** | 1 | 1 |  |  |  |  |  |  |  |
| AxionPhoton |  |  |  |  | **134** |  |  |  |  |  |  |  |  |
| AxionProton |  |  |  |  | 1 | **4** |  |  |  |  |  |  |  |
| DarkPhoton |  |  |  |  | 2 |  | **50** |  |  |  |  |  |  |
| MonopoleDipole |  |  |  |  |  |  |  | **2** |  |  |  |  |  |
| ScalarBaryon |  |  |  |  |  |  |  |  | **1** |  |  |  |  |
| ScalarElectron |  |  |  |  |  |  |  |  |  | **3** |  |  |  |
| ScalarNucleon |  |  |  |  |  |  |  |  |  |  | **2** |  |  |
| ScalarPhoton |  |  |  |  |  |  |  |  |  |  |  | **8** |  |
| VectorBL |  |  |  |  |  |  | 2 |  |  |  |  |  | **4** |

Off-diagonal confusions (GT → predicted, richest first):

- DarkPhoton → AxionPhoton: 2
- VectorBL → DarkPhoton: 2
- AxionNeutron → AxionPhoton: 1
- AxionNeutron → AxionProton: 1
- AxionProton → AxionPhoton: 1

## Extraction Quality — Interpolation Metric (primary)

Build log-log interpolation from extracted points, evaluate at ground-truth masses.

- **Papers compared**: 242 (218 with mass-range overlap, 24 with zero overlap)

**Coupling-value accuracy** (papers with mass-range overlap):
- **Median residual across papers**: 0.376 dex (IQR 0.131–1.038)
- **Mean residual across papers** (outlier-sensitive): 1.173 dex
- **Mean fraction within 0.3 dex (factor 2; the leaderboard headline is 10%, results/leaderboard.py)**: 45.2%
- **Mean fraction within 0.5 dex (factor 3)**: 56.5%

**Mass-range coverage** (a separate failure mode):
- **Mean interpolation coverage**: 74.2%
- **Zero-overlap papers**: 24/242 (9.9%) — extracted masses miss the GT range entirely (usually 1–2 extracted points or the wrong mass window)

**Reverse pass** (GT interpolated onto the *extracted* masses):
- Mirrors the forward pass. A large forward-vs-reverse gap, or a reverse coverage well below the forward coverage, flags an extraction whose mass *extent* or shape disagrees with the GT (e.g. running past the GT range).
- **Median reverse residual across papers**: 0.390 dex (forward: 0.376 dex)
- **Mean reverse interpolation coverage**: 73.4% (forward: 74.2%)

## Residual by Coupling Type — Micro vs Macro Average (issue #543)

The compared-paper pool is dominated by one coupling type (AxionPhoton), so the per-paper **micro-average** headline is largely that one type's number. The **macro-average** weights each coupling type equally (mean of the per-type medians), exposing how the pipeline does across the *range* of couplings rather than on the most common one.

- **Micro-average median residual** (per paper, 218 papers): 0.376 dex
- **Macro-average median residual** (equal weight per type, 13 types): 2.603 dex
- **Macro − micro gap**: +2.226 dex (macro is worse; a positive gap means the rarer couplings are harder than the AxionPhoton-dominated micro-average implies)

Per-type medians carry a bootstrap 95% CI (1000 resamples). Rows with **N < 5** are flagged small-sample — their median and CI are unstable and should not be read as a reliable per-type score.

| Coupling Type | N | Median Resid. (dex) | 95% CI (dex) | Flag |
|---------------|---|---------------------|--------------|------|
| AxionPhoton | 112 | 0.260 | [0.221, 0.346] |  |
| DarkPhoton | 46 | 0.367 | [0.206, 0.467] |  |
| AxionElectron | 13 | 0.360 | [0.046, 1.093] |  |
| AxionMass | 11 | 1.386 | [0.704, 4.195] |  |
| AxionNeutron | 9 | 0.973 | [0.177, 2.475] |  |
| ScalarPhoton | 8 | 0.749 | [0.549, 1.802] |  |
| AxionEDM | 4 | 2.989 | [0.005, 12.253] | ⚠ small-sample (N<5) |
| VectorBL | 4 | 0.787 | [0.341, 1.784] | ⚠ small-sample (N<5) |
| AxionProton | 3 | 0.227 | [0.038, 0.274] | ⚠ small-sample (N<5) |
| ScalarElectron | 3 | 0.947 | [0.888, 7.919] | ⚠ small-sample (N<5) |
| MonopoleDipole | 2 | 0.356 | [0.245, 0.467] | ⚠ small-sample (N<5) |
| ScalarNucleon | 2 | 12.070 | [3.466, 20.674] | ⚠ small-sample (N<5) |
| ScalarBaryon | 1 | 12.361 | [12.361, 12.361] | ⚠ small-sample (N<5) |

## Shape & Mass-Range Agreement — Symmetric Metrics (complementary)

These are symmetric, 2-D complements to the (asymmetric, vertical-only) interpolation residual. **Area-between-curves** integrates |Δ log10 coupling| over the overlapping log-mass range and normalises by the overlap width (a single shape+offset number, in dex; a pure mass shift inflates it even when the vertical residual looks fine). **Mass-range Jaccard** is the Jaccard index of the extracted vs GT log-mass intervals (1.0 = identical extent; small = over-/under-claimed mass range), reported separately from interpolation coverage.

- **Papers scored**: 233 (206 with mass overlap for area)
- **Median area-between-curves**: 0.463 dex (mean 1.269 dex)
- **Median mass-range Jaccard**: 0.667 (mean 0.574)

## Per-Paper Results

| arXiv ID | Coupling | Conf. | Interp. Cov. | Med. Resid. | Rev. Resid. | Area (dex) | Mass Jaccard | ≤0.3 dex | Points |
|----------|----------|-------|--------------|-------------|-------------|------------|--------------|----------|--------|
| 2208.07293 | ✓ | 0.90 | 100.0% | 0.064 | 0.064 | 0.064 | 0.052 | 100.0% | 2/2 |
| 2212.04413 | ✓ | 0.70 | 62.9% | 0.714 | 0.718 | 0.718 | 0.652 | 0.0% | 53/97 |
| 2410.19902 | ✓ | 0.75 | 100.0% | 4.195 | 4.195 | 4.195 | 0.234 | 0.0% | 35/2 |
| 1907.03767 | ✓ | 0.65 | 76.4% | 0.973 | 0.893 | 1.051 | 0.402 | 20.1% | 16/182 |
| 2209.06216 | ✗ (None) | 0.00 | no_prediction | — | — | — | — | — | — |
| 2005.14184 | ✓ | 0.75 | 0.0% | ∞ | ∞ | ∞ | 0.000 | 0.0% | 131/891 |
| 2504.00720 | ✓ | 0.75 | 97.1% | 3.546 | 3.862 | 3.524 | 0.848 | 1.5% | 35/70 |
| 2408.02668 | ✓ | 0.80 | 86.9% | 0.930 | 0.915 | 1.371 | 0.653 | 18.4% | 47/413 |
| 1905.13650 | ✗ (None) | 0.00 | no_prediction | — | — | — | — | — | — |
| 2110.03679 | ✓ | 0.85 | 99.2% | 0.036 | 0.012 | 0.133 | 0.244 | 75.0% | 15/129 |
| 2303.07370 | ✓ | 0.70 | 100.0% | 2.368 | 2.633 | 2.019 | 0.900 | 8.4% | 24/107 |
| 2309.16600 | ✓ | 0.80 | 87.8% | 0.177 | 0.185 | 0.244 | 0.892 | 81.8% | 32/188 |
| 2504.16044 | ✓ | 0.92 | gt_unusable | — | — | — | — | — | — |
| 2312.06746 | ✓ | 0.75 | 95.9% | 0.111 | 0.101 | 0.195 | 0.847 | 69.5% | 31/171 |
| 1310.8098 | ✓ | 0.65 | 21.5% | 2.907 | 2.917 | 2.680 | 0.053 | 0.0% | 269/135 |
| 2408.02368 | ✓ | 0.70 | 100.0% | 0.279 | 0.216 | 0.275 | 0.999 | 56.6% | 9/647 |
| 2011.07100 | ✓ | 0.70 | 60.8% | 0.467 | 0.455 | 0.449 | 0.152 | 14.6% | 104/79 |
| 2302.09096 | ✗ (None) | 0.00 | no_prediction | — | — | — | — | — | — |
| 1410.7267 | ✓ | 0.75 | 81.1% | 3.466 | 3.587 | 3.627 | 0.835 | 0.0% | 30/74 |
| 1712.00483 | ✓ | 0.78 | 99.2% | 12.361 | 12.641 | 12.573 | 0.426 | 0.0% | 19/119 |
| 1607.07327 | ✓ | 0.85 | 100.0% | 1.027 | 0.442 | 1.640 | 0.281 | 31.4% | 50/35 |
| 1611.05852 | ✗ (None) | 0.00 | no_prediction | — | — | — | — | — | — |
| 2111.06883 | ✗ (None) | 0.00 | no_prediction | — | — | — | — | — | — |
| 0802.2350 | ✓ | 0.95 | 70.8% | 20.674 | 20.616 | 20.656 | 0.700 | 0.0% | 6/24 |
| 2009.04517 | ✗ (None) | 0.50 | no_prediction | — | — | — | — | — | — |
| 2010.08107 | ✓ | 0.75 | 100.0% | 2.119 | 2.065 | 2.349 | 0.745 | 3.4% | 62/208 |
| 2201.02042 | — | — | EXCLUDED | — | — | — | — | — | — |
| 2403.03004 | ✓ | 0.75 | 94.9% | 1.784 | 1.844 | 1.866 | 0.921 | 0.0% | 42/414 |
| 2205.03617 | ✗ (None) | 0.00 | no_prediction | — | — | — | — | — | — |
| 2310.06017 | ✓ | 0.70 | 49.6% | 0.966 | 0.964 | 1.165 | 0.500 | 14.3% | 64/113 |
| 2102.08764 | ✓ | 0.95 | 100.0% | 0.000 | 0.000 | 0.000 | 0.892 | 100.0% | 2/2 |
| 2308.14656 | ✓ | 0.85 | 100.0% | 0.218 | 0.198 | 0.196 | 0.993 | 70.7% | 12/75 |
| 2207.03102 | ✓ | 0.90 | 100.0% | 0.000 | 0.000 | 0.000 | 0.360 | 100.0% | 6/2 |
| 1505.07455 | — | — | EXCLUDED | — | — | — | — | — | — |
| 2105.04603 | ✗ (None) | 0.00 | no_prediction | — | — | — | — | — | — |
| 2303.11792 | ✓ | 0.75 | 90.0% | 0.141 | 0.141 | 0.144 | 0.748 | 100.0% | 9/20 |
| 1607.06083 | ✗ (None) | 1.00 | no_prediction | — | — | — | — | — | — |
| 2108.04746 | ✗ (None) | 0.00 | no_prediction | — | — | — | — | — | — |
| 2208.12670 | ✓ | 0.78 | 100.0% | 0.000 | ∞ | — | — | 100.0% | 5/1 |
| 1806.05120 | ✓ | 0.70 | 0.0% | ∞ | ∞ | ∞ | 0.000 | 0.0% | 26/94 |
| 2101.01241 | ✓ | 0.90 | 100.0% | 0.005 | ∞ | — | — | 100.0% | 2/1 |
| 2404.14476 | ✓ | 0.85 | 92.2% | 0.408 | 0.878 | 0.450 | 0.109 | 44.7% | 50/51 |
| 2504.12377 | ✓ | 0.85 | 20.0% | 0.005 | 0.003 | 0.003 | 0.538 | 100.0% | 8/15 |
| 2408.15227 | ✓ | 0.70 | 100.0% | 0.143 | 0.130 | 0.133 | 0.905 | 100.0% | 8/230 |
| 2209.09917 | ✓ | 0.80 | 60.0% | 0.129 | 0.112 | 0.092 | 0.792 | 100.0% | 7/5 |
| 2406.00387 | ✓ | 0.92 | 99.1% | 0.108 | 0.077 | 0.265 | 0.987 | 67.3% | 94/108 |
| 1207.3275 | ✓ | 0.95 | 100.0% | 0.036 | 0.036 | ∞ | 0.000 | 100.0% | 1/9 |
| 2205.01079 | ✓ | 0.60 | 100.0% | 0.230 | 0.212 | 0.221 | 1.000 | 92.9% | 30/14 |
| 2212.02403 | ✓ | 0.75 | 97.6% | 1.542 | 1.410 | 0.994 | 0.687 | 2.4% | 28/42 |
| 1903.12190 | ✗ (None) | 0.00 | no_prediction | — | — | — | — | — | — |
| 2305.00890 | ✓ | 0.75 | 65.7% | 0.701 | 1.978 | 2.620 | 0.844 | 16.8% | 229/4991 |
| 1708.06367 | ✓ | 0.70 | 93.8% | 1.728 | 1.689 | 1.738 | 0.863 | 6.6% | 139/81 |
| 2312.13723 | — | — | EXCLUDED | — | — | — | — | — | — |
| 2410.10363 | ✗ (None) | 0.75 | no_prediction | — | — | — | — | — | — |
| 1202.5851 | — | — | EXCLUDED | — | — | — | — | — | — |
| 2208.06519 | ✓ | 0.95 | 100.0% | 0.097 | ∞ | — | — | 100.0% | 1/1 |
| 2401.16747 | ✓ | 0.85 | 81.8% | 0.193 | 0.233 | 0.268 | 0.796 | 66.7% | 485/66 |
| 2401.18076 | ✓ | 0.45 | 100.0% | 0.785 | 0.723 | 0.853 | 0.659 | 13.8% | 9/29 |
| 2503.13653 | ✓ | 0.80 | 0.0% | ∞ | ∞ | ∞ | 0.000 | 0.0% | 36/53 |
| 2308.06339 | ✓ | 0.65 | 92.1% | 0.235 | 0.273 | 0.305 | 0.959 | 80.0% | 30/76 |
| 2109.11734 | ✓ | 0.88 | 83.3% | 0.144 | 0.004 | 0.084 | 0.820 | 100.0% | 6/12 |
| 2308.09077 | ✓ | 0.75 | 0.0% | ∞ | ∞ | ∞ | 0.000 | 0.0% | 56/54 |
| 2110.06096 | ✓ | 0.60 | 94.2% | 0.292 | 0.278 | 0.239 | 0.956 | 52.2% | 49/242 |
| 2205.03679 | ✓ | 0.75 | 100.0% | 0.252 | 0.282 | 0.284 | 0.976 | 59.7% | 6/1525 |
| 2202.08858 | ✓ | 0.00 | no_extracted_points | — | — | — | — | — | — |
| 2503.14582 | ✓ | 0.70 | 78.4% | 0.324 | 0.233 | 0.293 | 0.711 | 44.7% | 50/196912 |
| 1207.2442 | ✗ (None) | 1.00 | no_prediction | — | — | — | — | — | — |
| 1609.00667 | — | — | EXCLUDED | — | — | — | — | — | — |
| 2407.03828 | ✓ | 0.80 | 99.1% | 0.125 | 0.111 | 0.111 | 0.342 | 100.0% | 104/116 |
| 1810.04602 | ✓ | 0.72 | 0.0% | ∞ | ∞ | ∞ | 0.000 | 0.0% | 24/55 |
| 2110.10262 | — | — | EXCLUDED | — | — | — | — | — | — |
| 2306.05934 | ✓ | 0.50 | no_extracted_points | — | — | — | — | — | — |
| 2306.01048 | ✓ | 0.70 | 11.1% | 0.274 | 0.051 | 3.230 | 0.200 | 50.0% | 16/36 |
| 2008.08773 | ✓ | 0.75 | 89.3% | 0.098 | 0.078 | 0.096 | 0.906 | 96.7% | 70/543 |
| 2007.04990 | — | — | EXCLUDED | — | — | — | — | — | — |
| 2207.11968 | ✓ | 0.75 | 72.7% | 0.227 | 0.198 | 0.242 | 0.662 | 87.1% | 11/128 |
| 0807.2926 | ✓ | 0.85 | 5.6% | 0.025 | 0.025 | 0.025 | 0.368 | 100.0% | 2/18 |
| 1508.02463 | ✓ | 0.65 | 66.7% | 0.245 | 0.138 | 0.465 | 0.140 | 52.7% | 21/111 |
| 0809.4700 | ✓ | 0.80 | 97.1% | 0.035 | 0.347 | 0.052 | 0.151 | 76.5% | 189/35 |
| 2006.07055 | ✓ | 0.55 | 100.0% | 7.919 | 7.303 | 7.734 | 0.382 | 0.0% | 12/158 |
| 2004.02733 | ✓ | 0.90 | 97.0% | 0.101 | 0.246 | 0.248 | 0.428 | 96.9% | 6/33 |
| 2111.09892 | ✓ | 0.75 | 100.0% | 4.494 | 4.494 | 4.494 | 0.230 | 0.0% | 80/2 |
| 1401.6460 | ✓ | 0.75 | 75.0% | 12.253 | 11.462 | 10.264 | 0.953 | 0.0% | 54/4 |
| 2204.01454 | ✓ | 0.60 | 100.0% | 5.915 | 5.819 | 5.282 | 0.395 | 2.4% | 20/42 |
| 2410.02218 | — | — | EXCLUDED | — | — | — | — | — | — |
| 1808.02340 | ✓ | 0.75 | 100.0% | 0.728 | 0.754 | 0.822 | 0.985 | 26.0% | 80/265 |
| 2311.16364 | ✓ | 0.85 | 100.0% | 0.946 | 0.946 | ∞ | 0.000 | 0.0% | 1/121 |
| 1704.02297 | ✓ | 0.95 | 1.7% | 0.000 | 0.000 | 0.000 | 0.634 | 100.0% | 2/58 |
| 1707.07921 | ✓ | 0.75 | 100.0% | 2.290 | 2.290 | 1.371 | 0.251 | 0.0% | 43/30 |
| 1806.00310 | ✓ | 0.90 | 100.0% | 0.002 | 0.002 | 0.002 | 0.001 | 100.0% | 2/8 |
| 2007.03694 | ✓ | 0.85 | 100.0% | 2.090 | 2.090 | 2.090 | 0.353 | 0.0% | 2/2 |
| 1911.11905 | ✓ | 0.95 | 100.0% | 0.046 | 0.058 | 0.050 | 0.988 | 98.8% | 388/256 |
| 1902.04246 | ✓ | 0.55 | 91.8% | 0.224 | 0.231 | 0.215 | 0.779 | 92.9% | 16/61 |
| 1708.02111 | — | — | EXCLUDED | — | — | — | — | — | — |
| 2006.09721 | ✓ | 0.70 | 97.3% | 1.200 | 1.198 | 1.246 | 0.665 | 0.0% | 11/148 |
| 1907.11485 | ✓ | 0.70 | 94.9% | 0.812 | 0.831 | 0.879 | 0.943 | 29.7% | 32/78 |
| 2112.12116 | ✗ (None) | 0.50 | no_prediction | — | — | — | — | — | — |
| 2006.12431 | ✓ | 0.75 | 100.0% | 0.360 | 0.352 | 0.377 | 0.916 | 41.1% | 18/90 |
| 2207.11330 | ✓ | 0.65 | 87.3% | 1.093 | 1.148 | 1.204 | 0.927 | 0.0% | 42/118 |
| 2412.08699 | — | — | EXCLUDED | — | — | — | — | — | — |
| 1512.06746 | — | — | EXCLUDED | — | — | — | — | — | — |
| 1606.07494 | — | — | EXCLUDED | — | — | — | — | — | — |
| 1906.00967 | — | — | EXCLUDED | — | — | — | — | — | — |
| 2108.05368 | — | — | EXCLUDED | — | — | — | — | — | — |
| 1705.00676 | — | — | EXCLUDED | — | — | — | — | — | — |
| 1509.00026 | — | — | EXCLUDED | — | — | — | — | — | — |
| 2402.00741 | ✗ (None) | 0.50 | no_prediction | — | — | — | — | — | — |
| 1708.07521 | — | — | EXCLUDED | — | — | — | — | — | — |
| 1606.03145 | — | — | EXCLUDED | — | — | — | — | — | — |
| 2401.17253 | — | — | EXCLUDED | — | — | — | — | — | — |
| 1412.0789 | — | — | EXCLUDED | — | — | — | — | — | — |
| 2206.11598 | — | — | EXCLUDED | — | — | — | — | — | — |
| 1902.04644 | — | — | EXCLUDED | — | — | — | — | — | — |
| 2306.08039 | ✓ | 0.72 | 98.8% | 0.038 | 0.038 | 0.055 | 0.982 | 99.2% | 1089/1158 |
| 2102.01448 | ✓ | 0.65 | 0.0% | ∞ | ∞ | ∞ | 0.000 | 0.0% | 0/70 |
| 2209.03289 | ✓ | 0.75 | 100.0% | 2.475 | 2.113 | 2.453 | 0.998 | 0.9% | 34/110 |
| 2209.13588 | ✓ | 0.75 | 95.7% | 0.227 | 0.207 | 0.270 | 0.962 | 62.7% | 99/350 |
| 1906.11844 | ✗ (AxionProton) | 0.70 | no_comparable_gt | — | — | — | — | — | — |
| hep-ph/0611223 | ✗ (AxionPhoton) | 0.70 | no_comparable_gt | — | — | — | — | — | — |
| 1810.12257 | ✓ | 0.75 | 100.0% | 0.832 | 0.681 | 0.742 | 0.997 | 9.8% | 19/3214 |
| 2102.06722 | ✓ | 0.70 | 0.0% | ∞ | ∞ | ∞ | 0.000 | 0.0% | 75/391 |
| 2404.12517 | ✓ | 0.70 | 99.6% | 0.318 | 0.213 | 0.200 | 0.998 | 45.6% | 7/284 |
| 0910.5914 | ✓ | 0.72 | 0.0% | ∞ | ∞ | ∞ | 0.000 | 0.0% | 5/27 |
| 1804.05750 | ✓ | 0.75 | 100.0% | 0.267 | 0.251 | 0.220 | 0.847 | 59.3% | 25/145 |
| 1910.08638 | ✓ | 0.80 | 0.0% | ∞ | ∞ | ∞ | 0.000 | 0.0% | 6/172 |
| 2504.07279 | ✓ | 0.72 | 83.8% | 1.251 | 0.851 | 1.007 | 0.890 | 0.0% | 26/234 |
| 1911.05772 | ✓ | 0.80 | 81.8% | 0.699 | 0.205 | 0.987 | 0.982 | 16.7% | 70/22 |
| 1901.00920 | ✓ | 0.75 | 0.0% | ∞ | ∞ | ∞ | 0.000 | 0.0% | 321/117 |
| 1004.1313 | ✓ | 0.72 | 16.7% | 0.411 | 0.427 | 0.412 | 0.056 | 15.8% | 39/228 |
| 2008.05355 | ✓ | 0.75 | 0.0% | ∞ | ∞ | ∞ | 0.000 | 0.0% | 72/49 |
| 2302.10206 | ✓ | 0.60 | 100.0% | 2.188 | 1.625 | 2.674 | 0.324 | 7.1% | 150/14 |
| 2101.11290 | ✓ | 0.85 | 50.0% | 0.000 | 0.000 | 0.000 | 0.010 | 100.0% | 2/2 |
| 2002.08370 | ✗ (None) | 0.50 | no_prediction | — | — | — | — | — | — |
| 2211.12699 | ✓ | 0.75 | 0.0% | ∞ | ∞ | ∞ | 0.000 | 0.0% | 673/75 |
| 2108.03316 | ✓ | 0.85 | 100.0% | 0.333 | 0.146 | 0.979 | 0.942 | 44.9% | 32/321 |
| 1709.00009 | ✗ (None) | 1.00 | no_prediction | — | — | — | — | — | — |
| 2007.13071 | ✓ | 0.85 | 0.0% | ∞ | ∞ | ∞ | 0.000 | 0.0% | 0/318 |
| 2009.09059 | ✓ | 0.65 | 39.5% | 0.030 | 0.062 | 0.096 | 0.152 | 80.0% | 9/114 |
| 2112.03439 | — | — | EXCLUDED | — | — | — | — | — | — |
| 2001.05102 | ✓ | 0.75 | 90.9% | 0.236 | 0.237 | 0.238 | 0.924 | 100.0% | 15/77 |
| 2008.10141 | ✓ | 0.70 | 98.6% | 0.311 | 0.312 | 0.303 | 0.966 | 34.6% | 20/220 |
| 2012.10764 | ✓ | 0.75 | 100.0% | 0.057 | 0.058 | 0.190 | 0.996 | 66.4% | 7/125 |
| 2206.08845 | ✓ | 0.80 | 99.1% | 0.146 | 0.144 | 0.144 | 0.953 | 99.9% | 20/2959 |
| 2207.13597 | ✓ | 0.60 | 93.9% | 2.196 | 2.195 | 2.197 | 0.969 | 0.0% | 3/49 |
| 2210.10961 | ✓ | 0.92 | 94.4% | 0.092 | 0.097 | 0.088 | 0.964 | 100.0% | 99/251 |
| 2312.11003 | ✓ | 0.95 | 91.2% | 0.144 | 0.145 | 0.144 | 0.945 | 100.0% | 8/181 |
| 2403.13390 | ✓ | 0.85 | 98.6% | 0.928 | 0.937 | 0.922 | 0.982 | 0.0% | 2/70 |
| 2402.12892 | ✓ | 0.65 | 100.0% | 0.674 | 0.674 | 0.766 | 0.977 | 0.0% | 23/362 |
| 2211.02902 | ✓ | 0.72 | 0.0% | ∞ | ∞ | ∞ | 0.000 | 0.0% | 40/169 |
| 1705.02290 | ✓ | 0.92 | 36.2% | 0.066 | 0.062 | 0.062 | 0.077 | 100.0% | 4/436 |
| hep-ex/0702006 | — | — | EXCLUDED | — | — | — | — | — | — |
| 1704.05189 | ✗ (None) | 0.00 | no_prediction | — | — | — | — | — | — |
| 2411.13701 | ✓ | 0.00 | no_extracted_points | — | — | — | — | — | — |
| 2109.03261 | ✓ | 0.70 | 58.6% | 0.224 | 0.008 | 0.116 | 0.297 | 52.9% | 17/29 |
| 1304.0989 | ✓ | 0.70 | 44.8% | 0.061 | 0.063 | 0.056 | 0.080 | 100.0% | 19/29 |
| 1703.07354 | ✓ | 0.75 | 63.6% | 0.078 | 0.077 | 0.152 | 0.226 | 71.4% | 76/44 |
| 1907.05475 | ✓ | 0.75 | 94.1% | 0.146 | 0.146 | 0.086 | 0.390 | 68.8% | 4/17 |
| 2104.12772 | ✓ | 0.15 | no_extracted_points | — | — | — | — | — | — |
| 2407.10618 | ✓ | 0.65 | 75.0% | 5.112 | 4.679 | 4.457 | 0.720 | 4.2% | 34/2612 |
| 2303.03594 | ✓ | 0.50 | 100.0% | 0.364 | 0.372 | 0.442 | 0.412 | 39.3% | 23/89 |
| 2311.05476 | ✓ | 0.75 | 47.1% | 1.165 | 1.176 | 1.129 | 0.381 | 0.0% | 79/121 |
| 2201.09890 | ✓ | 0.60 | 100.0% | 0.919 | 0.919 | 0.806 | 0.072 | 30.8% | 13/21 |
| 1110.2895 | ✗ (None) | 0.50 | no_prediction | — | — | — | — | — | — |
| 2412.02232 | ✓ | 0.75 | 91.1% | 0.889 | 0.829 | 0.819 | 0.913 | 14.2% | 35/124 |
| 2504.07559 | ✓ | 0.65 | 72.7% | 1.115 | 0.160 | 1.238 | 0.780 | 7.6% | 102/198 |
| 2404.17333 | ✓ | 0.95 | 20.0% | 0.124 | 0.137 | 0.461 | 0.052 | 80.0% | 5/25 |
| 2405.08059 | ✗ (None) | 1.00 | no_prediction | — | — | — | — | — | — |
| 2211.03414 | ✓ | 0.65 | 0.0% | ∞ | ∞ | ∞ | 0.000 | 0.0% | 77/109 |
| 1603.06978 | ✓ | 0.75 | 41.3% | 0.538 | 0.563 | 0.439 | 0.126 | 0.0% | 19/75 |
| 2305.10327 | ✓ | 0.70 | 61.2% | 2.402 | 2.892 | 1.988 | 0.232 | 0.0% | 53/49 |
| 2305.01002 | ✓ | 0.85 | 0.0% | ∞ | ∞ | ∞ | 0.000 | 0.0% | 9/38 |
| 2208.13794 | ✓ | 0.75 | 100.0% | 14.162 | 13.613 | 13.741 | 0.374 | 0.0% | 10/89 |
| 2501.17119 | ✓ | 0.75 | 100.0% | 0.078 | 0.069 | 0.069 | 0.937 | 100.0% | 50/799 |
| 1406.6053 | ✓ | 0.85 | 3.7% | 0.003 | 0.010 | 0.004 | 0.793 | 100.0% | 2/27 |
| 2110.14406 | ✓ | 0.95 | 100.0% | 0.000 | ∞ | — | — | 100.0% | 1/1 |
| 2203.04332 | ✓ | 0.85 | 95.9% | 0.124 | 0.124 | 0.124 | 0.336 | 99.3% | 60/148 |
| 1610.02580 | ✓ | 0.70 | 47.9% | 0.268 | 0.267 | 0.270 | 0.479 | 77.6% | 59/121 |
| 2008.01853 | ✓ | 0.75 | 46.8% | 1.499 | 2.496 | 2.100 | 0.191 | 0.0% | 4/111 |
| 2409.08998 | ✓ | 0.85 | 0.0% | ∞ | ∞ | ∞ | 0.000 | 0.0% | 0/324 |
| 1311.3148 | ✓ | 0.75 | 100.0% | 0.558 | 0.452 | 0.482 | 0.537 | 4.5% | 50/22 |
| 2301.06560 | ✓ | 0.72 | 78.4% | 0.410 | 0.713 | 0.562 | 0.667 | 39.5% | 24/97 |
| 2412.02543 | ✓ | 0.80 | 77.8% | 0.337 | 0.234 | 0.372 | 0.799 | 45.5% | 36/99 |
| 2209.06299 | — | — | EXCLUDED | — | — | — | — | — | — |
| 2310.15395 | ✓ | 0.75 | 40.8% | 0.642 | 0.660 | 0.645 | 0.280 | 3.7% | 776/262 |
| 2503.11753 | ✓ | 0.75 | 95.9% | 2.576 | 2.585 | 2.500 | 0.963 | 0.0% | 69/1844 |
| 1509.00476 | ✓ | 0.80 | 0.0% | ∞ | ∞ | ∞ | 0.000 | 0.0% | 41/21 |
| 2307.01365 | ✓ | 0.75 | 90.4% | 0.220 | 0.221 | 0.262 | 0.933 | 68.2% | 13/94 |
| 2111.08025 | ✓ | 0.75 | 91.4% | 0.106 | 0.118 | 0.128 | 0.905 | 98.8% | 16/93 |
| 2412.03660 | ✓ | 0.80 | 98.3% | 1.873 | 1.950 | 1.774 | 0.906 | 1.8% | 473/115 |
| 2409.11777 | ✓ | 0.65 | 100.0% | 0.140 | 0.140 | 0.200 | 0.989 | 94.2% | 98/86 |
| 2401.07798 | ✓ | 0.70 | 100.0% | 0.234 | 0.238 | 0.256 | 0.424 | 78.9% | 35/38 |
| 1811.10997 | ✓ | 0.85 | 92.4% | 0.601 | 0.567 | 0.593 | 0.919 | 25.6% | 119/144 |
| 2203.04319 | ✓ | 0.85 | 39.4% | 0.562 | 0.009 | 0.471 | 0.140 | 34.6% | 2/132 |
| 2307.03878 | ✓ | 0.75 | 97.4% | 1.895 | 1.371 | 2.329 | 0.999 | 8.1% | 51/76 |
| 2110.13636 | ✓ | 0.85 | 80.6% | 0.147 | 0.213 | 0.223 | 0.847 | 72.0% | 8/62 |
| 2008.09464 | ✓ | 0.65 | 100.0% | 0.246 | 0.306 | 0.174 | 0.791 | 60.0% | 10/50 |
| 2202.08274 | ✓ | 0.75 | 100.0% | 2.457 | 2.483 | 2.478 | 0.825 | 0.0% | 62/257 |
| 2203.12152 | ✓ | 0.75 | 92.7% | 0.167 | 0.204 | 0.227 | 0.707 | 88.6% | 52/123 |
| 2310.00904 | ✓ | 0.85 | 100.0% | 0.052 | 0.051 | 0.055 | 0.979 | 100.0% | 10/53 |
| 2407.18586 | ✓ | 0.87 | 100.0% | 0.043 | 0.031 | 0.046 | 0.990 | 99.2% | 13/265 |
| 1706.00209 | ✓ | 0.85 | 100.0% | 0.000 | ∞ | — | — | 100.0% | 2/1 |
| 1506.08082 | ✓ | 0.82 | 91.7% | 0.224 | 0.337 | 0.115 | 0.026 | 54.5% | 281/12 |
| 2303.08410 | ✓ | 0.75 | 89.6% | 0.328 | 0.295 | 0.309 | 0.798 | 46.5% | 128/192 |
| 2403.02096 | ✓ | 0.85 | 100.0% | 0.151 | 0.106 | 0.117 | 0.998 | 67.3% | 60/838 |
| 2412.02229 | ✓ | 0.70 | 61.7% | 2.616 | 1.181 | 1.708 | 0.594 | 0.0% | 94/120 |
| 1510.08052 | ✓ | 0.72 | 56.8% | 0.774 | 0.788 | 0.834 | 0.031 | 0.0% | 26/88 |
| 2409.10514 | ✓ | 0.75 | 94.9% | 0.137 | 0.099 | 0.127 | 0.908 | 79.1% | 57/156 |
| 1903.03586 | ✓ | 0.85 | 57.1% | 0.032 | 0.028 | 0.082 | 0.825 | 75.0% | 9/7 |
| 1903.06547 | ✓ | 0.95 | 100.0% | 0.000 | ∞ | — | — | 100.0% | 1/1 |
| 2012.09498 | ✓ | 0.82 | 100.0% | 0.079 | ∞ | — | — | 100.0% | 9/1 |
| 2304.07505 | ✓ | 0.65 | 90.6% | 0.263 | 0.233 | 0.352 | 0.735 | 55.2% | 33/32 |
| 2402.19063 | ✓ | 0.75 | 100.0% | 0.388 | 0.366 | 0.347 | 0.994 | 37.6% | 5/149 |
| 2104.13798 | ✓ | 0.95 | 100.0% | 0.222 | 0.222 | 0.222 | 1.000 | 100.0% | 2/2 |
| 2403.07790 | ✓ | 0.85 | 99.8% | 0.242 | 0.283 | 0.479 | 0.992 | 56.6% | 10/420 |
| 2409.01805 | ✓ | 0.65 | 20.9% | 2.046 | 1.234 | 1.329 | 0.193 | 15.8% | 45/91 |
| 2003.03348 | ✓ | 0.85 | 0.0% | ∞ | ∞ | ∞ | 0.000 | 0.0% | 66/857 |
| 2303.11395 | ✓ | 0.80 | 51.4% | 0.203 | 0.390 | 0.569 | 0.696 | 63.2% | 28/37 |
| 2304.01060 | ✓ | 0.75 | 0.0% | ∞ | ∞ | ∞ | 0.000 | 0.0% | 52/51 |
| 2212.09764 | ✓ | 0.92 | 97.0% | 0.001 | 0.004 | 0.002 | 0.136 | 100.0% | 77/33 |
| 2405.19393 | ✓ | 0.72 | 100.0% | 1.241 | 1.004 | 1.259 | 0.934 | 23.6% | 50/55 |
| 2306.11575 | ✓ | 0.75 | 100.0% | 0.049 | 0.049 | 0.068 | 0.997 | 100.0% | 13/415 |
| 2006.06722 | ✓ | 0.85 | 86.8% | 0.788 | 0.855 | 1.090 | 0.097 | 0.0% | 12/76 |
| 2203.16567 | ✓ | 0.92 | 100.0% | 0.081 | 0.057 | 0.068 | 0.457 | 98.3% | 300/115 |
| 2008.13662 | ✓ | 0.75 | 48.4% | 2.347 | 2.218 | 2.309 | 0.560 | 0.0% | 34/64 |
| 2205.05700 | ✓ | 0.75 | 100.0% | 0.905 | 0.706 | 0.823 | 0.722 | 3.3% | 22/122 |
| 2303.06968 | ✓ | 0.72 | 100.0% | 1.943 | 2.300 | 2.039 | 0.567 | 9.2% | 100/174 |
| 1501.01639 | ✓ | 0.70 | 11.1% | 0.258 | 0.264 | 0.260 | 0.307 | 100.0% | 2/18 |
| 2307.11216 | ✓ | 0.82 | 100.0% | 0.235 | 0.237 | 0.253 | 0.897 | 80.0% | 85/60 |
| 2112.09620 | ✓ | 0.82 | 77.1% | 0.204 | 0.207 | 0.327 | 0.912 | 59.4% | 80/83 |
| 2408.16045 | ✓ | 0.70 | 64.5% | 1.524 | 1.463 | 1.470 | 0.669 | 8.5% | 60/110 |
| 2205.05574 | ✓ | 0.80 | 0.0% | ∞ | ∞ | ∞ | 0.000 | 0.0% | 50/508 |
| 2307.07403 | ✓ | 0.75 | 66.3% | 1.066 | 1.001 | 1.081 | 0.746 | 0.0% | 11/555 |
| astro-ph/0611502 | ✓ | 0.60 | 67.0% | 4.139 | 4.168 | 4.013 | 0.795 | 0.0% | 6/91 |
| 2301.06778 | ✓ | 0.72 | 79.1% | 0.929 | 0.913 | 0.909 | 0.858 | 1.5% | 358/86 |
| 1912.07751 | — | — | EXCLUDED | — | — | — | — | — | — |
| 2402.07976 | ✓ | 0.65 | 97.6% | 0.681 | 0.476 | 0.557 | 0.940 | 17.4% | 10/10796 |
| 2102.00379 | ✓ | 0.65 | 96.2% | 0.480 | 0.361 | 1.961 | 0.919 | 44.0% | 35/26 |
| 2102.02207 | — | — | EXCLUDED | — | — | — | — | — | — |
| 2503.04726 | ✗ (None) | 0.50 | no_prediction | — | — | — | — | — | — |
| 2008.03305 | ✓ | 0.65 | 93.9% | 0.408 | 0.410 | 0.390 | 0.180 | 0.0% | 18/115 |
| 2412.09595 | — | — | EXCLUDED | — | — | — | — | — | — |
| 2008.02209 | ✓ | 0.85 | 91.7% | 0.317 | 0.095 | 0.308 | 0.921 | 45.5% | 5/12 |
| 2407.16628 | ✓ | 0.80 | 95.0% | 3.640 | 3.969 | 3.766 | 0.975 | 10.4% | 25/101 |
| 0801.1527 | ✗ (None) | 1.00 | no_prediction | — | — | — | — | — | — |
| 2002.05165 | ✓ | 0.75 | 84.6% | 0.460 | 0.545 | 0.554 | 0.480 | 1.6% | 58/671 |
| 2409.12940 | ✓ | 0.72 | 100.0% | 2.886 | 2.827 | 2.654 | 0.886 | 0.0% | 26/174 |
| 2409.12115 | ✓ | 0.75 | 98.8% | 0.005 | 0.003 | 0.106 | 0.999 | 100.0% | 60/80 |
| 1201.5902 | ✗ (None) | 0.50 | no_prediction | — | — | — | — | — | — |
| 1911.05086 | ✗ (None) | 0.00 | no_prediction | — | — | — | — | — | — |
| 2003.13698 | ✓ | 0.75 | 12.0% | 2.685 | 1.808 | 2.860 | 0.117 | 4.3% | 14/393 |
| 0810.5501 | ✓ | 0.75 | 69.6% | 0.004 | 0.007 | 0.009 | 0.614 | 100.0% | 201/112 |
| 2002.01796 | ✓ | 0.75 | no_comparable_gt | — | — | — | — | — | — |
| 1907.12628 | ✓ | 0.75 | 53.4% | 0.887 | 0.893 | 1.015 | 0.522 | 2.6% | 50/73 |
| 1906.08814 | ✓ | 0.75 | 100.0% | 0.000 | 0.043 | 0.048 | 1.000 | 100.0% | 9/2 |
| 2101.02805 | — | — | EXCLUDED | — | — | — | — | — | — |
| 2405.20444 | ✓ | 0.75 | 94.5% | 0.343 | 0.290 | 0.352 | 0.963 | 42.3% | 52/493 |
| 2301.11512 | ✓ | 0.75 | 62.5% | 0.460 | 0.525 | 0.667 | 0.641 | 40.0% | 14/16 |
| 2207.05767 | — | — | EXCLUDED | — | — | — | — | — | — |
| 2003.13144 | ✓ | 0.95 | 86.4% | 0.086 | 0.058 | 0.117 | 0.802 | 84.2% | 15/22 |
| 2310.13891 | ✓ | 0.95 | 100.0% | 0.026 | ∞ | 0.026 | 0.925 | 100.0% | 2/87 |
| 2304.12907 | ✓ | 0.75 | 100.0% | 0.568 | 0.414 | 0.530 | 0.972 | 25.0% | 54/152 |
| 2211.00022 | ✓ | 0.65 | 76.9% | 0.682 | 0.686 | 0.720 | 0.776 | 8.2% | 60/143 |
| 2406.19445 | ✓ | 0.85 | 0.0% | ∞ | ∞ | ∞ | 0.000 | 0.0% | 49/99 |
| 2402.17140 | — | — | EXCLUDED | — | — | — | — | — | — |
| 2110.01582 | ✓ | 0.65 | 0.0% | ∞ | ∞ | ∞ | 0.000 | 0.0% | 81/26 |
| 2301.03622 | ✗ (AxionPhoton) | 0.65 | no_comparable_gt | — | — | — | — | — | — |
| 1007.3766 | ✓ | 0.90 | 23.5% | 1.104 | 1.030 | 1.074 | 0.106 | 4.2% | 36/102 |
| 1410.5244 | ✓ | 0.75 | 100.0% | 0.194 | 0.074 | 0.690 | 0.533 | 71.4% | 19/21 |
| 2410.02858 | ✓ | 0.70 | 66.7% | 0.390 | 0.172 | 0.280 | 0.545 | 25.0% | 4/6 |
| 2110.10497 | ✓ | 0.65 | 65.3% | 0.535 | 0.519 | 0.548 | 0.673 | 23.4% | 142/72 |
| 2012.05427 | ✓ | 0.90 | 92.3% | 1.042 | 0.723 | 0.954 | 0.893 | 8.3% | 50/26 |
| 2204.03818 | ✓ | 0.75 | 98.2% | 0.121 | 0.111 | 0.166 | 0.982 | 84.8% | 16/3689 |
| 2405.12285 | ✓ | 0.60 | 96.7% | 0.402 | 0.397 | 0.429 | 0.956 | 28.4% | 17/91 |
| 2406.02546 | ✓ | 0.88 | 100.0% | 0.170 | 0.068 | 0.284 | 0.823 | 63.6% | 105/22 |
| 2209.03419 | ✓ | 0.80 | 98.2% | 0.150 | 0.135 | 0.136 | 0.993 | 87.8% | 15/325 |
| 2212.01971 | ✗ (AxionPhoton) | 0.95 | no_comparable_gt | — | — | — | — | — | — |
| 2305.09711 | ✓ | 0.85 | 100.0% | 1.000 | ∞ | ∞ | 0.000 | 0.0% | 2/57500 |
| 1502.04490 | ✓ | 0.75 | 45.5% | 0.518 | 0.504 | 0.487 | 0.435 | 8.9% | 49/123 |
| 1905.05579 | ✓ | 0.75 | 98.1% | 0.127 | 0.133 | 0.220 | 0.950 | 79.4% | 12/104 |
| 1301.6557 | ✓ | 0.78 | 59.3% | 0.403 | 0.397 | 0.414 | 0.591 | 4.1% | 22/123 |
| 2208.03183 | — | — | EXCLUDED | — | — | — | — | — | — |
| 2008.12231 | ✓ | 0.75 | 100.0% | 0.000 | ∞ | — | — | 100.0% | 5/1 |
| 2308.08337 | ✓ | 0.90 | 100.0% | 0.000 | ∞ | — | — | 100.0% | 1/1 |
| 1008.3536 | ✓ | 0.75 | 70.0% | 1.338 | 1.382 | 1.300 | 0.509 | 5.7% | 29/100 |
| 2106.00022 | ✓ | 0.78 | 62.1% | 0.467 | 0.480 | 0.486 | 0.744 | 16.7% | 70/58 |
| 1804.10777 | ✓ | 0.75 | 33.3% | 0.399 | 0.445 | 0.447 | 0.323 | 0.0% | 29/3 |
| 1504.00118 | ✓ | 0.65 | 100.0% | 0.112 | 0.076 | 0.109 | 0.273 | 83.3% | 9/12 |
| 2006.02828 | ✓ | 0.75 | 100.0% | 0.065 | 0.045 | 0.058 | 0.952 | 100.0% | 13/6 |
| 1907.12449 | ✓ | 0.60 | 28.1% | 0.321 | 0.420 | 0.322 | 0.279 | 48.1% | 15/555 |
| 1903.05101 | ✓ | 0.70 | 52.8% | 7.474 | 7.295 | 7.420 | 0.221 | 0.0% | 258/53 |
| 2006.13929 | ✓ | 0.82 | 99.0% | 1.135 | 2.935 | 1.334 | 0.456 | 14.4% | 328/98 |
| 1807.04512 | ✗ (None) | 0.00 | no_prediction | — | — | — | — | — | — |
| hep-ph/0307284 | ✗ (None) | 0.00 | no_prediction | — | — | — | — | — | — |
| 2103.03783 | ✓ | 0.60 | 100.0% | 0.947 | 0.824 | 0.983 | 0.137 | 8.7% | 11/69 |
| 2205.06817 | — | — | EXCLUDED | — | — | — | — | — | — |
| 2306.16219 | ✗ (None) | 0.95 | no_prediction | — | — | — | — | — | — |
| 2303.00778 | ✗ (None) | 0.00 | no_prediction | — | — | — | — | — | — |
| 2212.05721 | ✓ | 0.50 | 31.8% | 0.888 | 0.881 | 0.903 | 0.541 | 0.0% | 21/333 |
| 2005.14694 | — | — | EXCLUDED | — | — | — | — | — | — |
| 1503.06886 | ✓ | 0.78 | 77.4% | 0.549 | 1.244 | 1.087 | 0.897 | 44.7% | 28/1006 |
| 1902.02788 | ✗ (None) | 0.00 | no_prediction | — | — | — | — | — | — |
| 2301.03433 | ✓ | 0.80 | 91.3% | 0.633 | 0.653 | 0.818 | 0.932 | 1.9% | 59/172 |
| 2302.04565 | ✗ (None) | 0.00 | no_prediction | — | — | — | — | — | — |
| 1604.08514 | ✓ | 0.75 | 87.5% | 2.562 | 2.671 | 2.757 | 0.892 | 0.2% | 20/505 |
| quant-ph/0106045 | ✗ (None) | 0.00 | no_prediction | — | — | — | — | — | — |
| 2109.08822 | ✓ | 0.75 | 65.6% | 0.341 | 0.281 | 0.294 | 0.739 | 42.9% | 746/32 |
| 2105.13085 | ✗ (DarkPhoton) | 0.45 | no_comparable_gt | — | — | — | — | — | — |
| 2301.08736 | ✗ (None) | 0.75 | no_prediction | — | — | — | — | — | — |
| 2403.02381 | ✗ (None) | 0.95 | no_prediction | — | — | — | — | — | — |
| 2409.03814 | ✓ | 0.90 | 51.6% | 0.609 | 0.684 | 0.594 | 0.508 | 16.4% | 2/308 |
| 2112.07687 | ✗ (DarkPhoton) | 0.75 | no_comparable_gt | — | — | — | — | — | — |
| 2302.00685 | ✓ | 0.75 | 63.6% | 1.386 | 1.172 | 1.201 | 0.408 | 0.0% | 241/11 |
| 2011.11646 | ✗ (None) | 0.50 | no_prediction | — | — | — | — | — | — |
| 2406.10337 | ✓ | 0.70 | 100.0% | 13.593 | 13.593 | 13.600 | 0.130 | 0.0% | 38/51 |
| 2011.08693 | — | — | EXCLUDED | — | — | — | — | — | — |
| 2012.12790 | ✓ | 0.70 | 100.0% | 0.704 | 0.952 | 0.842 | 0.807 | 22.5% | 373/209 |
| 2412.03655 | ✓ | 0.75 | 100.0% | 1.222 | 1.120 | 1.389 | 0.656 | 6.6% | 20/545 |
| 2105.13963 | ✓ | 0.90 | 85.0% | 0.125 | 0.022 | 0.327 | 0.467 | 94.1% | 19/20 |
| 2404.00616 | — | — | EXCLUDED | — | — | — | — | — | — |
| 2412.20932 | ✓ | 0.72 | 100.0% | 0.888 | 0.888 | 0.888 | 0.810 | 0.0% | 65/2 |
| 2408.07740 | ✗ (None) | 1.00 | no_prediction | — | — | — | — | — | — |
| 2410.21590 | ✓ | 0.65 | 79.4% | 1.644 | 1.597 | 2.384 | 0.575 | 0.0% | 25/34 |
| 2205.01637 | ✓ | 0.85 | no_comparable_gt | — | — | — | — | — | — |
| 1708.08464 | ✗ (None) | 0.00 | no_prediction | — | — | — | — | — | — |
| 2303.09865 | ✓ | 0.75 | 100.0% | 0.623 | 0.623 | 0.995 | 0.259 | 28.0% | 100/2 |
| 2211.02661 | ✓ | 0.85 | 0.0% | ∞ | ∞ | ∞ | 0.000 | 0.0% | 25/167 |
| 2301.10784 | ✓ | 0.75 | 90.7% | 8.737 | 8.240 | 8.078 | 0.839 | 0.0% | 13/107 |
| 1003.0964 | — | — | EXCLUDED | — | — | — | — | — | — |
| 2312.11608 | — | — | EXCLUDED | — | — | — | — | — | — |

## Breakdown by Extraction Source

Median residual is over papers with mass-range overlap; zero-overlap papers are listed separately.

| Source | Papers | Compared | Zero-overlap | Med. Resid. | ≤0.3 dex |
|--------|--------|----------|--------------|-------------|----------|
| table | 6 | 6 | 0 | 1.117 dex | 44.0% |
| figure_vision | 175 | 167 | 15 | 0.463 dex | 39.2% |
| text | 30 | 27 | 2 | 0.064 dex | 74.8% |

## Breakdown by Difficulty

> Difficulty is a placeholder label for the repo-sourced pool (nearly all `medium`); this table is informational only.

| Difficulty | Papers | Coupling Acc. | Med. Resid. | ≤0.3 dex |
|------------|--------|---------------|-------------|----------|
| easy | 11 | 81.8% | 0.036 dex | 71.6% |
| medium | 251 | 86.1% | 0.435 dex | 42.2% |
| hard | 29 | 82.8% | 0.227 dex | 65.6% |

## Confidence Calibration

- "Accurate" = median interpolation residual < **0.32 dex** AND interpolation coverage ≥ 50%.
- The **0.32 dex** threshold is the run-to-run LLM extraction *noise floor* (90th-pct per-paper median-residual std across repeated extractions, PR #545) — the binding floor. It is **not** the upstream digitization floor, which is only ~0.034 dex for table/text-sourced papers (PR #558). So a residual gap here is **real extractor overconfidence, not a yardstick artifact**.

### Binned accuracy (pass/fail)

| Bin | N | Mean Conf. | Actual Acc. | Gap |
|-----|---|------------|-------------|-----|
| [0.5–0.7) | 38 | 61.8% | 23.7% | +0.38 |
| [0.7–0.7) | 40 | 70.6% | 17.5% | +0.53 |
| [0.8–0.8) | 75 | 75.0% | 33.3% | +0.42 |
| [0.8–0.8) | 58 | 82.7% | 41.4% | +0.41 |
| [0.9–0.9) | 31 | 92.2% | 77.4% | +0.15 |

> **Interpretation**: Gap > 0 means the pipeline is overconfident; Gap < 0 means underconfident.

### Continuous view: residual distribution per bin

Median (and IQR) of each bin's per-paper median residual, over papers with a finite residual (zero mass-overlap papers excluded from the distribution but still counted in N). If confidence tracked accuracy, the median residual would fall as confidence rises.

| Bin | N | N finite | Median resid. (dex) | IQR (dex) |
|-----|---|----------|---------------------|-----------|
| [0.5–0.7) | 38 | 35 | 0.68 | 0.28–1.38 |
| [0.7–0.7) | 40 | 35 | 0.71 | 0.30–1.39 |
| [0.8–0.8) | 75 | 69 | 0.54 | 0.17–1.54 |
| [0.8–0.8) | 58 | 48 | 0.23 | 0.12–0.65 |
| [0.9–0.9) | 31 | 31 | 0.08 | 0.00–0.13 |

### Continuous view: empirical P(residual < τ) per bin

Fraction of papers in each bin whose median residual is below τ dex (τ = 0.32 is the noise floor used above). A well-calibrated, accurate extractor would show these probabilities rising with confidence.

| Bin | N | P(<0.10) | P(<0.32) | P(<0.50) | P(<1.00) |
|-----|---|----|----|----|----|
| [0.5–0.7) | 38 | 2.6% | 26.3% | 39.5% | 63.2% |
| [0.7–0.7) | 40 | 5.0% | 27.5% | 40.0% | 57.5% |
| [0.8–0.8) | 75 | 13.3% | 33.3% | 44.0% | 60.0% |
| [0.8–0.8) | 58 | 19.0% | 46.6% | 55.2% | 72.4% |
| [0.9–0.9) | 31 | 61.3% | 87.1% | 87.1% | 90.3% |

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
