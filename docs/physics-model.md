# Physics Model

## Общие соглашения

- Внутренние расчеты выполняются в SI.
- Глубина по умолчанию: `TVD` в метрах.
- Сжимающие напряжения считаются положительными.
- Давления и напряжения внутри ядра хранятся в MPa.
- Плотность внутри расчетов хранится в kg/m3.
- Ускорение свободного падения: `g = 9.80665 m/s2`.
- Все oilfield units допускаются только на входе/выходе и должны явно конвертироваться.

## Основные обозначения

- `Sv`: vertical stress / overburden stress.
- `Pp`: pore pressure.
- `Shmin`: minimum horizontal stress.
- `SHmax`: maximum horizontal stress.
- `sigma_v_eff`: vertical effective stress.
- `alpha`: Biot coefficient.
- `UCS`: unconfined compressive strength.
- `phi`: internal friction angle.
- `T0`: tensile strength.
- `MW`: mud weight.

## Vertical Stress

Базовая модель:

```text
Sv(z) = integral rho(z) * g * dz
```

Требования:

- интегрировать по TVD, не по MD;
- учитывать water depth/air gap отдельными поправками, если они заданы;
- поддерживать константную или интерполированную плотность в интервалах пропусков;
- выводить `Sv` в MPa и эквивалентный градиент.

## Pore Pressure

MVP:

1. Hydrostatic pressure:

```text
Pp(z) = rho_fluid * g * z
```

2. User-defined pressure curve.

Дальнейшее развитие:

- Eaton sonic method;
- Eaton resistivity method;
- Bowers method;
- regional normal compaction trend;
- pressure calibration with MDT/RFT.

Все методы порового давления должны возвращать:

- `Pp`;
- метод;
- параметры;
- диагностические предупреждения;
- confidence flag по интервалам.

## Effective Stress

Базовое соглашение:

```text
sigma_eff = sigma_total - alpha * Pp
```

Для MVP допускается `alpha = 1.0`, но пользователь должен видеть и менять этот параметр.

## Horizontal Stresses

MVP должен поддерживать инженерную модель:

```text
Shmin = f(Sv, Pp, elastic_properties, tectonic_strain, calibration)
SHmax = f(Shmin, stress_regime, calibration, constraints)
```

Конкретные уравнения фиксируются в отдельном ADR перед реализацией production-версии.

Минимальная реализация для прототипа может начинаться с:

- пользовательского градиента `Shmin`;
- calibration points from LOT/FIT/XLOT;
- ограничений по stress regime.

## Rock Properties

Базовые свойства:

- dynamic Young's modulus;
- dynamic Poisson's ratio;
- static Young's modulus via correlation;
- UCS via selected correlation or user curve;
- friction angle;
- tensile strength.

Все корреляции должны иметь:

- источник/название;
- применимость;
- единицы входов и выходов;
- предупреждение, если входные данные вне разумного диапазона.

## Wellbore Stability

Для расчета окна бурового раствора нужны:

- нижняя граница по pore pressure/kick;
- нижняя граница по shear failure/breakout;
- верхняя граница по tensile failure;
- верхняя граница по fracture/losses.

MVP:

- вертикальная или почти вертикальная скважина;
- 1D профиль;
- Mohr-Coulomb criterion;
- простая оценка fracture pressure через `Shmin`.

Post-MVP:

- произвольная траектория MD/TVD/inclination/azimuth;
- Kirsch equations;
- anisotropy;
- bedding plane weakness;
- thermal stress;
- depletion/injection scenarios.

## Что нельзя делать молча

- менять знак напряжений;
- смешивать MD и TVD;
- использовать ppg как pressure;
- экстраполировать длинные пропуски;
- подменять неизвестную density дефолтной без warning;
- калибровать параметры без записи в audit trail.
