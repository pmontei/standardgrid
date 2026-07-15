from standardgrid import Grid


def test_constructor():

    grid = Grid(
        standard="csquares",
        resolution=0.01,
    )

    assert grid.standard.code == "csquares"
    assert grid.resolution == 0.01
    assert grid.points is None
    assert grid.bbox is None


def test_generate():

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

    assert grid.bbox == (
        10.231,
        35.004,
        10.298,
        35.091,
    )

    assert grid.points is not None

    assert list(grid.points.columns) == [
        "x",
        "y",
    ]

    assert len(grid.points) == 70

    print(grid.points.head())
    print()
    print("First x:", repr(grid.points.iloc[0]["x"]))
    print("First y:", repr(grid.points.iloc[0]["y"]))
    print("Last x:", repr(grid.points.iloc[-1]["x"]))
    print("Last y:", repr(grid.points.iloc[-1]["y"]))

    assert grid.points.iloc[0]["x"] == 10.235
    assert grid.points.iloc[0]["y"] == 35.005

    assert grid.points.iloc[-1]["x"] == 10.295
    assert grid.points.iloc[-1]["y"] == 35.095


def test_invalid_resolution():

    try:

        Grid(
            standard="csquares",
            resolution=0.013,
        )

        raise AssertionError(
            "Expected ValueError was not raised."
        )

    except ValueError as e:

        assert "not supported" in str(e)


if __name__ == "__main__":

    test_constructor()
    test_generate()
    test_invalid_resolution()

    print("All tests passed.")