from __future__ import annotations
from typing import List

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        # Convert each "HH:MM" to total minutes from 00:00
        minutes_list = []
        for time in timePoints:
            h, m = map(int, time.split(':'))
            minutes_list.append(h * 60 + m)
        
        # Sort the minute values to easily compare adjacent times
        minutes_list.sort()
        
        # Initialize answer with large value (max possible minutes in a day = 1440)
        min_diff = 1440  # 24 * 60
        
        # Compare adjacent times in sorted order
        for i in range(1, len(minutes_list)):
            diff = minutes_list[i] - minutes_list[i-1]
            if diff < min_diff:
                min_diff = diff
        
        # Special circular comparison: compare last and first (wrapping around midnight)
        # Time difference going through midnight: (1440 - last) + first
        circular_diff = 1440 - minutes_list[-1] + minutes_list[0]
        if circular_diff < min_diff:
            min_diff = circular_diff
        
        return min_diff