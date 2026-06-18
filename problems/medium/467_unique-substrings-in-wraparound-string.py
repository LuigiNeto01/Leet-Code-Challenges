class Solution:
    def findSubstringInWraproundString(self, s: str) -> int:
        # Key insight: Track the maximum length of valid substring ending with each letter
        # For each letter, the number of unique substrings ending with it equals the max length
        # Example: if max length ending with 'c' is 3 (like "abc"), we have substrings: "c", "bc", "abc"
        
        # Dictionary to store max length of valid substring ending with each character
        max_len = {}
        
        # Current length of consecutive valid substring
        length = 0
        
        for i in range(len(s)):
            # Check if current char continues the wraparound sequence from previous char
            # Two cases: normal consecutive (a->b, b->c) or wraparound (z->a)
            if i > 0 and (ord(s[i]) - ord(s[i-1])) % 26 == 1:
                # Continue the sequence, increment length
                length += 1
            else:
                # Start a new sequence
                length = 1
            
            # Update max length for substring ending with current character
            # If we've seen this char before, keep the maximum length
            max_len[s[i]] = max(max_len.get(s[i], 0), length)
        
        # Sum all max lengths - each represents count of unique substrings ending with that char
        # This avoids double-counting because we only count the longest valid substring ending with each letter
        return sum(max_len.values())