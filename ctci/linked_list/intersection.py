from __future__ import annotations
from typing import Optional
from ctci.utils.linked_lists import Node


def intersect(a: Node, b: Node) -> Optional[Node]:
    """Returns the intersecting node in two linked lists if it exists

    Args:
        a (Node): head of the first linked list
        b (Node): head of the second linked list

    Returns:
        Optional[Node]: the common linked list between the two lists
    """

    # Get length of list a
    length_a = length(a)

    # Get length of list b
    length_b = length(b)

    # Move the longer of the two lists
    node = a if length_a > length_b else b
    other = a if node is b else b

    # Node to the next until the remaining lists are at the same length
    for _ in range(abs(length_a - length_b)):
        node = node.next

    # Sanity check, assure lengths are the same now
    assert length(other) == length(node)

    # Loop through the lists
    while node is not None and other is not None:

        # If the nodes share the same reference, then return true
        if node is other:
            return node

        # Move the nodes to be the next in the list
        node = node.next
        other = other.next

    # If we completed the loop then return false
    return None


def length(head: Optional[Node]) -> int:
    """Returns the length of a non circular linked list

    Args:
        head (Node): head of the linked list

    Returns:
        int: length of the linked list
    """

    node = head
    length = 0

    while node is not None:
        length += 1
        node = node.next

    return length
