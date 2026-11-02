from __future__ import annotations
from collections import deque

class Solution:
    def shortestBridge(self, grid: list[list[int]]) -> int:
        n = len(grid)
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        # Step 1: Find all cells of the first island using DFS
        first_island = []
        found = False
        for i in range(n):
            if found:
                break
            for j in range(n):
                if grid[i][j] == 1:
                    stack = [(i, j)]
                    grid[i][j] = 2
                    while stack:
                        x, y = stack.pop()
                        first_island.append((x, y))
                        for dx, dy in dirs:
                            nx, ny = x + dx, y + dy
                            if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 1:
                                grid[nx][ny] = 2
                                stack.append((nx, ny))
                    found = True
                    break
        
        # Step 2: BFS from first island to find shortest path to second island
        queue = deque(first_island)
        distance = 0
        
        while queue:
            level_size = len(queue)
            for _ in range(level_size):
                x, y = queue.popleft()
                for dx, dy in dirs:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < n:
                        if grid[nx][ny] == 1:
                            return distance
                        elif grid[nx][ny] == 0:
                            grid[nx][ny] = 2
                            queue.append((nx, ny))
            distance += 1
        
        return distance