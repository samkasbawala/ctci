from ctci.utils.linked_lists import Node
from ctci.linked_list import detect_loop


def test_intersect_with_intersection():
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")
    e = Node("e")

    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = c

    assert detect_loop(a) is c


def test_intersect_with_no_intersection():
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")
    e = Node("e")

    a.next = b
    b.next = c
    c.next = d
    d.next = e

    assert detect_loop(a) is None
