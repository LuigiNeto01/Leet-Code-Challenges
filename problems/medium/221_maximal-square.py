from typing import List

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # handle trivial empty-matrix cases immediately
        if not matrix or not matrix[0]:
            return 0

        m = len(matrix)      # number of rows
        n = len(matrix[0])   # number of columns

        # dp[i][j] will store the side length of the largest square
        # whose bottom-right corner is at cell (i, j)
        # initialize with zeros
        dp = [[0] * n for _ in range(m)]

        max_side = 0  # track the largest side length seen

        # iterate through every cell to compute dp values
        for i in range(m):
            for j in range(n):
                # only cells with '1' can contribute to a square
                if matrix[i][j] == '1':
                    if i == 0 or j == 0:
                        # first row or first column: only 1x1 squares possible
                        dp[i][j] = 1
                    else:
                        # cell can extend a square from top, left, and top-left
                        # take the minimum of these three to ensure all sides can form a square
                        dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
                    # update global maximum side length
                    if dp[i][j] > max_side:
                        max_side = dp[i][j]
                else:
                    # cell is '0' -> cannot be part of a square of '1's
                    dp[i][j] = 0

        # area is side length squared
        return max_side * max_side