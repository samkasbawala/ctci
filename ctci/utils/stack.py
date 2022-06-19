from __future__ import annotations
from typing import Any, Optional


class StackNode:
    def __init__(
        self, data: Any, next: Optional[StackNode], prev: Optional[StackNode]
    ) -> None:
        self.data = data
        self.next: Optional[StackNode] = next
        self.prev: Optional[StackNode] = prev

    def __str__(self) -> str:
        return str(self.data)


class Stack:
    def __init__(self) -> None:
        self.head: Optional[StackNode] = None
        self.tail: Optional[StackNode] = None

    def push(self, value: Any) -> None:
        """Push an item onto the stack. Sets the tail to be a node and sets the prev and
        next references accordingly.

        Args:
            value (Any): item for the stack node to have
        """
        # Create a new node, the prev value will be the current tail
        node = StackNode(value, prev=self.tail)

        # If there is nothing on the stack, the head and the tail will be this new node
        if self.is_empty():
            self.head = node
            self.tail = self.head

        # Otherwise, set the newly created node to be the tail
        else:
            self.tail.next = node
            self.tail = self.tail.next

    def pop(self) -> Optional[StackNode]:
        """Returns the node at the top of the stack. If the stack is empty, then return
        nothing.

        Returns:
            Optional[StackNode]: the node on the top of the stack
        """

        # If the stack is not empty
        if not self.is_empty():

            # Get the tail, make the new tail the prev of current tail node
            tail = self.tail
            self.tail = self.tail.prev

            # Clear the tail's next and prev (the node we are going to return)
            tail.prev = None
            tail.next = None

            return tail

    def peek(self) -> Optional[Any]:
        """Returns the data held by the node on top of the stack. Returns None if the
        stack is empty.

        Returns:
            Optional[Any]: the data that the top StackNode is holding
        """

        # Return the value that the top node holds of the stack is not empty
        if not self.is_empty():
            return self.tail.data

    def is_empty(self) -> bool:
        """Returns a bool indicating whether or not the stack is empty

        Returns:
            bool: states whether the stack is empty or not
        """
        return True if (self.head is None and self.tail) is None else False
