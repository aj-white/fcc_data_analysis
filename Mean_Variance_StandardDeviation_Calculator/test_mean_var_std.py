import numpy as np
import pytest

import mean_var_std


@pytest.fixture()
def flat_list():
    return [0, 1, 2, 3, 4, 5, 6, 7, 8]


@pytest.fixture()
def short_list():
    return [1, 2, 3]


@pytest.fixture()
def array_3_by_3():
    return np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])


def test_create_array_3_by_3(flat_list, array_3_by_3):
    np.testing.assert_array_equal(
        mean_var_std.create_array_3_by_3(flat_list), array_3_by_3
    )


def test_create_array_short_list(short_list):
    with pytest.raises(ValueError) as err:
        assert mean_var_std.create_array_3_by_3(short_list)
    assert str(err.value) == "List must contain nine numbers."


def test_calc_mean_by_axis(array_3_by_3):
    assert mean_var_std.calc_mean_by_axis(array_3_by_3) == [
        [3.0, 4.0, 5.0],
        [1.0, 4.0, 7.0],
        4.0,
    ]


def test_calc_var_by_axis(array_3_by_3):
    assert mean_var_std.calc_var_by_axis(array_3_by_3) == [
        [6.0, 6.0, 6.0],
        [0.6666666666666666, 0.6666666666666666, 0.6666666666666666],
        6.666666666666667,
    ]


def test_calc_std_by_axis(array_3_by_3):
    assert mean_var_std.calc_std_by_axis(array_3_by_3) == [
        [2.449489742783178, 2.449489742783178, 2.449489742783178],
        [0.816496580927726, 0.816496580927726, 0.816496580927726],
        2.581988897471611,
    ]


def test_calc_max_by_axis(array_3_by_3):
    assert mean_var_std.calc_max_by_axis(array_3_by_3) == [[6, 7, 8], [2, 5, 8], 8]


def test_calc_min_by_axis(array_3_by_3):
    assert mean_var_std.calc_min_by_axis(array_3_by_3) == [[0, 1, 2], [0, 3, 6], 0]


def test_calc_sum_by_axis(array_3_by_3):
    assert mean_var_std.calc_sum_by_axis(array_3_by_3) == [[9, 12, 15], [3, 12, 21], 36]


def test_calculate(flat_list):
    assert mean_var_std.calculate(flat_list) == {
        "mean": [[3.0, 4.0, 5.0], [1.0, 4.0, 7.0], 4.0],
        "variance": [
            [6.0, 6.0, 6.0],
            [0.6666666666666666, 0.6666666666666666, 0.6666666666666666],
            6.666666666666667,
        ],
        "standard deviation": [
            [2.449489742783178, 2.449489742783178, 2.449489742783178],
            [0.816496580927726, 0.816496580927726, 0.816496580927726],
            2.581988897471611,
        ],
        "max": [[6, 7, 8], [2, 5, 8], 8],
        "min": [[0, 1, 2], [0, 3, 6], 0],
        "sum": [[9, 12, 15], [3, 12, 21], 36],
    }
