from typing import List

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # dp[i] = number of combinations that sum to i
        dp = [0] * (target + 1)
        # Base case: one way to make 0 (empty combination)
        dp[0] = 1
        
        # For each amount from 1 to target
        for amount in range(1, target + 1):
            # Try using each number in nums
            for num in nums:
                # If we can use this num (amount >= num)
                # then add the number of ways to make (amount - num)
                if amount >= num:
                    dp[amount] += dp[amount - num]
        
        return dp[target]