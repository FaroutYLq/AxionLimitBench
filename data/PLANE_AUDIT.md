# AxionLimitBench AxionLimitBench: verification of proposed GT plane corrections

Read-only audit against the upstream compilation checkout
(the AutoAxionLimits checkout: `PlotFuncs.py`,
`PlotFuncs_ScalarVector.py`, `Vectors.ipynb`, `Scalars.ipynb`, `AxionCPV.ipynb`,
`AxionProton.ipynb`, `limit_data/**`) and the bench ingestion rules
(`AxionLimitBench/scorer/ground_truth.py`, `scorer/conventions.py`, `docs/TASK.md`).
Where a stored file could be in one of two planes, I digitised the source paper's
figure (cached PDFs in `~/.cache/aal_pdf_cache/`) and compared the ratio
file/paper across the mass range; the ratio is quoted in the table.

Constants used: e = sqrt(4 pi alpha_EM) = 0.30282 (Heaviside-Lorentz);
m_n = 0.93957 GeV, m_p = 0.93828 GeV (the values in `PlotFuncs.py`);
M_Pl^2/(4 pi u^2) = 1.367e37 (the `1.37e37` in the notebooks: M_Pl = 1.2209e19 GeV, u = 0.9315 GeV);
hbar c = 1.9733e-7 eV m.

Confidence key: H = code + header + paper agree, or paper-figure digitisation ratio is
flat and unambiguous; M = code and header agree but no independent paper check;
L = inferred.

---

## 1. VectorBL: which files store g_B-L and which store epsilon = g/e

**Plotting code.** Every VectorB-L file is loaded by `class VectorBL` in
`PlotFuncs_ScalarVector.py` (lines 375-508) and passed unchanged to
`FilledLimit`/`UnfilledLimit` (`PlotFuncs.py` 65-83: `plt.fill_between(dat[:,0],dat[:,1],...)`).
No y-factor is applied at plot time for ANY VectorB-L file. The y axis is labelled
`Gauge coupling, $g_{B-L}$` (`Vectors.ipynb` cell 0, `FigSetup(... g_min=1e-29, g_max=1e-9 ...)`).

**So the plane of each file is whatever O'Hare wrote into it**, and this is mixed:

