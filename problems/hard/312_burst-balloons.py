from typing import List

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # Key insight: Instead of thinking about which balloon to burst first,
        # think about which balloon to burst LAST in a range.
        # When we burst balloon k last in range [left, right], the balloons
        # at left-1 and right+1 are still there, making the subproblems independent.
        
        # Add virtual balloons with value 1 at both ends to handle boundaries
        nums = [1] + nums + [1]
        n = len(nums)
        
        # dp[i][j] = max coins obtainable by bursting all balloons between i and j (exclusive)
        dp = [[0] * n for _ in range(n)]
        
        # length is the distance between left and right boundaries
        # We build up from smaller subproblems to larger ones
        for length in range(2, n):  # length starts at 2 (adjacent boundaries)
            # For each possible left boundary
            for left in range(n - length):
                right = left + length
                # Try bursting each balloon k between left and right as the LAST one
                for k in range(left + 1, right):
                    # When k is burst last in this range:
                    # - left and right balloons are still present
                    # - All balloons between left and k are already burst (dp[left][k])
                    # - All balloons between k and right are already burst (dp[k][right])
                    # - Bursting k gives us nums[left] * nums[k] * nums[right]
                    coins = nums[left] * nums[k] * nums[right]
                    coins += dp[left][k] + dp[k][right]
                    dp[left][right] = max(dp[left][right], coins)
        
        # Return max coins for bursting all balloons between the two virtual boundaries
        return dp[0][n - 1]