from __future__ import annotations
from typing import Any, Optional


class QueueNode:
    def __init__(
        self, data: Any, next: Optional[QueueNode], prev: Optional[QueueNode]
    ) -> None:
        self.data = data
        self.next = next
        self.prev = prev

    def __str__(self) -> str:
        return str(self.data)


class Queue:
    def __init__(self) -> None:
        self.head: Optional[QueueNode] = None
        self.tail: Optional[QueueNode] = None

    def add(self, value: Any) -> None:
        """Adds a new node with the passed in value to the end of the queue

        Args:
            value (Any): the value that the newly added node to the queue should hold
        """
        # Create a new node, the prev value will be the current tail
        node = QueueNode(value, prev=self.tail)

        # If there is nothing in the queue, the head and the tail will be this new node
        if self.is_empty():
            self.head = node
            self.tail = self.head

        # Otherwise, set the newly created node to be the tail
        else:
            self.tail.next = node
            self.tail = self.tail.next

    def remove(self) -> Optional[QueueNode]:
        """Returns the first item in the queue if the queue is not empty

        Returns:
            Optional[QueueNode]: first item in the queue
        """
        if not self.is_empty():

            # Get the current head, the new head will be the next node in the queue
            node = self.head
            self.head = self.head.next

            # Clear the new head's prev node
            self.head.prev = None

            # Clear the return node's next value
            node.next = None

            return node

    def peek(self) -> Optional[Any]:
        """Returns the value of the first item in the queue if the queue is not empty

        Returns:
            Optional[Any]: the value that is held by the first item in the queue
        """
        if not self.is_empty():
            return self.tail.data

    def is_empty(self) -> bool:
        """Returns a bool indicating whether or not the queue is empty

        Returns:
            bool: states whether the stack is empty or not
        """
        return True if (self.head is None and self.tail is None) else False
