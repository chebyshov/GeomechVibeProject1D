# Current

## Current Sprint Goal

Собрать расчетное ядро MVP для 1D геомеханики: units, depth validation, vertical stress, hydrostatic pore pressure and effective stress.

## Task 1: Units Module

Goal: сделать единый модуль конвертации единиц.

Acceptance criteria:

- depth conversion: ft <-> m;
- density conversion: g/cm3 <-> kg/m3;
- pressure conversion: psi <-> MPa;
- mud weight conversion: SG <-> ppg;
- tests for all conversions.

## Task 2: Depth Validation

Goal: запретить расчеты на некорректной глубине.

Acceptance criteria:

- monotonic TVD passes;
- duplicate depth fails or warns according to policy;
- decreasing TVD fails;
- NaN depth fails.

## Task 3: Vertical Stress

Goal: рассчитать `Sv` интегрированием плотности по TVD.

Acceptance criteria:

- constant density benchmark passes;
- output in MPa;
- handles first depth point correctly;
- raises error for invalid density;
- documents assumptions.

## Task 4: Hydrostatic Pore Pressure

Goal: рассчитать базовое `Pp`.

Acceptance criteria:

- hydrostatic benchmark passes;
- fluid density is configurable;
- output in MPa.

## Task 5: Effective Stress

Goal: рассчитать эффективные напряжения.

Acceptance criteria:

- supports Biot coefficient;
- default `alpha = 1.0`;
- benchmark case 003 passes.
