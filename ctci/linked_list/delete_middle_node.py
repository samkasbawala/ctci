from __future__ import annotations
from ctci.utils.linked_lists import Node


def delete_middle_node(node: Node) -> None:
    """Deletes the node specified in a singly linked list. Cannot be the head or tail
    node.

    Args:
        node (Node): Node to be deleted from the linked list
    """

    if node.next is None:
        return None

    node.value = node.next.value
    node.next = node.next.next
