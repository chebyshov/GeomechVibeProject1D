# ADR-002: Pore Pressure Model

## Status

Accepted for MVP scope; advanced methods pending separate ADR.

## Context

Поровое давление является одним из ключевых входов для эффективных напряжений и окна бурового раствора. Ошибка в `Pp` напрямую влияет на рекомендации по бурению.

## Decision

MVP поддерживает:

1. Hydrostatic pore pressure.
2. User-defined pore pressure curve.
3. Calibration points for pressure tests as overlay, без автоматической инверсии на первом этапе.

Advanced methods будут добавляться отдельно:

- Eaton sonic;
- Eaton resistivity;
- Bowers;
- normal compaction trend based methods.

## Requirements

Каждый метод должен возвращать:

- calculated `Pp_MPa`;
- method name;
- parameters;
- warnings;
- confidence or quality flag if applicable.

## Consequences

- MVP остается простым и проверяемым;
- сложные методы не смешиваются с базовой архитектурой;
- перед реализацией Eaton/Bowers нужно добавить отдельные benchmark cases.
