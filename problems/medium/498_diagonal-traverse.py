from __future__ import annotations
from typing import List

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        # Handle trivial empty input defensively
        if not mat or not mat[0]:
            return []
        m, n = len(mat), len(mat[0])
        # Result list of size m*n to collect traversal order
        result: List[int] = []
        # There are m + n - 1 diagonals indexed by sum s = i + j
        for s in range(m + n - 1):
            # Determine bounds for i (row index) on this diagonal:
            # i ranges from max(0, s-(n-1)) to min(s, m-1)
            i_min = max(0, s - (n - 1))
            i_max = min(s, m - 1)
            # If s is even, we traverse upwards (i decreases, j increases)
            if s % 2 == 0:
                # Start from i_max down to i_min
                i = i_max
                while i >= i_min:
                    j = s - i  # column determined by sum
                    # j is guaranteed in [0, n-1] by bounds selection
                    result.append(mat[i][j])
                    i -= 1
            else:
                # If s is odd, traverse downwards (i increases, j decreases)
                i = i_min
                while i <= i_max:
                    j = s - i
                    result.append(mat[i][j])
                    i += 1
        return result