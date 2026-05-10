from typing import List

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # Sort both greed factors and cookie sizes to use greedy approach
        # We want to assign smallest cookies to children with smallest greed
        g.sort()
        s.sort()
        
        child_idx = 0  # pointer for children
        cookie_idx = 0  # pointer for cookies
        content_count = 0  # count of content children
        
        # Try to satisfy children one by one with available cookies
        while child_idx < len(g) and cookie_idx < len(s):
            # If current cookie can satisfy current child
            if s[cookie_idx] >= g[child_idx]:
                # Assign cookie to child
                content_count += 1
                child_idx += 1  # move to next child
                cookie_idx += 1  # move to next cookie
            else:
                # Current cookie too small, try next larger cookie
                cookie_idx += 1
        
        return content_count