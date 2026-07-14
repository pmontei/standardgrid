# standardgrid

# standardgrid

**standardgrid** is a Python library for generating official spatial reference grids aligned to recognised standards such as **C-Squares** and **INSPIRE**.

The project focuses on reproducible and standards-compliant grid generation for GIS, marine spatial planning, habitat mapping and environmental analysis.

## Features

- Official C-Squares support
- Official INSPIRE support
- Automatic grid alignment
- Grid centroid generation
- Pandas output
- Simple Python API

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