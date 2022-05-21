from ctci.strings_and_arrays import check_permutation
from ctci.strings_and_arrays import check_permutation_freq
import pytest


@pytest.mark.parametrize(
    "test_input_string_1,test_input_string_2,expected",
    [
        ("", "", True),
        ("  ", "  ", True),
        ("abc", "cab", True),
        ("abcd", "abc", False),
        ("a", "b", False),
    ],
)
def test_check_permutations(test_input_string_1, test_input_string_2, expected):
    assert check_permutation(test_input_string_1, test_input_string_2) == expected
    assert check_permutation_freq(test_input_string_1, test_input_string_2) == expected
