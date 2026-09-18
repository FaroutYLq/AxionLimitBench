# Independent re-audits of the agent's 37 remaining misses (card the task card run, AxionLimitBench references)

Two auditors worked independently from the PDF, e-print, agent transcript and curator file, without access to the the initial ingestion failure audit. Auditor B read 3-5 values off each figure before looking at the agent's answer. Taxonomy: P perception, C conversion, ID identification, POL compilation policy the paper does not fix, REF reference defect, SC scorer.

| cause | A | B |
|---|---|---|
| P | 4 | 0 |
| C | 0 | 0 |
| ID | 1 | 0 |
| POL | 21 | 25 |
| REF | 6 | 5 |
| SC | 5 | 7 |

Agreement on primary cause: 26/37. Neither auditor found a conversion error. The 11 disagreements are all at the P/POL and REF/SC/POL boundaries: four 'band reduction' choices (centre vs conservative edge of a thick band, lower envelope vs spiky curve: 2503.14582, 1401.6460, 1902.02788, 2109.08822) that A files as perception and B as policy; one scope call (2403.02381); and six papers where both say the benchmark is at fault but differ on whether the reference, the scorer or a policy is the proximate cause.

## Verified and acted on (AxionLimitBench)

- 2310.06017: both auditors found a flat +0.52 dex offset = the AxionLimitBench ingestion multiplying a g_B-L file by e; the paper states Fig. 5 is in g_B-L. Factor removed. Now 0.01 dex.
- 2104.13798, 1906.08814: two-vertex flat references scored at the band edges; the min-in-window rule now covers references of <=3 vertices spanning <=0.3 dex. Now 0.09 and 0.00 dex.
- 2303.00778: agent's g_B = 6.5e-13 vs file 6.54e-13, graded no_comparable_gt for declaring ScalarBaryon where the compilation files the curve under ScalarNucleon. Plane alias added.
- 2201.02042, 2207.05767, 2110.10262: reference defects re-verified by the maintainer (vector traces, stated scan range) and excluded with evidence (data/EXCLUSIONS.md).
- 1905.13650: B's claimed 0.27 dex unit defect is not one: the scorer applies the 2m_n family default to AxionNeutron GeV^-1 files at comparison time (conventions.file_source_convention).
- 1712.00483: both auditors call the reference a different paper's re-derivation; the paper's own text ('exclude a new region above |d_e| = 1e-4') matches the curator's plateau while its Fig. 5 line sits at 2.3e-4, so the reference is kept and the miss stands as both-defensible.

## Not acted on

- Band/spiky-limit reduction (2503.14582, 1902.02788, 2109.08822, 1401.6460, 2404.12517, 2110.10497, 2301.08736): the scorer evaluates at every reference vertex, so a smoothed or centred trace of a noisy limit pays the reference's own scatter, and the task card does not say which edge or statistic the compilation records. Left as misses; documented as a limitation, candidate for a binned secondary metric.
- Scenario / main-coupling policy (the remaining POL cases): the curator's choice is not recorded anywhere a system could read; left as misses.

## Per-paper verdicts

