from __future__ import annotations

class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        n = len(cost)
        # dp[i] = minimum cost to reach step i (the position just before paying for step i)
        # Since we start before the staircase, dp[0] = 0 and dp[1] = 0
        # because we can start from step 0 or step 1 without paying first
        dp0, dp1 = 0, 0  # dp[i-2] and dp[i-1] for current i
        
        for i in range(2, n + 1):  # i represents step index we are trying to reach
            # To reach step i, we can come from i-1 (pay cost[i-1]) or i-2 (pay cost[i-2])
            # Take the minimum of these two options
            current = min(dp1 + cost[i-1], dp0 + cost[i-2])
            # Shift dp state for next iteration
            dp0, dp1 = dp1, current
        
        # At the end, dp1 holds the min cost to reach the top (position n)
        return dp1