from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        # Edge case: empty or single house
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        # Dynamic programming approach:
        # At each house i, we have two choices:
        # 1. Rob house i: get nums[i] + max money from houses up to i-2
        # 2. Don't rob house i: get max money from houses up to i-1
        # We take the maximum of these two options
        
        # Use two variables to track the max money:
        # prev2: max money robbed up to house i-2
        # prev1: max money robbed up to house i-1
        prev2 = 0  # initially, no houses robbed
        prev1 = nums[0]  # rob first house
        
        # Iterate through houses starting from index 1
        for i in range(1, len(nums)):
            # Current max is either:
            # - rob current house + prev2 (skip adjacent house)
            # - don't rob current house, keep prev1
            current = max(nums[i] + prev2, prev1)
            
            # Shift variables for next iteration
            prev2 = prev1
            prev1 = current
        
        # prev1 now holds the maximum money we can rob
        return prev1