from ctci.strings_and_arrays import is_unique, is_unique_no_additional_data_structure
import pytest


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("", True),
        ("s", True),
        ("sam", True),
        ("sammy", False),
        ("abcdefghijklmnopqrstuvwxyz", True),
        ("aa", False),
        ("111", False),
        ("1234567890", True),
    ],
)
def test_is_unique(test_input, expected):
    assert is_unique(test_input) == expected
    assert is_unique_no_additional_data_structure(test_input) == expected
