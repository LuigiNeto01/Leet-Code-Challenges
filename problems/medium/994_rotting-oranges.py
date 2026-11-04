from __future__ import annotations
from collections import deque

class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        fresh = 0
        queue = deque()

        # Collect all initially rotten oranges and count fresh ones.
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        # No fresh oranges means zero minutes are needed.
        if fresh == 0:
            return 0

        minutes = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # BFS level by level: each level represents one minute.
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        queue.append((nr, nc))
            minutes += 1

        # If any fresh oranges remain, they were never reachable.
        return minutes - 1 if fresh == 0 else -1