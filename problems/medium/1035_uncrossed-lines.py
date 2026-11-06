from __future__ import annotations

class Solution:
    def maxUncrossedLines(self, nums1: list[int], nums2: list[int]) -> int:
        # Get lengths of both arrays
        m, n = len(nums1), len(nums2)
        
        # dp[i][j] = max uncrossed lines using first i of nums1 and first j of nums2
        # Initialize (m+1) x (n+1) with zeros (dp[0][*] and dp[*][0] are 0)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Fill dp table iteratively
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if nums1[i - 1] == nums2[j - 1]:
                    # Matching numbers -> we can draw a line and add 1 to previous best
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    # No match -> take the best from either skipping nums1[i-1] or nums2[j-1]
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        # The bottom-right cell contains the answer
        return dp[m][n]