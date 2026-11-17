from __future__ import annotations

class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        n, m = len(str1), len(str2)
        
        # dp[i][j] = length of LCS of str1[:i] and str2[:j]
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        
        # Fill DP table for LCS lengths
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if str1[i - 1] == str2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        # Backtrack to build the shortest common supersequence
        i, j = n, m
        scs_chars = []
        
        while i > 0 or j > 0:
            if i > 0 and j > 0 and str1[i - 1] == str2[j - 1]:
                # Characters match — include once and move diagonally
                scs_chars.append(str1[i - 1])
                i -= 1
                j -= 1
            elif i > 0 and (j == 0 or dp[i - 1][j] > dp[i][j - 1]):
                # Character from str1 is part of LCS (or str2 exhausted)
                scs_chars.append(str1[i - 1])
                i -= 1
            else:
                # Character from str2 is part of LCS (or str1 exhausted)
                scs_chars.append(str2[j - 1])
                j -= 1
        
        # We built the string backwards; reverse it
        return ''.join(reversed(scs_chars))