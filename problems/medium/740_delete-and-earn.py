from __future__ import annotations
from collections import Counter
from typing import List

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        # Count total points we can get from each value
        # If we decide to take a value, we earn value * frequency
        points = Counter(nums)
        
        # Sort unique values to process in order
        unique_vals = sorted(points.keys())
        
        # DP variables for house robber style solution:
        # When we process values in increasing order, picking a value
        # means we cannot pick value+1 (which is the next in sorted order)
        # But we also need to handle gaps: if values are not consecutive,
        # we can freely take both without restriction.
        
        prev_earn = 0      # max points up to and including previous value
        curr_earn = 0      # max points up to current value
        
        for i, val in enumerate(unique_vals):
            # Points earned if we take this value
            take = val * points[val]
            
            if i > 0 and val == unique_vals[i-1] + 1:
                # Consecutive values: cannot take both this and previous
                # Classic house robber: max of (not take current = prev_earn,
                # take current + earnings from two steps back)
                # Use temporary variable to store the new curr_earn
                new_curr = max(curr_earn, prev_earn + take)
                prev_earn, curr_earn = curr_earn, new_curr
            else:
                # Gap exists: we can safely take current value
                # plus the best from all previous values
                prev_earn, curr_earn = curr_earn, curr_earn + take
        
        return curr_earn