from __future__ import annotations

class Solution:
    def uniquePathsIII(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        # Find start (1) and end (2), and count all non-obstacle cells
        start_i = start_j = end_i = end_j = -1
        total_empty = 0  # includes start and end cells
        for i in range(m):
            for j in range(n):
                if grid[i][j] != -1:
                    total_empty += 1
                if grid[i][j] == 1:
                    start_i, start_j = i, j
                elif grid[i][j] == 2:
                    end_i, end_j = i, j

        # recursion uses backtracking: mark visited by setting cell to -1
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        ans = 0  # will be mutated inside closure

        def dfs(x: int, y: int, visited: int) -> None:
            nonlocal ans
            # Base: if we reached the end cell
            if x == end_i and y == end_j:
                # Path is valid only if we have visited all non-obstacle cells
                if visited == total_empty:
                    ans += 1
                return

            # Mark current cell as visited (temporarily obstacle)
            grid[x][y] = -1

            # Explore neighbours
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] != -1:
                    dfs(nx, ny, visited + 1)

            # Backtrack: restore original cell value
            # We don't know original value (0 or 2 because start is already used)
            # Only start cell had 1, but we never backtrack from start (called once).
            # For non-start cells, original can be 0 or 2.
            # Restoring to 0 is safe because end cell is also 0 here (we never step on end before base case)
            # But we must restore correctly: if we are at end cell, we wouldn't backtrack (base case returned).
            # So grid[x][y] must have been 0 originally (since start is only visited once).
            grid[x][y] = 0

        # Start DFS from start cell, with visited count 1 (the start cell)
        # The start cell is already counted, so visited=1.
        dfs(start_i, start_j, 1)

        return ans