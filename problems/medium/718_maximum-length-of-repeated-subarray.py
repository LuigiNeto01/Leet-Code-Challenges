from __future__ import annotations

class Solution:
    def findLength(self, nums1: list[int], nums2: list[int]) -> int:
        # Dynamic programming: dp[j] stores length of longest common suffix
        # of current prefix of nums1 (up to i) and prefix of nums2 (up to j).
        # We use a 1D array and update from right to left to avoid overwriting
        # the previous row's values needed for the next computation.
        m, n = len(nums1), len(nums2)
        dp = [0] * (n + 1)  # dp[0..n], dp[0] is dummy for easier indexing
        max_len = 0

        for i in range(m):
            # Iterate backwards so dp[j] refers to dp[j-1] from the previous row
            for j in range(n, 0, -1):
                if nums1[i] == nums2[j - 1]:
                    # Extend the common suffix from the previous prefixes
                    dp[j] = 1 + dp[j - 1]
                    max_len = max(max_len, dp[j])
                else:
                    # No match resets the suffix length for this (i, j)
                    dp[j] = 0

        return max_len