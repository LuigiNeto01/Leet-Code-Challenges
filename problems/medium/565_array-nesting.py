from __future__ import annotations
from typing import List

class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        # Because nums is a permutation of 0..n-1, starting from any index
        # follows a cycle. Each element belongs to exactly one cycle.
        # Once a cycle is fully visited, any member yields the same set length.
        # We mark visited indices to avoid reprocessing.
        
        n = len(nums)
        visited = [False] * n
        max_len = 0
        
        for i in range(n):
            if visited[i]:
                continue
            
            # Traverse current cycle starting from i
            length = 0
            cur = i
            while not visited[cur]:
                visited[cur] = True
                length += 1
                cur = nums[cur]
            
            # Update max length found so far
            max_len = max(max_len, length)
            
            # Small optimization: if we already found a cycle of maximum possible length,
            # no need to explore further (though n <= 1e5, this speeds up worst-case)
            if max_len == n:
                break
                
        return max_len