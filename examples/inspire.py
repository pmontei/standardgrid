from standardgrid import Grid

grid = Grid(
    standard="inspire",
    resolution=1000,
)

grid.generate(
    (
        3500000,
        2000000,
        3600000,
        2100000,
    )
)

print(grid.points.head())

grid.to_csv("inspire_grid.csv")