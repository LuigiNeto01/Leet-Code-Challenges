from collections import deque
from typing import List

class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        m, n = len(forest), len(forest[0])
        
        # If the starting cell is blocked, it's impossible to begin
        if forest[0][0] == 0:
            return -1
        
        # Collect all trees (cells with height > 1) and sort by height
        trees = []
        for i in range(m):
            for j in range(n):
                if forest[i][j] > 1:
                    trees.append((forest[i][j], i, j))
        trees.sort()  # sort by height (first element)
        
        # BFS to find shortest distance between two cells (walkable only on cells > 0)
        def bfs(sr: int, sc: int, tr: int, tc: int) -> int:
            if sr == tr and sc == tc:
                return 0
            visited = [[False] * n for _ in range(m)]
            q = deque()
            q.append((sr, sc, 0))
            visited[sr][sc] = True
            dirs = [(1,0), (-1,0), (0,1), (0,-1)]
            while q:
                r, c, dist = q.popleft()
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc] and forest[nr][nc] != 0:
                        if nr == tr and nc == tc:
                            return dist + 1
                        visited[nr][nc] = True
                        q.append((nr, nc, dist + 1))
            return -1  # target unreachable
        
        # Start from (0,0)
        cur_r, cur_c = 0, 0
        total_steps = 0
        
        # Process trees in increasing height order
        for _, target_r, target_c in trees:
            steps = bfs(cur_r, cur_c, target_r, target_c)
            if steps == -1:
                return -1
            total_steps += steps
            cur_r, cur_c = target_r, target_c
        
        return total_steps