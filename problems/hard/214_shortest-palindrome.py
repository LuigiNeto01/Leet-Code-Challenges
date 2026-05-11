class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if not s:
            return s
        
        # Key insight: Find the longest palindrome starting at index 0
        # Then prepend the reverse of the remaining suffix
        
        # Use KMP-style matching to find longest palindromic prefix
        # Create string: s + "#" + reverse(s)
        # The LPS array will tell us the longest prefix-suffix match
        
        rev_s = s[::-1]
        # Concatenate s with a separator and its reverse
        combined = s + "#" + rev_s
        
        # Build KMP failure function (LPS array)
        n = len(combined)
        lps = [0] * n
        
        # lps[i] = length of longest proper prefix which is also suffix
        # for combined[0:i+1]
        for i in range(1, n):
            j = lps[i - 1]
            
            # Fall back using the failure function
            while j > 0 and combined[i] != combined[j]:
                j = lps[j - 1]
            
            # If characters match, extend the length
            if combined[i] == combined[j]:
                j += 1
            
            lps[i] = j
        
        # lps[-1] gives us the length of longest prefix of s that matches
        # a suffix of rev_s, which means longest palindromic prefix of s
        palindrome_len = lps[-1]
        
        # Characters after the palindromic prefix need to be prepended (reversed)
        suffix_to_add = s[palindrome_len:]
        
        return suffix_to_add[::-1] + s