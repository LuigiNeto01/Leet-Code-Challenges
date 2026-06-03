from typing import List

class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m, n = len(dungeon), len(dungeon[0])
        
        # dp[i][j] = minimum HP needed when entering cell (i, j) to reach the end
        # We work backwards from bottom-right to top-left
        dp = [[float('inf')] * n for _ in range(m)]
        
        # Bottom-right corner: we need enough HP to survive this room and have at least 1 HP
        # If dungeon[m-1][n-1] = -5, we need 6 HP to enter (6 - 5 = 1)
        # If dungeon[m-1][n-1] = 10, we need 1 HP to enter (1 + 10 = 11, which is fine)
        dp[m-1][n-1] = max(1, 1 - dungeon[m-1][n-1])
        
        # Fill last column (can only move down, so no choice)
        for i in range(m-2, -1, -1):
            # HP needed at (i, n-1) = HP needed at (i+1, n-1) - dungeon[i][n-1]
            # But must be at least 1
            dp[i][n-1] = max(1, dp[i+1][n-1] - dungeon[i][n-1])
        
        # Fill last row (can only move right, so no choice)
        for j in range(n-2, -1, -1):
            dp[m-1][j] = max(1, dp[m-1][j+1] - dungeon[m-1][j])
        
        # Fill the rest of the table
        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                # We can go right or down; choose the path that requires less HP
                # min_hp_needed_after = minimum HP we need after leaving this cell
                min_hp_needed_after = min(dp[i+1][j], dp[i][j+1])
                
                # HP needed to enter this cell = min_hp_needed_after - dungeon[i][j]
                # But must be at least 1 (can't have 0 or negative HP)
                dp[i][j] = max(1, min_hp_needed_after - dungeon[i][j])
        
        return dp[0][0]