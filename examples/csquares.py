from standardgrid import Grid

grid = Grid(
    standard="csquares",
    resolution=0.01,
)

grid.generate(
    (-10.1, 36.6, -7.3, 41.9)
)

print(grid.points.head())

grid.to_csv("csquares_grid.csv")