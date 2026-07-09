# Data Formats

## Поддерживаемые входы

### LAS

Обязательные возможности:

- чтение LAS 2.0;
- чтение LAS 3.0 по возможности;
- извлечение mnemonics, units, null value;
- сохранение исходного имени кривой;
- mapping на внутренние имена.

### CSV

Требования:

- первая строка содержит заголовки;
- единицы могут быть указаны в заголовке: `RHOB[g/cm3]`;
- разделитель определяется автоматически или задается пользователем;
- кодировка должна поддерживать UTF-8.

### XLSX

Требования:

- выбор листа;
- выбор строки заголовков;
- mapping колонок;
- сохранение имени листа как source metadata.

## Внутренние имена кривых

| Internal name | Description | Preferred unit |
| --- | --- | --- |
| `MD` | measured depth | m |
| `TVD` | true vertical depth | m |
| `RHOB` | bulk density | g/cm3 input, kg/m3 internal |
| `DTC` | compressional slowness | us/ft input, s/m internal |
| `DTS` | shear slowness | us/ft input, s/m internal |
| `GR` | gamma ray | API |
| `NPHI` | neutron porosity | fraction |
| `PHI` | porosity | fraction |
| `RES` | resistivity | ohm.m |
| `PP` | pore pressure | MPa |
| `UCS` | unconfined compressive strength | MPa |
| `FA` | friction angle | deg |
| `TSTR` | tensile strength | MPa |

## Project File

Проект расчета должен хранить:

- metadata скважины;
- пути или embedded copy входных данных;
- mapping кривых;
- единицы;
- параметры расчетного кейса;
- операции подготовки данных;
- калибровочные точки;
- версии расчетных модулей.

## Export

Поддерживаемые выходы:

- CSV result curves;
- XLSX result workbook;
- PNG/PDF plots;
- PDF/HTML engineering report;
- JSON project metadata.

## Минимальные поля результата

| Field | Description |
| --- | --- |
| `TVD_m` | true vertical depth |
| `Sv_MPa` | vertical stress |
| `Pp_MPa` | pore pressure |
| `SvEff_MPa` | vertical effective stress |
| `Shmin_MPa` | minimum horizontal stress |
| `SHmax_MPa` | maximum horizontal stress |
| `MW_low_SG` | lower mud window bound |
| `MW_high_SG` | upper mud window bound |
| `RiskFlag` | interval risk indicator |
