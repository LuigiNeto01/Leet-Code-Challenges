from __future__ import annotations

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Get lengths of both strings
        m, n = len(text1), len(text2)
        
        # DP table: dp[i][j] = LCS length of text1[:i] and text2[:j]
        # Initialize (m+1) x (n+1) with zeros, where first row/col = 0 for empty strings
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Fill DP table from top-left to bottom-right
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    # Characters match: extend the subsequence by 1
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    # Characters differ: take max of skipping one character from either string
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        # Bottom-right cell holds the length of LCS for full strings
        return dp[m][n]