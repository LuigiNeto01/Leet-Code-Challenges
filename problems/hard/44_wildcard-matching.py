class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # Use dynamic programming approach
        # dp[i][j] = True if s[0:i] matches p[0:j]
        m, n = len(s), len(p)
        
        # Initialize DP table
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        
        # Empty string matches empty pattern
        dp[0][0] = True
        
        # Handle patterns that start with '*' which can match empty string
        # e.g., "*", "**", "***" all match empty string
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 1]
        
        # Fill the DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    # '*' can match empty sequence (dp[i][j-1])
                    # or match one or more characters (dp[i-1][j])
                    dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
                elif p[j - 1] == '?' or p[j - 1] == s[i - 1]:
                    # '?' matches any single character
                    # or characters match exactly
                    dp[i][j] = dp[i - 1][j - 1]
                # else: dp[i][j] remains False (mismatch)
        
        return dp[m][n]