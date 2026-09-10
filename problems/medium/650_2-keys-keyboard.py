class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0
        dp = [float('inf')] * (n + 1)
        dp[1] = 0
        for i in range(2, n + 1):
            for j in range(1, i):
                if i % j == 0:
                    ops = dp[j] + 1 + (i // j - 1)
                    dp[i] = min(dp[i], ops)
        return dp[n]