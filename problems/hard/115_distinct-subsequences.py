class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        
        # dp[i][j] = number of distinct subsequences of s[0..i-1] that equal t[0..j-1]
        # We use i+1 and j+1 dimensions to handle empty string cases easily
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Base case: empty t can be formed by any prefix of s in exactly one way (delete all chars)
        for i in range(m + 1):
            dp[i][0] = 1
        
        # Fill the DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # Option 1: Don't use s[i-1] to match t[j-1]
                # Count carries over from previous position in s
                dp[i][j] = dp[i-1][j]
                
                # Option 2: If characters match, we can also use s[i-1] to match t[j-1]
                # Add the count where both s and t are one character shorter
                if s[i-1] == t[j-1]:
                    dp[i][j] += dp[i-1][j-1]
        
        return dp[m][n]