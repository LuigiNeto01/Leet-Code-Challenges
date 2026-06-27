from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Use a dictionary to group strings by their sorted character signature
        # Anagrams will have the same sorted character sequence
        anagram_groups = defaultdict(list)
        
        for s in strs:
            # Sort the characters of the string to create a key
            # All anagrams will produce the same sorted key
            key = ''.join(sorted(s))
            # Group strings with the same key together
            anagram_groups[key].append(s)
        
        # Return all groups as a list of lists
        return list(anagram_groups.values())