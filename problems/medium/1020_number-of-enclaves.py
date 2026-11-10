from __future__ import annotations
from typing import List
from collections import deque

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        queue = deque()
        
        for j in range(n):
            if grid[0][j] == 1:
                queue.append((0, j))
                grid[0][j] = 0
            if grid[m-1][j] == 1:
                queue.append((m-1, j))
                grid[m-1][j] = 0
        
        for i in range(1, m-1):
            if grid[i][0] == 1:
                queue.append((i, 0))
                grid[i][0] = 0
            if grid[i][n-1] == 1:
                queue.append((i, n-1))
                grid[i][n-1] = 0
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                    queue.append((nr, nc))
                    grid[nr][nc] = 0
        
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    count += 1
        
        return count