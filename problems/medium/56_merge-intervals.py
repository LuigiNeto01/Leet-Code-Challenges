from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Edge case: empty or single interval
        if not intervals or len(intervals) == 1:
            return intervals
        
        # Sort intervals by start time to process them in order
        intervals.sort(key=lambda x: x[0])
        
        # Initialize result with the first interval
        merged = [intervals[0]]
        
        # Process each interval starting from the second one
        for i in range(1, len(intervals)):
            current_start, current_end = intervals[i]
            last_start, last_end = merged[-1]
            
            # Check if current interval overlaps with the last merged interval
            # Overlap occurs when current start <= last end
            if current_start <= last_end:
                # Merge by extending the end of the last interval
                # Take the max end to handle cases where current is contained in last
                merged[-1][1] = max(last_end, current_end)
            else:
                # No overlap, add current interval as a new separate interval
                merged.append(intervals[i])
        
        return merged