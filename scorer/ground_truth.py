# Vendored from AutoAxionLimits evaluation/ground_truth.py at master 73682236 (2026-09-09); import paths rewritten, no logic changes.
"""Load and validate ground-truth dataset."""

from __future__ import annotations

import json
import logging
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

import numpy as np

logger = logging.getLogger(__name__)

GROUND_TRUTH_DIR = Path(__file__).parent.parent / "data"
PAPERS_JSON = GROUND_TRUTH_DIR / "papers.json"
DATA_DIR = GROUND_TRUTH_DIR / "ground_truth"

# --- Ingestion-time unit normalization (post-full346 Phase 1b) ---------------
#
# Several repo files do not store (mass [eV], coupling) directly; comparing
# against them raw is a units gap, not extraction error. The conversions below
# are DETERMINISTIC and declared in the source files' own headers, so they are
# applied when populating ground_truth/data/ (the GT numbers remain O'Hare's,
# only re-expressed in the benchmark's axes).
#
# 1. Fifth-force / monopole-dipole files whose x-column is the Yukawa range
#    lambda in METERS (header contains "lambda [m]"): converted to mediator
#    mass via m [eV] = (hbar*c) / lambda = 1.9732698e-7 eV.m / lambda[m].
_HBARC_EV_M = 1.9732698e-7
_LAMBDA_HEADER_TOKEN = "lambda [m]"
# 2. Per-file y-column scale factors, each justified by the file's own header.
#    COBEFIRAS_Cyr.txt stores "epsilon defined as g_agamma*B0_T/(1e-11 GeV^-1
#    * 1 nG)", i.e. g_agamma [GeV^-1] = epsilon * 1e-11 at the B0 = 1 nG
#    normalization (the curve the paper's Fig. 13 headline uses) — see
#    failure_analysis_full346_detail.md § 2411.13701.
_FILE_Y_SCALE: dict[str, float] = {
    # AxionLimitBench: the file header's "1e-11 GeV^-1" is a typo; the paper's Eq. (3c)
    # normalises epsilon to 1e-10 GeV^-1 and Fig. 13's 1-nG FIRAS curve matches
    # y*1e-10 to 0.05 dex (data/PLANE_AUDIT_AxionLimitBench.md, item 3).
    "limit_data/AxionPhoton/COBEFIRAS_Cyr.txt": 1e-10,
}
# AxionLimitBench: VectorB-L files the compilation stores as epsilon = g/e (the gauge
# coupling normalised to the electromagnetic one) although its axis is the
# gauge coupling g; the plotting code applies no factor, so the compilation is
# internally inconsistent (8 files in epsilon, 8 in g). The canonical plane is
# g, so these are multiplied by e = sqrt(4 pi alpha) = 0.30282 at ingestion.
# Each file verified against its paper's figure (PLANE_AUDIT_AxionLimitBench.md, item 1).
_E_CHARGE = 0.30282
# AxionLimitBench: LISAPathfinder-RelativeAcceleration.txt REMOVED from this list. The
# paper (2310.06017, p. 7) states that its Fig. 5 "y-axis shows the gauge
# coupling g_B-L = eps_B-L e", the file header says g_B-L, and the file matches
# Fig. 5 to <0.1 dex; the AxionLimitBench plane audit had compared it with the per-axis
# epsilon curves of Fig. 3, which is a different quantity. Two independent
# re-audits of the agent's misses found the +0.52 dex flat offset.
for _f in ("EotwashEP", "KAGRA", "LISAPathfinder",
           "LIGO-O1", "LIGOVirgo", "InverseSquareLaw", "Casimir"):
    _FILE_Y_SCALE[f"limit_data/VectorB-L/{_f}.txt"] = _E_CHARGE
# AxionLimitBench: files whose y column is a PRODUCT with the mass column, undone at plot
# time (DarkPhoton/Solar-Global.txt: "kinetic mixing * mass [eV]", PlotFuncs
# divides by mass). Ingested as y / x.
_FILE_Y_DIVIDE_BY_X: set[str] = {"limit_data/DarkPhoton/Solar-Global.txt"}
# AxionLimitBench: fifth-force files ("lambda [m]  alpha" header) under ScalarNucleon /
# ScalarBaryon store the Yukawa strength relative to gravity; the compilation
# plots g_s^N = sqrt(alpha / 1.37e37) (AxionCPV.ipynb, g_scalar_nucleon), i.e.
# g = sqrt(4 pi G u^2 alpha) with M_Pl^2/(4 pi u^2) = 1.367e37. Applied at
# ingestion when the header names alpha (magnitude is not a valid key: several
# alpha files sit below 1e3).
_ALPHA_TO_G_DENOM = 1.37e37
_ALPHA_DIRS = ("limit_data/ScalarNucleon/", "limit_data/ScalarBaryon/")

