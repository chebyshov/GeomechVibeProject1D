# ADR-001: Units

## Status

Accepted for MVP.

## Context

Нефтяная геомеханика часто смешивает SI и oilfield units. Это опасно для расчетов давления, напряжений и mud weight window.

## Decision

Внутренние расчеты выполняются только в SI-derived units:

- depth: `m`;
- density: `kg/m3`;
- pressure/stress: `MPa`;
- gradient: `MPa/m` or `MPa/km`;
- slowness: `s/m`;
- velocity: `m/s`;
- angle: `deg` for user input, `rad` if needed internally;
- mud weight output: `SG`, `ppg`, `MPa`.

Входные oilfield units разрешены, но конвертируются на границе `io` или `units`.

## Consequences

- расчетные функции должны иметь явные unit suffixes в именах или типах;
- нельзя передавать `ppg` туда, где ожидается pressure;
- каждый импорт должен сохранять исходные единицы как metadata;
- тесты должны проверять conversion roundtrip.
