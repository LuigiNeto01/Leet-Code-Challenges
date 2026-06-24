from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Edge case: if the list is empty, return empty string
        if not strs:
            return ""
        
        # Edge case: if any string is empty, the common prefix is empty
        if any(s == "" for s in strs):
            return ""
        
        # Start with the first string as the initial prefix candidate
        prefix = strs[0]
        
        # Compare prefix with each subsequent string
        for i in range(1, len(strs)):
            # Shrink the prefix until it matches the start of strs[i]
            while not strs[i].startswith(prefix):
                # Remove the last character from prefix
                prefix = prefix[:-1]
                # If prefix becomes empty, no common prefix exists
                if not prefix:
                    return ""
        
        return prefix