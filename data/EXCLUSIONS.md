# Ground-truth benchmark exclusions

Entries in `papers.json` carrying `"excluded": true`. An excluded entry stays in
`papers.json` (documented, visible, reversible — never a silent deletion), is
skipped by all scoring in `evaluation/evaluate.py`, and is listed in the
"Excluded GT Entries" table of every report. Source analysis:
`evaluation/eval_runs/failure_analysis_full346_detail.md` (per-paper sections),
summarized in `failure_analysis_full346.md` (Lever 2).

To un-exclude an entry: remove the `excluded`/`exclusion_reason`/
`exclusion_evidence` keys and delete its section here. Each section below states
what would justify that.

---

## AxionMass prediction-band files (13 entries, 11 papers)

**Papers:** 1202.5851 (Kawasaki12), 1505.07455 (Berkowitz15), 1509.00026
(Fleury15), 1606.03145 (Petreczky16), 1608.05414 (Ballesteros16), 1705.00676
(Dine17), 1906.00967 (Buschmann20), 2007.04990 (Gorghetto20 + GorghettoDW_6),
2108.05368 (Buschmann21), 2206.11598 (VISHnu), 2412.08699 (Benabou24 +
Benabou24_DW).

**What the papers report:** theoretical/lattice predictions of the QCD-axion
dark-matter mass window (e.g. "Predicted axion masses (in eV)" in the repo file
headers). These are cosmological mass *predictions*, not exclusion limits on
any coupling.

**Why the GT cannot grade them:** the repo files store `(m_lo, m_hi)` — *both
columns are masses*, consumed by `PlotTheoryMass` as horizontal bands. The GT
auto-expansion mis-ingested column 2 as a dimensionless coupling, producing a
single `(mass, coupling)` "point" that no correct extraction can ever match.
In the full346 run the extractor *correctly* identified each of these papers as
a mass prediction (its notes quote the exact band endpoints) and returned 0
points — correct refusals graded as failures.

**What would un-exclude them:** a dedicated mass-band-overlap comparator
(score the predicted `(m_lo, m_hi)` window against the extraction's reported
window) plus a matching extractor output schema for mass predictions. This
alternative was left open at plan review; until it exists, these entries are
not gradeable.

---

## 2005.14694 — BACON optical-clock network (ScalarPhoton/BACON.txt)

**What the paper reports (arXiv):** 18-digit-accuracy frequency-ratio
measurements. No dark-matter exclusion appears in any arXiv version (full-text
search: zero "boson"/"ultralight"/"d_e" hits).

**Why the GT cannot grade it:** the repo `BACON.txt` d_e curve is digitized
from a figure that exists only in the published Nature 591, 564 (2021) version.
The benchmark feeds the extractor the arXiv PDF, from which the limit is
unreachable.

**What would un-exclude it:** pointing the benchmark's input at the published
PDF (out of scope for the arXiv-PDF pipeline), or an arXiv revision that adds
the DM analysis.

---

## 2011.08693 — Type IIB superradiance landscape (fa/BlackHoleSpins_Mehta.txt)

**What the paper reports:** black-hole-superradiance exclusion statistics over
>2e5 Calabi–Yau compactifications (ensemble KDEs, per-BH exclusion-probability
examples, fraction-excluded vs Hodge number). No general BHSR exclusion curve
in the (m_a, 1/f_a) plane is published in the paper.

**Why the GT cannot grade it:** the 178-point repo curve's own header says
"private communication" — the data was never published in the paper and is
inherently non-extractable from the PDF.

**What would un-exclude it:** the authors publishing the compilation curve in a
paper version the pipeline can read.

---

## 2112.03439 — Breakthrough Listen radio search (AxionPhoton/BreakthroughListen.txt)

**What the paper reports:** model-independent DM decay-rate (λ ~ 1e-32 s⁻¹) and
annihilation cross-section limits over 1020–2700 MHz. It never quotes g_aγγ.

**Why the GT cannot grade it:** the repo g_aγγ = 4.1e-8 GeV⁻¹ value is a
physics conversion O'Hare derived from the λ limit (halo + stimulated-emission
assumptions); the number does not appear in the paper, so the GT demands a
quantity that is not extractable. The extractor's refusal (ct=None, 0 points)
was correct.

**What would un-exclude it:** a vetted decay-rate → g_aγγ converter applied on
*both* sides at scoring time (the Γ-plane converter of Phase 1d covers papers
that plot Γ curves, but this paper's λ is for χ→γγ of generic DM, and the GT is
a 2-point derived band — revisit after 1d lands).

---

## 1003.0964 — first UWA microwave-cavity LSW (tombstone, no repo file)

**What the paper reports:** hidden-photon kinetic mixing χ = 2.9e-5 peak at
m = 37.88 µeV, explicitly "within already established limits".

