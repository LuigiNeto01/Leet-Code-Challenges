from typing import List

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # dp[x] = number of combinations to make amount x using processed coins
        dp = [0] * (amount + 1)
        dp[0] = 1  # There is exactly one way to make amount 0: use no coins

        # Process each coin type once to avoid counting different orders separately
        for coin in coins:
            # Forward iteration lets this same coin be used multiple times (unbounded)
            for x in range(coin, amount + 1):
                dp[x] += dp[x - coin]

        return dp[amount]