from typing import List

class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        # Greedy: sort pairs by ending value (right endpoint)
        # then pick the earliest-finishing interval that doesn't overlap
        pairs.sort(key=lambda x: x[1])  # sort by second element (c, d) -> d
        
        count = 0
        current_end = float('-inf')  # last selected pair's right value
        
        for left, right in pairs:
            # If current pair's start is greater than last chosen end, it's valid
            if left > current_end:
                count += 1
                current_end = right  # update end to this pair's right
        
        return count