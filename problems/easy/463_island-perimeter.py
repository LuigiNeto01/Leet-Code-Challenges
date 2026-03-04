from __future__ import annotations
from typing import List

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # Handle empty grid edge case
        if not grid or not grid[0]:
            return 0

        rows, cols = len(grid), len(grid[0])
        perimeter = 0

        # Iterate each cell; each land cell contributes 4 edges initially.
        # If a neighboring cell to the up or left is also land, the shared edge
        # is counted twice (once for each cell). Subtract 2 for each shared edge.
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    perimeter += 4  # each land cell starts with 4 sides

                    # Subtract shared edge with the upper cell if it's land
                    if i > 0 and grid[i - 1][j] == 1:
                        perimeter -= 2  # shared edge counted for both cells

                    # Subtract shared edge with the left cell if it's land
                    if j > 0 and grid[i][j - 1] == 1:
                        perimeter -= 2  # another shared edge

        return perimeter