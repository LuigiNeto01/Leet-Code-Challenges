class Solution:
    def getMoneyAmount(self, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        
        for length in range(2, n + 1):
            for i in range(1, n - length + 2):
                j = i + length - 1
                dp[i][j] = float('inf')
                
                for k in range(i, j + 1):
                    left_cost = dp[i][k - 1] if k > i else 0
                    right_cost = dp[k + 1][j] if k < j else 0
                    cost = k + max(left_cost, right_cost)
                    
                    dp[i][j] = min(dp[i][j], cost)
        
        return dp[1][n]