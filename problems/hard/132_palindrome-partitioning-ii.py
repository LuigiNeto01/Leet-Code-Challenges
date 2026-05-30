class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        
        # Build palindrome lookup table
        # is_palindrome[i][j] = True if s[i:j+1] is a palindrome
        is_palindrome = [[False] * n for _ in range(n)]
        
        # Every single character is a palindrome
        for i in range(n):
            is_palindrome[i][i] = True
        
        # Check for length 2 palindromes
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                is_palindrome[i][i + 1] = True
        
        # Check for palindromes of length 3 and more
        # A substring s[i:j+1] is palindrome if s[i] == s[j] and s[i+1:j] is palindrome
        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j] and is_palindrome[i + 1][j - 1]:
                    is_palindrome[i][j] = True
        
        # dp[i] = minimum cuts needed for s[0:i+1]
        dp = [float('inf')] * n
        
        for i in range(n):
            # If s[0:i+1] is itself a palindrome, no cuts needed
            if is_palindrome[0][i]:
                dp[i] = 0
            else:
                # Try all possible last partitions
                # If s[j+1:i+1] is palindrome, we can partition after j
                for j in range(i):
                    if is_palindrome[j + 1][i]:
                        dp[i] = min(dp[i], dp[j] + 1)
        
        return dp[n - 1]