from ctci.strings_and_arrays import palindrome_permutation
import pytest


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("", True),
        ("   ", True),
        ("s", True),
        ("sam", False),
        ("sammy", False),
        ("abcdefghijklmnopqrstuvwxyz", False),
        ("aA", True),
        ("111", True),
        ("1234567890", False),
        ("Tact Coa", True),
        ("KA kaY ", True),
    ],
)
def test_palindrome_permutation(test_input, expected):
    assert palindrome_permutation(test_input) == expected
