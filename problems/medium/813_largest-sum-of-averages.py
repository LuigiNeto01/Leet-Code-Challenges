class Solution:
    def largestSumOfAverages(self, nums: list[int], k: int) -> float:
        n = len(nums)
        # Prefix sums for quick average calculations
        prefix = [0] * (n + 1)
        for i, v in enumerate(nums):
            prefix[i + 1] = prefix[i] + v

        # dp[i][j] = max score for first i elements split into exactly j groups
        dp = [[0.0] * (k + 1) for _ in range(n + 1)]

        # Base case: one group
        for i in range(1, n + 1):
            dp[i][1] = prefix[i] / i

        # Fill for 2 groups and above
        for j in range(2, k + 1):
            for i in range(j, n + 1):
                best = 0.0
                # Let the last group start after p elements
                for p in range(j - 1, i):
                    avg = (prefix[i] - prefix[p]) / (i - p)
                    best = max(best, dp[p][j - 1] + avg)
                dp[i][j] = best

        # "at most k" means we can use any number from 1 to k
        return max(dp[n])  # dp[n][0] is 0, so this also works