import heapq

class MedianFinder:

    def __init__(self):
        # max heap for the smaller half (negate values for max behavior)
        self.small = []
        # min heap for the larger half
        self.large = []

    def addNum(self, num: int) -> None:
        # Always add to small heap first (as max heap using negation)
        heapq.heappush(self.small, -num)
        
        # Balance: ensure every element in small <= every element in large
        # Move the max of small to large if it violates this property
        if self.small and self.large and (-self.small[0] > self.large[0]):
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        
        # Balance sizes: small should have at most 1 more element than large
        if len(self.small) > len(self.large) + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        
        # If large has more elements, move one to small
        if len(self.large) > len(self.small):
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)

    def findMedian(self) -> float:
        # If odd number of elements, median is the top of small heap
        if len(self.small) > len(self.large):
            return float(-self.small[0])
        # If even number of elements, median is average of both heap tops
        return (-self.small[0] + self.large[0]) / 2.0