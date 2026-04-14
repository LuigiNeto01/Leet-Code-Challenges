from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Edge case: empty grid -> no islands
        if not grid or not grid[0]:
            return 0

        m, n = len(grid), len(grid[0])
        count = 0

        # 4-directional moves for adjacency (horizontal and vertical only)
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # We will mutate grid in-place to mark visited land as '0' (water).
        # This avoids extra memory for a visited set and is acceptable per problem.
        for i in range(m):
            for j in range(n):
                # When we find unvisited land, we've discovered a new island
                if grid[i][j] == '1':
                    count += 1
                    # Start iterative DFS (stack) to mark the whole island
                    grid[i][j] = '0'  # mark start cell visited immediately
                    stack = [(i, j)]
                    while stack:
                        x, y = stack.pop()
                        # Explore 4-neighbors
                        for dx, dy in directions:
                            nx, ny = x + dx, y + dy
                            # Check bounds and whether neighbor is unvisited land
                            if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == '1':
                                # Mark visited and push to stack to continue flood fill
                                grid[nx][ny] = '0'
                                stack.append((nx, ny))
                        # Loop continues until entire connected component is consumed
                    # After the DFS completes, the whole island is marked visited
        return count