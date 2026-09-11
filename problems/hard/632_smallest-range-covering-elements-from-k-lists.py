from typing import List
import heapq

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        k = len(nums)
        # Min-heap stores (value, list_index, element_index)
        heap = []
        current_max = float('-inf')
        
        # Initialize heap with the first element of each list
        for i in range(k):
            if nums[i]:  # list is non-empty per constraints
                val = nums[i][0]
                heapq.heappush(heap, (val, i, 0))
                current_max = max(current_max, val)
        
        # Best range found so far: [start, end]
        best_start = heap[0][0]  # current min
        best_end = current_max
        best_range = best_end - best_start
        
        # Slide the window by advancing the list with the smallest current element
        while True:
            # Pop the smallest element
            val, list_idx, elem_idx = heapq.heappop(heap)
            # Check if current range is smaller than best
            if current_max - val < best_range:
                best_start = val
                best_end = current_max
                best_range = current_max - val
            # If there's a next element in this list, push it and update max
            if elem_idx + 1 < len(nums[list_idx]):
                next_val = nums[list_idx][elem_idx + 1]
                heapq.heappush(heap, (next_val, list_idx, elem_idx + 1))
                current_max = max(current_max, next_val)
            else:
                # One list is exhausted, we cannot cover all lists anymore
                break
        
        return [best_start, best_end]