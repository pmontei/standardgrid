import numpy.testing as npt

from standardgrid.generator import GridGenerator
from standardgrid import get_standard


def test_constructor():
    g = GridGenerator(
        get_standard("csquares"),
        0.01,
    )

    assert g.standard.code == "csquares"
    assert g.resolution == 0.01


def test_snap_down():
    g = GridGenerator(
        get_standard("csquares"),
        0.01,
    )

    npt.assert_allclose(
        g._snap_down(10.236, 0),
        10.23,
    )

    npt.assert_allclose(
        g._snap_down(-10.236, 0),
        -10.24,
    )


def test_snap_up():
    g = GridGenerator(
        get_standard("csquares"),
        0.01,
    )

    npt.assert_allclose(
        g._snap_up(10.231, 0),
        10.24,
    )

    npt.assert_allclose(
        g._snap_up(-10.236, 0),
        -10.23,
    )


def test_snap_bbox():
    g = GridGenerator(
        get_standard("csquares"),
        0.01,
    )

    bbox = g._snap_bbox(
        (
            10.231,
            35.004,
            10.298,
            35.091,
        )
    )

    expected = (
        10.23,
        35.00,
        10.30,
        35.10,
    )

    npt.assert_allclose(
        bbox,
        expected,
    )


def test_generate_axis():
    g = GridGenerator(
        get_standard("csquares"),
        0.01,
    )

    xs = g._generate_axis(
        10.231,
        10.298,
        0,
    )

    assert len(xs) == 7

    npt.assert_allclose(
        xs[0],
        10.235,
    )

    npt.assert_allclose(
        xs[-1],
        10.295,
    )


def test_generate():
    g = GridGenerator(
        get_standard("csquares"),
        0.01,
    )

    df = g.generate(
        (
            10.231,
            35.004,
            10.298,
            35.091,
        )
    )

    assert list(df.columns) == ["x", "y"]

    assert len(df) == 70

    npt.assert_allclose(
        df.iloc[0]["x"],
        10.235,
    )

    npt.assert_allclose(
        df.iloc[0]["y"],
        35.005,
    )

    npt.assert_allclose(
        df.iloc[-1]["x"],
        10.295,
    )

    npt.assert_allclose(
        df.iloc[-1]["y"],
        35.095,
    )


if __name__ == "__main__":

    test_constructor()
    test_snap_down()
    test_snap_up()
    test_snap_bbox()
    test_generate_axis()
    test_generate()

    print("All tests passed.")