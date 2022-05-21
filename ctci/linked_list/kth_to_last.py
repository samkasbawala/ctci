from __future__ import annotations
from typing import Any
from ctci.utils.linked_lists import Node


def kth_to_last(head: Node, k: int) -> Any:
    """Returns the kth to last element in a singly linked list. If there are less than k
    elements in the list, then the value at the head is returned.

    Args:
        head (Node): the head of the linked list
        k (int): an integer that must be greater than 0

    Raises:
        ValueError: k must be an integer greater than 0

    Returns:
        Any: returns the value at the kth to last node
    """

    if k < 1:
        raise ValueError("k must be an integer greater than 0")

    trailer = head
    leader = head

    skips = k - 1

    # Offset the lead pointer by from the head
    while leader.next is not None and skips > 0:
        leader = leader.next
        skips -= 1

    # If we cannot offset by k, then return None
    if skips > 0:
        return head.value

    # Loop until trailer hits the last node
    while leader.next is not None and trailer.next is not None:
        leader, trailer = leader.next, trailer.next

    return trailer.value
