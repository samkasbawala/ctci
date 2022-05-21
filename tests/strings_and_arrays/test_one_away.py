from ctci.strings_and_arrays import one_away
import pytest


@pytest.mark.parametrize(
    "test_input_string_1,test_input_string_2,expected",
    [
        ("", "", True),
        ("  ", "  ", True),
        ("abc", "cab", False),
        ("abcd", "abc", True),
        ("a", "b", True),
        ("pale", "ple", True),
        ("pales", "pale", True),
        ("pale", "bale", True),
        ("pale", "bake", False),
    ],
)
def test_one_away(test_input_string_1, test_input_string_2, expected):
    assert one_away(test_input_string_1, test_input_string_2) == expected
