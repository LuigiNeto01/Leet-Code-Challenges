class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        # Edge case: if p is longer than s, no anagrams possible
        if len(p) > len(s):
            return []
        
        result = []
        p_len = len(p)
        
        # Build frequency map for pattern p
        p_count = {}
        for char in p:
            p_count[char] = p_count.get(char, 0) + 1
        
        # Build frequency map for the first window in s
        window_count = {}
        for i in range(p_len):
            char = s[i]
            window_count[char] = window_count.get(char, 0) + 1
        
        # Check if first window is an anagram
        if window_count == p_count:
            result.append(0)
        
        # Slide the window through the rest of s
        for i in range(p_len, len(s)):
            # Add new character to the right of window
            new_char = s[i]
            window_count[new_char] = window_count.get(new_char, 0) + 1
            
            # Remove character from the left of window
            old_char = s[i - p_len]
            window_count[old_char] -= 1
            # Clean up zero counts to allow proper dict comparison
            if window_count[old_char] == 0:
                del window_count[old_char]
            
            # Check if current window is an anagram
            if window_count == p_count:
                result.append(i - p_len + 1)
        
        return result