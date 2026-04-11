from typing import List

class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        # Precompute a 2D prefix sum (also called summed-area table).
        # We use an extra row and column (dimensions (m+1)x(n+1)) to simplify boundary handling.
        # ps[i+1][j+1] stores sum of matrix[0..i][0..j].
        if not matrix or not matrix[0]:
            # handle empty matrix edge-case: keep a minimal prefix matrix so sumRegion can safely return 0
            self._ps = [[0]]
            self._m = 0
            self._n = 0
            return

        m = len(matrix)
        n = len(matrix[0])
        self._m = m
        self._n = n

        # initialize prefix sum array with zeros
        ps = [[0] * (n + 1) for _ in range(m + 1)]

        # fill prefix sums: ps[i+1][j+1] = ps[i][j+1] + ps[i+1][j] - ps[i][j] + matrix[i][j]
        # this ensures any rectangle sum can be computed in O(1) using inclusion-exclusion
        for i in range(m):
            # accumulate row by row; helps locality
            row = matrix[i]
            for j in range(n):
                ps[i+1][j+1] = ps[i][j+1] + ps[i+1][j] - ps[i][j] + row[j]

        self._ps = ps

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # If matrix was empty, always return 0 (defensive)
        if self._m == 0 or self._n == 0:
            return 0

        # Use precomputed prefix sums. Convert coordinates to prefix indices by adding 1.
        # sum of rectangle (row1,col1) to (row2,col2) inclusive:
        # = ps[row2+1][col2+1] - ps[row1][col2+1] - ps[row2+1][col1] + ps[row1][col1]
        ps = self._ps
        r1 = row1
        c1 = col1
        r2 = row2
        c2 = col2

        # apply inclusion-exclusion; this is O(1)
        return ps[r2+1][c2+1] - ps[r1][c2+1] - ps[r2+1][c1] + ps[r1][c1]

# Provide alias expected by the test harness
Solution = NumMatrix