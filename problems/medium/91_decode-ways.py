class Solution:
    def numDecodings(self, s: str) -> int:
        # Edge case: empty string or starts with '0'
        if not s or s[0] == '0':
            return 0
        
        n = len(s)
        
        # dp[i] represents the number of ways to decode s[0:i]
        # We use dp of size n+1 where dp[0] = 1 (empty string has one way)
        dp = [0] * (n + 1)
        dp[0] = 1  # Base case: empty string
        dp[1] = 1  # First character is valid (we checked it's not '0')
        
        # Iterate through the string starting from index 1
        for i in range(1, n):
            # Current character (1-indexed in dp)
            current = s[i]
            # Previous character
            previous = s[i - 1]
            
            # Single digit decode: valid if current digit is not '0'
            if current != '0':
                dp[i + 1] += dp[i]
            
            # Two digit decode: valid if forms a number between 10 and 26
            two_digit = int(previous + current)
            if 10 <= two_digit <= 26:
                dp[i + 1] += dp[i - 1]
        
        return dp[n]