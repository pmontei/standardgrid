from standardgrid import Grid

grid = Grid(
    standard="inspire",
    resolution=1000,
)

grid.generate(
    (4000000, 2500000, 4010000, 2510000)
)

print(grid.points.head())

grid.to_csv("inspire_grid.csv")