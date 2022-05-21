from __future__ import annotations
from typing import Optional
from ctci.utils.linked_lists import Node


def partition(head: Node, x: int) -> Node:
    """Partitions a singly linked list such that all elements that are less than x come
    before the elements that are greater than or equal to x.

    Args:
        head (Node): head of the linked list
        x (int): number to partition on

    Returns:
        Node: returns the head of the new linked list
    """

    if head.next is None:
        return head

    p1: Optional[Node] = head

    # Loop through all the points
    while p1 is not None:

        # p1 is < x, no need to switch
        if p1.value < x:
            p1 = p1.next
            continue

        p2: Optional[Node] = p1

        # Loop through all the points from p1 and beyond if p1 is >= x
        while p2 is not None:

            # p2 is >= than x and after p1, then no need to switch
            if p2.value >= x:
                p2 = p2.next
                continue

            # Switch values
            p1.value, p2.value = p2.value, p1.value
            break

        # Move onto next element
        p1 = p1.next

    return head


def partition_faster(node: Node, x: int) -> Node:
    """Partitions a singly linked list such that all elements that are less than x come
    before the elements that are greater than or equal to x.

    Args:
        node (Node): head of the linked list
        x (int): number to partition on

    Returns:
        Node: returns the head of the new linked list
    """

    # Grow list from the head and the tail
    head = node
    tail = node

    # Loop through nodes
    while node is not None:

        # Temp var for next node
        next_node = node.next

        # If the node is less than x, attach it to the current head
        if node.value < x:
            node.next = head
            head = node

        # Node is greater than or equal to x, attach it to the tail
        else:
            tail.next = node
            node.next = None
            tail = node

        node = next_node

    return head
