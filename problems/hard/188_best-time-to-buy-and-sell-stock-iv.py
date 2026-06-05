from typing import List

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        
        # Edge case: empty or single price
        if n <= 1:
            return 0
        
        # If k >= n/2, we can do as many transactions as we want (unlimited case)
        # because each transaction needs at least 2 days (buy + sell)
        if k >= n // 2:
            profit = 0
            for i in range(1, n):
                # Sum up all positive price differences
                profit += max(0, prices[i] - prices[i-1])
            return profit
        
        # DP approach for limited transactions
        # dp[i][j] = max profit using at most i transactions up to day j
        # But to save space, we use buy and sell arrays
        # buy[i] = max profit after at most i transactions with stock in hand
        # sell[i] = max profit after at most i transactions with no stock in hand
        
        # Initialize buy and sell arrays for k transactions
        buy = [-float('inf')] * (k + 1)
        sell = [0] * (k + 1)
        
        # Process each day
        for price in prices:
            # Process transactions in reverse to avoid using updated values in same iteration
            for i in range(k, 0, -1):
                # sell[i] = max(previous sell[i], sell after buying and then selling today)
                # If we sell today, we must have bought before, so profit is buy[i] + price
                sell[i] = max(sell[i], buy[i] + price)
                
                # buy[i] = max(previous buy[i], buy today after completing i-1 transactions)
                # If we buy today, we use profit from i-1 completed transactions minus today's price
                buy[i] = max(buy[i], sell[i-1] - price)
        
        # Maximum profit with at most k transactions and no stock in hand
        return sell[k]