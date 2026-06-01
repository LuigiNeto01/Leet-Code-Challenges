class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # Dynamic programming approach
        # dp[i][j] = True if s[0:i] matches p[0:j]
        m, n = len(s), len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        
        # Empty string matches empty pattern
        dp[0][0] = True
        
        # Handle patterns like a*, a*b*, a*b*c* that can match empty string
        for j in range(2, n + 1):
            # Pattern with '*' can match empty if the part before it also matches empty
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]
        
        # Fill the DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # Current characters in s and p (0-indexed)
                s_char = s[i - 1]
                p_char = p[j - 1]
                
                if p_char == '*':
                    # '*' matches zero or more of the preceding element
                    # We need to look at p[j-2] (the character before '*')
                    prev_p_char = p[j - 2]
                    
                    # Case 1: Use '*' to match zero occurrences of prev_p_char
                    # So we check if s[0:i] matches p[0:j-2]
                    dp[i][j] = dp[i][j - 2]
                    
                    # Case 2: Use '*' to match one or more occurrences
                    # This is valid if prev_p_char matches current s_char
                    # and s[0:i-1] already matched p[0:j]
                    if prev_p_char == s_char or prev_p_char == '.':
                        dp[i][j] = dp[i][j] or dp[i - 1][j]
                
                elif p_char == '.' or p_char == s_char:
                    # '.' matches any character, or exact character match
                    # Check if the strings without current characters match
                    dp[i][j] = dp[i - 1][j - 1]
                
                # else: characters don't match and no wildcard, dp[i][j] stays False
        
        return dp[m][n]