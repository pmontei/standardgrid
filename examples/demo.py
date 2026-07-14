from Scripts.GITHUB.standardgrid.standardgrid import Reference_grid

grid = Reference_grid(
    standard="csquares",
    resolution=0.01,
    bbox=(-10.1, -7.3, 36.6, 41.9)
)

print(grid.points.head())

grid.to_csv("Portugal.csv")