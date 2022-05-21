from ctci.strings_and_arrays import urlify
import pytest


@pytest.mark.parametrize(
    "test_input_string,test_input_length,expected",
    [
        (
            [
                "M",
                "r",
                " ",
                "J",
                "o",
                "h",
                "n",
                " ",
                "S",
                "m",
                "i",
                "t",
                "h",
                " ",
                " ",
                " ",
                " ",
            ],
            13,
            [
                "M",
                "r",
                "%",
                "2",
                "0",
                "J",
                "o",
                "h",
                "n",
                "%",
                "2",
                "0",
                "S",
                "m",
                "i",
                "t",
                "h",
            ],
        ),
        ([" "], 1, [" "]),
        (["S", "a", "m"], 3, ["S", "a", "m"]),
        (
            ["H", "e", "l", "l", "o", " ", "W", "o", "r", "l", "d", " ", " "],
            11,
            ["H", "e", "l", "l", "o", "%", "2", "0", "W", "o", "r", "l", "d"],
        ),
    ],
)
def test_urlify(test_input_string, test_input_length, expected):
    assert urlify(test_input_string, test_input_length) == expected
