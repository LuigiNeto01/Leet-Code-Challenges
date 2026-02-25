from __future__ import annotations
from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # If there are no intervals, nothing to remove
        if not intervals:
            return 0

        # Sort intervals by their end time (earliest finish first)
        intervals.sort(key=lambda x: x[1])

        removals = 0
        # Initialize last_end to the end of the first interval (we keep it)
        last_end = intervals[0][1]

        # Iterate through the rest to detect overlaps
        for i in range(1, len(intervals)):
            start, end = intervals[i]
            if start >= last_end:
                # No overlap with the previously kept interval
                last_end = end  # update the end to the current interval's end
            else:
                # Overlap detected; we must remove this interval
                removals += 1
                # Do not update last_end, since we are keeping the previous interval

        return removals