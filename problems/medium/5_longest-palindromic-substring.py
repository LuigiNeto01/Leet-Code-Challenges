class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        
        # Track the start and max length of the longest palindrome found
        start = 0
        max_len = 0
        
        def expand_around_center(left: int, right: int) -> int:
            # Expand outward from center while characters match
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # Return the length of the palindrome found
            # (right - left - 1) because we've gone one step too far on each side
            return right - left - 1
        
        # Check each possible center position
        for i in range(len(s)):
            # Case 1: Odd-length palindrome (single character center)
            len1 = expand_around_center(i, i)
            # Case 2: Even-length palindrome (center between two characters)
            len2 = expand_around_center(i, i + 1)
            
            # Take the longer of the two palindromes found at this position
            current_max = max(len1, len2)
            
            # Update the result if we found a longer palindrome
            if current_max > max_len:
                max_len = current_max
                # Calculate starting position: center minus half the length (adjusted for integer division)
                start = i - (current_max - 1) // 2
        
        # Return the substring from start position with max_len characters
        return s[start:start + max_len]