from __future__ import annotations

class Solution:
    def matrixScore(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])

        # The first column has the highest bit value, so make it 1 in every row.
        # Flip each row whose leading bit is currently 0.
        for r in range(m):
            if grid[r][0] == 0:
                for c in range(n):
                    grid[r][c] ^= 1

        # For each remaining column, flipping the column is good if it creates
        # more 1s than 0s in that column.
        for c in range(1, n):
            ones = sum(grid[r][c] for r in range(m))
            if ones * 2 < m:  # more zeros than ones
                for r in range(m):
                    grid[r][c] ^= 1

        # Convert each row to its binary value and sum the scores.
        ans = 0
        for row in grid:
            value = 0
            for bit in row:
                value = (value << 1) | bit
            ans += value

        return ans