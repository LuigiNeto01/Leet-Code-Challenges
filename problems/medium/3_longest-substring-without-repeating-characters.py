class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Use sliding window with a set to track characters in current window
        char_set = set()
        left = 0
        max_length = 0
        
        # Expand window with right pointer
        for right in range(len(s)):
            # Shrink window from left until no duplicate exists
            # If s[right] is already in set, remove chars from left until it's gone
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            
            # Add current character to the set
            char_set.add(s[right])
            
            # Update max length with current window size
            max_length = max(max_length, right - left + 1)
        
        return max_length