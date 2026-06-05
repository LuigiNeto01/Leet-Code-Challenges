class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Use sliding window approach
        # Window is valid if: window_length - max_freq <= k
        # (meaning we can replace the non-majority chars with at most k operations)
        
        char_count = {}  # Track frequency of each character in current window
        max_freq = 0  # Track the maximum frequency of any single character in current window
        left = 0  # Left pointer of sliding window
        max_length = 0  # Result: maximum valid window size seen
        
        for right in range(len(s)):
            # Expand window by including s[right]
            char_count[s[right]] = char_count.get(s[right], 0) + 1
            
            # Update max_freq with the frequency of the current character
            # max_freq represents the count of the most frequent character in the window
            max_freq = max(max_freq, char_count[s[right]])
            
            # Check if current window is valid
            # window_length - max_freq gives us the number of chars that need to be replaced
            window_length = right - left + 1
            
            # If we need more than k replacements, shrink window from left
            if window_length - max_freq > k:
                char_count[s[left]] -= 1
                left += 1
                # Note: we don't update max_freq when shrinking because we only care about
                # finding windows where max_freq is high enough. Even if the actual max_freq
                # decreases, we're looking for the maximum window size, and a smaller max_freq
                # won't give us a larger window anyway.
            
            # Update result with current valid window size
            max_length = max(max_length, right - left + 1)
        
        return max_length