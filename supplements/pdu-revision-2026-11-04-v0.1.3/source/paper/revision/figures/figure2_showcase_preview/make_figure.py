"""Figure 2 preview: Fable agent and pipeline versus the collaboration PCL.

Run in straxion: python paper/revision/figures/figure2_showcase_preview/make_figure.py
Frozen curve inputs are in data/. The background uses the original showcase
worktree's PlotFuncs and limit files. This does not replace manuscript figures.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import os
import tempfile
os.environ.setdefault("MPLCONFIGDIR", tempfile.mkdtemp(prefix="aal-fig2-mpl-"))
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.axes as _mpl_axes
import matplotlib.figure as _mpl_figure
import matplotlib.pyplot as plt

OUT = Path(__file__).resolve().parent
ROOT = OUT.parents[3] / "figure2_background"
DATA = OUT / "data"
sys.path.insert(0, str(ROOT))
import os
os.chdir(ROOT)  # PlotFuncs loads limit_data/ by relative path

import PlotFuncs as PF  # noqa: E402

# --- grey-out monkey-patch (verbatim technique from pipeline/plot_regen.py) ---
_GREY_FACE = "#dddddd"
_GREY_EDGE = "#bbbbbb"
_ACTIVE = {"highlight": False}

_orig_fill_between = _mpl_axes.Axes.fill_between
_orig_fill = _mpl_axes.Axes.fill
_orig_plot = _mpl_axes.Axes.plot
_orig_text = _mpl_axes.Axes.text
_orig_axhline = _mpl_axes.Axes.axhline
_orig_axvline = _mpl_axes.Axes.axvline
_orig_arrow = _mpl_axes.Axes.arrow
_orig_fig_text = _mpl_figure.Figure.text


def _p_fill_between(self, x, y1, y2=0, **kw):
    if not _ACTIVE["highlight"]:
        kw.pop("color", None); kw["facecolor"] = _GREY_FACE
        kw.pop("edgecolor", None); kw["edgecolor"] = None
    return _orig_fill_between(self, x, y1, y2=y2, **kw)


def _p_fill(self, *a, **kw):
    if not _ACTIVE["highlight"]:
        kw.pop("color", None); kw["facecolor"] = _GREY_FACE
        kw.pop("edgecolor", None); kw["edgecolor"] = None
    return _orig_fill(self, *a, **kw)


def _p_plot(self, *a, **kw):
    if not _ACTIVE["highlight"]:
        _FMT = set("bgrcmykwBGRCMYKW")
        cleaned = []
        for x in a:
            if isinstance(x, str) and len(x) <= 4:
                x = "".join(ch for ch in x if ch not in _FMT) or "-"
            cleaned.append(x)
        kw["color"] = _GREY_EDGE; kw["alpha"] = 0.0
        kw.pop("path_effects", None)
        return _orig_plot(self, *cleaned, **kw)
    return _orig_plot(self, *a, **kw)


def _p_text(self, *a, **kw):
    if not _ACTIVE["highlight"]:
        kw["alpha"] = 0.0; kw.pop("path_effects", None)
    return _orig_text(self, *a, **kw)


def _p_fig_text(self, *a, **kw):
    if not _ACTIVE["highlight"]:
        kw["alpha"] = 0.0; kw.pop("path_effects", None)
    return _orig_fig_text(self, *a, **kw)


def _p_axhline(self, y=0, **kw):
    if not _ACTIVE["highlight"]:
        kw["color"] = _GREY_EDGE; kw["alpha"] = 0.3
    return _orig_axhline(self, y=y, **kw)


def _p_axvline(self, x=0, **kw):
    if not _ACTIVE["highlight"]:
        kw["color"] = _GREY_EDGE; kw["alpha"] = 0.3
    return _orig_axvline(self, x=x, **kw)


def _p_arrow(self, *a, **kw):
    if not _ACTIVE["highlight"]:
        kw["alpha"] = 0.0
    return _orig_arrow(self, *a, **kw)


def _install():
    _mpl_axes.Axes.fill_between = _p_fill_between
    _mpl_axes.Axes.fill = _p_fill
    _mpl_axes.Axes.plot = _p_plot
    _mpl_axes.Axes.text = _p_text
    _mpl_axes.Axes.axhline = _p_axhline
    _mpl_axes.Axes.axvline = _p_axvline
    _mpl_axes.Axes.arrow = _p_arrow
    _mpl_figure.Figure.text = _p_fig_text


def _uninstall():
    _mpl_axes.Axes.fill_between = _orig_fill_between
    _mpl_axes.Axes.fill = _orig_fill
    _mpl_axes.Axes.plot = _orig_plot
    _mpl_axes.Axes.text = _orig_text
    _mpl_axes.Axes.axhline = _orig_axhline
    _mpl_axes.Axes.axvline = _orig_axvline
    _mpl_axes.Axes.arrow = _orig_arrow
    _mpl_figure.Figure.text = _orig_fig_text


# the DarkPhoton.ipynb cell-0 call list (methods only; kwargs irrelevant under grey)
CALLS = [
    "DarkMatter", "Haloscopes", "LSW", "CAST", "SHIPS", "Hinode", "Coulomb",
    "TEXONO", "SuperMAG", "Xenon", "DAMIC", "SENSEI", "SuperCDMS", "DarkSide",
    "FUNK", "LAMPOST", "Tokyo", "SHUKET", "DarkEfield", "WISPDMX", "SQuAD",
    "DMPathfinder", "ORPHEUS", "MuDHI", "DOSUE", "FAST", "LOFAR", "QUALIPHIDE",
    "QuantumCyclotron", "BRASS", "SHANHE", "AMAILS", "SNIPE", "MADMAX",
    "StellarBounds", "COBEFIRAS", "Planck_unWISE", "Jupiter", "Earth", "Crab",
    "ISM", "LeoT", "GasClouds", "NeutronStarCooling", "JWST",
    "ParkerSolarProbe", "INTEGRAL",
]


# Legend label for the extraction curve, per producing channel. The agent
# stage (AAL_EXTRACTOR=agent) writes its own trace rather than selecting among
# staged channels, so the inset must name what actually produced the curve.
_CHANNEL_LABEL = {
    "vector_trace": r"pipeline \texttt{vector\_trace} (%d pts)",
    "source_data": r"pipeline \texttt{source\_data} (%d pts)",
    "text": r"pipeline text channel (%d pts)",
    "vision": r"pipeline vision trace (%d pts)",
}


STAGED_JSON = DATA / "qualiphide2_fable_extraction.json"


def main(extraction=None):
    extraction = Path(extraction) if extraction else STAGED_JSON
    ext = json.load(open(extraction))
    pts = np.array(ext["data_points"], dtype=float)
    # When the figure shows a different extraction (the agent stage), the
    # staged pipeline's own trace stays in the inset as a dashed reference so
    # the two systems can be compared on the same axes.
    ref = None
    if extraction.resolve() != STAGED_JSON.resolve():
        ref = np.array(json.load(open(STAGED_JSON))["data_points"], dtype=float)
    gt = np.loadtxt(DATA / "qualiphide2_gt.txt")
    anchor_m, anchor_chi = 0.050, 1.5e-12  # text channel: stated power-constrained bound
    is_agent = (ext.get("extractor_stage") or "").lower() == "agent"
    # The agent stage runs no channel split, so the paper's single quoted
    # number is the agent's own headline check, not a rival text candidate.
    anchor_label = (r"paper's quoted $\chi=1.5\times10^{-12}$ @ 50 meV"
                    if is_agent else
                    r"text channel: stated $\chi=1.5\times10^{-12}$ @ 50 meV")
    if is_agent:
        ext_label = r"Fable 5 agent (%d pts)" % len(pts)
    else:
        ext_label = _CHANNEL_LABEL.get(
            ext.get("data_source") or "", "pipeline extraction (%d pts)") % len(pts)
    print(f"extraction: {extraction.name} src={ext.get('data_source')} "
          f"stage={ext.get('extractor_stage', 'pipeline')} "
          f"model={ext.get('extractor_model')} n={len(pts)}")

    _install()
    try:
        fig, ax = PF.DarkPhoton.FigSetup()
        for name in CALLS:
            try:
                if name == "Haloscopes":
                    # the notebook passes col= explicitly; default path needs it
                    PF.DarkPhoton.Haloscopes(ax, text_on=False, col="darkred")
                else:
                    getattr(PF.DarkPhoton, name)(ax)
            except Exception as e:  # tolerate any single method failure
                print(f"  (skip {name}: {e})", file=sys.stderr)
        # --- the proposed new limit, in red, exactly like plot_regen ---
        _ACTIVE["highlight"] = True
        ax.fill_between(pts[:, 0], pts[:, 1], y2=1e0,
                        facecolor="#c0392b", edgecolor="#922b21", lw=1.5,
                        zorder=1000, alpha=0.85)
    finally:
        _uninstall()
        _ACTIVE["highlight"] = False

    # --- zoom inset: the three artifacts, all paper-native (rho = 0.45) ---
    # Upper-left corner, enlarged 30% (0.29x0.35 -> 0.377x0.455); axis labels
    # and title removed (the caption already identifies the panel and curves).
    axin = fig.add_axes([0.215, 0.405, 0.377, 0.455])  # upper-left, clear of parent y-ticks
    axin.set_facecolor("white"); axin.set_zorder(2000)
    axin.set_xscale("log"); axin.set_yscale("log")
    axin.fill_between(gt[:, 0], gt[:, 1], 1e-10, color="0.75", alpha=0.5, lw=0)
    axin.plot(gt[:, 0], gt[:, 1], color="0.35", lw=2.5,
              label=f"Collaboration PCL ({len(gt)} pts)")
    if ref is not None:
        axin.plot(ref[:, 0], ref[:, 1], color="#1f4e79", lw=1.3, ls="--",
                  dashes=(5, 2.5), alpha=0.95,
                  label=r"Fable 5 pipeline (%d pts)" % len(ref))
    axin.plot(pts[:, 0], pts[:, 1], color="#c0392b", lw=1.6, alpha=0.9,
              label=ext_label)
    axin.plot([anchor_m], [anchor_chi], "o", color="black", ms=9, mew=1.5,
              mfc="none", label=anchor_label)
    axin.set_xlim(1.2e-2, 5.5e-1); axin.set_ylim(8e-13, 8e-11)
    axin.tick_params(labelsize=14)
    axin.legend(fontsize=12.5, loc="upper left", framealpha=0.95)
    for s in axin.spines.values():
        s.set_edgecolor("#922b21"); s.set_linewidth(1.2)

    out = OUT / "figure2_showcase"
    fig.savefig(f"{out}.pdf", bbox_inches="tight")
    fig.savefig(f"{out}.png", bbox_inches="tight", dpi=140)
    print(f"wrote {out}.pdf")

    # numbers for the tex (stdout provenance)
    def _resid(curve, tag):
        lo = max(curve[:, 0].min(), gt[:, 0].min())
        hi = min(curve[:, 0].max(), gt[:, 0].max())
        sel = curve[(curve[:, 0] >= lo) & (curve[:, 0] <= hi)]
        gi = np.interp(np.log10(sel[:, 0]), np.log10(gt[:, 0]), np.log10(gt[:, 1]))
        res = np.abs(np.log10(sel[:, 1]) - gi)
        print(f"{tag}: median {np.median(res):.3f} dex, "
              f"p90 {np.percentile(res, 90):.3f}, max {res.max():.3f}, n={len(sel)}")

    _resid(pts, "figure curve")
    if ref is not None:
        _resid(ref, "staged ref ")


if __name__ == "__main__":
    main(DATA / "qualiphide2_fable_agent_extraction.json")
