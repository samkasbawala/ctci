import pytest
from ctci.utils.linked_lists import Node
from ctci.linked_list import sum_lists
from ctci.linked_list import reverse_ll
from ctci.linked_list import sum_lists_forward


@pytest.mark.parametrize(
    "test_input_num_1,test_input_num_2,expected",
    (
        (
            Node(7, Node(1, Node(6))),
            Node(5, Node(9, Node(2))),
            "2 => 1 => 9",
        ),
        (
            Node(0),
            Node(0),
            "0",
        ),
        (
            Node(9, Node(9, Node(9, Node(9)))),
            Node(9, Node(9)),
            "8 => 9 => 0 => 0 => 1",
        ),
        (
            Node(9),
            Node(7),
            "6 => 1",
        ),
    ),
)
def test_sum_lists(test_input_num_1, test_input_num_2, expected):
    assert str(sum_lists(test_input_num_1, test_input_num_2)) == expected


@pytest.mark.parametrize(
    "test_input,expected",
    (
        (
            Node(1, (Node(2, Node(3)))),
            "3 => 2 => 1",
        ),
        (
            Node(1),
            "1",
        ),
        (
            Node(3, Node(2)),
            "2 => 3",
        ),
    ),
)
def test_reverse_ll(test_input, expected):
    assert str(reverse_ll(test_input)) == expected


@pytest.mark.parametrize(
    "test_input_num_1,test_input_num_2,expected",
    (
        (
            Node(6, Node(1, Node(7))),
            Node(2, Node(9, Node(5))),
            "9 => 1 => 2",
        ),
        (
            Node(0),
            Node(0),
            "0",
        ),
        (
            Node(9, Node(9, Node(9, Node(9)))),
            Node(9, Node(9)),
            "1 => 0 => 0 => 9 => 8",
        ),
        (
            Node(9),
            Node(7),
            "1 => 6",
        ),
        (
            Node(1, Node(0, Node(0))),
            Node(5, Node(3)),
            "1 => 5 => 3",
        ),
    ),
)
def test_sum_lists_forward(test_input_num_1, test_input_num_2, expected):
    assert str(sum_lists_forward(test_input_num_1, test_input_num_2)) == expected
