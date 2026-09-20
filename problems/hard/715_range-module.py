from __future__ import annotations
import bisect
from typing import List, Tuple

class RangeModule:
    def __init__(self):
        # Maintain a sorted list of disjoint intervals [start, end)
        # using a list of tuples for O(log n) binary search and O(n) insertion/deletion
        self.intervals: List[Tuple[int, int]] = []

    def addRange(self, left: int, right: int) -> None:
        """Add [left, right) to tracked ranges, merging overlaps."""
        # Find insertion point and merge overlapping intervals
        start_idx = bisect.bisect_left(self.intervals, (left, -float('inf')))
        end_idx = bisect.bisect_right(self.intervals, (right, float('inf')))
        
        # Extract the segment being replaced
        new_left = left
        new_right = right
        
        # Check immediate left neighbor if it overlaps
        if start_idx > 0 and self.intervals[start_idx-1][1] >= left:
            start_idx -= 1
            new_left = min(new_left, self.intervals[start_idx][0])
        
        # Merge all overlapping intervals
        for i in range(start_idx, end_idx):
            new_left = min(new_left, self.intervals[i][0])
            new_right = max(new_right, self.intervals[i][1])
        
        # Replace merged range with new merged interval
        self.intervals[start_idx:end_idx] = [(new_left, new_right)]

    def queryRange(self, left: int, right: int) -> bool:
        """Return True if every point in [left, right) is tracked."""
        # Binary search to find potential containing interval
        idx = bisect.bisect_right(self.intervals, (left, float('inf'))) - 1
        if idx < 0:
            return False
        start, end = self.intervals[idx]
        # Must be fully contained in the found interval
        return start <= left and right <= end

    def removeRange(self, left: int, right: int) -> None:
        """Remove [left, right) from tracked ranges."""
        # Find affected intervals
        start_idx = bisect.bisect_left(self.intervals, (left, -float('inf')))
        end_idx = bisect.bisect_right(self.intervals, (right, float('inf')))
        
        # Collect pieces to keep (non-overlapping parts)
        new_intervals = []
        for i in range(len(self.intervals)):
            cur_start, cur_end = self.intervals[i]
            # If no overlap with [left, right), keep as is
            if cur_end <= left or cur_start >= right:
                new_intervals.append(self.intervals[i])
                continue
            
            # Overlap detected: keep any non-touched prefix/suffix
            if cur_start < left:
                new_intervals.append((cur_start, min(cur_end, left)))
            if cur_end > right:
                new_intervals.append((max(cur_start, right), cur_end))
        
        # Sort for consistency (though we built in order, but safe)
        self.intervals = sorted(new_intervals)