from ctci.utils.linked_lists import Node


def sum_lists(ll_1: Node, ll_2: Node) -> Node:
    """Given two integers represented as linked lists, add them together and return the
    head of the resulting linked list. The digits in ll_1 and ll_2 are stored in reverse
    order, meaning that the 1's digit is at the head of the list.

    Args:
        ll_1 (Node): head of the first number represented by a linked list
        ll_2 (Node): head of the second number represented by a linked list

    Returns:
        Node: the head of the sum represented by a linked list
    """

    # This first node will be a dummy node
    head_sum = Node(0)

    curr_sum_node = head_sum
    pointer_1 = ll_1
    pointer_2 = ll_2
    carry = 0

    # Loop through both linked lists until at least one of them is empty
    while pointer_1 is not None and pointer_2 is not None:
        sum = carry + pointer_1.value + pointer_2.value
        carry = 0 if sum <= 9 else 1

        curr_sum_node.next = Node(sum % 10)
        curr_sum_node = curr_sum_node.next

        pointer_1 = pointer_1.next
        pointer_2 = pointer_2.next

    # Loop over the remaining elements in ll_1
    while pointer_1 is not None:
        sum = carry + pointer_1.value
        carry = 0 if sum <= 9 else 1

        curr_sum_node.next = Node(sum % 10)
        curr_sum_node = curr_sum_node.next

        pointer_1 = pointer_1.next

    # Loop over the remaining elements in ll_2
    while pointer_2 is not None:
        sum = carry + pointer_2.value
        carry = 0 if sum <= 9 else 1

        curr_sum_node.next = Node(sum % 10)
        curr_sum_node = curr_sum_node.next

        pointer_2 = pointer_2.next

    # If the last sum induces a carry over value
    if carry > 0:
        curr_sum_node.next = Node(1)
        curr_sum_node = curr_sum_node.next

    return head_sum.next


def sum_lists_forward(ll_1: Node, ll_2: Node) -> Node:
    """Given two integers represented as linked lists, add them together and return the
    head of the resulting linked list. The digits in ll_1 and ll_2 are stored in the
    correct order, meaning that the greatest place is at the head of the list.

    Args:
        ll_1 (Node): head of the first number represented by a linked list
        ll_2 (Node): head of the second number represented by a linked list

    Returns:
        Node: the head of the sum represented by a linked list
    """

    # Reverse the list
    ll_1 = reverse_ll(ll_1)
    ll_2 = reverse_ll(ll_2)

    # This first node will be a dummy node
    head_sum = Node(0)

    curr_sum_node = head_sum
    pointer_1 = ll_1
    pointer_2 = ll_2
    carry = 0

    # Loop through both linked lists until at least one of them is empty
    while pointer_1 is not None and pointer_2 is not None:
        sum = carry + pointer_1.value + pointer_2.value
        carry = 0 if sum <= 9 else 1

        curr_sum_node.next = Node(sum % 10)
        curr_sum_node = curr_sum_node.next

        pointer_1 = pointer_1.next
        pointer_2 = pointer_2.next

    # Loop over the remaining elements in ll_1
    while pointer_1 is not None:
        sum = carry + pointer_1.value
        carry = 0 if sum <= 9 else 1

        curr_sum_node.next = Node(sum % 10)
        curr_sum_node = curr_sum_node.next

        pointer_1 = pointer_1.next

    # Loop over the remaining elements in ll_2
    while pointer_2 is not None:
        sum = carry + pointer_2.value
        carry = 0 if sum <= 9 else 1

        curr_sum_node.next = Node(sum % 10)
        curr_sum_node = curr_sum_node.next

        pointer_2 = pointer_2.next

    # If the last sum induces a carry over value
    if carry > 0:
        curr_sum_node.next = Node(1)
        curr_sum_node = curr_sum_node.next

    return reverse_ll(head_sum.next)


def reverse_ll(head: Node) -> Node:
    """Reverses a linked list, given the head, and returns the head of the reversed
    list

    Args:
        head (Node): head of the linked list

    Returns:
        Node: head of the reversed linked list
    """

    # Set current node and prev node
    prev = None
    node = head

    # Set the .next pointer to the previous item in the list
    while node is not None:

        # Temp reference to next object before we overwrite it
        next_node = node.next

        node.next = prev
        prev = node
        node = next_node

    # Prev will be at the head of the new list
    return prev
