# Changelog

All notable changes to this project will be documented in this file.

This project follows Semantic Versioning (SemVer).

---

## [0.6.0] - 2026-07-15

### Added

- Initial public release.
- Support for official C-Squares reference grids.
- Support for official INSPIRE reference grids.
- `GridGenerator` core engine.
- Public `Grid` API.
- Automatic alignment of bounding boxes to the selected grid standard.
- Generation of grid centroid coordinates.
- Grid metadata:
  - Bounds
  - Number of rows
  - Number of columns
  - Number of points
- Export to CSV.
- Export to Microsoft Excel (`.xlsx`).
- Unit tests for `GridGenerator`.
- Unit tests for `Grid`.
- Unit tests for export functions.