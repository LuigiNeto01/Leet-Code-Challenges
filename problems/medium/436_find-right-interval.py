from typing import List
import bisect

class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        # Store start values with their original indices
        # Since each start is unique, we can create a mapping
        starts = []
        for i, interval in enumerate(intervals):
            starts.append((interval[0], i))
        
        # Sort by start value for binary search
        starts.sort()
        
        result = []
        
        # For each interval, find the smallest start >= its end
        for interval in intervals:
            end = interval[1]
            
            # Binary search for the leftmost start >= end
            # bisect_left finds insertion point to keep sorted order
            # We need the smallest start >= end, which is at position idx
            idx = bisect.bisect_left(starts, (end, -1))
            
            # If idx is within bounds, we found a right interval
            if idx < len(starts):
                result.append(starts[idx][1])
            else:
                # No right interval exists
                result.append(-1)
        
        return result