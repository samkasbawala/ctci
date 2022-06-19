from ctci.stacks_and_queues import MinStack


def test_empty_min_stack_min():
    assert MinStack().min() is None


def test_empty_min_stack_pop():
    assert MinStack().pop() is None


def test_min_stack_min_and_pop():
    stack = MinStack()

    stack.push(1)
    stack.push(2)
    stack.push(0)

    assert stack.min() == 0
    assert stack.pop() == 0
    assert stack.min() == 1
    assert stack.pop() == 2
    assert stack.min() == 1
    assert stack.pop() == 1
