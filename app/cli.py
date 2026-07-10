"""Small command line entry point for the MVP calculation core."""

from __future__ import annotations

import argparse
import csv
from pathlib import Path
from typing import Iterable, List, Tuple

from .core.stress import (
    effective_stress_mpa,
    hydrostatic_pore_pressure_mpa,
    vertical_stress_mpa,
)


def _read_depth_density_csv(path: Path) -> Tuple[List[float], List[float]]:
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        rows = list(reader)

    missing = {"TVD_m", "RHOB_g_cm3"} - set(reader.fieldnames or [])
    if missing:
        raise ValueError(f"CSV is missing required columns: {', '.join(sorted(missing))}")

    depth_tvd_m = [float(row["TVD_m"]) for row in rows]
    density_g_cm3 = [float(row["RHOB_g_cm3"]) for row in rows]
    return depth_tvd_m, density_g_cm3


def _write_results(
    rows: Iterable[Tuple[float, float, float, float, float]],
    output_path: Path,
) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(["TVD_m", "RHOB_g_cm3", "Sv_MPa", "Pp_MPa", "SvEff_MPa"])
        writer.writerows(rows)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run the 1D geomechanics MVP core.")
    parser.add_argument(
        "--input",
        type=Path,
        default=Path("benchmarks/case_001_constant_density/input.csv"),
        help="CSV with TVD_m and RHOB_g_cm3 columns.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("examples/mvp_results.csv"),
        help="Path for calculated result curves.",
    )
    parser.add_argument(
        "--fluid-density-kg-m3",
        type=float,
        default=1000.0,
        help="Fluid density used for hydrostatic pore pressure.",
    )
    parser.add_argument(
        "--biot",
        type=float,
        default=1.0,
        help="Biot coefficient for effective stress.",
    )
    return parser


def main() -> None:
    args = build_parser().parse_args()
    depth_tvd_m, density_g_cm3 = _read_depth_density_csv(args.input)

    sv_mpa = vertical_stress_mpa(depth_tvd_m, density_g_cm3)
    pp_mpa = hydrostatic_pore_pressure_mpa(depth_tvd_m, args.fluid_density_kg_m3)
    sv_eff_mpa = effective_stress_mpa(sv_mpa, pp_mpa, args.biot)

    rows = zip(depth_tvd_m, density_g_cm3, sv_mpa, pp_mpa, sv_eff_mpa)
    _write_results(rows, args.output)

    print(f"Wrote {len(depth_tvd_m)} rows to {args.output}")
    print(f"Bottom Sv: {sv_mpa[-1]:.2f} MPa")
    print(f"Bottom Pp: {pp_mpa[-1]:.2f} MPa")
    print(f"Bottom vertical effective stress: {sv_eff_mpa[-1]:.2f} MPa")

