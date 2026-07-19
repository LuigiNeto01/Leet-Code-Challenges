from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Track the maximum index we can reach from any position visited so far
        max_reach = 0
        
        # Iterate through each position in the array
        for i in range(len(nums)):
            # If current position is beyond what we can reach, we're stuck
            if i > max_reach:
                return False
            
            # Update the maximum reachable index from current position
            # From position i, we can reach up to i + nums[i]
            max_reach = max(max_reach, i + nums[i])
            
            # Early exit: if we can already reach or pass the last index
            if max_reach >= len(nums) - 1:
                return True
        
        # If we've gone through all reachable positions and can reach the end
        return True