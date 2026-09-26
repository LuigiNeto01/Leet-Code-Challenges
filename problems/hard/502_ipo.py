from __future__ import annotations
import heapq
from typing import List

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        # Number of projects available
        n = len(profits)
        
        # Pair each project's capital requirement with its profit
        projects = list(zip(capital, profits))
        
        # Sort projects by capital required (ascending) so we can pick
        # all projects we can currently afford as our capital grows
        projects.sort(key=lambda x: x[0])
        
        # Max-heap to store profits of affordable projects
        # (Python heapq is min-heap; store negative profit for max-heap behavior)
        max_profit_heap = []
        
        # Index to iterate through sorted projects
        idx = 0
        
        # Try to pick at most k projects
        for _ in range(k):
            # While there are still projects we can afford with current capital w,
            # push their profit into the max-heap (as negative for max-heap simulation)
            while idx < n and projects[idx][0] <= w:
                heapq.heappush(max_profit_heap, -projects[idx][1])
                idx += 1
            
            # If no project is affordable, we cannot proceed further
            if not max_profit_heap:
                break
            
            # Pick the most profitable project among affordable ones
            # (pop negative value and negate back to positive profit)
            w += -heapq.heappop(max_profit_heap)
        
        # Return final maximized capital
        return w