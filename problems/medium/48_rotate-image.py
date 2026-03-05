from __future__ import annotations
from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Rotate the nxn matrix by 90 degrees clockwise in-place.

        Approach:
        1) Transpose the matrix (swap mirror elements across diagonal).
           After this, rows become columns but in the same order.
        2) Reverse each row to achieve the clockwise rotation.

        This avoids creating a new matrix and handles in-place constraints.
        """
        n = len(matrix)
        # Step 1: Transpose in-place (swap matrix[i][j] with matrix[j][i] for i < j)
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Step 2: Reverse each row in-place
        for i in range(n):
            left, right = 0, n - 1
            while left < right:
                matrix[i][left], matrix[i][right] = matrix[i][right], matrix[i][left]
                left += 1
                right -= 1