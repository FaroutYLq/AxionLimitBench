"""Vendored fragments of AutoAxionLimits `pipeline/` that the scorer needs
(generated from pipeline/config.py and pipeline/reviewer.py at master 73682236).
"""
from __future__ import annotations

import logging

logger = logging.getLogger(__name__)

COUPLING_TYPES: dict = {'DarkPhoton': {'data_dir': 'limit_data/DarkPhoton', 'y_axis': 'kinetic mixing chi'}, 'AxionPhoton': {'data_dir': 'limit_data/AxionPhoton', 'y_axis': 'g_agamma [GeV^-1]'}, 'AxionElectron': {'data_dir': 'limit_data/AxionElectron', 'y_axis': 'g_ae'}, 'AxionNeutron': {'data_dir': 'limit_data/AxionNeutron', 'y_axis': 'g_an'}, 'AxionProton': {'data_dir': 'limit_data/AxionProton', 'y_axis': 'g_ap'}, 'AxionEDM': {'data_dir': 'limit_data/AxionEDM', 'y_axis': 'd_n [e cm]'}, 'AxionCPV': {'data_dir': 'limit_data/AxionCPV', 'y_axis': 'coupling'}, 'AxionMass': {'data_dir': 'limit_data/AxionMass', 'y_axis': 'm_a [eV]'}, 'MonopoleDipole': {'data_dir': 'limit_data/MonopoleDipole', 'y_axis': 'coupling'}, 'ScalarPhoton': {'data_dir': 'limit_data/ScalarPhoton', 'y_axis': 'd_e'}, 'ScalarElectron': {'data_dir': 'limit_data/ScalarElectron', 'y_axis': 'd_e'}, 'ScalarBaryon': {'data_dir': 'limit_data/ScalarBaryon', 'y_axis': 'coupling'}, 'ScalarNucleon': {'data_dir': 'limit_data/ScalarNucleon', 'y_axis': 'coupling'}, 'VectorBL': {'data_dir': 'limit_data/VectorB-L', 'y_axis': 'g_BL'}}

