from __future__ import annotations
import heapq

class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        # Use a max-heap by negating values (Python has min-heap by default)
        # Negate to simulate max-heap behavior
        max_heap = [-stone for stone in stones]
        heapq.heapify(max_heap)
        
        # Continue smashing until at most one stone remains
        while len(max_heap) > 1:
            # Extract the two heaviest stones (largest negatives = smallest positives)
            y = -heapq.heappop(max_heap)  # Heavier stone (y >= x)
            x = -heapq.heappop(max_heap)  # Lighter stone
            
            # If they are different, the remainder (y - x) goes back
            if x != y:
                # Push the remaining weight (negated for max-heap)
                heapq.heappush(max_heap, -(y - x))
            # If equal, both are destroyed (nothing to push back)
        
        # If a stone remains, return its weight; otherwise 0
        return -max_heap[0] if max_heap else 0