* O'Hare's own conversions show that his intended plane is the gauge coupling g
  (HL normalisation, alpha_g = g^2/4pi): on 2024-06-17 (commit `3aea3908`) he added a
  notebook cell `dat = loadtxt('limit_data/VectorB-L/PPTA.txt'); dat[:,1] *= 0.303;
  savetxt(...)` converting PPTA from the paper's epsilon to g (old file 2.33e-25 =
  raw paper epsilon; new 7.06e-26). MICROSCOPE (paper quotes `g_B-L <~ 7e-26`,
  file min 7.00e-26), POLONAISE (paper `g_B-L <~ 2.98e-21`, file 2.95e-21),
  Eot-Wash DM (paper `g_B-L (hbar c)^-1/2`), and the 2304.12907 stellar bounds
  (paper's `g_Z'`, ratio file/paper = 1.0) are all stored in g.
* But `Vectors.ipynb` cell 1 builds ISL and Casimir from the scalar-nucleon g by
  `dat[:,1]*sqrt(137/(4*pi))` (= 1/e = 3.302) "rescaled to g_B-L defined relative to
  EM", i.e. those two are in epsilon = g/e, and the EP, KAGRA, both LIGO files,
  and both LISA Pathfinder files are ALSO in epsilon (verified below). These are
  unconverted leftovers, inconsistent with the PPTA/MICROSCOPE/POLONAISE/EotWashDM
  files on the same axis (a factor 3.3 internal inconsistency in the compilation;
  worth reporting upstream).

Canonical task-card plane: `g_BL (dimensionless)` = gauge coupling g. **Bench must
multiply the epsilon files by e = 0.30282**; the g files need no change. The claim
in the task (EotwashEP, KAGRA, LISAPathfinder stored as epsilon, multiply by
0.3028) is CORRECT, and the same applies to LIGO-O1, LIGOVirgo,
LISAPathfinder-RelativeAcceleration, InverseSquareLaw and Casimir. EotWashDM is
NOT in epsilon (claim in the task list is a question; answer: it is in g).

| file (limit_data/VectorB-L/) | header | plotting line | stored variable | conversion to canonical g_B-L | conf. |
|---|---|---|---|---|---|
| EotwashEP.txt (1207.2442) | `mass [eV]  g_B-L` | PSV.py 382-383 raw | epsilon = g_HL/e. Paper Fig. 6 gives Yukawa alpha~ (alpha~ = g~^2/(4 pi G u^2), Eq. 4); long-range plateau alpha~ = 1.5e-11 -> g_HL = sqrt(1.5e-11/1.37e37) = 1.05e-24; file plateau 3.65e-24 = g_HL/e (0.02 dex). Eot-Wash themselves draw this EP line at g = 1.06e-24 in 2109.08822 Fig. 5, confirming g_HL = 1.05e-24. | y * 0.30282 | H |
| KAGRA.txt (2403.03004) | `mass [eV] g_B-L` | PSV.py 424-425 raw | epsilon_B-L (paper Fig. 5 y-axis is epsilon_B-L, "gauge coupling normalised by the EM coupling", Eq. 1 `-eps_D e J A`). Digitised min(blue,orange) envelope: file/paper = 1.03 +- 0.05 over 20-900 Hz (x e would give 0.30). | y * 0.30282 | H |
| LISAPathfinder.txt (2301.08736) | `Rescaled by factor 2 for B-L coupling rather than B; mass [eV] g_B-L` | PSV.py 439-440 raw | 2 x epsilon_B (paper Fig. 5 is epsilon^2 for baryon coupling, Eq. 2 `-eps e J A`). Digitised upper envelope of fully-coherent limits: file / (2 sqrt(eps^2_top)) = 0.94-1.08 over 1e-19..5e-15 eV (x e would give ~3.3). | y * 0.30282 | H |
| LISAPathfinder-RelativeAcceleration.txt (2310.06017) | `mass [eV]  g_B-L` | PSV.py 444-445 raw | epsilon_B-L (paper Fig. 3 "rescaled coupling eps_B-L", g = eps e). Vector-digitised min(x,y,z) curves: file/paper = 0.82 +- 0.05 constant (a digitisation offset, not 0.30). | y * 0.30282 | H |
| **CORRECTION AxionLimitBench** | | | The row above is WRONG: the paper (p. 7) states Fig. 5's y-axis is g_B-L = eps e, the header says g_B-L and the file matches Fig. 5 to <0.1 dex (agent 8.83e-26 vs file 9.43e-26 at 4.2e-19 eV); the 0.82 ratio was against Fig. 3's per-axis eps curves, a different quantity. Factor removed; the file is ingested raw. | none | H |
| LIGO-O1.txt (2105.13085, misnamed; NOT Guo et al. 1905.04316: shape 10x off) | `mass [eV]  g_B-L` | PSV.py 429-430 raw | 2 x epsilon_B from arXiv v1 Fig. 3 BSD (black/cyan) curve ("multiply by four" on eps^2 -> x2 on eps). file / (2 eps_B,BSD-bottom) = 2.0-2.4 over 30-1500 Hz i.e. file ~ 2 x eps_B. | y * 0.30282 | M (curve id ambiguous, plane not) |
| LIGOVirgo.txt (2105.13085) | `mass [eV]  g_B-L` | PSV.py 434-435 raw | 2 x epsilon_B from arXiv v1 Fig. 3 cross-correlation lower envelope: file / eps_B = 2.00 +- 0.02 over 30-1500 Hz (flat). | y * 0.30282 | H |
| InverseSquareLaw.txt | `compiled from ScalarNucleon/Union_InverseSquareLaw.txt, rescaled to g_B-L defined relative to EM` | PSV.py 387-388 raw; built in `Vectors.ipynb` cell 1: `dat[:,1]*sqrt(137/(4*pi))` | g_HL/e = epsilon | y * 0.30282 | H |
| Casimir.txt (quant-ph/0106045 etc.) | same "relative to EM" header | PSV.py 392-393 raw; built in cell 1: `sqrt(dat[:,1]/1.37e37)*sqrt(137/(4*pi))` on ScalarNucleon/Casimir.txt (alpha) | g_HL/e = epsilon | y * 0.30282 | H |
| EotwashDM.txt (2109.08822) | `mass [eV]  g_B-L` | PSV.py 418-419 raw | g_B-L (paper Fig. 5 y = `g_B-L (hbar c)^-1/2`, which is the HL g: its EP line sits at 1.06e-24 = sqrt(4 pi alpha~ G u^2)). Digitised X-panel top envelope: file/paper = 1.0-1.5 (spike envelope), NOT 3.3. | none | H |
| MICROSCOPE.txt (2403.02381) | `mass [eV]  g_B-L` | PSV.py 377-378 raw | g_B-L (paper: `g_B-L <~ 7e-26`, `|g_B-L| = (4/5)|eps_B-L| e`); file min 7.00e-26 | none | H |
| POLONAISE.txt (2409.03814) | `mass [eV]  g_B-L` | PSV.py 500-501 raw | g_B-L (paper `L = -g_B-L j A`, `g_B-L <~ 2.98e-21`); file min 2.95e-21 | none | H |
| PPTA.txt (2112.07687) | `Mass [eV] g_B-L` | PSV.py 449-450 raw | g = eps x 0.303 (commit 3aea3908 cell `dat[:,1] *= 0.303`). Vector-digitised Fig. 1 right (eps^2): file/eps = 0.30 flat over 3e-24..9e-22 eV | none | H |
| Sun.txt, HorizontalBranch.txt, RedGiant.txt (2304.12907) | `mass [eV] g_B-L` | PSV.py 403-414 raw | g_Z' from Fig. 4 B-L panel (`D_mu = d_mu - i g_Z' Q_X X_mu`, HL); vector-digitised ratio file/paper = 0.8-1.1 for all three | none | H |
| DMStability.txt (2205.03617) | `mass [eV] g_B-L` | PSV.py 397-398 raw | gauge coupling g: file = 1.1 x sqrt(8 pi H0/m) (Gamma(V->nu nu) = H0) for m >> 2 eV | none | H |
| Projections/OptomechanicalMembranes (2007.04899), HELIOS (2309.07995), TorsionBalance/SKA (1512.06165), LISA/Asteroids (2210.09324), STE-QUEST, MAGIS100 | `g_B-L` | PSV.py 456-495 raw (UnfilledLimit) | papers quote g_B-L directly (2007.04899 Eq. 12, 2309.07995 Fig. 1 "vector coupling constant g_B-L", 1512.06165 Eq. 1); stored raw | none (assumed) | M/L, out of measured-limit scope |

Bench note: `scorer/conventions.py` has no VectorBL epsilon->g converter
(`_FOREIGN_CLASS_TOKENS_BY_CT["VectorBL"]` only fails closed on "alpha"); the
epsilon-plane GT files above need a per-file `_FILE_Y_SCALE`-style factor 0.30282
at ingestion (or a `_FILE_CONVENTION` token "eps_over_e" with `to_canonical` -> `g = e*eps`).

---

## 2. DarkPhoton/Solar-Global.txt (1501.01639)

| file | header | plotting line | stored | conversion | conf. |
|---|---|---|---|---|---|
| limit_data/DarkPhoton/Solar-Global.txt | `# mass [eV]  kinetic mixing * mass [eV]`; two rows `1e-6 1.7878e-12`, `5e-1 1.7878e-12` | `PlotFuncs.py` 3572-3574: `Solar = loadtxt(".../Solar-Global.txt"); plt.fill_between(Solar[:,0],Solar[:,1]/Solar[:,0],...); plt.plot(Solar[:,0],Solar[:,1]/Solar[:,0],...)` | chi * m [eV] = 1.788e-12 eV (the paper's global-fit bound chi m_gamma' < 1.8e-12 eV) | chi = y / x, i.e. divide the y column by the mass column at ingestion (x unchanged). Canonical: `kinetic mixing chi (dimensionless)`. | H |

The claim is confirmed exactly by the code. Currently the bench ingests the raw
1.79e-12 as if it were chi (wrong by 6-12 dex across the file's mass range).

---

## 3. AxionPhoton/COBEFIRAS_Cyr.txt (2411.13701)

| file | header | plotting line | stored | conversion | conf. |
|---|---|---|---|---|---|
| limit_data/AxionPhoton/COBEFIRAS_Cyr.txt | `# epsilon defined as g_agamma*B0_T/(1e-11 GeV^-1 * 1 nG)`; `mass [eV] epsilon`; 164 pts, eps = 1.2e-4 (5e-14 eV) rising to a plateau 3.2e-2 (1e-9..1e-5 eV) | **Not plotted anywhere**: no `PlotFuncs.py` method or notebook cell loads it (only `docs/ap.md` line 267 links it; `AxionPhoton.COBEFIRAS` at PlotFuncs.py 1489 loads `COBE-FIRAS.txt`, a different file). Added in commit 1f01cc27 (2024-12-16). | epsilon of paper Eq. (3c): `eps = g_agamma B0_rms,T / (1e-10 GeV^-1 nG)` (paper text; the header's 1e-11 is a typo). The file matches Fig. 11's FIRAS curve (single-conversion black + multiple-conversion red at low mass). | g_agamma [GeV^-1] = **y * 1e-10** at B0_rms,T = 1 nG, f = 1. Cross-check: vector-digitised Fig. 13 "B0_rms = 1 nG" FIRAS curve vs y*1e-10 gives ratio 1.02-1.15 over 1e-13..5e-5 eV; y*1e-11 gives 0.10-0.11 (1 dex too strong). | H |

The bench's current `_FILE_Y_SCALE = {"...COBEFIRAS_Cyr.txt": 1e-11}` follows the
header typo and makes the GT 10x stronger than the paper's Fig. 13 headline.
Change to 1e-10. (Plane caveat unchanged: the g-plane curve is model-dependent on
B0 = 1 nG, which is the Fig. 13 headline choice.)

---

## 4. Scalar files flagged by the range heuristic (ymax > 1e3 -> d_e_large / coupling_large)

**Plotting code.** Every `ScalarPhoton/*` and `ScalarElectron/*` file is loaded by
`class ScalarPhoton` (PSV.py 47-208) / `class ScalarElectron` (211-373) and passed
unchanged to `FilledLimit`/`UnfilledLimit`; there is no arithmetic on `dat` anywhere
in those classes. The notebook axes are `Scalars.ipynb` cell 0:
`FigSetup(... ylab='Scalar-EM coupling, $d_e$', g_min=1e-13, g_max=1e10 ...)` and cell 1:
`ylab='Scalar-electron coupling, $d_{m_e}$', g_min=1e-14, g_max=1e8`, with
`AlternativeCouplingAxis(ax, scale=1/(sqrt(2)*M_pl))` giving g_phi-gamma. So large
values ARE d_e / d_me: weak clock/cavity/interferometer bounds legitimately sit at
d ~ 1e3-1e10 on the compilation's own axis. **The heuristic is wrong for the
ScalarPhoton and ScalarElectron directories: every file there is already canonical
d_e / d_me and should be compared raw.** Only two files are whitelisted today
(`_HEADER_CANONICAL_DE_FILES`: HQuartzSapphire, DyQuartz); the rest are falsely
excluded as convention mismatches.

Values >= 1e19 are already filtered by the scorer (`_SENTINEL_FLOOR`), but the
1e10 polygon-closure walls in DyQuartz, Cavities, RbQuartz, HELIOS are not, so
those trip the threshold purely on a wall value (interior max 48, 191, 3.9e4).

| file | header | plotting line | interior y (walls excl.) | stored variable | conversion | conf. |
|---|---|---|---|---|---|---|
| ScalarPhoton/Holometer.txt (2108.04746) | `mass [eV]  d_e` | PSV.py 138-139 raw | 9.4e3 .. 4e13 (genuine curve, top part above the 1e10 axis) | d_e | none (canonical) | H |
| ScalarPhoton/DAMNED.txt (2006.07055) | `d_e` | 121-122 raw | 0.14 .. 7.7e6 (wall 1e30) | d_e | none | H |
| ScalarPhoton/DynamicDecoupling.txt (1902.02788) | `d_e` | 144-145 raw | 4.8e5 .. 1.2e11 (wall 1e30) | d_e | none | H |
| ScalarPhoton/CsCav.txt (2201.02042) | `d_e` | 150-151 raw | 1.1e4 .. 1.6e8 (wall 1e30) | d_e | none | H |
| ScalarPhoton/I2.txt (2111.06883) | `d_e` | 116-117 raw | 1.2e4 .. 7e9 (wall 1e30) | d_e | none | H |
| ScalarPhoton/GEO600.txt (2103.03783) | `d_e` | 127-128 raw | 0.19 .. (wall 1e30) | d_e | none | H |
| ScalarPhoton/LIGO.txt (2401.18076) | `d_e` | 132-133 raw | 0.16 .. (wall 1e20) | d_e | none | H |
| ScalarPhoton/HQuartzSapphire.txt (2010.08107) | `d_e` | 111-112 raw | 1.6 .. 7.6e5 (wall 1e20) | d_e (already whitelisted) | none | H |
| ScalarPhoton/DyQuartz.txt (2212.04413) | `d_e` | 79-80 raw | 1.8e-3 .. 48 (wall 1e10 only) | d_e (already whitelisted) | none | H |
| ScalarPhoton/QSNET.txt (2302.04565) | `mass [eV] d_gamma` | 85-86 raw | 1.1e-7 .. (wall 1e20) | d_e (d_gamma is the same quantity) | none | H |
| ScalarPhoton/GlobularClusters.txt (2207.03102) | `m_phi d_e` | 64-65 raw | 1.6e8 flat | d_e | none | H |
| ScalarPhoton/FifthForce.txt (compiled) | `d_e` | 59-60 raw; built in Scalars.ipynb cell 2 as `500*sqrt(alpha)` | 3.9e-3 .. 2e18 | d_e (Q_e = 1/500 assumption) | none | H |
| ScalarElectron/Cavities.txt (2312.13723) | `mass [eV]  d_me` | 274-275 raw | 1.66 .. 191 (wall 1e10 only) | d_me | none | H |
| ScalarElectron/Holometer.txt (2108.04746) | `d_me` | 279-280 raw | 9.4e3 .. 4e13 | d_me | none | H |
| ScalarElectron/DAMNED.txt (2006.07055) | `d_me` | 264-265 raw | 0.08 .. 1.9e7 | d_me | none | H |
| ScalarElectron/CsCav.txt | `d_me` | 269-270 raw | 2.7e4 .. 3.6e8 | d_me | none | H |
| ScalarElectron/I2.txt | `d_me` | 249-250 raw | 2e5 .. 1.3e10 | d_me | none | H |
| ScalarElectron/GEO600.txt, LIGO.txt | `d_me` | 254-255, 294-295 raw | 0.19/0.15 .. walls | d_me | none | H |
| ScalarElectron/HQuartzSapphire.txt | `d_g = 0; d_me` | 259-260 raw | 5.9 .. 2.4e5 | d_me (d_g = 0 scenario) | none | H |
| ScalarElectron/HSi.txt (2008.08773) | `d_me` | 239-240 raw | 1.2e-5 .. wall 1e30 | d_me | none | H |
| ScalarElectron/RbQuartz.txt (2212.04413) | `d_me` | 284-285 raw | 52 .. 3.9e4 (wall 1e10) | d_me | none | H |
| ScalarElectron/YbCs.txt (2212.05721) | `d_me` | 289-290 raw | 1.6e-6 .. wall 1e20 | d_me | none | H |
| ScalarElectron/EotWashEP.txt (1807.04512) | `m_phi |d_me - d_g|` | 219-220 raw | 1.2e-2 .. 3.1e3 | |d_me - d_g| plotted as d_me | none (compare raw; note the combination) | H |
| ScalarElectron/FifthForce.txt (compiled) | header says `d_e` (typo; built as `4000*sqrt(alpha)` in Scalars.ipynb cell 3 with Q_me = 1/4000) | 224-225 raw | 3e-2 .. 1.5e22 | d_me | none | H |
| ScalarElectron/RedGiants.txt (1611.05852) | `m_phi d_me` | 229-230 raw | 4.7e6 flat | d_me | none | H |
| ScalarElectron/WhiteDwarfs.txt (2303.00778) | `m_phi d_me` | 234-235 raw | 2.6e6 flat | d_me (the conventions.py comment "correctly kept excluded" is wrong; its own sin-theta converter was spot-checked against this file as d_me) | none | H |
| ScalarPhoton/ScalarElectron Projections (Resonator-*, NuclearClock, HELIOS) | `d_e` / `d_me` | 178-200, 333-371 raw | up to 8.9e5 / 5e7 / 1e10 wall | d_e / d_me | none | H (out of measured scope) |

Recommendation: drop the `ymax > 1e3` override for ScalarPhoton/ScalarElectron
entirely (return the canonical token); the plane inference for these directories
should come from the header (`d_e`, `d_me`, `d_gamma`, `|d_me - d_g|`), all of which
are the canonical variable. For ScalarNucleon/ScalarBaryon see item 5: the
non-canonical files there are identified by the `lambda [m]  alpha` header, not by
magnitude (several alpha files have y < 1e3 and are currently NOT flagged).

---

## 5. Fifth-force alpha files (ScalarNucleon / ScalarBaryon, header `lambda [m]  alpha`)

**Plotting code** (`AxionCPV.ipynb` cell 0 and cell 3):

```python
def mLambda(m_a):                  # cell 0
    return 0.1973*1e-6/m_a         # lambda[m] <-> m[eV]
def g_scalar_nucleon(alph):        # cell 0: "Scalar-nucleon coupling from Yukawa alpha"
    return sqrt(alph/1.37e37)
...
fig,ax = FigSetup(ylab=r'Scalar nucleon coupling, $g_s^N$', ...)   # cell 3
dat = loadtxt(dirc+'IUPUI.txt'); dat[:,0] = mLambda(dat[:,0]); dat[:,1] = g_scalar_nucleon(dat[:,1])*g_scale
dat = loadtxt(dirc+'Stanford.txt'); dat[:,0] = mLambda(dat[:,0]); dat[:,1] = g_scalar_nucleon(dat[:,1])*g_scale
# same for EotWash2006/2020, HUST2012/2020, Irvine, Wuhan, Maryland, YaleCasimir, Casimir, EP files
```
and `MakeJoinedLimit_ScalarNucleon` (cell 0) builds `Union_InverseSquareLaw.txt`,
`Union_EquivalencePrinciple.txt`, `Union.txt` (header `m [eV]  g_s_nucleon [dimensionless]`)
with the same two maps. The claim `g_s^N = sqrt(alpha/1.37e37)` is CONFIRMED verbatim.

Derivation of the constant: with the Yukawa strength defined relative to gravity per
atomic mass unit, alpha = g^2/(4 pi G u^2) (Wagner et al. Eq. 4; V = (g^2/4 pi) q1 q2 e^{-r/lambda}/r,
HL normalisation), so g = sqrt(4 pi G u^2 alpha) = sqrt(alpha / (M_Pl^2/(4 pi u^2))) =
sqrt(alpha/1.367e37) = **2.702e-19 sqrt(alpha)**. This is a dimensionless
scalar-nucleon coupling in the `L = g_N phi N-bar N` sense of the task card.

| file | header | plotting line | stored | conversion to canonical `coupling (dimensionless)` | conf. |
|---|---|---|---|---|---|
| ScalarNucleon/IUPUI.txt (1410.7267) | `lambda [m]  alpha` (7.5e3..2.2e17) | AxionCPV cell 3 (above) | Yukawa alpha vs lambda | x -> 1.9733e-7/lambda (bench already does this); **y -> sqrt(y/1.37e37) = 2.702e-19 sqrt(y)** | H |
| ScalarNucleon/Stanford.txt (0802.2350) | `lambda [m]  alpha` (2.3e2..9.7e9) | cell 3 | alpha | same | H |
| ScalarNucleon/Casimir.txt (2009.04517) | `lambda [m]  alpha` (1.4e12..7e18) | via Union / Vectors.ipynb cell 1 `sqrt(dat/1.37e37)` | alpha | same | H |
| ScalarNucleon/EotWash2006, EotWash2020, HUST2012, HUST2020, Irvine, Maryland, Wuhan, YaleCasimir, EotWash_EP_1999, EotWash_EP_2007_left/right, MICROSCOPE (1712.00483) | `lambda [m]  alpha` | cell 3 / cell 0 union | alpha; NOTE several have alpha < 1e3 (HUST2012 1e-3..1e-2, Irvine, Wuhan, EP files 1e-10..4e-2, MICROSCOPE 1e-11..8e-5) so the range heuristic does NOT flag them and they are currently compared raw as if dimensionless (10-19 dex off) | same | H |
| ScalarBaryon/IUPUI.txt (1410.7267) | `lambda [m]  alpha`; byte-identical to ScalarNucleon/IUPUI.txt | not plotted anywhere (ScalarBaryon has no plot; the dir only feeds Scalars.ipynb cells 2/3) | alpha | same as ScalarNucleon: y -> sqrt(y/1.37e37) (the compilation has no separate g_B plane; the only repo use of ScalarBaryon alpha is `500*sqrt(alpha)` -> d_e and `4000*sqrt(alpha)` -> d_me, i.e. a d_e-plane recast, not a baryon coupling) | M (plane choice is the bench's; formula H) |
| ScalarBaryon/MICROSCOPE.txt (1712.00483), EotWash_EP_1999.txt, FifthForce_CI.txt (hep-ph/0307284), FifthForce_Mars.txt | `lambda [m]  alpha` | Scalars.ipynb cells 2-3 (`d_e = 500*sqrt(alpha)`, `d_me = 4000*sqrt(alpha)`) | alpha | same as above for the ScalarBaryon plane; if a ScalarPhoton/ScalarElectron GT is wanted use 500*sqrt / 4000*sqrt as the notebook does | M |
| ScalarNucleon/Raffelt.txt | `lambda [m]  g_s_N [dimensionless]` | AxionCPV cell 8 | already g_s^N | x -> hbar c/lambda only; **no y conversion** (bench's lambda->eV path applies no y factor: OK) | H |
| ScalarNucleon/NeutronStars.txt, Union*.txt | `mass [eV]  g^s_N` | cell 3 raw | g_s^N | none | H |
| ScalarNucleon/RedGiant.txt (1611.05852), WhiteDwarfs.txt (2303.00778) | `m [eV]  alpha_NN [dimensionless]` / `g` | not plotted in the current notebook | ambiguous (alpha_NN may be g^2/4pi) | unverified; do not apply the fifth-force formula blindly | L |

**Scorer's existing alpha handling is wrong for ScalarNucleon/ScalarBaryon.**
`conventions.py` 476-481: for `conv in ("alpha_fifthforce","alpha","yukawa_alpha")`
it returns `pref*sqrt(alpha)` with `pref = 4000` (ScalarElectron) else `500`, i.e. it
maps alpha onto the d_e plane (the Scalars.ipynb Q_e = 1/500 recast) even when
`coupling_type` is ScalarNucleon or ScalarBaryon, where the canonical variable is
g_N = 2.702e-19 sqrt(alpha): a 21.3 dex error (500 vs 2.7e-19). Also this converter
is only ever applied to the extraction side; `file_source_convention` returns None
for every Scalar* GT file, so the alpha GT files are never converted (they are
excluded by the range heuristic when alpha > 1e3, and compared raw when alpha < 1e3).
Fix: (a) at ingestion, when the header is `lambda [m]  alpha` and the directory is
ScalarNucleon or ScalarBaryon, apply y -> sqrt(y/1.37e37) alongside the existing
x -> hbar c / lambda; (b) in `to_canonical`, use pref = 2.702e-19 for ScalarNucleon /
ScalarBaryon (keep 500 / 4000 only for ScalarPhoton / ScalarElectron).

---

## 6. AxionNeutron/SNO.txt (2004.02733)

| file | header | plotting line | stored | conversion | conf. |
|---|---|---|---|---|---|
| limit_data/AxionNeutron/SNO.txt | `m_a [eV]  g_an/m_n [GeV^-1]` (4e-5..1.6e-3) | `PlotFuncs.py` 2721-2722: `dat = loadtxt("limit_data/AxionNeutron/SNO.txt"); dat[:,1] *= AxionNeutron.m_n  # Note that their notation defines their g_an as my g_an/m_n not g_an/2m_n as other use.` (m_n = 0.93957, line 2475) | g_an/m_n [GeV^-1] | y * m_n = y * 0.93957 (NOT 2 m_n) | H |
| limit_data/AxionProton/SNO.txt | `m_a [eV]  g_ap/m_p [GeV^-1]` | 2871-2872: `dat[:,1] *= AxionProton.m_p` (0.93828) | g_ap/m_p | y * 0.93828 | H |

Bench: `_FILE_CONVENTION` maps both SNO files to `"g_aN_over_mN_inv_gev"` and
`to_canonical` applies `f = m_n` (conventions.py 470-474). This is CORRECT and
matches PlotFuncs; SNO is the documented exception to the family default
`g_aNN_inv_gev` (x 2 m_N). No change needed.

---

## 7. AxionNeutron / AxionProton: every file, header and plot-time factor

Family default in the bench (`file_source_convention`): `g_aNN_inv_gev` -> x 2 m_N
for any file not in `_FILE_CONVENTION`. Class constants: `AxionNeutron.m_n = 0.93957`,
`AxionProton.m_p = 0.93828` (identical to `_M_NUCLEON_GEV`). Line numbers are
`PlotFuncs.py`. "Bench" column = what the current scorer does; mismatches in bold.

| file | header | plotting line / factor | stored | conversion to canonical g_aN | bench today | conf. |
|---|---|---|---|---|---|---|
| AxionNeutron/129Xe.txt | `mass [eV] g_an` | 2703-2705 raw | g_an | none | None (ok) | H |
| AxionNeutron/CASPEr_Comagnetometer.txt (1905.13650) | `g_an/2m_n [GeV^-1]` | 2652 `*= 2*m_n` | GeV^-1 | x 2 m_n | default (ok) | H |
| AxionNeutron/CASPEr_ZULF.txt (1902.04644) | `g_an/2m_n [GeV^-1]` | 2635 `*= 2*m_n` | GeV^-1 | x 2 m_n | default (ok) | H |
| AxionNeutron/Casimir.txt (2009.04517) | `g_an` | 2712-2714 raw | g_an | none | None (ok) | H |
| AxionNeutron/ChangE.txt (2306.08039), ChangE-NMR.txt (2309.16600) | `g_an/2m_n [GeV^-1]` | 2562, 2567 `*= 2*m_n` | GeV^-1 | x 2 m_n | default (ok) | H |
| AxionNeutron/Hefei.txt (2102.01448) | `g_an/2m_n [GeV^-1]`; header warns the analysis omitted the 129Xe neutron spin fraction 0.63 | 2613 `dat[:,1] *= 2*AxionNeutron.m_n/0.63  # last factor is to correct for missing spin fraction` | GeV^-1, paper-native (uncorrected) | **x 2 m_n / 0.63 = x 2.983** to reproduce the compilation's plotted curve (x 2 m_n reproduces the paper) | **default x 2 m_n only: GT is 0.63x (-0.20 dex) below the plotted curve**; decide which is "the GT" and make it explicit | H |
| AxionNeutron/JEDI.txt (2208.07293) | `mass g_an` (flat 1.33e-5 over 4.6e-10..5.6e-10 eV) | 2593-2594: `dat = loadtxt('limit_data/AxionNeutron/JEDI.txt'); plt.fill_between(dat[:,0],dat[:,1],y2=1e0,...)` **raw, no factor** | numerically the paper's |C_d/f_a| < 1.5e-5 GeV^-1 with L = (C_f/2f_a) da Psi-bar gamma gamma5 Psi, so canonical g = m_N (C/f_a) = 1.4e-5, which is what the raw file value already equals (0.03 dex) | **none** | **default x 2 m_n = +0.27 dex error; add `"limit_data/AxionNeutron/JEDI.txt": None`** | H |
| AxionNeutron/K-3He_Comagnetometer.txt (0809.4700) | `g_an` | 2685-2687 raw | g_an | none | None (ok) | H |
| AxionNeutron/K-3He_Comagnetometer_DarkMatter.txt (2209.03289) | `g_aNN [GeV^-1]` | 2673 `*= 2*m_n` | GeV^-1 | x 2 m_n | default (ok) | H |
| AxionNeutron/Mainz_Krakow.txt (2408.02668) | `g_app/2m_p [GeV^-1]` (proton header in the neutron dir) | 2540 `*= 2*m_n` | GeV^-1 | x 2 m_n (as plotted) | default (ok) | H |
| AxionNeutron/NASDUCK.txt (2105.04603), NASDUCK-SERF.txt (2209.13588) | `g_aNN [GeV^-1]` | 2578, 2581 `*= 2*m_n` | GeV^-1 | x 2 m_n | default (ok) | H |
| AxionNeutron/NeutronStars.txt (2111.09892) | `g_an` | 2770-2772 raw | g_an | none | None (ok) | H |
| AxionNeutron/OldComagnetometers.txt (1907.03767) | `g_an/2m_n [GeV^-1]` | 2524 `*= 2*m_n` | GeV^-1 | x 2 m_n | default (ok) | H |
| AxionNeutron/PSI_HgM.txt (2212.02403) | `g_aNN [GeV^-1]` | 2603 `*= 2*m_n` | GeV^-1 | x 2 m_n | default (ok) | H |
| AxionNeutron/SN1987A.txt (1906.11844) | `g_an` | 2764-2766 commented out (not plotted) | g_an | none | None (ok) | H |
| AxionNeutron/SNO.txt (2004.02733) | `g_an/m_n [GeV^-1]` | 2722 `*= m_n` | see item 6 | x m_n | g_aN_over_mN (ok) | H |
| AxionNeutron/TorsionBalance.txt (hep-ph/0611223) | `g_an` (header notes it is a 2-boson-exchange bound) | 2695-2697 raw | g_an | none | None (ok) | H |
| AxionNeutron/nEDM.txt (1708.06367 / 1902.04644) | `g_an/2m_n [GeV^-1]` | 2552 `*= 2*m_n` | GeV^-1 | x 2 m_n | default (ok) | H |
| AxionNeutron/Projections/ElectrostaticStorageRing.txt (2211.08439) | `[GeV^-1]` (unspecified nucleon) | 2732 `*= 2*m_n` | GeV^-1 | x 2 m_n | default (ok) | H |
| AxionNeutron/Projections/CASPEr_ZULF, CASPEr_wind, FutureComagnetometers, SuperfluidHe3 | headers say `g_an/m_n [GeV^-1]` but code applies `*= 2*m_n` (2641, 2663, 2530, 2622) | header/code mismatch in the compilation; follow the code (x 2 m_n) if ever used | | x 2 m_n | default | M (projections, out of scope) |
| AxionProton/CASPEr-gradient.txt (2504.16044) | `g_aP [GeV^-1]` | `AxionProton.ipynb` cell 1: `PlotBound(ax,"limit_data/AxionProton/CASPEr-gradient.txt",...,scale_y=2*AxionProton.m_p)` (PlotFuncs.py 38-45 `dat[:,1] *= scale_y`) | GeV^-1 | x 2 m_p | default (ok) | H |
| AxionProton/Casimir.txt | `g_an` | 2862-2864 raw | g_ap | none | None (ok) | H |
| AxionProton/ChangE.txt, ChangE-NMR.txt | `g_ap/2m_p [GeV^-1]` | 2882, 2887 `*= 2*m_p` | GeV^-1 | x 2 m_p | default (ok) | H |
| AxionProton/Mainz_Krakow.txt | `g_app/2m_p [GeV^-1]` | 2897 `*= 2*m_p` | GeV^-1 | x 2 m_p | default (ok) | H |
| AxionProton/NASDUCK-SERF.txt | `g_ap/2m_p [GeV^-1]` | 2825 `*= 2*m_p` | GeV^-1 | x 2 m_p | default (ok) | H |
| AxionProton/NASDUCK.txt (2105.04603) | `g_ap/2m_p [GeV^-1]` ("limit retracted in published version") | 2819-2822 commented out (would be `*= 2*m_p`) | GeV^-1 | x 2 m_p | default (consistent with header) | M |
| AxionProton/NeutronStars.txt (2111.09892) | `g_ap` | 2948-2950 raw | g_ap | none | None (ok) | H |
| AxionProton/SN1987A.txt (2306.01048) | `g_ap` | 2942-2944 raw | g_ap | none | None (ok) | H |
| AxionProton/SNO.txt | `g_ap/m_p [GeV^-1]` | 2872 `*= m_p` | see item 6 | x m_p | ok | H |
| AxionProton/SuperKamiokande.txt (2412.09595) | `mass [eV] g_ap` (5.4e-6 flat below 1e6 eV, rising to 2.3e-4) | **not plotted anywhere** (docs/app.md: "at higher masses not shown"); no PlotFuncs/notebook reference | dimensionless g_ap: paper Eq. (1) `L = g_a (d_mu a / 2 m_N)[C_ap p-bar gamma gamma5 p + ...]`, `g_ap = g_a C_ap`, trapping-regime values quoted as `g_a = 5e-6, 1e-5, 5e-5`, exactly the canonical (g_aN/2m_N) normalisation | **none** | **default x 2 m_p = +0.27 dex error; the audit's "scorer wrongly x2m_p'd a dimensionless file" is CORRECT. Add `"limit_data/AxionProton/SuperKamiokande.txt": None`** | H |
| AxionProton/TorsionBalance.txt | `g_an` | 2854-2856 raw | g_ap | none | None (ok) | H |
| AxionProton/Projections/MnCO3.txt (2307.08577) | `g_app [dimensionless]` | 2916-2918 raw | g_ap | none | None (ok) | H |
| AxionProton/Projections/ProtonStorageRing.txt | `g_aNN [GeV^-1]  m_a [eV]` (column order as written looks swapped relative to the data; not checked further) | 2907 `*= 2*m_p` | GeV^-1 | x 2 m_p | default | L (projection) |
| AxionProton/DSNALPB_*.txt, GammaDecay_Bound_*.txt, SNEnergyDeposition_*.txt | no header | not plotted anywhere | unknown (values 1e-11..1e-4 look like dimensionless g_ap) | unverified | not in GT | L |

Summary for item 7: the "x 2 m_N for all AxionNeutron/AxionProton files" default
matches PlotFuncs for every file that PlotFuncs multiplies, and the existing
`_FILE_CONVENTION` None-list matches every raw-plotted file EXCEPT two GT entries:
**AxionNeutron/JEDI.txt** (plotted raw, PlotFuncs.py 2593-2594) and
**AxionProton/SuperKamiokande.txt** (unplotted, header `g_ap`, paper convention
canonical). Both need `None`. **AxionNeutron/Hefei.txt** additionally carries a
1/0.63 spin-fraction correction at plot time that the default omits.

---

## Consolidated list of bench changes implied by this audit

1. VectorBL ingestion: multiply y by e = 0.30282 for `VectorB-L/EotwashEP.txt`,
   `KAGRA.txt`, `LISAPathfinder.txt`, `LISAPathfinder-RelativeAcceleration.txt`,
   `LIGO-O1.txt`, `LIGOVirgo.txt`, `InverseSquareLaw.txt`, `Casimir.txt`. Leave
   `EotwashDM`, `MICROSCOPE`, `POLONAISE`, `PPTA`, `Sun`, `HorizontalBranch`,
   `RedGiant`, `DMStability` and the projections unchanged (already g).
2. `DarkPhoton/Solar-Global.txt`: y -> y / x at ingestion.
3. `AxionPhoton/COBEFIRAS_Cyr.txt`: `_FILE_Y_SCALE` 1e-11 -> 1e-10.
4. Remove the `ymax > 1e3` override for ScalarPhoton/ScalarElectron (all files are
   d_e/d_me, plotted raw); `_HEADER_CANONICAL_DE_FILES` whitelist becomes moot.
5. ScalarNucleon/ScalarBaryon `lambda [m]  alpha` files: y -> sqrt(y/1.37e37)
   (= 2.702e-19 sqrt(alpha)) at ingestion, keyed on the header (not on magnitude,
   since HUST2012, Irvine, Wuhan, EP and MICROSCOPE alpha files are < 1e3); and in
   `to_canonical` use 2.702e-19 (not 500) for ScalarNucleon/ScalarBaryon alpha.
   Remove the `coupling_large` override once the header-keyed conversion exists.
6. SNO: no change (x m_N is correct).
7. `_FILE_CONVENTION`: add `AxionNeutron/JEDI.txt: None`,
   `AxionProton/SuperKamiokande.txt: None`; decide Hefei (x 2 m_n vs x 2 m_n/0.63)
   and encode it explicitly.
