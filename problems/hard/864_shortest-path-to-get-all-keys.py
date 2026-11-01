from collections import deque
from typing import List

class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        m, n = len(grid), len(grid[0])
        start_r = start_c = -1
        all_keys_mask = 0

        # Locate start and compute bitmask of all keys in grid.
        for r in range(m):
            for c in range(n):
                ch = grid[r][c]
                if ch == '@':
                    start_r, start_c = r, c
                elif 'a' <= ch <= 'z':          # a key
                    all_keys_mask |= 1 << (ord(ch) - ord('a'))

        # BFS: (row, col, keys_mask)
        # visited[r][c][mask] = True
        visited = [[[False] * (1 << 6) for _ in range(n)] for _ in range(m)]
        q = deque()
        q.append((start_r, start_c, 0, 0))      # (r, c, mask, steps)
        visited[start_r][start_c][0] = True

        dirs = [(-1,0), (1,0), (0,-1), (0,1)]

        while q:
            r, c, mask, steps = q.popleft()
            # If we have all keys, return the number of steps taken.
            if mask == all_keys_mask:
                return steps

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if not (0 <= nr < m and 0 <= nc < n):
                    continue
                cell = grid[nr][nc]
                if cell == '#':
                    continue

                new_mask = mask
                if 'a' <= cell <= 'z':                # key
                    new_mask = mask | (1 << (ord(cell) - ord('a')))
                elif 'A' <= cell <= 'Z':              # lock – need key to pass
                    if not (mask >> (ord(cell) - ord('A')) & 1):
                        continue
                # '.' or '@' – no mask change

                if not visited[nr][nc][new_mask]:
                    visited[nr][nc][new_mask] = True
                    q.append((nr, nc, new_mask, steps + 1))

        # Exhausted BFS without collecting all keys
        return -1