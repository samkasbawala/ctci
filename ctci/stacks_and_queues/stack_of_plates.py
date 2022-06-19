from typing import List, Optional, Any


class Stack:
    def __init__(self) -> None:
        self._stack: List[Any] = []

    def push(self, value: Any) -> None:
        self._stack.append(value)

    def pop(self) -> Optional[Any]:
        return self._stack.pop() if self._stack else None

    def peek(self) -> Optional[Any]:
        return self._stack[-1] if self._stack else None

    def is_empty(self) -> bool:
        return True if not self._stack else False


class SetOfStacks:
    def __init__(self, capacity: int) -> None:
        self._stacks: List[Stack] = []
        self._capacity = capacity

    def push(self, value: Any) -> None:

        # If there is already a stack and the current stack is under capacity
        if self._stacks and len(self._stacks[-1]._stack) < self._capacity:
            self._stacks[-1].push(value)

        # A new stack needs to be added
        else:
            self._stacks.append(Stack())
            self._stacks[-1].push(value)

    def pop(self) -> Optional[Any]:
        ret_val = self._stacks[-1].pop() if self._stacks else None

        if self._stacks and len(self._stacks[-1]._stack) <= 0:
            self._stacks.pop()

        return ret_val

    def peek(self) -> Optional[Any]:
        return self._stacks[-1].peek() if self._stacks else None

    def is_empty(self) -> bool:
        return True if not self._stacks else False

    def pop_at(self, index: int) -> Any:
        ret_value = self._stacks[index].pop()

        if self._stacks[index].is_empty():
            self._stacks.pop(index)

        return ret_value
