from ctci.utils.linked_lists import Node
from ctci.linked_list import remove_dups
from ctci.linked_list import remove_dups_no_buffer


def test_remove_dups():
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

    assert str(remove_dups(a)) == "a => b => c => d"

    a.next = None
    assert str(remove_dups(a)) == "a"

    a.next = a_2
    a_2.next = None

    assert str(remove_dups(a)) == "a"

    a.next = b
    b.next = c
    c.next = d
    d.next = None

    assert str(remove_dups(a)) == "a => b => c => d"
    assert str(remove_dups(b)) == "b => c => d"
    assert str(remove_dups(c)) == "c => d"
    assert str(remove_dups(d)) == "d"


def test_remove_dups_no_buffer():
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

    assert str(remove_dups_no_buffer(a)) == "a => b => c => d"

    a.next = None
    assert str(remove_dups_no_buffer(a)) == "a"

    a.next = a_2
    a_2.next = None

    assert str(remove_dups_no_buffer(a)) == "a"

    a.next = b
    b.next = c
    c.next = d
    d.next = None

    assert str(remove_dups_no_buffer(a)) == "a => b => c => d"
    assert str(remove_dups_no_buffer(b)) == "b => c => d"
    assert str(remove_dups_no_buffer(c)) == "c => d"
    assert str(remove_dups_no_buffer(d)) == "d"
