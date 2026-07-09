# Roadmap

## Phase 0: Project Foundation

Цель: создать основу для совместной работы людей, Codex и Claude Code.

Deliverables:

- структура `docs/`, `tasks/`, `benchmarks/`, `tests/`, `examples/`;
- продуктовые требования;
- физические соглашения;
- ADR по единицам;
- ADR по поровому давлению;
- первый backlog.

Exit criteria:

- документы лежат в git;
- все участники понимают MVP;
- следующая задача может быть выдана агенту без устных пояснений.

## Phase 1: Calculation Core MVP

Цель: реализовать минимальное расчетное ядро.

Deliverables:

- импорт простых CSV;
- depth curve validation;
- units conversion;
- `Sv` from density;
- hydrostatic `Pp`;
- effective stress;
- базовые result curves;
- unit tests;
- synthetic benchmarks 001-005.

Exit criteria:

- все тесты проходят;
- benchmark values совпадают с допусками;
- расчет можно запустить из CLI или простого script/notebook.

## Phase 2: LAS Import and Data Preparation

Цель: сделать работу с реальными каротажными данными.

Deliverables:

- LAS import;
- curve mapping;
- null handling;
- interpolation rules;
- resampling;
- data quality warnings;
- audit trail.

Exit criteria:

- можно загрузить `West_Siberia_Well1_4000m.las`;
- пользователь видит, какие кривые найдены;
- расчет не выполняется при critical data issues.

## Phase 3: Basic Stress and Mud Window

Цель: получить первый полезный инженерный результат.

Deliverables:

- simple `Shmin` model;
- user/calibrated `Shmin` gradient;
- basic `SHmax` constraints;
- UCS/friction angle user curves or constants;
- Mohr-Coulomb breakout lower bound;
- fracture/tensile upper bound;
- mud window output in SG/ppg/MPa.

Exit criteria:

- строится окно бурового раствора по глубине;
- narrow window intervals отмечаются автоматически;
- все ключевые параметры видны пользователю.

## Phase 4: UI Prototype

Цель: сделать интерактивный прототип для инженера.

Deliverables:

- загрузка файла через UI;
- mapping curves;
- depth tracks;
- расчет по кнопке;
- графики `Sv`, `Pp`, stresses, mud window;
- экспорт CSV.

Exit criteria:

- пользователь может пройти workflow без редактирования кода;
- ошибки данных отображаются понятным языком;
- UI использует core API, не содержит формул.

## Phase 5: Calibration and Reports

Цель: приблизить продукт к инженерной работе.

Deliverables:

- LOT/FIT/XLOT points;
- MDT/RFT pressure points;
- calibration overlay on plots;
- case save/load;
- engineering report;
- result workbook export.

Exit criteria:

- расчет можно сохранить и повторить;
- отчет содержит методы, параметры и warnings;
- калибровочные точки отображаются на треках.

## Phase 6: Advanced Models

Цель: расширить физику и применимость.

Candidate features:

- Eaton sonic/resistivity pore pressure;
- Bowers pore pressure;
- dynamic-to-static elastic correlations;
- Kirsch equations for inclined wells;
- stress regime classification;
- anisotropy;
- thermal stress;
- depletion scenario;
- uncertainty ranges.

Exit criteria:

- каждый новый метод имеет ADR, docs, tests and benchmarks;
- UI позволяет сравнить несколько расчетных cases.

## Phase 7: Product Hardening

Цель: подготовить стабильную версию.

Deliverables:

- packaging;
- automated tests in CI;
- example datasets;
- documentation for users;
- validation report;
- performance checks;
- error telemetry/logging for local debugging.

Exit criteria:

- новая установка запускается без ручной настройки;
- smoke tests проходят на чистом окружении;
- есть демонстрационный проект.
