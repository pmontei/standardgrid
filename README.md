# StandardGrid

**StandardGrid** is a lightweight Python library for generating official spatial reference grids aligned with recognised standards such as **C-Squares** and **INSPIRE**.

The library was developed within the **EMODnet Seabed Habitats** project to support the harmonisation and automation of composite habitat map production carried out under **Work Package 3 (WP3)**. Its primary objective is to provide a reproducible and standardised way of generating reference grids for large-scale spatial analyses and map compilation.

Although initially developed for EMODnet Seabed Habitats, StandardGrid is intended as a general-purpose library for any application requiring standardised spatial reference grids.

---
## Supported resolutions

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

You can also query the supported resolutions directly from the API:

            from standardgrid import get_standard

            csquares = get_standard("csquares")

            print(csquares.resolutions)

            print(csquares.name)
            print(csquares.crs)
            print(csquares.units)
            print(csquares.resolutions)

## Why StandardGrid?

Combining habitat maps from different sources is often challenging because datasets are produced using different spatial resolutions, grid origins or processing workflows.

StandardGrid addresses this problem by generating grids that are precisely aligned with official spatial reference systems, ensuring that different datasets can be integrated consistently and reproducibly.

Typical applications include:

- Essential Fish Habitats (EFH)
- Vulnerable Marine Ecosystems (VME)
- Essential Ocean Variables (EOV)
- Habitat suitability modelling
- Marine spatial planning
- Environmental assessments
- Other harmonised marine habitat products

---

## Features

- Official C-Squares support
- Official INSPIRE support
- Automatic alignment to official reference grids
- Grid centroid generation
- Pandas DataFrame output
- CSV export
- Excel export
- Simple and lightweight Python API

---

## Installation

```bash
pip install standardgrid
```

or

```bash
git clone https://github.com/pmontei/standardgrid.git
```

---

## Example

```python
from standardgrid import Grid

grid = Grid(
    standard="csquares",
    resolution=0.01,
)

grid.generate(
    (-10.1, 36.6, -7.3, 41.9)
)

print(grid.points)

grid.to_csv("grid.csv")
```

---

## Supported standards

Currently supported:

- C-Squares
- INSPIRE Grid

Additional reference grids may be added in future releases.

---

## Acknowledgements

StandardGrid was developed within the **EMODnet Seabed Habitats** project.

The initial motivation for the library was the harmonisation and automation of composite habitat map production under **Work Package 3**, including products such as:

- Essential Fish Habitats (EFH)
- Vulnerable Marine Ecosystems (VME)
- Essential Ocean Variables (EOV)

EMODnet Seabed Habitats is funded by the European Union.

---

## License

This project is released under the MIT License.


Developed by: Pedro Monteiro, CCMAR – University of Algarve
Project: EMODnet Seabed Habitats