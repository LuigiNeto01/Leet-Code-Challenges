from __future__ import annotations

class Solution:
    def minIncrementForUnique(self, nums: list[int]) -> int:
        # Sort the array to process duplicates in ascending order
        nums.sort()
        moves = 0
        # Track the minimum allowed value for the next unique number
        next_available = 0
        
        for num in nums:
            # Each number must be at least next_available to be unique
            if num < next_available:
                # We need to increment num to next_available
                moves += next_available - num
            else:
                # num already satisfies uniqueness, set next_available to num+1
                next_available = num
            
            # After processing this number, the next must be at least current+1
            next_available += 1
        
        return moves