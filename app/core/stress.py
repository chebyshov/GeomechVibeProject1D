"""Stress and pressure calculations for the MVP 1D geomechanics core."""

from __future__ import annotations

from typing import Iterable, List

from .constants import MPA_PER_PA, STANDARD_GRAVITY_M_S2
from .units import g_cm3_to_kg_m3
from .validation import (
    require_same_length,
    validate_biot_coefficient,
    validate_non_negative,
    validate_positive,
    validate_strictly_increasing,
)


def vertical_stress_mpa(
    depth_tvd_m: Iterable[float],
    density_g_cm3: Iterable[float],
    gravity_m_s2: float = STANDARD_GRAVITY_M_S2,
) -> List[float]:
    """Calculate vertical stress by integrating bulk density over TVD.

    The first stress value is 0 MPa at the first input depth. For each interval,
    trapezoidal integration uses the density at both interval boundaries.
    """

    depth = validate_strictly_increasing(depth_tvd_m, "depth_tvd_m")
    density = validate_positive(density_g_cm3, "density_g_cm3")
    require_same_length(depth, density, "depth_tvd_m", "density_g_cm3")

    sv_mpa = [0.0]
    accumulated_pa = 0.0
    for index in range(1, len(depth)):
        dz_m = depth[index] - depth[index - 1]
        avg_density_kg_m3 = 0.5 * (
            g_cm3_to_kg_m3(density[index - 1]) + g_cm3_to_kg_m3(density[index])
        )
        accumulated_pa += avg_density_kg_m3 * gravity_m_s2 * dz_m
        sv_mpa.append(accumulated_pa * MPA_PER_PA)
    return sv_mpa


def hydrostatic_pore_pressure_mpa(
    depth_tvd_m: Iterable[float],
    fluid_density_kg_m3: float = 1000.0,
    gravity_m_s2: float = STANDARD_GRAVITY_M_S2,
) -> List[float]:
    """Calculate hydrostatic pore pressure from TVD and fluid density."""

    depth = validate_strictly_increasing(depth_tvd_m, "depth_tvd_m")
    validate_positive([fluid_density_kg_m3], "fluid_density_kg_m3")
    return [fluid_density_kg_m3 * gravity_m_s2 * item * MPA_PER_PA for item in depth]


def effective_stress_mpa(
    total_stress_mpa: Iterable[float],
    pore_pressure_mpa: Iterable[float],
    biot_alpha: float = 1.0,
) -> List[float]:
    """Calculate effective stress using sigma_eff = sigma_total - alpha * Pp."""

    total = validate_non_negative(total_stress_mpa, "total_stress_mpa")
    pore = validate_non_negative(pore_pressure_mpa, "pore_pressure_mpa")
    alpha = validate_biot_coefficient(biot_alpha)
    require_same_length(total, pore, "total_stress_mpa", "pore_pressure_mpa")
    return [stress - alpha * pressure for stress, pressure in zip(total, pore)]
