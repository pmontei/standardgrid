from standardgrid import Grid, __version__

print(__version__)


grid = Grid(
    standard="csquares",
    resolution=0.01,
)

grid.generate((-10, 36, -9.9, 36.1))

print(grid)
print(grid.points.head())