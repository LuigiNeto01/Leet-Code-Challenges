class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        # Grid dimensions
        m = len(grid)
        n = len(grid[0]) if m > 0 else 0

        max_area = 0

        # Iterate over every cell in the grid
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    # Start a DFS (iterative) to count the island area
                    stack = [(i, j)]
                    grid[i][j] = 0  # mark visited immediately
                    current_area = 0

                    while stack:
                        r, c = stack.pop()
                        current_area += 1

                        # Explore 4-directionally adjacent cells
                        for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                            nr, nc = r + dr, c + dc
                            if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                                grid[nr][nc] = 0  # mark visited to avoid revisiting
                                stack.append((nr, nc))

                    # Update the maximum island area found so far
                    max_area = max(max_area, current_area)

        return max_area