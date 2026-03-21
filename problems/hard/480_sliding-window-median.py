from typing import List
import heapq
from collections import defaultdict

class DualHeap:
    def __init__(self, k: int):
        # max-heap for the smaller half; store negatives to simulate max-heap
        self.small = []
        # min-heap for the larger half
        self.large = []
        # values scheduled for lazy deletion once they reach heap top
        self.delayed = defaultdict(int)
        # logical sizes exclude delayed elements still buried in heaps
        self.small_size = 0
        self.large_size = 0
        self.k = k

    def prune(self, heap) -> None:
        # Remove top elements that already slid out of the window
        while heap:
            num = -heap[0] if heap is self.small else heap[0]
            if self.delayed[num] == 0:
                break
            self.delayed[num] -= 1
            if self.delayed[num] == 0:
                del self.delayed[num]
            heapq.heappop(heap)

    def make_balance(self) -> None:
        # Keep sizes valid:
        # - small may have exactly one more element than large
        # - otherwise both heaps have equal logical size
        if self.small_size > self.large_size + 1:
            num = -heapq.heappop(self.small)
            heapq.heappush(self.large, num)
            self.small_size -= 1
            self.large_size += 1
            # Top may now be a delayed element after moving one out
            self.prune(self.small)
        elif self.small_size < self.large_size:
            num = heapq.heappop(self.large)
            heapq.heappush(self.small, -num)
            self.large_size -= 1
            self.small_size += 1
            # Same idea for the large heap
            self.prune(self.large)

    def insert(self, num: int) -> None:
        # Put new number into the correct half based on current max of small
        if not self.small or num <= -self.small[0]:
            heapq.heappush(self.small, -num)
            self.small_size += 1
        else:
            heapq.heappush(self.large, num)
            self.large_size += 1
        self.make_balance()

    def erase(self, num: int) -> None:
        # Mark number for deletion; actual removal happens only at heap top
        self.delayed[num] += 1

        # Decide which heap logically owns this number
        if num <= -self.small[0]:
            self.small_size -= 1
            # If it is already at the top, prune immediately
            if num == -self.small[0]:
                self.prune(self.small)
        else:
            self.large_size -= 1
            if self.large and num == self.large[0]:
                self.prune(self.large)

        self.make_balance()

    def get_median(self) -> float:
        # Odd window: top of small is the median
        if self.k % 2 == 1:
            return float(-self.small[0])
        # Even window: average of both middle values
        return (-self.small[0] + self.large[0]) / 2.0


class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        # Dual heaps support O(log k) insert/remove with lazy deletion
        dh = DualHeap(k)

        # Build the first window
        for i in range(k):
            dh.insert(nums[i])

        ans = [dh.get_median()]

        # Slide the window one step at a time
        for i in range(k, len(nums)):
            dh.insert(nums[i])          # new element enters
            dh.erase(nums[i - k])       # old element leaves
            ans.append(dh.get_median())

        return ans