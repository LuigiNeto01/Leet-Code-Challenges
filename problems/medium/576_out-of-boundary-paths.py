class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        MOD = 10**9 + 7
        # If no moves allowed, cannot leave the grid
        if maxMove == 0:
            return 0

        # dp[i][j] = number of ways to be at (i,j) after current number of moves
        dp = [[0] * n for _ in range(m)]
        dp[startRow][startColumn] = 1
        total = 0

        # Directions: up, down, left, right
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for step in range(1, maxMove + 1):
            new_dp = [[0] * n for _ in range(m)]
            for i in range(m):
                for j in range(n):
                    if dp[i][j] == 0:
                        continue
                    ways = dp[i][j]
                    for di, dj in dirs:
                        ni, nj = i + di, j + dj
                        if 0 <= ni < m and 0 <= nj < n:
                            # Inside grid: accumulate ways for next step
                            new_dp[ni][nj] = (new_dp[ni][nj] + ways) % MOD
                        else:
                            # Out of boundary: add to total paths
                            total = (total + ways) % MOD
            dp = new_dp

        return total % MOD