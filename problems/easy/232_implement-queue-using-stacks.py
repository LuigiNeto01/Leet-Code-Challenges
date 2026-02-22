class MyQueue:
    def __init__(self):
        # Two stacks approach:
        # in_stack stores elements pushed recently (back of queue),
        # out_stack stores elements ready to be popped/peeked (front of queue).
        self.in_stack = []
        self.out_stack = []

    def push(self, x: int) -> None:
        # Push new element onto in_stack.
        self.in_stack.append(x)

    def _transfer(self) -> None:
        # Move all elements from in_stack to out_stack to maintain queue order.
        # This reverses the order so the oldest element ends up on top of out_stack.
        while self.in_stack:
            self.out_stack.append(self.in_stack.pop())

    def pop(self) -> int:
        # If out_stack is empty, transfer from in_stack to expose the front element.
        if not self.out_stack:
            self._transfer()
        # The front of the queue is on top of out_stack.
        return self.out_stack.pop()

    def peek(self) -> int:
        # Ensure there is an element to peek by transferring if needed.
        if not self.out_stack:
            self._transfer()
        # The front element is the last element added to out_stack (top).
        return self.out_stack[-1]

    def empty(self) -> bool:
        # Queue is empty only when both stacks have no elements.
        return not self.in_stack and not self.out_stack