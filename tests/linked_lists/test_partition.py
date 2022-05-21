from ctci.utils.linked_lists import Node
from ctci.linked_list import partition
from ctci.linked_list import partition_faster


def test_partition():
    a = Node(3)
    b = Node(5)
    c = Node(8)
    d = Node(5)
    e = Node(10)
    f = Node(2)
    g = Node(1)

    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f
    f.next = g

    partition(a, 5)
    assert str(a) == "3 => 2 => 1 => 5 => 10 => 5 => 8"


def test_partition_2():
    a = Node(3)
    b = Node(5)
    c = Node(8)
    d = Node(5)
    e = Node(10)
    f = Node(2)
    g = Node(1)

    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f
    f.next = g

    partition(a, 10)
    assert str(a) == "3 => 5 => 8 => 5 => 2 => 1 => 10"


def test_partition_3():
    a = Node(3)
    b = Node(5)
    c = Node(8)
    d = Node(5)
    e = Node(10)
    f = Node(2)
    g = Node(1)

    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f
    f.next = g

    partition(a, 0)
    assert str(a) == "3 => 5 => 8 => 5 => 10 => 2 => 1"


def test_partition_faster():
    a = Node(3)
    b = Node(5)
    c = Node(8)
    d = Node(5)
    e = Node(10)
    f = Node(2)
    g = Node(1)

    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f
    f.next = g

    ll = partition_faster(a, 5)
    assert str(ll) == "1 => 2 => 3 => 5 => 8 => 5 => 10"


def test_partition_faster_2():
    a = Node(3)
    b = Node(5)
    c = Node(8)
    d = Node(5)
    e = Node(10)
    f = Node(2)
    g = Node(1)

    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f
    f.next = g

    ll = partition_faster(a, 10)
    assert str(ll) == "1 => 2 => 5 => 8 => 5 => 3 => 10"


def test_partition_faster_3():
    a = Node(3)
    b = Node(5)
    c = Node(8)
    d = Node(5)
    e = Node(10)
    f = Node(2)
    g = Node(1)

    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f
    f.next = g

    ll = partition_faster(a, 0)
    assert str(ll) == "3 => 5 => 8 => 5 => 10 => 2 => 1"
