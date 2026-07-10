# Current

## Current Sprint Goal

Собрать расчетное ядро MVP для 1D геомеханики: units, depth validation, vertical stress, hydrostatic pore pressure and effective stress.

Status: first pass implemented in `app/core` with `unittest` coverage. Next step is to connect this core to real LAS/CSV import workflow and expand benchmark cases.

## Next Task 1: CSV/LAS Import Bridge

Goal: связать расчетное ядро с реальными входными файлами.

Acceptance criteria:

- CSV import supports mapped depth and density columns;
- LAS import extracts `DEPT/TVD` and `RHOB`;
- invalid or missing units produce clear errors;
- example calculation can run on a real/synthetic LAS-derived table.

## Next Task 2: Benchmark Expansion

Goal: добавить benchmark cases из `docs/validation-cases.md`.

Acceptance criteria:

- case 002 hydrostatic pore pressure;
- case 003 effective stress;
- case 005 non-monotonic depth;
- expected outputs are stored in benchmark folders;
- all benchmarks run from one command.

## Completed Task 1: Units Module

Goal: сделать единый модуль конвертации единиц.

Acceptance criteria:

- depth conversion: ft <-> m;
- density conversion: g/cm3 <-> kg/m3;
- pressure conversion: psi <-> MPa;
- mud weight conversion: SG <-> ppg;
- tests for all conversions.

## Completed Task 2: Depth Validation

Goal: запретить расчеты на некорректной глубине.

Acceptance criteria:

- monotonic TVD passes;
- duplicate depth fails or warns according to policy;
- decreasing TVD fails;
- NaN depth fails.

## Completed Task 3: Vertical Stress

Goal: рассчитать `Sv` интегрированием плотности по TVD.

Acceptance criteria:

- constant density benchmark passes;
- output in MPa;
- handles first depth point correctly;
- raises error for invalid density;
- documents assumptions.

## Completed Task 4: Hydrostatic Pore Pressure

Goal: рассчитать базовое `Pp`.

Acceptance criteria:

- hydrostatic benchmark passes;
- fluid density is configurable;
- output in MPa.

## Completed Task 5: Effective Stress

Goal: рассчитать эффективные напряжения.

Acceptance criteria:

- supports Biot coefficient;
- default `alpha = 1.0`;
- benchmark case 003 passes.