**Why the GT cannot grade it:** the entry's former mapping,
`DarkPhoton/LSW_UWA.txt`, belongs to arXiv:1410.5244 (per the file's own
header) — the `docs/dp.md` LSW-ADMX/LSW-UWA reference links are swapped
upstream. This paper's own limit has no repo data file, so after re-keying
LSW_UWA.txt to 1410.5244 there is nothing valid left to grade against. (The
LSW_ADMX.txt entry was likewise re-keyed to its header id 1007.3766.)

**What would un-exclude it:** digitizing this paper's own Fig. 11 sliver into
the repo (upstream science change).

---

## 2312.11608 — DM21cm forecast (tombstone for GammaRayDecayCompilation.txt)

**What the paper reports:** projected HERA 21-cm sensitivity to decaying DM
(lifetime vs mass); pre-existing gamma-ray constraints appear only as
background curves in its figure.

**Why this GT file cannot grade it:**
`AxionPhoton/GammaRayDecayCompilation.txt` is a compilation of PRE-EXISTING
limits (HEAO-1/COMPTEL/EGRET/Fermi) that O'Hare took from the paper's
*background* curves — not the paper's own result. The active 2312.11608 entry
now points at the paper's actual headline, `AxionPhoton/Projections/21cm.txt`
(`is_projection: true`).

**What would un-exclude it:** nothing — the file is genuinely not this paper's
result; the tombstone exists so the auto-expander does not silently re-add the
wrong mapping.

## 1609.00667 — NuSTAR sterile-neutrino window (AxionPhoton/NuSTAR.txt)

**What the paper reports:** sterile-neutrino dark-matter limits from the
NuSTAR X-ray line search — the active–sterile mixing angle sin²(2θ) and the
decay rate Γ versus sterile-neutrino mass (10–50 keV). It never quotes an
axion-photon coupling.

**Why the GT cannot grade it:** the repo `AxionPhoton/NuSTAR.txt` g_aγγ curve
is the maintainer's derived conversion of the same X-ray line-flux limit to
decaying-ALP dark matter; the number does not appear in the paper, so the GT
demands a quantity that is not extractable. Same class as the 2112.03439
Breakthrough Listen exclusion. The extractor's refusal (ct=None) was correct
and is reproduced independently by both the Opus (`final347_remediated`) and
Fable (`final347_fable`) arms.

**What would un-exclude it:** a vetted line-flux → g_aγγ converter applied on
both sides at scoring time (the same machinery the Breakthrough Listen entry
is waiting on).

---

## 2102.02207 — XMM-Newton blank-sky decaying DM (AxionPhoton/XMM-Newton.txt)

**What the paper reports:** decaying dark-matter limits via the
sterile-neutrino mixing angle sin²(2θ) versus m_χ (5–16 keV) from XMM-Newton
blank-sky observations. It never quotes an axion-photon coupling.

**Why the GT cannot grade it:** the repo `AxionPhoton/XMM-Newton.txt` g_aγγ
curve is the maintainer's derived conversion to decaying-ALP dark matter; the
GT demands a quantity that is not extractable from the paper. Same class as
the 2112.03439 Breakthrough Listen exclusion. The extractor's refusal
(ct=None) was correct.

**What would un-exclude it:** a vetted line-flux → g_aγγ converter applied on
both sides at scoring time.

---

## AxionLimitBench exclusions (2026-09-16 failure audit, 18 papers / 19 entries)

Applied by `data/build_references.py` from the per-paper audit in `results/agent_claude_code/fable5_failure_audit_2x.json`.
Each is a defect of the reference itself: a curve digitised from a superseded arXiv version, a projection or
prediction ingested as a measured limit, or a file whose values cannot correspond to the paper. Un-exclude by
re-digitising the reference from the current version (future work) or, for prediction bands, never.