| arXiv id | A | B | A verdict | B verdict |
|---|---|---|---|---|
| 1905.13650 | POL | POL | both defensible (curator's per-experiment split is the compilation convention; agent's env | both defensible (curator: per-experiment curve; agent: paper's combined envelope); GT addi |
| 1712.00483 | REF | REF | agent right (paper's own Fig. 5 supports the agent's curve in both arXiv versions); curato | agent right (matches the paper's Fig. 5); curator file does not match this paper's figure |
| 1611.05852 | POL | POL | both defensible; multi-coupling paper (scalars to electrons/nucleons, dark photon, Higgs p | both defensible: multi-coupling paper; agent emitted the SN1987A dark-photon bound (faithf |
| 2111.06883 | POL | POL | both defensible; agent reported the abstract's headline quark/gluon-coupling combination ( | both defensible but not comparable: agent emitted the paper's headline QCD-sector combinat |
| 2201.02042 | REF | REF | agent right; curator's curve has a different shape from the paper's Exp. B curve (mis-digi | agent right (Exp. B is the paper's exclusion); curator digitised Exp. A, which the paper s |
| 2205.03617 | POL | POL | both defensible; paper gives separate constraint plots for L_mu-L_tau (Fig. 4), gauged B-L | both defensible: agent emitted the paper's own new dark-photon dispersion bound (Fig. 6 da |
| 2310.06017 | SC | REF | agent right and curator right; the benchmark's ingestion multiplies a file already in g_B- | agent right (reproduces Fig. 5 blue region to <0.1 dex); curator file is a uniform factor  |
| 2503.13653 | POL | POL | both defensible; curator took the normal-CCSN (1 B) contour, agent the low-energy-SN (0.1  | both defensible: agent took the 0.1 B low-energy-SN contour (tightest), curator the 1 B no |
| 2503.14582 | P | POL | curator right; agent traced the smooth 'schematic' boundary of Fig. 1 (the lower envelope  | both defensible; agent traced the smooth lower envelope (Fig. 1 'schematic'), curator stor |
| 2110.10262 | REF | REF | agent right per the paper's abstract and frequency axis; curator's masses follow the figur | agent right on mass placement (h*f of the frequency axis matches the abstract's 4796.7-479 |
| 1401.6460 | P | POL | curator closer to the paper; agent reported the geometric centre of the thick BBN band, 0. | both defensible: agent reports the geometric centre of the thick BBN band, curator sits at |
| 1707.07921 | POL | POL | both defensible; agent reported the galactic ALP-DM channel (Fig. 4), the benchmark's file | both defensible: paper reports three channels (solar CBRD, solar 57Fe, galactic ALP DM); a |
| 1906.11844 | POL | POL | both defensible; Eq. (3.3) bounds a quadratic combination of g_an and g_ap, the agent set  | both defensible: Eq. 3.3 bounds a g_an/g_ap combination; agent projected onto g_ap (KSVZ d |
| 2404.12517 | SC | SC | agent right on inspection (per-band medians agree within 0.1-0.25 dex); residual is the sp | agent right; agent and curator sample the same noisy limit band, the residual is reference |
| 2302.10206 | POL | REF | both defensible; agent took the main-text benchmark core-halo relation (Fig. 3, M_S ~ M_h^ | agent right vs the current (v2) figure; curator's 10-vertex polygon does not match the v2  |
| 2002.08370 | POL | POL | both defensible; agent traced the standard-cosmology (blue dashed) BBN+N_eff curve of the  | both defensible: agent took the standard-cosmology curve (blue dashed), curator the most c |
| 1110.2895 | POL | POL | both defensible; agent returned the union envelope of all the paper's cosmological regions | both defensible: agent emitted the union boundary of all cosmological regions in Fig. 1, c |
| 1509.00476 | POL | POL | curator's choice is the one literally in the canonical plane (Fig. 4b, coupling only to ph | curator's choice (photon-only coupling panel) fits the g_agamma plane better; agent chose  |
| 2104.13798 | SC | SC | agent right on inspection (curve minimum 4.9e-13 vs headline 4e-13); curator stored the he | agent right (traced the observed spiky curve of the Fig. 9 inset); curator stores a flat h |
| 2402.07976 | POL | POL | both defensible; agent reported the NFW-profile conservative bound the abstract headlines, | both defensible: agent emitted the NFW-conservative bound quoted in the abstract, curator  |
| 2407.16628 | POL | POL | both defensible; agent traced the main-result Fig. 4 (gamma_sp = 2.3, R_em = 4 R_s, Mrk 42 | both defensible; agent traced the paper's main-result Fig. 4 (R_em = 4 R_s, gamma_sp = 2.3 |
| 2002.01796 | POL | POL | both defensible; title 'Axion and dark photon limits from Crab Nebula': agent reported the | both defensible: the paper (title: 'Axion and dark photon limits from Crab Nebula') report |
| 1906.08814 | SC | SC | agent right on inspection (minimum 1.50e-9 at 2.035 neV = paper's quoted limit); curator's | agent right (traced the Fig. 3a curve); curator stores a 2-point flat line at the best val |
| 2207.05767 | REF | POL | agent right for the paper as it exists today (v2, Mar 2023); curator's file matches the su | both defensible: agent reports per-bin log-medians of the jagged FAST limit, curator store |
| 2110.10497 | SC | SC | agent right on inspection (minimum 5.5e-11 vs paper's 6.86e-11 and GT 6.9e-11); both sides | agent and curator trace the same extremely spiky Fig. 11 curve with different sparse sampl |
| 2012.05427 | POL | POL | both defensible; agent reported the headline Cas A bound (Eq. 37, eps m < 1.5e-8 MeV), cur | both defensible: agent emitted the Cas A bound alone (paper's headline, Eq. 37), curator's |
| 2212.01971 | POL | POL | undecided between POL and REF: the paper's Fig. 1 shows two ORGAN dark-photon curves (opaq | both defensible: agent emitted the paper's opaque fixed-polarisation curve, benchmark GT i |
| 1807.04512 | POL | POL | both defensible; the paper re-derives several linear-coupling EP curves ('summarize existi | both defensible: paper derives several UFF curves in Fig. 3; agent chose MICROSCOPE Ti/Pt  |
| hep-ph/0307284 | REF | SC | agent right for the paper's own plane; the benchmark's two GT files for this review are cu | agent followed the task card (fifth-force paper -> ScalarNucleon with native |alpha|(lambd |
| 2303.00778 | POL | SC | agent and curator agree numerically (6.5e-13 vs 6.54e-13 flat); the miss is the type label | agent right: its flat g_B = 6.5e-13 equals the curator's ScalarNucleon/WhiteDwarfs.txt val |
| 1902.02788 | P | POL | curator right; agent returned the per-bin minimum (lower envelope) of a spiky limit, which | both defensible but the agent's lower envelope is optimistic: agent took per-bin minima of |
| 2302.04565 | POL | POL | both defensible; agent traced the upper envelope of the jagged Yb+/Sr 95% CL spectrum, whi | both defensible: agent emitted the upper envelope (conservative edge) of the jagged 95% CL |
| quant-ph/0106045 | REF | SC | agent right in plane; the benchmark's only GT for this review is a B-L recast of a Casimir | agent followed the task card (Casimir/Yukawa constraints -> native |alpha_G|(lambda) under |
| 2109.08822 | P | POL | curator right (follows the paper's drawn exclusion boundary = upper edge of the noisy band | both defensible: agent reports the centre of the noisy 491k-point limit band (matches the  |
| 2301.08736 | POL | POL | both defensible on the band; curator additionally applied a x2 B->B-L charge rescale that  | both defensible: agent reports the per-bin median of a limit band that is 1-5 decades wide |
| 2403.02381 | ID | POL | curator right under the task card's rule; the paper derives its own updated MICROSCOPE B-L | both defensible: the paper is a projection framework (agent: is_projection, no points), bu |
| 2302.00685 | POL | POL | both defensible; agent took the strongest (blue, T_osc optimised) of three nested excluded | both defensible: agent traced the blue (optimised T_osc, strongest) region, curator the gr |