# Per-file x-scale factors (mass-column corrections). Xenon1T.txt: the repo
# file's header claims "mass [eV]" but the values are keV — PlotFuncs.py
# multiplies dat[:,0] by 1e3 at plot time (`plt.fill_between(1e3*dat[:,0],
# ...)`), and the paper's own e-print ancillary file (1907.11485
# anc/5f_results_darkphoton.csv) has header `mass_kev` with identical values.
# Ingest with the same correction so the GT is in true eV.
_FILE_X_SCALE: dict[str, float] = {
    "limit_data/DarkPhoton/Xenon1T.txt": 1e3,
}


def _loadtxt_tolerant(path: Path) -> Optional[np.ndarray]:
    """Load an Nx2 numeric data file, tolerating whitespace- or comma-delimited
    columns. A few repo-sourced ground-truth files are comma-separated (e.g.
    ``1e-17,2.0``), which the default whitespace-splitting ``np.loadtxt`` cannot
    parse. We try whitespace first (the common case), then comma. A genuinely
    unparseable file is warned about and skipped (returns None) rather than
    crashing the whole metrics run."""
    try:
        return np.loadtxt(str(path), ndmin=2)
    except ValueError:
        pass
    try:
        return np.loadtxt(str(path), ndmin=2, delimiter=",")
    except ValueError as e:
        logger.warning("Could not parse data file %s (%s); skipping", path, e)
        return None


@dataclass
class GroundTruthEntry:
    arxiv_id: str
    paper_title: str
    coupling_type: str
    coupling_convention: Optional[str]  # e.g. "d_e", "f_a_GeV", "epsilon"
    coupling_units: Optional[str]       # human-readable y-axis units
    is_new_limit: bool
    is_projection: bool
    data_source_expected: str  # "table" | "figure_vision" | "text"
    confidence_level: float
    dm_density_assumed: Optional[float]
    difficulty: str  # "easy" | "medium" | "hard"
    tags: list[str]
    notes: str
    ground_truth_data_file: Optional[str]  # filename in data/ dir
    reference_repo_file: Optional[str]  # path in repo (for auto-populating)
    ground_truth_mass_range_eV: Optional[tuple[float, float]]
    ground_truth_coupling_range: Optional[tuple[float, float]]
    ground_truth_num_points: Optional[int]
    verified_by: str
    verification_date: str
    # Benchmark exclusion (post-full346 Phase 1a). An excluded entry stays in
    # papers.json (documented, visible, reversible — never a silent deletion)
    # but is skipped by residual scoring and listed in a dedicated report
    # table. See evaluation/ground_truth/EXCLUSIONS.md.
    excluded: bool = False
    exclusion_reason: Optional[str] = None
    exclusion_evidence: Optional[str] = None
    # Coupling planes the paper demonstrably publishes a limit in but the
    # benchmark pool never ingested a curve for (multi-plane papers: EP tests,
    # stellar-cooling papers, reviews). A prediction of any of these is a
    # correct identification for classification grading, even though no curve
    # comparison is possible against them. Evidence (abstract quote, figure
    # number, or repo-file header attribution) is mandatory — never add a type
    # here merely because the extractor picked it.
    also_published_types: list[str] = field(default_factory=list)
    also_published_evidence: Optional[str] = None

    def load_data(self) -> Optional[np.ndarray]:
        """Load ground-truth data as Nx2 array (mass_eV, coupling)."""
        if self.ground_truth_data_file is None:
            return None
        path = DATA_DIR / self.ground_truth_data_file
        if not path.exists():
            logger.warning("Ground truth data file not found: %s", path)
            return None
        return _loadtxt_tolerant(path)

    def load_reference_data(self, repo_root: Path) -> Optional[np.ndarray]:
        """Load the reference data from the repo (upstream-curated)."""
        if self.reference_repo_file is None:
            return None
        path = repo_root / self.reference_repo_file
        if not path.exists():
            logger.warning("Reference repo file not found: %s", path)
            return None
        return _loadtxt_tolerant(path)


