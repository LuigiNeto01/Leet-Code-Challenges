from collections import deque
from typing import List

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        # Initialize result with a large sentinel value (unvisited)
        dist = [[float('inf')] * n for _ in range(m)]
        q = deque()
        
        # First pass: enqueue all zero cells, set their distance to 0
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    dist[i][j] = 0
                    q.append((i, j))
        
        # BFS from all zeros simultaneously (multi-source BFS)
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while q:
            x, y = q.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                # If neighbor is within bounds and not yet visited (still INF)
                if 0 <= nx < m and 0 <= ny < n and dist[nx][ny] == float('inf'):
                    # Distance to this neighbor is one more than current cell
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))
        
        return dist