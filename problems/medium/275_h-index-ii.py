from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        left, right = 0, n - 1
        
        # Binary search to find the leftmost position where citations[i] >= n - i
        # n - i represents the number of papers with at least citations[i] citations
        while left <= right:
            mid = (left + right) // 2
            # Number of papers from mid to end (inclusive)
            papers_count = n - mid
            
            # Check if we have at least papers_count papers with papers_count citations
            if citations[mid] >= papers_count:
                # This position qualifies, but there might be a better (smaller index) position
                right = mid - 1
            else:
                # Need more citations, move to the right
                left = mid + 1
        
        # left now points to the leftmost position where citations[i] >= n - i
        # The h-index is n - left (number of papers from left to end)
        return n - left