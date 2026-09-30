from __future__ import annotations

from heapq import heapify, heappush, heappop


class KthLargest:
    def __init__(self, k: int, nums: list[int]):
        self.k = k
        # Min-heap stores only the k largest scores seen so far.
        self.heap = nums[:]
        heapify(self.heap)

        # Remove extra smaller elements so heap size is at most k.
        while len(self.heap) > k:
            heappop(self.heap)

    def add(self, val: int) -> int:
        # Add new score, then remove the smallest if the heap exceeds k.
        heappush(self.heap, val)
        if len(self.heap) > self.k:
            heappop(self.heap)

        # The kth largest is the smallest element in the min-heap.
        return self.heap[0]