from __future__ import annotations

class Solution:
    def intervalIntersection(self, firstList: list[list[int]], secondList: list[list[int]]) -> list[list[int]]:
        """
        Returns the intersection of two sorted, disjoint interval lists.
        Uses two-pointer technique to merge intervals in O(n+m) time.
        """
        # Pointers for both lists
        i = 0  # index in firstList
        j = 0  # index in secondList
        result = []
        
        # Traverse both lists until one is exhausted
        while i < len(firstList) and j < len(secondList):
            # Current intervals from each list
            a_start, a_end = firstList[i]
            b_start, b_end = secondList[j]
            
            # Calculate the overlapping part (intersection) if any
            # The intersection start is the later start point
            inter_start = max(a_start, b_start)
            # The intersection end is the earlier end point
            inter_end = min(a_end, b_end)
            
            # If inter_start <= inter_end, we have a valid intersection
            if inter_start <= inter_end:
                result.append([inter_start, inter_end])
            
            # Advance the pointer of the interval that ends first
            # Because its later intervals cannot overlap with the current interval of the other list
            if a_end < b_end:
                i += 1  # firstList interval ended first, move to next in firstList
            else:
                j += 1  # secondList interval ended first (or equal), move to next in secondList
        
        return result