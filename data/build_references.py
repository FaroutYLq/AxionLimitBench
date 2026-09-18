"""Rebuild the this release reference set from the pinned AutoAxionLimits checkout.

    python3 data/build_references.py --repo /path/to/AutoAxionLimits [--apply]

Steps (all deterministic, all logged):
  1. re-ingest every entry's reference file with the this release ingestion rules
     (scorer/ground_truth.py) and report which data files changed;
  2. re-infer each entry's stored coupling_convention / coupling_units;
  3. apply the this release exclusions (reason + evidence from the failure audit);
  4. add reference entries for curator files of multi-plane papers that the
     initial pool never ingested.
Without --apply nothing is written; the report is printed either way.
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
from scorer.ground_truth import _ingest_reference_file, DATA_DIR, PAPERS_JSON  # noqa: E402
from scorer.conventions import infer_convention_for_repo_file  # noqa: E402

EXCLUSIONS = {  # arxiv_id -> (reason, evidence)   [audit: results/agent_claude_code/fable5_failure_audit.json]
    "1912.07751": ("Reference digitised from a superseded arXiv version", "UPLOAD.txt header 'UPLOAD 1st paper'; v3 (June 2021) erratum moved the limit from ~1e-6 to 3e-3 GeV^-1 (3.8 dex); both benchmark arms are 'catastrophic' on the stale curve"),
    "2312.13723": ("Reference digitised from a superseded arXiv version", "Cavities.txt matches v1 Fig. 2 (floor d_me ~2-10); v2 (Sept 2024) revised the floor by ~4 dex and added a GPS region"),
    "2402.17140": ("Reference digitised from a superseded arXiv version", "JWST.txt (eps 3.5e-10 -> 1.9e-12) is v1's in-space constraint, withdrawn in v3 which keeps only a projection 2-2.5 dex lower"),
    "2209.06299": ("Reference digitised from a superseded arXiv version", "INTEGRAL.txt reproduces v1 Fig. 3; v4 is 'revised to correct for error in bounds' (rendered both versions)"),
    "2412.09595": ("Reference digitised from a superseded arXiv version", "SuperKamiokande.txt floor 5e-6 is v1; v2-v4 corrected the floor to 2e-5"),
    "2101.02805": ("Reference encodes a projected curve, not the measured limit", "DarkEfield.txt level (~1e-13, starting at 60 MHz) matches Fig. 12's green Phase-I '5 sigma extrapolated ... after 1 month' projection, not the blue Pilot limit (~1e-12, abstract 'eps ~ 1e-12')"),
    "2205.06817": ("Reference is a projection from mock data ingested as a measured limit", "Paper Sec. III.D: 'we place projected constraints' from mock IPTA data; IPTA.txt is drawn UnfilledLimit in the compilation"),
    "2404.00616": ("Reference is a projected constraint stored outside Projections/", "fa/I2Ca.txt is Fig. 3(b)'s 'projected constraint ... this work' with is_projection=false in the pool"),
    "1708.02111": ("Reference is a 1-sigma hint band, not an exclusion limit", "WDhint.txt encodes g_ae = 1.6 +0.29/-0.34 e-13 (a white-dwarf cooling hint); the paper's only 'bound' on g_ap is the PDG SN value re-parametrised"),
    "2201.02042": ("Reference matches neither curve of the paper's exclusion figure", "CsCav.txt vs a vector trace of Fig. 2(a) g_gamma panel (e-print exclusions.pdf): Exp. B (the paper's exclusion; p. 11 states the Exp. A threshold is 'the sensitivity region, these are not limits') minus curator = +0.02..+1.06 dex (median +0.69), Exp. A minus curator = -1.01..-0.42; the file's log-curve is stretched about ~1e-7 eV, which no constant conversion produces. The agent's trace sits on Exp. B (median +0.05 dex). ScalarElectron/CsCav.txt shows the same stretched shape (audit A)"),  # this release
    "2207.05767": ("Reference digitised from a superseded arXiv version", "FAST.txt lies BELOW the local minimum of the v2 (Mar 2023, e-print final-plot.pdf) red curve at 180 of 237 masses (median 0.16 dex below the minimum), so it is not a trace of v2; it matches v1's stronger curve (rho_DM 0.4 -> 0.3 and reanalysis between versions). The agent's per-bin medians match the v2 curve to 0.03 dex"),  # this release
    "2110.10262": ("Reference follows a figure mass axis inconsistent with the paper's stated scan", "ADMX_Sidecar_JTWPA.txt spans 19.8344-19.8452 ueV = 4795.9-4798.6 MHz, but the abstract scans 4796.7-4799.5 MHz (h f = 19.8385-19.8501 ueV); the e-print figure's top mass axis is offset ~0.9 MHz from h f of its own frequency axis and the curator digitised against it. In a 2.7-MHz window whose depth varies by ~1 dex, no extraction from the stated scan range overlaps it correctly (agent shape matches, coverage 0.67, 0.49 dex)"),  # this release
    "1512.06746": ("QCD-axion mass prediction band (m_lo, m_hi), no coupling column", "AxionMass/Bonati16.txt is a theory prediction; same class as the 13 PlotTheoryMass entries already excluded"),
    "1606.07494": ("QCD-axion mass prediction band (m_lo, m_hi), no coupling column", "AxionMass/Borsanyi16.txt (50-1500 ueV band); same class as the existing PlotTheoryMass exclusions"),
    "1708.07521": ("QCD-axion mass prediction band (m_lo, m_hi), no coupling column", "AxionMass/Klaer17.txt; the pipeline's 0.127 dex 'hit' is an f_a number against the band's upper mass edge"),
    "2401.17253": ("QCD-axion mass prediction band (m_lo, m_hi), no coupling column", "AxionMass/Saikawa24.txt (95-450 ueV band)"),
    "1412.0789": ("QCD-axion mass window stored as a single reference point", "AxionMass/SaikawaDW_6_10.txt is the N_DW=6 PlotTheoryMass window (5.8e-4, 4.5e-3 eV), not a measured limit"),
    "2410.02218": ("Reference has a mis-set log-axis calibration", "fa/ONIX.txt vs the figure's vector paths: GT_log = 1.55 x true + 5.6 (up to 1.6 dex off at 1e-20 eV); AxionEDM/ONIX.txt is the same digitisation in the g_d plane"),
    "hep-ex/0702006": ("Reference mixes later buffer-gas results into this paper's curve", "CAST_highm.txt above 0.02 eV (2e-10 flat to 1.17 eV) is the Phase II 4He/3He result, absent from the 2007 vacuum paper whose Fig. 8 rises ~m^2 above 0.02 eV"),
    "2208.03183": ("Reference resonance placed at the wrong mass", "SQMS.txt centred on 1.3048 GHz vs the paper's f0 = 1.294605478 GHz (42 peV off for a 16-peV-wide feature, tail mirrored); no correct extraction can overlap it"),
    "1902.04644": ("Reference file belongs to a different paper", "CASPEr_ZULF.txt is the stochastic-corrected (x8.4) curve from 1905.13650 (docs/an.md), not this paper's Fig. 3 (values exceed the plotted axis range)"),
}
ADDITIONS = [  # curator files for multi-plane papers that the initial ingestion missed
    dict(arxiv_id="0807.2926", coupling_type="AxionPhoton", reference_repo_file="limit_data/AxionPhoton/SolarNu.txt",
         paper_title="SolarNu", notes="the paper's headline g_agamma < 7e-10 GeV^-1 (solar axion flux vs neutrino data); the initial pool held only the g_ae recast"),
    dict(arxiv_id="1508.02463", coupling_type="MonopoleDipole", reference_repo_file="limit_data/MonopoleDipole/ElectronNucleon/Washington_Terrano.txt",
         paper_title="Washington_Terrano", notes="the paper's Fig. 5 monopole-dipole limit; the initial pool held only the AxionElectron (Fig. 4) entry"),
    dict(arxiv_id="2303.00778", coupling_type="ScalarNucleon", reference_repo_file="limit_data/ScalarNucleon/WhiteDwarfs.txt",
         paper_title="WhiteDwarfs", notes="the paper's scalar-nucleon bound; the initial pool held only the d_me recast"),
]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", required=True)
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args()
    repo = Path(args.repo)
    p = json.loads(PAPERS_JSON.read_text())
    papers = p["papers"]
    today = date.today().isoformat()
    changed_files, conv_changes, excl_applied, added = [], [], [], []

    # 1. re-ingest
    for e in papers:
        rf, gf = e.get("reference_repo_file"), e.get("ground_truth_data_file")
        if not rf or not gf:
            continue
        src = repo / rf
        if not src.exists():
            print("  missing in repo:", rf); continue
        new = "\n".join(_ingest_reference_file(src, rf)) + "\n"
        dst = DATA_DIR / gf
        old = dst.read_text() if dst.exists() else None
        if old != new:
            changed_files.append((e["arxiv_id"], rf))
            if args.apply:
                dst.write_text(new)
    # 2. re-infer conventions (after files are rewritten)
    for e in papers:
        gf = e.get("ground_truth_data_file")
        if not gf:
            continue
        # directory-keyed, as at original ingestion (an entry's coupling_type can
        # differ from its file's directory on multi-plane papers)
        conv, units = infer_convention_for_repo_file(e.get("reference_repo_file"), e["coupling_type"], DATA_DIR / gf)
        if (conv, units) != (e.get("coupling_convention"), e.get("coupling_units")):
            conv_changes.append((e["arxiv_id"], e.get("coupling_convention"), conv))
            if args.apply:
                e["coupling_convention"], e["coupling_units"] = conv, units
    # 3. exclusions
    for e in papers:
        if e["arxiv_id"] in EXCLUSIONS and not e.get("excluded"):
            reason, evidence = EXCLUSIONS[e["arxiv_id"]]
            excl_applied.append(e["arxiv_id"])
            if args.apply:
                e["excluded"] = True
                e["exclusion_reason"] = f"{reason}"
                e["exclusion_evidence"] = evidence
    # 4. additions
    have = {(e["arxiv_id"], e.get("reference_repo_file")) for e in papers}
    for a in ADDITIONS:
        if (a["arxiv_id"], a["reference_repo_file"]) in have:
            continue
        src = repo / a["reference_repo_file"]
        if not src.exists():
            print("  addition missing in repo:", a["reference_repo_file"]); continue
        lines = _ingest_reference_file(src, a["reference_repo_file"])
        gf = f"{a['arxiv_id'].replace('/', '_')}__{a['coupling_type']}_{Path(a['reference_repo_file']).stem}.txt"
        tmpl = next(e for e in papers if e["arxiv_id"] == a["arxiv_id"])
        entry = dict(tmpl)
        entry.update(a)
        entry.update(ground_truth_data_file=gf, ground_truth_num_points=len(lines), excluded=False,
                     exclusion_reason=None, exclusion_evidence=None, also_published_types=[], also_published_evidence=None,
                     verified_by="this release_audit", verification_date=today, tags=list(set(tmpl.get("tags", [])) | {"this release_added"}))
        if args.apply:
            (DATA_DIR / gf).write_text("\n".join(lines) + "\n")
            conv, units = infer_convention_for_repo_file(entry["reference_repo_file"], entry["coupling_type"], DATA_DIR / gf)
            entry["coupling_convention"], entry["coupling_units"] = conv, units
            papers.append(entry)
        added.append((a["arxiv_id"], a["reference_repo_file"], len(lines)))
    if args.apply:
        p["description"] = p.get("description", "") + f" | this release reference set rebuilt {today} (data/build_v02.py; see data/PLANE_AUDIT_this release.md and EXCLUSIONS.md)"
        PAPERS_JSON.write_text(json.dumps(p, indent=2) + "\n")
    print(f"data files changed: {len(changed_files)}")
    for x in changed_files: print("   ", x)
    print(f"convention labels changed: {len(conv_changes)}")
    for x in conv_changes: print("   ", x)
    print(f"exclusions applied: {len(excl_applied)}: {excl_applied}")
    print(f"entries added: {added}")
    print("APPLIED" if args.apply else "DRY RUN (no files written)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
