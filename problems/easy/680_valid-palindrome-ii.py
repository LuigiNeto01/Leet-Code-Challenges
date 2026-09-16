from __future__ import annotations

class Solution:
    def validPalindrome(self, s: str) -> bool:
        # Helper to check if substring s[left:right+1] is a plain palindrome
        def is_palindrome_range(left: int, right: int) -> bool:
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True
        
        # Main two-pointer scan from both ends
        left, right = 0, len(s) - 1
        
        while left < right:
            # When mismatch found, try deleting either the left or right character
            if s[left] != s[right]:
                # If either resulting substring is palindrome, we can delete one char
                return is_palindrome_range(left + 1, right) or is_palindrome_range(left, right - 1)
            left += 1
            right -= 1
        
        # If loop completes without mismatch, already a palindrome (or empty after deletions)
        return True