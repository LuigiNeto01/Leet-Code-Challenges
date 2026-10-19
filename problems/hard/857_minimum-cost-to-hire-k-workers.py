from __future__ import annotations
import heapq

class Solution:
    def mincostToHireWorkers(self, quality: list[int], wage: list[int], k: int) -> float:
        n = len(quality)
        
        # Each worker has a "wage/quality" ratio (the minimum rate they must be paid per unit of quality)
        # To form a valid group, we must pay all workers based on the highest ratio in the group.
        # So we sort workers by this ratio (ascending) and consider each worker as the one who sets the ratio.
        workers = [(wage[i] / quality[i], quality[i]) for i in range(n)]
        workers.sort(key=lambda x: x[0])
        
        # We will maintain a max-heap (as negative) for the largest qualities among selected workers.
        # We want to keep sum of qualities as low as possible for a given ratio.
        max_heap = []
        total_quality = 0
        best_cost = float('inf')
        
        for ratio, q in workers:
            total_quality += q
            heapq.heappush(max_heap, -q)  # use negative for max-heap
            
            # If we have more than k workers, remove the one with the highest quality (to minimize total quality)
            if len(max_heap) > k:
                total_quality += heapq.heappop(max_heap)  # pop negative, so adding negative = subtracting quality
            
            # When we have exactly k workers, calculate the cost using the current ratio (which is the max ratio in the group)
            if len(max_heap) == k:
                cost = total_quality * ratio
                best_cost = min(best_cost, cost)
        
        return best_cost