class MyCircularDeque:
    def __init__(self, k: int):
        # Allocate fixed-size array of length k
        self.capacity = k
        self.arr = [0] * k
        # 'front' points to the first element; 'rear' points to the next insertion slot at the back
        self.front = 0
        self.rear = 0
        # number of elements currently in deque
        self.size = 0

    def insertFront(self, value: int) -> bool:
        # Cannot insert if already full
        if self.size == self.capacity:
            return False
        # Move front one step backward (circularly) and place value there
        self.front = (self.front - 1 + self.capacity) % self.capacity
        self.arr[self.front] = value
        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.size == self.capacity:
            return False
        # Place value at current rear, then advance rear
        self.arr[self.rear] = value
        self.rear = (self.rear + 1) % self.capacity
        self.size += 1
        return True

    def deleteFront(self) -> bool:
        if self.size == 0:
            return False
        # Simply move front forward; the old slot becomes irrelevant
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return True

    def deleteLast(self) -> bool:
        if self.size == 0:
            return False
        # Move rear backward; the previous rear slot is now unused
        self.rear = (self.rear - 1 + self.capacity) % self.capacity
        self.size -= 1
        return True

    def getFront(self) -> int:
        if self.size == 0:
            return -1
        return self.arr[self.front]

    def getRear(self) -> int:
        if self.size == 0:
            return -1
        # Rear points to next empty slot, so last element is at (rear - 1) mod capacity
        return self.arr[(self.rear - 1 + self.capacity) % self.capacity]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity