from __future__ import annotations
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # If there are no prices, no profit can be made
        if not prices:
            return 0

        # State definitions:
        # dp0: max profit on current day when we do not hold stock and are not in cooldown
        # dp1: max profit on current day when we hold a stock
        # dp2: max profit on current day when we are in cooldown (not allowed to buy today)
        dp0 = 0
        dp1 = -prices[0]      # we buy on day 0 to hold stock
        dp2 = float('-inf')    # cooldown not possible on day 0

        # Iterate over days starting from day 1
        for price in prices[1:]:
            # If we are not holding and not cooldown today, we could come from:
            # - staying in not holding/not cooldown (dp0)
            # - finishing cooldown yesterday (dp2) today becomes free to buy again
            new_dp0 = max(dp0, dp2)

            # If we hold a stock today, we could:
            # - keep holding (dp1)
            # - buy today from not holding state yesterday (dp0 - price)
            new_dp1 = max(dp1, dp0 - price)

            # If we are in cooldown today, it means we sold stock today from holding yesterday
            new_dp2 = dp1 + price

            # Update states for next iteration
            dp0, dp1, dp2 = new_dp0, new_dp1, new_dp2

        # Final max profit can be in not holding state or cooldown state on the last day
        return max(dp0, dp2)