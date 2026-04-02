class PeekingIterator:
    def __init__(self, iterator):
        self.iterator = iterator
        self._next = iterator.next() if iterator.hasNext() else None
        self._has_next = self._next is not None

    def peek(self):
        return self._next

    def next(self):
        current = self._next
        if self.iterator.hasNext():
            self._next = self.iterator.next()
            self._has_next = True
        else:
            self._next = None
            self._has_next = False
        return current

    def hasNext(self):
        return self._has_next


class Solution(PeekingIterator):
    pass