class Solution:
    def maxProfit(self, prices: list[int], fee: int) -> int:
        # State variables:
        # cash: maximum profit when we have no stock in hand
        # hold: maximum profit when we own one share
        cash = 0
        hold = -prices[0]  # buy on day 0 (profit is negative cost)

        for i in range(1, len(prices)):
            # Option 1: do nothing, or sell the stock we hold (pay fee)
            cash = max(cash, hold + prices[i] - fee)
            # Option 2: do nothing, or buy a stock using current cash
            hold = max(hold, cash - prices[i])

        # Maximum profit is always with no stock (cash state)
        return cash