def load_ground_truth(path: Path = PAPERS_JSON) -> list[GroundTruthEntry]:
    """Load all ground-truth entries from papers.json."""
    with open(path) as f:
        data = json.load(f)

    assert data["schema_version"] == 1, f"Unsupported schema version: {data['schema_version']}"

    entries = []
    for p in data["papers"]:
        mass_range = p.get("ground_truth_mass_range_eV")
        if mass_range is not None:
            mass_range = tuple(mass_range)
        coupling_range = p.get("ground_truth_coupling_range")
        if coupling_range is not None:
            coupling_range = tuple(coupling_range)

        entries.append(GroundTruthEntry(
            arxiv_id=p["arxiv_id"],
            paper_title=p["paper_title"],
            coupling_type=p["coupling_type"],
            coupling_convention=p.get("coupling_convention"),
            coupling_units=p.get("coupling_units"),
            is_new_limit=p["is_new_limit"],
            is_projection=p["is_projection"],
            data_source_expected=p["data_source_expected"],
            confidence_level=p["confidence_level"],
            dm_density_assumed=p.get("dm_density_assumed"),
            difficulty=p["difficulty"],
            tags=p.get("tags", []),
            notes=p.get("notes", ""),
            ground_truth_data_file=p.get("ground_truth_data_file"),
            reference_repo_file=p.get("reference_repo_file"),
            ground_truth_mass_range_eV=mass_range,
            ground_truth_coupling_range=coupling_range,
            ground_truth_num_points=p.get("ground_truth_num_points"),
            verified_by=p["verified_by"],
            verification_date=p["verification_date"],
            excluded=bool(p.get("excluded", False)),
            exclusion_reason=p.get("exclusion_reason"),
            exclusion_evidence=p.get("exclusion_evidence"),
            also_published_types=list(p.get("also_published_types", [])),
            also_published_evidence=p.get("also_published_evidence"),
        ))

    logger.info("Loaded %d ground-truth entries", len(entries))
    return entries


def _ingest_reference_file(src: Path, reference_repo_file: str) -> list[str]:
    """Read a repo reference file, strip comments, and apply the deterministic
    ingestion-time unit conversions declared in the file's own header (see the
    module-level note): lambda[m] → mass[eV] on the x-column, and per-file
    y-scale factors. Returns the data lines to write."""
    raw = src.read_text(errors="replace").splitlines()
    header = "\n".join(l for l in raw if l.strip().startswith("#")).lower()
    lambda_axis = _LAMBDA_HEADER_TOKEN in header
    y_scale = _FILE_Y_SCALE.get(reference_repo_file)
    x_scale = _FILE_X_SCALE.get(reference_repo_file)
    y_div_x = reference_repo_file in _FILE_Y_DIVIDE_BY_X
    alpha_to_g = (lambda_axis and "alpha" in header
                  and reference_repo_file.startswith(_ALPHA_DIRS))

    lines: list[str] = []
    for line in raw:
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        if lambda_axis or y_scale is not None or x_scale is not None or y_div_x:
            parts = stripped.replace(",", " ").split()
            try:
                x, y = float(parts[0]), float(parts[1])
            except (IndexError, ValueError):
                logger.warning("Unparseable row in %s: %r", src, stripped)
                continue
            if lambda_axis:
                if x <= 0:
                    continue
                x = _HBARC_EV_M / x
            if x_scale is not None:
                x *= x_scale
            if y_scale is not None:
                y *= y_scale
            if y_div_x:
                y = y / x if x > 0 else y
            if alpha_to_g and y > 0:
                y = (y / _ALPHA_TO_G_DENOM) ** 0.5
            stripped = f"{x:.6e} {y:.6e}"
        lines.append(stripped)
    return lines


def populate_data_from_repo(repo_root: Path, force: bool = False) -> int:
    """Copy reference repo files into ground_truth/data/ for entries that have
    reference_repo_file set but no local data file yet (all entries when
    ``force``), applying the deterministic ingestion conversions above.

    Returns the number of files written.
    """
    entries = load_ground_truth()
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    copied = 0

    for entry in entries:
        if entry.ground_truth_data_file is None or entry.reference_repo_file is None:
            continue
        dest = DATA_DIR / entry.ground_truth_data_file
        if dest.exists() and not force:
            continue
        src = repo_root / entry.reference_repo_file
        if not src.exists():
            logger.warning("Reference file %s not found, skipping", src)
            continue

        lines = _ingest_reference_file(src, entry.reference_repo_file)
        with open(dest, "w") as f:
            f.write("\n".join(lines) + "\n")

        logger.info("Copied %s → %s (%d data lines)", src.name, dest.name, len(lines))
        copied += 1

    return copied
