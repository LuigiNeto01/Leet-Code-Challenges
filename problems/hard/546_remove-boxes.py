from typing import List
from functools import lru_cache

class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        # dp[l][r][k] where l, r is the range of boxes, k is the number of
        # boxes of the same color as boxes[l] that we have already collected
        # to the left of l (so we can combine them with boxes[l])
        @lru_cache(None)
        def dp(l: int, r: int, k: int) -> int:
            if l > r:
                return 0
            # Option 1: remove boxes[l] immediately, along with the k extra
            # same-colored boxes we have accumulated to the left.
            res = (k + 1) * (k + 1) + dp(l + 1, r, 0)
            # Option 2: try to combine boxes[l] with other boxes of the same
            # color inside the range. If we find one at index i (i>l), we can
            # remove boxes from l+1 to i-1 first, then later remove boxes[l]
            # together with the i-th box.
            for i in range(l + 1, r + 1):
                if boxes[i] == boxes[l]:
                    # Remove boxes[l+1..i-1] first, then we have k+1 boxes of
                    # same color (the k accumulated + boxes[l]) to the left of i.
                    res = max(res, dp(l + 1, i - 1, 0) + dp(i, r, k + 1))
            return res

        return dp(0, len(boxes) - 1, 0)