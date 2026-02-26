from __future__ import annotations
from typing import List
import math

class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        # Start from the largest possible width (the square root bound)
        # and move downwards to ensure the difference L - W is minimized.
        max_w = int(math.isqrt(area))  # integer sqrt gives the boundary where W <= L
        for w in range(max_w, 0, -1):
            if area % w == 0:
                l = area // w
                return [l, w]  # L >= W by construction
        # Fallback (theoretically unreachable for area >= 1)
        return [area, 1]