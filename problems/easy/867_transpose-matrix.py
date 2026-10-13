from __future__ import annotations

class Solution:
    def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
        m = len(matrix)
        n = len(matrix[0])
        
        # The transposed matrix has dimensions n x m.
        # For each column j, collect the corresponding row elements from all rows.
        return [[matrix[i][j] for i in range(m)] for j in range(n)]