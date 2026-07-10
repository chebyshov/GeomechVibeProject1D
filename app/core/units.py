"""Unit conversions used at IO boundaries.

The calculation core keeps depth in m, density in kg/m3, and pressure/stress in
MPa. Oilfield units are converted before entering geomechanics formulas.
"""

from __future__ import annotations

from .constants import MPA_PER_PSI, PPG_PER_SG, PSI_PER_MPA

FT_PER_M = 3.280839895013123
M_PER_FT = 1.0 / FT_PER_M


def ft_to_m(value_ft: float) -> float:
    return value_ft * M_PER_FT


def m_to_ft(value_m: float) -> float:
    return value_m * FT_PER_M


def g_cm3_to_kg_m3(value_g_cm3: float) -> float:
    return value_g_cm3 * 1000.0


def kg_m3_to_g_cm3(value_kg_m3: float) -> float:
    return value_kg_m3 / 1000.0


def psi_to_mpa(value_psi: float) -> float:
    return value_psi * MPA_PER_PSI


def mpa_to_psi(value_mpa: float) -> float:
    return value_mpa * PSI_PER_MPA


def sg_to_ppg(value_sg: float) -> float:
    return value_sg * PPG_PER_SG


def ppg_to_sg(value_ppg: float) -> float:
    return value_ppg / PPG_PER_SG

