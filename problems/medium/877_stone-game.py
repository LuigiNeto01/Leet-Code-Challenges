class Solution:
    def stoneGame(self, piles: list[int]) -> bool:
        n = len(piles)
        # dp[i][j] = maximum net advantage (Alice - Bob) for piles[i..j]
        dp = [[0] * n for _ in range(n)]
        # Base case: single pile – the player whose turn it is takes it
        for i in range(n):
            dp[i][i] = piles[i]
        # Fill table for increasing lengths
        for length in range(2, n + 1):
            for i in range(0, n - length + 1):
                j = i + length - 1
                # Alice picks left pile: her gain is piles[i], then Bob's optimal advantage from rest is dp[i+1][j]
                left = piles[i] - dp[i+1][j]
                # Alice picks right pile: similar
                right = piles[j] - dp[i][j-1]
                dp[i][j] = max(left, right)
        # If Alice's net advantage > 0, she wins
        return dp[0][n-1] > 0