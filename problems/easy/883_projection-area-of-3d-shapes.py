from __future__ import annotations

class Solution:
    def projectionArea(self, grid: list[list[int]]) -> int:
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])

        # XY projection: each cell with at least one cube contributes 1
        xy_area = 0
        # ZX projection: for each row, the maximum height contributes
        zx_area = 0
        # YZ projection: for each column, the maximum height contributes
        yz_area = 0

        # Compute XY and ZX areas by iterating rows
        for i in range(m):
            row_max = 0
            for j in range(n):
                h = grid[i][j]
                if h > 0:
                    xy_area += 1
                if h > row_max:
                    row_max = h
            zx_area += row_max

        # Compute YZ area by iterating columns
        for j in range(n):
            col_max = 0
            for i in range(m):
                h = grid[i][j]
                if h > col_max:
                    col_max = h
            yz_area += col_max

        return xy_area + yz_area + zx_area