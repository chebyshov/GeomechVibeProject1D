# Backlog

## Product and Architecture

- Define project file format.
- Define result curve schema.
- Define audit trail schema.
- Add ADR for horizontal stress model.
- Add ADR for wellbore stability criterion.

## Core Calculations

- Implement units conversion module.
- Implement depth monotonicity validation.
- Implement vertical stress from density.
- Implement hydrostatic pore pressure.
- Implement user-defined pore pressure curve.
- Implement effective stress calculation.
- Implement simple `Shmin` model.
- Implement basic mud weight window.

## Data IO

- Implement CSV import.
- Implement LAS import.
- Implement XLSX import.
- Implement curve mapping.
- Implement result CSV export.

## Validation

- Add benchmark case 001 constant density.
- Add benchmark case 002 hydrostatic pore pressure.
- Add benchmark case 003 effective stress.
- Add benchmark case 004 missing density.
- Add benchmark case 005 non-monotonic depth.
- Add benchmark case 006 narrow mud window.

## UI

- Create first interactive screen.
- Add file upload.
- Add curve mapping view.
- Add depth tracks.
- Add mud window plot.
- Add warning panel.

## Reports

- Export result curves to CSV/XLSX.
- Generate short engineering report.
- Add methods and assumptions section to report.
