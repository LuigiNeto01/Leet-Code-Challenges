from __future__ import annotations
from typing import List

class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        # Use a set to store all distinct OR results across subarrays.
        result_set = set()
        
        # The set of OR values for subarrays ending at the current position.
        # We'll rebuild it as we iterate to avoid storing all subarrays explicitly.
        cur = set()
        
        for num in arr:
            # Start with the single-element subarray [num]
            # and combine with all previous subarray ORs (from cur) to extend them.
            new_cur = {num}
            for prev_or in cur:
                new_cur.add(prev_or | num)
            cur = new_cur
            
            # Add all OR values ending at this position to the global set.
            result_set.update(cur)
        
        # The size of the set is the number of distinct OR results.
        return len(result_set)