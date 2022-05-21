from ctci.strings_and_arrays import string_compression
import pytest


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("", ""),
        ("s", "s"),
        ("sam", "sam"),
        ("sammy", "sammy"),
        ("abcdefghijklmnopqrstuvwxyz", "abcdefghijklmnopqrstuvwxyz"),
        ("aA", "aA"),
        ("aabcccccaaa", "a2b1c5a3"),
        ("aaaaaaaaaa", "a10"),
    ],
)
def test_string_compression(test_input, expected):
    assert string_compression(test_input) == expected
