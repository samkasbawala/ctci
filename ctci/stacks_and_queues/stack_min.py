from typing import List, Optional, Tuple


class MinStack:
    def __init__(self) -> None:

        # Store min value of the current state as the second value in the tuple
        self._stack: List[Tuple[int, int]] = []

    def push(self, value: int) -> None:
        """Pushes the supplied value onto the stack.

        Args:
            value (int): value that should be added on to the stack
        """

        # If there is already an element on the stack, determine what the min will be
        if self._stack:
            self._stack.append((value, min(self._stack[-1][-1], value)))
        else:
            self._stack.append((value, value))

    def pop(self) -> Optional[int]:
        """Returns the value on the top of the stack. If the stack is empty, then None
        is returned

        Returns:
            Optional[int]: _description_
        """
        return self._stack.pop()[0] if self._stack else None

    def min(self) -> Optional[int]:
        """Returns the minimum value in the stack

        Returns:
            int: the minimum value that is in the stack
        """
        return self._stack[-1][-1] if self._stack else None