_COUPLING_ALIASES: dict[str, str] = {
    # AxionProton
    "axionproton": "AxionProton",
    "g_ap": "AxionProton",
    "g_app": "AxionProton",
    "alp-proton": "AxionProton",
    "alp proton": "AxionProton",
    "axion proton": "AxionProton",
    "axion-proton": "AxionProton",
    # AxionNeutron (also default for generic "nucleon" coupling)
    "axionneutron": "AxionNeutron",
    "axionnucleon": "AxionNeutron",
    "axion nucleon": "AxionNeutron",
    "axion-nucleon": "AxionNeutron",
    "alp-nucleon": "AxionNeutron",
    "alp nucleon": "AxionNeutron",
    "g_an": "AxionNeutron",
    "g_ann": "AxionNeutron",
    "alp-neutron": "AxionNeutron",
    "alp neutron": "AxionNeutron",
    "axion neutron": "AxionNeutron",
    "axion-neutron": "AxionNeutron",
    # AxionElectron
    "axionelectron": "AxionElectron",
    "g_ae": "AxionElectron",
    "gaee": "AxionElectron",
    "g_aee": "AxionElectron",
    "axion-electron": "AxionElectron",
    "axion-electron coupling": "AxionElectron",
    "alp-electron": "AxionElectron",
    "axion electron": "AxionElectron",
    # AxionPhoton
    "axionphoton": "AxionPhoton",
    "gagg": "AxionPhoton",
    "g_agamma": "AxionPhoton",
    "gaγγ": "AxionPhoton",
    "g_aγγ": "AxionPhoton",
    "axion-photon coupling": "AxionPhoton",
    "axion-diphoton coupling": "AxionPhoton",
    "alp-photon": "AxionPhoton",
    "alp photon": "AxionPhoton",
    "axion photon": "AxionPhoton",
    "axion photon coupling": "AxionPhoton",
    # DarkPhoton
    "darkphoton": "DarkPhoton",
    "dark photon": "DarkPhoton",
    "kinetic mixing": "DarkPhoton",
    "hidden photon": "DarkPhoton",
    "hidden sector photon": "DarkPhoton",
    # AxionEDM
    "axionedm": "AxionEDM",
    "axion edm": "AxionEDM",
    # AxionCPV
    "axioncpv": "AxionCPV",
    "axion cpv": "AxionCPV",
    "axion cp violation": "AxionCPV",
    # AxionMass
    "axionmass": "AxionMass",
    "axion mass": "AxionMass",
    # MonopoleDipole
    "monopoledipole": "MonopoleDipole",
    "monopole dipole": "MonopoleDipole",
    "monopole-dipole": "MonopoleDipole",
    "spin-mass": "MonopoleDipole",
    "spin-mass coupling": "MonopoleDipole",
    "g_s g_p": "MonopoleDipole",
    "fifth force axion": "MonopoleDipole",
    "exotic spin-dependent": "MonopoleDipole",
    # ScalarPhoton
    "scalarphoton": "ScalarPhoton",
    "scalar photon": "ScalarPhoton",
    "scalar-photon": "ScalarPhoton",
    "d_e photon": "ScalarPhoton",
    "d_gamma": "ScalarPhoton",
    "dilaton photon": "ScalarPhoton",
    "fine structure constant variation": "ScalarPhoton",
    "fine structure variation": "ScalarPhoton",
    "alpha variation": "ScalarPhoton",
    "clock comparison photon": "ScalarPhoton",
    # ScalarElectron
    "scalarelectron": "ScalarElectron",
    "scalar electron": "ScalarElectron",
    "scalar-electron": "ScalarElectron",
    "d_me": "ScalarElectron",
    "d_e electron": "ScalarElectron",
    "dilaton electron": "ScalarElectron",
    "electron mass variation": "ScalarElectron",
    "clock comparison electron": "ScalarElectron",
    # ScalarBaryon
    "scalarbaryon": "ScalarBaryon",
    "scalar baryon": "ScalarBaryon",
    "scalar-baryon": "ScalarBaryon",
    "d_baryon": "ScalarBaryon",
    "d_g": "ScalarBaryon",
    "fifth force baryon": "ScalarBaryon",
    "yukawa baryon": "ScalarBaryon",
    "dilaton baryon": "ScalarBaryon",
    "equivalence principle baryon": "ScalarBaryon",
    # ScalarNucleon
    "scalarnucleon": "ScalarNucleon",
    "scalar nucleon": "ScalarNucleon",
    "scalar-nucleon": "ScalarNucleon",
    "d_nucleon": "ScalarNucleon",
    "d_hat": "ScalarNucleon",
    "yukawa_interaction_strength": "ScalarNucleon",
    "yukawa interaction": "ScalarNucleon",
    "yukawa nucleon": "ScalarNucleon",
    "fifth force nucleon": "ScalarNucleon",
    "dilaton nucleon": "ScalarNucleon",
    "equivalence principle nucleon": "ScalarNucleon",
    # VectorBL
    "vectorbl": "VectorBL",
    "vector b-l": "VectorBL",
    "b-l gauge": "VectorBL",
    "b-l gauge boson": "VectorBL",
    "gauged b-l": "VectorBL",
    "g_bl": "VectorBL",
    "u(1)_b-l": "VectorBL",
    "u(1)_{b-l}": "VectorBL",
    "z prime b-l": "VectorBL",
    "baryon minus lepton": "VectorBL",
    "b minus l": "VectorBL",
}


def _normalize_coupling_type(raw: str) -> str:
    """
    Map a free-form LLM coupling type string to a canonical COUPLING_TYPES key.
    Returns the canonical key if found, otherwise raises KeyError.
    """
    # Exact match first
    if raw in COUPLING_TYPES:
        return raw
    # Case-insensitive alias lookup — also try stripping parenthetical suffixes
    key = raw.lower().strip()
    # Strip anything after '(' e.g. "g_ap (ALP-proton coupling)" → "g_ap"
    key_no_paren = key.split("(")[0].strip()
    for candidate in (key, key_no_paren):
        if candidate in _COUPLING_ALIASES:
            canonical = _COUPLING_ALIASES[candidate]
            logger.info("Normalized coupling type %r → %r", raw, canonical)
            return canonical
    # Fuzzy: check if any alias is a substring of the input.
    # Use longest match to avoid e.g. "d_g" matching before "d_gamma".
    matches = [(alias, canonical) for alias, canonical in _COUPLING_ALIASES.items() if alias in key]
    if matches:
        alias, canonical = max(matches, key=lambda x: len(x[0]))
        logger.info("Normalized coupling type %r → %r (substring match on %r)", raw, canonical, alias)
        return canonical
    raise KeyError(raw)
