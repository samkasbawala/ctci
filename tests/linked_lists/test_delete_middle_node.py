from ctci.utils.linked_lists import Node
from ctci.linked_list import delete_middle_node


def test_delete_middle_node():
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

    delete_middle_node(c)
    assert str(a) == "a => b => d => a => b"

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

    delete_middle_node(a_2)
    assert str(a) == "a => b => c => d => b"