| arXiv id | reason | evidence |
|---|---|---|
| 1912.07751 | Reference digitised from a superseded arXiv version | UPLOAD.txt header 'UPLOAD 1st paper'; v3 (June 2021) erratum moved the limit from ~1e-6 to 3e-3 GeV^-1 (3.8 dex); both benchmark arms are 'catastrophic' on the stale curve |
| 2312.13723 | Reference digitised from a superseded arXiv version | Cavities.txt matches v1 Fig. 2 (floor d_me ~2-10); v2 (Sept 2024) revised the floor by ~4 dex and added a GPS region |
| 2402.17140 | Reference digitised from a superseded arXiv version | JWST.txt (eps 3.5e-10 -> 1.9e-12) is v1's in-space constraint, withdrawn in v3 which keeps only a projection 2-2.5 dex lower |
| 2209.06299 | Reference digitised from a superseded arXiv version | INTEGRAL.txt reproduces v1 Fig. 3; v4 is 'revised to correct for error in bounds' (rendered both versions) |
| 2412.09595 | Reference digitised from a superseded arXiv version | SuperKamiokande.txt floor 5e-6 is v1; v2-v4 corrected the floor to 2e-5 |
| 2101.02805 | Reference encodes a projected curve, not the measured limit | DarkEfield.txt level (~1e-13, starting at 60 MHz) matches Fig. 12's green Phase-I '5 sigma extrapolated ... after 1 month' projection, not the blue Pilot limit (~1e-12, abstract 'eps ~ 1e-12') |
| 2205.06817 | Reference is a projection from mock data ingested as a measured limit | Paper Sec. III.D: 'we place projected constraints' from mock IPTA data; IPTA.txt is drawn UnfilledLimit in the compilation |
| 2404.00616 | Reference is a projected constraint stored outside Projections/ | fa/I2Ca.txt is Fig. 3(b)'s 'projected constraint ... this work' with is_projection=false in the pool |
| 1708.02111 | Reference is a 1-sigma hint band, not an exclusion limit | WDhint.txt encodes g_ae = 1.6 +0.29/-0.34 e-13 (a white-dwarf cooling hint); the paper's only 'bound' on g_ap is the PDG SN value re-parametrised |
| 1512.06746 | QCD-axion mass prediction band (m_lo, m_hi), no coupling column | AxionMass/Bonati16.txt is a theory prediction; same class as the 13 PlotTheoryMass entries already excluded |
| 1606.07494 | QCD-axion mass prediction band (m_lo, m_hi), no coupling column | AxionMass/Borsanyi16.txt (50-1500 ueV band); same class as the existing PlotTheoryMass exclusions |
| 1708.07521 | QCD-axion mass prediction band (m_lo, m_hi), no coupling column | AxionMass/Klaer17.txt; the pipeline's 0.127 dex 'hit' is an f_a number against the band's upper mass edge |
| 2401.17253 | QCD-axion mass prediction band (m_lo, m_hi), no coupling column | AxionMass/Saikawa24.txt (95-450 ueV band) |
| 1412.0789 | QCD-axion mass window stored as a single reference point | AxionMass/SaikawaDW_6_10.txt is the N_DW=6 PlotTheoryMass window (5.8e-4, 4.5e-3 eV), not a measured limit |
| 2410.02218 | Reference has a mis-set log-axis calibration | fa/ONIX.txt vs the figure's vector paths: GT_log = 1.55 x true + 5.6 (up to 1.6 dex off at 1e-20 eV); AxionEDM/ONIX.txt is the same digitisation in the g_d plane |
| hep-ex/0702006 | Reference mixes later buffer-gas results into this paper's curve | CAST_highm.txt above 0.02 eV (2e-10 flat to 1.17 eV) is the Phase II 4He/3He result, absent from the 2007 vacuum paper whose Fig. 8 rises ~m^2 above 0.02 eV |
| 2208.03183 | Reference resonance placed at the wrong mass | SQMS.txt centred on 1.3048 GHz vs the paper's f0 = 1.294605478 GHz (42 peV off for a 16-peV-wide feature, tail mirrored); no correct extraction can overlap it |
| 1902.04644 | Reference file belongs to a different paper | CASPEr_ZULF.txt is the stochastic-corrected (x8.4) curve from 1905.13650 (docs/an.md), not this paper's Fig. 3 (values exceed the plotted axis range) |

## AxionLimitBench (2026-09-17): found by two independent re-audits of the agent's 37 remaining misses

| arXiv id | reason | evidence |
|---|---|---|
| 2201.02042 | Reference matches neither curve of the paper's exclusion figure | CsCav.txt vs a vector trace of Fig. 2(a) g_gamma panel (e-print exclusions.pdf): Exp. B (the paper's exclusion; p. 11 states the Exp. A threshold is 'the sensitivity region, these are not limits') minus curator = +0.02..+1.06 dex (median +0.69), Exp. A minus curator = -1.01..-0.42; the file's log-curve is stretched about ~1e-7 eV, which no constant conversion produces. The agent's trace sits on Exp. B (median +0.05 dex). ScalarElectron/CsCav.txt shows the same stretched shape (audit A) |
| 2207.05767 | Reference digitised from a superseded arXiv version | FAST.txt lies BELOW the local minimum of the v2 (Mar 2023, e-print final-plot.pdf) red curve at 180 of 237 masses (median 0.16 dex below the minimum), so it is not a trace of v2; it matches v1's stronger curve (rho_DM 0.4 -> 0.3 and reanalysis between versions). The agent's per-bin medians match the v2 curve to 0.03 dex |
| 2110.10262 | Reference follows a figure mass axis inconsistent with the paper's stated scan | ADMX_Sidecar_JTWPA.txt spans 19.8344-19.8452 ueV = 4795.9-4798.6 MHz, but the abstract scans 4796.7-4799.5 MHz (h f = 19.8385-19.8501 ueV); the e-print figure's top mass axis is offset ~0.9 MHz from h f of its own frequency axis and the curator digitised against it. In a 2.7-MHz window whose depth varies by ~1 dex, no extraction from the stated scan range overlaps it correctly (agent shape matches, coverage 0.67, 0.49 dex) |
