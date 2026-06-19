from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # Use two pointers: one at start, one at end
        left = 0
        right = len(s) - 1
        
        # Swap elements while moving pointers toward center
        while left < right:
            # Swap characters at left and right positions
            s[left], s[right] = s[right], s[left]
            # Move pointers closer to center
            left += 1
            right -= 1