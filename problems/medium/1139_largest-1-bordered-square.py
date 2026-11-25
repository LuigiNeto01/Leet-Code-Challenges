from typing import List

class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        # right[i][j] = number of consecutive 1s to the right including (i,j)
        right = [[0] * n for _ in range(m)]
        # down[i][j] = number of consecutive 1s downward including (i,j)
        down = [[0] * n for _ in range(m)]

        # Precompute right consecutive 1s (traverse rows right-to-left)
        for i in range(m):
            for j in range(n - 1, -1, -1):
                if grid[i][j] == 1:
                    if j == n - 1:
                        right[i][j] = 1
                    else:
                        right[i][j] = right[i][j + 1] + 1
                else:
                    right[i][j] = 0

        # Precompute down consecutive 1s (traverse columns bottom-to-top)
        for i in range(m - 1, -1, -1):
            for j in range(n):
                if grid[i][j] == 1:
                    if i == m - 1:
                        down[i][j] = 1
                    else:
                        down[i][j] = down[i + 1][j] + 1
                else:
                    down[i][j] = 0

        max_side = 0
        # Try every possible top-left corner
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    continue
                # Maximum possible side length from this (i,j)
                possible_side = min(right[i][j], down[i][j])
                # Check decreasing side lengths (largest first to break early)
                for s in range(possible_side, 0, -1):
                    # Verify bottom edge: (i+s-1, j) must have >= s right
                    # Verify right edge: (i, j+s-1) must have >= s down
                    if (right[i + s - 1][j] >= s and
                        down[i][j + s - 1] >= s):
                        max_side = max(max_side, s)
                        break  # largest square from this corner found

        return max_side * max_side