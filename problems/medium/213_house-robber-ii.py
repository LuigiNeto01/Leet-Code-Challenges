from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        # Edge case: single house - just rob it
        if len(nums) == 1:
            return nums[0]
        
        # Edge case: two houses - rob the one with more money
        if len(nums) == 2:
            return max(nums[0], nums[1])
        
        # Since houses are in a circle, first and last are neighbors
        # We can't rob both the first and last house
        # Solution: run House Robber I twice:
        #   1) Consider houses from index 0 to n-2 (exclude last)
        #   2) Consider houses from index 1 to n-1 (exclude first)
        # Return the maximum of these two scenarios
        
        def rob_linear(houses):
            # Classic House Robber DP with O(1) space
            # prev2 = max money robbed up to i-2
            # prev1 = max money robbed up to i-1
            prev2 = 0
            prev1 = 0
            
            for money in houses:
                # Either rob current house + prev2, or skip current and keep prev1
                current = max(prev1, prev2 + money)
                prev2 = prev1
                prev1 = current
            
            return prev1
        
        # Scenario 1: Rob houses from 0 to n-2 (can include first, exclude last)
        max1 = rob_linear(nums[:-1])
        
        # Scenario 2: Rob houses from 1 to n-1 (exclude first, can include last)
        max2 = rob_linear(nums[1:])
        
        return max(max1, max2)