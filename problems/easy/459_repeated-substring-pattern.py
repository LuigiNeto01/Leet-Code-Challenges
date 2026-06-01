class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        
        # Try all possible substring lengths that can divide the total length
        # We only need to check divisors of n
        for length in range(1, n // 2 + 1):
            # Only consider lengths that evenly divide the string length
            if n % length == 0:
                # Extract the candidate substring
                substring = s[:length]
                # Check if repeating this substring gives us the original string
                # Number of repetitions needed
                repetitions = n // length
                if substring * repetitions == s:
                    return True
        
        return False