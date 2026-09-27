from __future__ import annotations
from typing import List

class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        # Create grid: 1 for valid cells, 0 for mines
        grid = [[1] * n for _ in range(n)]
        for x, y in mines:
            grid[x][y] = 0

        # DP matrices for consecutive 1s in four directions (inclusive of cell)
        left = [[0] * n for _ in range(n)]
        right = [[0] * n for _ in range(n)]
        up = [[0] * n for _ in range(n)]
        down = [[0] * n for _ in range(n)]

        # Compute left and up in a single pass; right and down in reverse passes
        for i in range(n):
            row_left = 0
            col_up = 0
            for j in range(n):
                # Left direction: consecutive 1s ending at (i, j) from left
                if grid[i][j] == 1:
                    row_left += 1
                else:
                    row_left = 0
                left[i][j] = row_left

                # Up direction: consecutive 1s ending at (j, i) from top (transposed)
                if grid[j][i] == 1:
                    col_up += 1
                else:
                    col_up = 0
                up[j][i] = col_up

        # Compute right and down by scanning in reverse
        for i in range(n):
            row_right = 0
            col_down = 0
            for j in range(n - 1, -1, -1):
                # Right direction: consecutive 1s starting at (i, j) going right
                if grid[i][j] == 1:
                    row_right += 1
                else:
                    row_right = 0
                right[i][j] = row_right

                # Down direction: consecutive 1s starting at (j, i) going down (transposed)
                if grid[j][i] == 1:
                    col_down += 1
                else:
                    col_down = 0
                down[j][i] = col_down

        # Find the maximum order k = min(left, right, up, down) for each cell
        max_order = 0
        for i in range(n):
            for j in range(n):
                # Order k: the smallest inclusive arm length gives the largest plus sign center at (i,j)
                k = min(left[i][j], right[i][j], up[i][j], down[i][j])
                max_order = max(max_order, k)

        return max_order