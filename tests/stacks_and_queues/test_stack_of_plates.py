from ctci.stacks_and_queues import SetOfStacks
import pytest


def test_empty_set_of_stacks():
    stack = SetOfStacks(capacity=3)
    assert stack.peek() is None
    assert stack.pop() is None


def test_one_stack_push():
    stack = SetOfStacks(capacity=3)

    assert stack.is_empty() is True

    stack.push(0)

    assert stack.is_empty() is False

    stack.push(1)

    assert stack.peek() == 1
    assert len(stack._stacks) == 1
    assert len(stack._stacks[-1]._stack) == 2


def test_one_stack_pop():
    stack = SetOfStacks(capacity=3)

    stack.push(0)
    stack.push(1)

    assert stack.pop() == 1
    assert len(stack._stacks) == 1
    assert len(stack._stacks[-1]._stack) == 1
    assert stack.peek() == 0


def test_multiple_stack_push():
    stack = SetOfStacks(capacity=1)

    stack.push(0)

    assert len(stack._stacks) == 1

    stack.push(1)

    assert stack.peek() == 1
    assert len(stack._stacks) == 2
    assert len(stack._stacks[-1]._stack) == 1


def test_multiple_stack_pop():
    stack = SetOfStacks(capacity=1)

    stack.push(0)
    stack.push(1)

    assert stack.pop() == 1
    assert len(stack._stacks) == 1
    assert len(stack._stacks[-1]._stack) == 1
    assert stack.peek() == 0


def test_pop_at():
    stack = SetOfStacks(capacity=2)

    stack.push(0)
    stack.push(1)
    stack.push(2)

    assert len(stack._stacks[0]._stack) == 2
    assert stack.pop_at(0) == 1
    assert len(stack._stacks) == 2
    assert len(stack._stacks[0]._stack) == 1
    assert len(stack._stacks[1]._stack) == 1

    assert stack.pop() == 2
    assert len(stack._stacks) == 1

    stack.push(1)
    stack.push(2)

    assert stack.pop_at(0) == 1
    assert len(stack._stacks) == 2
    assert stack.peek() == 2
    assert stack.pop_at(0) == 0
    assert len(stack._stacks) == 1
    assert stack.peek() == 2

    with pytest.raises(IndexError):
        stack.pop_at(3)
