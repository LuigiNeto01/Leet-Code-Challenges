import heapq
from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Max-heap via negative distance: keep the k smallest distances.
        heap = []
        for x, y in points:
            # Use squared Euclidean distance to avoid floating point.
            dist_sq = x * x + y * y
            # Push negative distance so the heap behaves like a max-heap.
            heapq.heappush(heap, (-dist_sq, [x, y]))
            if len(heap) > k:
                # Remove the point with the largest distance (smallest negative).
                heapq.heappop(heap)
        # Extract the points from the heap (order does not matter).
        return [pt for _, pt in heap]