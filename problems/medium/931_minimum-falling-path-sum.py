class Solution:
    def minFallingPathSum(self, matrix: list[list[int]]) -> int:
        n = len(matrix)
        # dp: minimum sum to reach each column of the current row
        dp = matrix[0]                     # start with first row

        # process remaining rows
        for i in range(1, n):
            new_dp = [0] * n
            for j in range(n):
                # best from previous row: directly above, left, or right
                best = dp[j]
                if j > 0:
                    best = min(best, dp[j - 1])
                if j < n - 1:
                    best = min(best, dp[j + 1])
                new_dp[j] = matrix[i][j] + best
            dp = new_dp

        # minimum over last row
        return min(dp)