from collections import Counter
from typing import Optional

class Solution:
    def longestPalindrome(self, s: str) -> int:
        # Count frequency of each character in the string
        # Using Counter simplifies tallying and handles both cases (upper/lower)
        freq = Counter(s)
        
        # total length contributed by paired characters (even counts)
        length = 0
        # flag to record if we can place a single center character (an odd leftover)
        has_center = False
        
        # Iterate over character counts to compute maximum paired characters
        for ch, cnt in freq.items():
            # If count is even, we can use all of them symmetrically in pairs
            if cnt % 2 == 0:
                length += cnt
            else:
                # If count is odd, we can use cnt - 1 as pairs (largest even number <= cnt)
                length += cnt - 1
                # One odd count allows placing a single character in the center of palindrome
                has_center = True
        
        # If there was at least one odd count, we can add one center character
        if has_center:
            length += 1
        
        return length