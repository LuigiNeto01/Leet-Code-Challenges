class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Use two pointers approach from both ends
        left = 0
        right = len(s) - 1
        
        while left < right:
            # Skip non-alphanumeric characters from left
            while left < right and not s[left].isalnum():
                left += 1
            
            # Skip non-alphanumeric characters from right
            while left < right and not s[right].isalnum():
                right -= 1
            
            # Compare characters case-insensitively
            if s[left].lower() != s[right].lower():
                return False
            
            # Move both pointers inward
            left += 1
            right -= 1
        
        # All valid characters matched, it's a palindrome
        return True