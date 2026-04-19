from __future__ import annotations
from typing import List

class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        # Handle trivial cases quickly: empty or single-element arrays
        if not nums:
            return 0
        n = len(nums)
        if n == 1:
            return 1

        # up: length of longest wiggle subsequence ending with a positive difference
        # down: length of longest wiggle subsequence ending with a negative difference
        # Initialize to 1 because any single element counts as length 1 subsequence
        up = 1
        down = 1

        # Iterate once through the array (O(n) time)
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                # Positive difference: extend a sequence that previously ended with a negative diff
                up = down + 1
            elif nums[i] < nums[i - 1]:
                # Negative difference: extend a sequence that previously ended with a positive diff
                down = up + 1
            else:
                # Equal elements produce zero difference -> do not change up/down
                # We just skip as zeros cannot contribute to "strictly" alternating signs
                pass

        # The result is the best of the two possibilities
        return max(up, down)