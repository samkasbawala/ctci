from __future__ import annotations
from typing import Optional
from ctci.utils.linked_lists import Node


def remove_dups(head: Node) -> Optional[Node]:
    """Removes any duplicates from a linked list

    Args:
        head (Node): the beginning of a linked list

    Returns:
        Optional[Node]: returns the head of the linked list with duplicates removed
    """

    # Set to see which values we have seen
    seen = set()

    # If the head is none, return none
    if head is None:
        return None

    # Loop through the elements and delete the node if we come across a value that has
    # already been seen
    cur_node: Optional[Node] = head
    prev: Optional[Node] = None
    while cur_node is not None:

        if cur_node.value in seen and prev is not None:
            prev.next = cur_node.next

        else:
            seen.add(cur_node.value)
            prev = cur_node

        cur_node = cur_node.next

    return head


def remove_dups_no_buffer(head: Node) -> Optional[Node]:
    """Removes any duplicates from a linked list

    Args:
        head (Node): the beginning of a linked list

    Returns:
        Optional[Node]: returns the head of the linked list with duplicates removed
    """

    # If the head is none, return none
    if head is None:
        return None

    # Implement two pointer approach
    first_pointer: Optional[Node] = head
    while first_pointer is not None:

        # Second pointer to start right after current pointer
        second_pointer: Optional[Node] = first_pointer.next
        prev: Optional[Node] = first_pointer

        # Go through the items after the first pointer and compare them with the second
        # pointer
        while second_pointer is not None and prev is not None:
            if first_pointer.value == second_pointer.value:
                prev.next = second_pointer.next
            else:
                prev = second_pointer

            second_pointer = second_pointer.next

        first_pointer = first_pointer.next

    return head
