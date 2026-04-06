from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        # dp[c] stores the minimum path sum to reach current row, column c
        dp = [0] * cols

        # Initialize the first cell
        dp[0] = grid[0][0]

        # First row can only be reached from the left
        for c in range(1, cols):
            dp[c] = dp[c - 1] + grid[0][c]

        # Process each remaining row
        for r in range(1, rows):
            # First column can only be reached from above
            dp[0] += grid[r][0]

            for c in range(1, cols):
                # Choose the cheaper way to reach this cell:
                # from above (old dp[c]) or from left (new dp[c - 1])
                dp[c] = min(dp[c], dp[c - 1]) + grid[r][c]

        # Bottom-right entry holds the best total cost
        return dp[-1]