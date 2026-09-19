class MyLinkedList:
    # Node definition for singly linked list
    class _Node:
        __slots__ = ('val', 'next')
        def __init__(self, val=0, next_node=None):
            self.val = val
            self.next = next_node

    def __init__(self):
        # Dummy head simplifies insertions/deletions at index 0
        self._dummy = self._Node()
        self._size = 0

    def get(self, index: int) -> int:
        # Return value at given index, -1 if invalid
        if index < 0 or index >= self._size:
            return -1
        cur = self._dummy.next
        for _ in range(index):
            cur = cur.next
        return cur.val

    def addAtHead(self, val: int) -> None:
        # Insert at front: new node after dummy
        new_node = self._Node(val, self._dummy.next)
        self._dummy.next = new_node
        self._size += 1

    def addAtTail(self, val: int) -> None:
        # Traverse to last node and append
        cur = self._dummy
        while cur.next:
            cur = cur.next
        cur.next = self._Node(val)
        self._size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        # Insert before the node at index; do nothing if index > size
        if index < 0 or index > self._size:
            return
        # Find predecessor of insertion point (node at index-1)
        prev = self._dummy
        for _ in range(index):
            prev = prev.next
        new_node = self._Node(val, prev.next)
        prev.next = new_node
        self._size += 1

    def deleteAtIndex(self, index: int) -> None:
        # Remove node at index if valid
        if index < 0 or index >= self._size:
            return
        prev = self._dummy
        for _ in range(index):
            prev = prev.next
        # Skip the node to be deleted
        prev.next = prev.next.next
        self._size -= 1