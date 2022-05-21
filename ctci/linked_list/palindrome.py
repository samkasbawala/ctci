from typing import Optional
from ctci.utils.linked_lists import Node


def palindrome(head: Optional[Node]) -> bool:
    """Determines whether or not the passed in linked list, given the head, is a
    palindrome

    Args:
        head (Optional[Node]): head of the linked list

    Returns:
        bool: boolean indicating whether or not the linked list is a palindrome
    """

    # Base case
    if head is None or head.next is None:
        return True

    # Iterate until node is at the end of the list
    node = head
    prev = None

    while node.next is not None:
        prev = node
        node = node.next

    # node is now at the end of the list
    if head.value == node.value:

        # Remove the last element and have the second to last element be the new tail
        prev.next = None
        return palindrome(head.next)

    # If the first element and the last element do not match
    else:
        return False
