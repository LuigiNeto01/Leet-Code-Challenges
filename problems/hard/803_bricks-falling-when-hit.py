from __future__ import annotations

class Solution:
    def hitBricks(self, grid: list[list[int]], hits: list[list[int]]) -> list[int]:
        m, n = len(grid), len(grid[0])
        top = m * n

        # Remove all hit bricks once. Empty hit cells become negative,
        # so they can be ignored when restoring bricks in reverse.
        for r, c in hits:
            grid[r][c] -= 1

        parent = list(range(top + 1))
        size = [1] * (top + 1)
        size[top] = 0

        def find(x: int) -> int:
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a: int, b: int) -> None:
            ra, rb = find(a), find(b)
            if ra == rb:
                return
            if size[ra] < size[rb]:
                ra, rb = rb, ra
            parent[rb] = ra
            size[ra] += size[rb]

        def idx(r: int, c: int) -> int:
            return r * n + c

        # Build DSU for the state after all hit bricks have been erased.
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    node = idx(r, c)
                    if r == 0:
                        union(node, top)
                    if c + 1 < n and grid[r][c + 1] == 1:
                        union(node, idx(r, c + 1))
                    if r + 1 < m and grid[r + 1][c] == 1:
                        union(node, idx(r + 1, c))

        ans = [0] * len(hits)
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # Restore hits backwards.
        for i in range(len(hits) - 1, -1, -1):
            r, c = hits[i]

            before = size[find(top)]
            grid[r][c] += 1

            # This hit was on an originally empty cell, or it has already
            # been restored by an earlier reverse step.
            if grid[r][c] != 1:
                continue

            node = idx(r, c)

            if r == 0:
                union(node, top)

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                    union(node, idx(nr, nc))

            after = size[find(top)]
            ans[i] = max(0, after - before - 1)

        return ans