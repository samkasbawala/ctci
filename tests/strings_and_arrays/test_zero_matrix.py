from ctci.strings_and_arrays import zero_matrix
import pytest


@pytest.mark.parametrize(
    "test_input,expected",
    [
        (
            [
                [0, 1, 1],
                [1, 1, 1],
                [1, 1, 1],
            ],
            [
                [0, 0, 0],
                [0, 1, 1],
                [0, 1, 1],
            ],
        ),
        (
            [
                [0, 1, 1, 1],
                [1, 1, 1, 0],
                [1, 1, 1, 1],
            ],
            [
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 1, 1, 0],
            ],
        ),
        (
            [],
            [],
        ),
        (
            [
                [0, 1],
                [1, 1],
                [0, 1],
            ],
            [
                [0, 0],
                [0, 1],
                [0, 0],
            ],
        ),
        (
            [
                [1, 1],
                [1, 1],
                [1, 1],
            ],
            [
                [1, 1],
                [1, 1],
                [1, 1],
            ],
        ),
    ],
)
def test_zero_matrix(test_input, expected):
    assert zero_matrix(test_input) == expected
