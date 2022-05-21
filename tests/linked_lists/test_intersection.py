from ctci.utils.linked_lists import Node
from ctci.linked_list import intersect


def test_intersect_not_intersecting():
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")
    e = Node("e")

    a.next = b
    b.next = c
    c.next = d

    assert intersect(a, e) is None


def test_intersect_empty_lists():
    assert intersect(None, None) is None


def test_intersect_same_lists():
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")

    a.next = b
    b.next = c
    c.next = d

    assert intersect(a, a) is a


def test_intersect_with_intersect():
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")

    a.next = b
    b.next = c
    c.next = d

    assert intersect(a, b) is b
    assert intersect(a, c) is c
    assert intersect(a, d) is d
