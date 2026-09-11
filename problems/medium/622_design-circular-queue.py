from __future__ import annotations

class MyCircularQueue:
    """Circular queue (ring buffer) with fixed capacity using an array."""

    def __init__(self, k: int):
        # Allocate array of given size; indices wrap using modulo k
        self.capacity = k
        self.queue = [0] * k
        # front points to the first element; rear points to the last element
        self.front = 0
        self.rear = -1   # start with no element, rear will be updated on first enqueue
        self.size = 0    # number of elements currently in the queue

    def enQueue(self, value: int) -> bool:
        """Add an element to the rear. Return True if successful, False if full."""
        if self.isFull():
            return False
        # Move rear forward circularly and insert
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = value
        self.size += 1
        return True

    def deQueue(self) -> bool:
        """Remove an element from the front. Return True if successful, False if empty."""
        if self.isEmpty():
            return False
        # Move front forward circularly (the element is logically removed)
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return True

    def Front(self) -> int:
        """Get the front element. Return -1 if the queue is empty."""
        if self.isEmpty():
            return -1
        return self.queue[self.front]

    def Rear(self) -> int:
        """Get the last element. Return -1 if the queue is empty."""
        if self.isEmpty():
            return -1
        return self.queue[self.rear]

    def isEmpty(self) -> bool:
        """Check whether the queue is empty."""
        return self.size == 0

    def isFull(self) -> bool:
        """Check whether the queue is full."""
        return self.size == self.capacity