from pathlib import Path

from standardgrid import Grid


def test_csv_export():

    grid = Grid(
        standard="csquares",
        resolution=0.01,
    )

    grid.generate(
        (
            10.231,
            35.004,
            10.298,
            35.091,
        )
    )

    filename = "test_grid.csv"

    grid.to_csv(filename)

    assert Path(filename).exists()

    Path(filename).unlink()


def test_excel_export():

    grid = Grid(
        standard="csquares",
        resolution=0.01,
    )

    grid.generate(
        (
            10.231,
            35.004,
            10.298,
            35.091,
        )
    )

    filename = "test_grid.xlsx"

    grid.to_excel(filename)

    assert Path(filename).exists()

    Path(filename).unlink()


if __name__ == "__main__":

    test_csv_export()
    test_excel_export()

    print("All tests passed.")




    