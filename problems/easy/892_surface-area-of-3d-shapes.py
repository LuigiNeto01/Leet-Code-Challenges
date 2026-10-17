from __future__ import annotations

class Solution:
    def surfaceArea(self, grid: list[list[int]]) -> int:
        n = len(grid)
        total_area = 0

        for i in range(n):
            for j in range(n):
                h = grid[i][j]
                if h == 0:
                    continue  # no cubes, nothing to add

                # top and bottom faces (each cube has both)
                total_area += 2

                # check four neighbors to count exposed side faces
                # up
                if i == 0:
                    total_area += h  # entire side is exposed
                else:
                    total_area += max(0, h - grid[i - 1][j])

                # down
                if i == n - 1:
                    total_area += h
                else:
                    total_area += max(0, h - grid[i + 1][j])

                # left
                if j == 0:
                    total_area += h
                else:
                    total_area += max(0, h - grid[i][j - 1])

                # right
                if j == n - 1:
                    total_area += h
                else:
                    total_area += max(0, h - grid[i][j + 1])

        return total_area