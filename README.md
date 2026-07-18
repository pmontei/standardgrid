# StandardGrid

**StandardGrid** is a lightweight Python library for generating **standards-compliant spatial reference grids** aligned with recognised reference systems such as **C-Squares** and **INSPIRE**.

The library was originally developed within the **EMODnet Seabed Habitats** project to support the harmonisation and automation of composite habitat map production carried out under **Work Package 3 (WP3)**. Its primary objective is to provide a reproducible and standardised way of generating reference grids for large-scale spatial analyses and map compilation.

Although originally developed for EMODnet Seabed Habitats, StandardGrid is intended as a general-purpose Python library for any GIS application requiring official and reproducible spatial reference grids.

---

## Why StandardGrid?

Combining spatial datasets from different sources is often challenging because they are produced using different grid origins, spatial resolutions or processing workflows.

StandardGrid addresses this problem by generating centroid grids that are precisely aligned with recognised spatial reference standards, ensuring that different datasets can be integrated consistently and reproducibly.

Typical applications include:

* Essential Fish Habitats (EFH)
* Vulnerable Marine Ecosystems (VME)
* Essential Ocean Variables (EOV)
* Habitat suitability modelling
* Marine spatial planning
* Environmental assessments
* Large-scale composite habitat mapping
* Any workflow requiring standards-aligned reference grids

---

## Features

* Official C-Squares support
* Official INSPIRE support
* Standards-compliant centroid generation
* Automatic alignment to official reference grids
* Validation of supported resolutions
* Simple and lightweight Python API
* Pandas DataFrame output
* CSV export
* Excel export

---

## Installation

Install directly from PyPI:

```bash
pip install standardgrid
```

or install from the GitHub repository:

```bash
git clone https://github.com/pmontei/standardgrid.git

cd standardgrid

pip install .
```

---

## Quick Start

```python
from standardgrid import Grid

grid = Grid(
    standard="csquares",
    resolution=0.01,
)

grid.generate(
    (-10.1, 36.6, -7.3, 41.9)
)

print(grid)

print(grid.points.head())

grid.to_csv("grid.csv")

The generated grid is available as a pandas DataFrame through `grid.points`.

```

---

## Public API

StandardGrid exposes a compact and stable public API.

Most users will only need the `Grid` class to generate standards-aligned reference grids.

```python
from standardgrid import (
    Grid,
    GridStandard,
    available_standards,
    get_standard,
    standards,
)
```

The remaining functions provide access to metadata describing the supported spatial reference standards.


## Supported Standards

StandardGrid currently supports the following official spatial reference systems.

| Standard     | CRS       | Units   |
| ------------ | --------- | ------- |
| C-Squares    | EPSG:4326 | Degrees |
| INSPIRE      | EPSG:3035 | Metres  |

Additional standards may be incorporated in future releases.


## API identifiers

Standards are selected in the API using their **identifier** (`code`), while documentation uses their official name.

| API identifier | Official name |
|----------------|---------------|
| `csquares`     | C-Squares     |
| `inspire`      | INSPIRE       |

Example:

```python
grid = Grid(
    standard="csquares",
    resolution=0.01,
)
```

---

## Supported Resolutions

Each supported standard defines a fixed set of official grid resolutions.

The requested resolution is validated automatically during grid creation.


| Standard  | Resolution | Description            |
| --------- | ---------: | ---------------------- |
| C-Squares |        10° | Global reference grid  |
| C-Squares |         5° |                        |
| C-Squares |         1° |                        |
| C-Squares |       0.5° |                        |
| C-Squares |       0.1° |                        |
| C-Squares |      0.05° | ICES statistical grid  |
| C-Squares |      0.01° | Common habitat mapping |
| INSPIRE   |   100000 m | 100 km                 |
| INSPIRE   |    10000 m | 10 km                  |
| INSPIRE   |     1000 m | 1 km                   |
| INSPIRE   |      100 m | 100 m                  |
| INSPIRE   |       10 m | 10 m                   |
| INSPIRE   |        1 m | 1 m                    |

Attempting to use an unsupported resolution raises a `ValueError`.

---

## Working with Standards

The supported standards and their properties can be queried directly from the API.

```python
from standardgrid import available_standards, get_standard

for code in available_standards():

    standard = get_standard(code)

    print(standard.name)
    print(standard.crs)
    print(standard.units)
    print(standard.resolutions)
```
Alternatively, all supported standards can be accessed directly:

```python
from standardgrid import standards

for standard in standards():
    print(f"{standard.name} ({standard.code})")
```

Output:


```text
C-Squares
EPSG:4326
degrees
(10.0, 5.0, 1.0, 0.5, 0.1, 0.05, 0.01, 0.005, 0.001, 0.0005, 0.0001, 0.00005, 0.00001)

INSPIRE
EPSG:3035
metres
(100000.0, 10000.0, 1000.0, 100.0, 10.0, 1.0)
```

---

## Project Background

StandardGrid was originally developed within the **EMODnet Seabed Habitats** project to support the harmonisation and automation of composite habitat mapping workflows developed under **Work Package 3 (WP3)**.

The library was initially designed to facilitate the production of harmonised pan-European spatial products, including:

* Essential Fish Habitats (EFH)
* Vulnerable Marine Ecosystems (VME)
* Essential Ocean Variables (EOV)

By ensuring that all datasets share exactly the same spatial reference grid, StandardGrid simplifies rasterisation, spatial overlay, data aggregation and reproducible GIS workflows.

Although originally developed for marine habitat mapping, the library is applicable to any GIS workflow requiring official standards-aligned reference grids.

---

## Citation

If StandardGrid contributes to published research or technical reports, please cite the project and acknowledge the EMODnet Seabed Habitats initiative where appropriate.

---

## License

This project is released under the **MIT License**.

---

**Developed by**

Pedro Monteiro
CCMAR – Centre of Marine Sciences
University of Algarve

**Project**

EMODnet Seabed Habitats
