import pytest
from ctci.utils.linked_lists import Node
from ctci.linked_list import kth_to_last


def test_kth_to_last():
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")
    a_2 = Node("a")
    b_2 = Node("b")

    a.next = b
    b.next = c
    c.next = d
    d.next = a_2
    a_2.next = b_2

    assert kth_to_last(a, 1) == "b"
    assert kth_to_last(a, 2) == "a"
    assert kth_to_last(a, 3) == "d"
    assert kth_to_last(a, 4) == "c"
    assert kth_to_last(a, 5) == "b"
    assert kth_to_last(a, 6) == "a"
    assert kth_to_last(a, 7) == "a"
    assert kth_to_last(a, 8) == "a"

    with pytest.raises(ValueError) as _:
        kth_to_last("a", 0)
        kth_to_last("a", -1)

    assert kth_to_last(b_2, 8) == "b"
    assert kth_to_last(b_2, 1) == "b"
