class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Dynamic programming approach
        # dp[i][j] = number of unique paths to reach cell (i, j)
        # We can reach (i, j) from (i-1, j) or (i, j-1)
        # So dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        # Create a 2D DP table
        dp = [[0] * n for _ in range(m)]
        
        # Base case: there's only one way to reach any cell in the first row
        # (keep moving right)
        for j in range(n):
            dp[0][j] = 1
        
        # Base case: there's only one way to reach any cell in the first column
        # (keep moving down)
        for i in range(m):
            dp[i][0] = 1
        
        # Fill the DP table
        # For each cell, sum the ways from the cell above and the cell to the left
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        # The answer is in the bottom-right corner
        return dp[m-1][n-1]