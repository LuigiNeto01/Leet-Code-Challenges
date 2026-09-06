from __future__ import annotations

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        Returns the minimum number of deletions to make word1 and word2 equal.
        This is equivalent to: total length - 2 * length of longest common subsequence (LCS).
        """
        m, n = len(word1), len(word2)
        # dp[i][j] = LCS length of word1[:i] and word2[:j]
        # Use (m+1) x (n+1) matrix with 0-initialized borders.
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    # characters match, extend LCS
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    # take the maximum of skipping one character from either string
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        lcs_len = dp[m][n]
        # total deletions needed
        return (m - lcs_len) + (n - lcs_len)