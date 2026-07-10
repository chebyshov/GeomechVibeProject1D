# Geomech Vibe Project 1D

This repository is a shared workspace for the 1D geomechanics vibe project.

## For Salavat / pes1

Open this repository in Claude Code to inspect the project state and continue work:

```bash
git clone https://github.com/chebyshov/GeomechVibeProject1D.git
cd GeomechVibeProject1D
claude
```

Current state: the repository has been initialized and connected to GitHub.
Project source files can be added here as the work develops.

## Calculation Core MVP

The first Python calculation core lives in `app/core`.

It currently provides:

- unit conversions for depth, density, pressure, and mud weight;
- strict TVD validation;
- vertical stress integration from density;
- hydrostatic pore pressure;
- effective stress with Biot coefficient;
- benchmark input for the constant-density case.

Run tests:

```bash
python3 -m unittest discover -s tests
```

Run the MVP calculation example:

```bash
python3 -m app \
  --input benchmarks/case_001_constant_density/input.csv \
  --output examples/mvp_results.csv
```

The example writes `TVD_m`, `RHOB_g_cm3`, `Sv_MPa`, `Pp_MPa`, and `SvEff_MPa`.

## 1D Geomechanics HTML Model

Open `index.html` in a browser to run the current prototype. The page can:

- parse a LAS file from upload;
- auto-load `data/pes1.las`, `pes1.las`, `well.las`, or `data/well.las` when one is added to git;
- build simple 1D elastic-property correlations;
- calculate a poroelastic stress model for normal stress regime;
- calculate a first-pass wellbore stability window;
- plot GR, porosity, elastic properties, stresses, WBS, and caliper tracks;
- recalibrate `Shmin` from a user-specified calibration point.

If no LAS file is present, the app starts with a synthetic fallback dataset so the model and plots are still visible.
