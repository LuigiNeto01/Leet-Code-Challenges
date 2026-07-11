from typing import List

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # Key insight: partition nums into two groups P (positive) and N (negative)
        # sum(P) - sum(N) = target
        # sum(P) + sum(N) = sum(nums)
        # => 2*sum(P) = target + sum(nums)
        # => sum(P) = (target + sum(nums)) / 2
        # Problem reduces to: count subsets with sum = (target + sum(nums)) / 2
        
        total = sum(nums)
        
        # Check if solution is possible
        # target + total must be even and >= 0
        if (target + total) % 2 != 0 or target + total < 0:
            return 0
        
        # Also check if target is achievable (not beyond total sum)
        if abs(target) > total:
            return 0
        
        # Calculate the subset sum we need to find
        subset_sum = (target + total) // 2
        
        # DP: dp[s] = number of ways to achieve sum s
        dp = [0] * (subset_sum + 1)
        dp[0] = 1  # One way to achieve sum 0: pick nothing
        
        # For each number in nums
        for num in nums:
            # Traverse backwards to avoid using same element multiple times
            for s in range(subset_sum, num - 1, -1):
                # Add ways: either include current num or don't
                dp[s] += dp[s - num]
        
        return dp[subset_sum]