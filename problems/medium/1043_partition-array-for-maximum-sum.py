class Solution:
    def maxSumAfterPartitioning(self, arr: list[int], k: int) -> int:
        # DP approach: dp[i] = max sum for arr[0:i] (first i elements)
        n = len(arr)
        dp = [0] * (n + 1)  # dp[0] = 0 (empty prefix)

        # Process prefixes from left to right
        for i in range(1, n + 1):
            # We consider the last subarray ending at i-1,
            # try all possible lengths from 1 to min(k, i)
            max_val = 0
            # j is the start index of the last subarray (inclusive)
            # The subarray is from index j to i-1
            for j in range(i - 1, max(i - k - 1, -1), -1):
                # update the max value in this subarray as we extend leftwards
                max_val = max(max_val, arr[j])
                # size of this subarray = i - j
                subarray_sum = max_val * (i - j)
                # total = best of prefix up to j + sum of this subarray
                dp[i] = max(dp[i], dp[j] + subarray_sum)

        return dp[n]