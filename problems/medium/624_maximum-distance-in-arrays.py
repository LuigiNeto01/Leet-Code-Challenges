from typing import List

class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        # Initialize with first array's min and max
        min_val = arrays[0][0]          # smallest element of first array
        max_val = arrays[0][-1]         # largest element of first array
        max_distance = 0

        # Process the remaining arrays
        for i in range(1, len(arrays)):
            cur_min = arrays[i][0]      # first element (min) of current array
            cur_max = arrays[i][-1]     # last element (max) of current array

            # Compare current array's max with previous min
            # Compare current array's min with previous max
            # Both are valid because they come from different arrays
            max_distance = max(max_distance, cur_max - min_val, max_val - cur_min)

            # Update global min and max for future comparisons
            min_val = min(min_val, cur_min)
            max_val = max(max_val, cur_max)

        return max_distance