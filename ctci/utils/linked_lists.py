from __future__ import annotations
from typing import Any, Optional


class Node:
    """Node class for a singly linked list"""

    def __init__(self, value: Any, next: Optional[Node] = None) -> None:
        self.value = value
        self.next = next

    def append_to_tail(self, value: Any) -> None:
        """Appends a new node to the last element in the linked list"""

        # New node that will be added to the end of the list
        new_node = Node(value)

        # Loop to get to the end of the list
        cur_node = self
        while cur_node.next is not None:
            cur_node = cur_node.next

        # Assign the new node to the very end
        cur_node.next = new_node

    def __str__(self) -> str:
        """String representation of a Node and it's next values

        Returns:
            str: string
        """

        # All items in the linked list starting with the current node.
        items = []

        cur_node: Optional[Node] = self
        while cur_node is not None:
            items.append(str(cur_node.value))
            cur_node = cur_node.next

        return " => ".join(items)


def delete_node(head: Node, value: Any) -> Optional[Node]:
    """Deletes a node in a linked list given the head of the list and value that needs
    to be deleted

    Args:
        head (Node): head of the linked list
        value (Any): the value the node contains

    Returns:
        Node: returns the head of the list with the specified value deleted from the
        linked list
    """

    # If head is None
    if head is None:
        return None

    # If head is the value
    if head.value == value:
        return head.next

    # Loop through the elements and delete the one that matches the value
    cur_node = head
    while cur_node.next is not None:

        # If we find the value that we are looking for
        if cur_node.next.value == value:
            cur_node.next = cur_node.next.next
            return head

        # Move on to next element
        cur_node = cur_node.next

    # Item is not in the linked list
    return head
