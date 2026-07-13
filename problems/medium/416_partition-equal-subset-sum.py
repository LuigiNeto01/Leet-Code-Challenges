from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # Calculate total sum of all elements
        total = sum(nums)
        
        # If total is odd, we cannot partition into two equal subsets
        if total % 2 != 0:
            return False
        
        # Target sum for each subset
        target = total // 2
        
        # DP set to track all possible sums we can achieve
        # Start with 0 (we can always make sum 0 by selecting nothing)
        dp = {0}
        
        # For each number in the array
        for num in nums:
            # Create new possible sums by adding current num to existing sums
            # Use list() to avoid modifying set while iterating
            new_sums = set()
            for curr_sum in dp:
                new_sum = curr_sum + num
                # If we reach target, we found a valid partition
                if new_sum == target:
                    return True
                # Only add sums less than target (optimization)
                if new_sum < target:
                    new_sums.add(new_sum)
            # Add all new possible sums to dp
            dp.update(new_sums)
        
        # Check if target sum is achievable
        return target in dp