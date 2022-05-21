import pytest
from ctci.utils.linked_lists import Node
from ctci.linked_list import palindrome


@pytest.mark.parametrize(
    "test_input,expected",
    (
        (
            Node("k", Node("a", Node("y", Node("a", Node("k"))))),
            True,
        ),
        (
            Node("n", Node("o", Node("o", Node("n")))),
            True,
        ),
        (
            Node("N", Node("o", Node("o", Node("n")))),
            False,
        ),
        (
            Node("m", Node("o", Node("o", Node("n")))),
            False,
        ),
        (
            Node("s", Node("a", Node("m", Node("m", Node("y"))))),
            False,
        ),
    ),
)
def test_palindrome(test_input, expected):
    assert palindrome(test_input) == expected
