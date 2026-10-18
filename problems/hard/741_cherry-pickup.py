from __future__ import annotations

class Solution:
    def cherryPickup(self, grid: list[list[int]]) -> int:
        n = len(grid)
        NEG = -10**9

        # Treat the return trip as a second trip from (0,0) to (n-1,n-1).
        # dp[r1][r2] = best cherries after the same number of steps, with
        # the two walkers currently at rows r1 and r2.
        dp = [[NEG] * n for _ in range(n)]
        dp[0][0] = grid[0][0]

        moves = 2 * n - 2

        for step in range(moves):
            ndp = [[NEG] * n for _ in range(n)]

            for r1 in range(n):
                c1 = step - r1
                if not (0 <= c1 < n) or grid[r1][c1] == -1:
                    continue

                for r2 in range(n):
                    c2 = step - r2
                    if not (0 <= c2 < n) or grid[r2][c2] == -1:
                        continue

                    cur = dp[r1][r2]
                    if cur == NEG:
                        continue

                    # Both walkers take one step: either down or right.
                    for dr1, dc1 in ((1, 0), (0, 1)):
                        nr1 = r1 + dr1
                        nc1 = c1 + dc1
                        if nr1 >= n or nc1 >= n or grid[nr1][nc1] == -1:
                            continue

                        for dr2, dc2 in ((1, 0), (0, 1)):
                            nr2 = r2 + dr2
                            nc2 = c2 + dc2
                            if nr2 >= n or nc2 >= n or grid[nr2][nc2] == -1:
                                continue

                            # Add cherries on the two new cells.
                            # If both walkers land on the same cell, count it once.
                            add = grid[nr1][nc1] + grid[nr2][nc2]
                            if nr1 == nr2 and nc1 == nc2:
                                add = grid[nr1][nc1]

                            if cur + add > ndp[nr1][nr2]:
                                ndp[nr1][nr2] = cur + add

            dp = ndp

        # If destination is unreachable, dp[n-1][n-1] stays NEG.
        return max(0, dp[n - 1][n - 1])