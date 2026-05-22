from typing import List
import heapq

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        
        # Use a min heap to efficiently get the k-th smallest element
        # Each heap entry is (value, row, col)
        min_heap = []
        
        # Initialize heap with the first element of each row
        # We only need to add min(n, k) rows since we only need k elements
        for r in range(min(n, k)):
            heapq.heappush(min_heap, (matrix[r][0], r, 0))
        
        # Extract k-1 elements, the k-th extraction will be our answer
        result = 0
        for _ in range(k):
            result, r, c = heapq.heappop(min_heap)
            
            # If there's a next element in the same row, add it to the heap
            if c + 1 < n:
                heapq.heappush(min_heap, (matrix[r][c + 1], r, c + 1))
        
        return result