from __future__ import annotations
from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Edge case: no amount -> no coins needed
        if amount == 0:
            return 0

        # dp[a] will hold the minimum number of coins to make amount 'a'
        # Initialize with a value larger than any possible answer
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        # Build up solutions for all amounts from 1 to 'amount'
        for a in range(1, amount + 1):
            for c in coins:
                if c <= a:
                    # If we can use coin 'c', update dp[a] with a smaller count
                    dp[a] = min(dp[a], dp[a - c] + 1)

        # If dp[amount] is still unchanged, it's impossible to form the target
        return dp[amount] if dp[amount] <= amount else -1