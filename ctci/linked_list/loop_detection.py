from __future__ import annotations
from typing import Optional, Set
from ctci.utils.linked_lists import Node


def detect_loop(head: Node) -> Optional[Node]:
    """Returns the node at the beginning of a loop in a linked list if such a loop
    exists

    Args:
        head (Node): head of the linked list

    Returns:
        Optional[Node]: start of the loop in the linked list
    """
    # Keep track of the nodes that we have seen
    seen: Set[Node] = set()

    node = head
    while node is not None:
        if node in seen:
            return node
        seen.add(node)
        node = node.next

    # There is no loop in the linked list
    return None
