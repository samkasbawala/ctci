from ctci.strings_and_arrays import string_rotation
import pytest


@pytest.mark.parametrize(
    "test_input_string_1,test_input_string_2,expected",
    [
        ("", "", True),
        ("  ", "  ", True),
        ("abc", "cab", True),
        ("abcd", "abc", False),
        ("a", "b", False),
        ("waterbottle", "erbottlewat", True),
        ("sammy", "ymmas", False),
    ],
)
def test_string_rotation(test_input_string_1, test_input_string_2, expected):
    assert string_rotation(test_input_string_1, test_input_string_2) == expected
