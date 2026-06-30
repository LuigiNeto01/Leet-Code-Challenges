from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Track the minimum price seen so far (best buy price)
        min_price = float('inf')
        # Track the maximum profit achievable
        max_profit = 0
        
        # Iterate through each price
        for price in prices:
            # Update minimum price if current price is lower
            # This represents the best day to buy so far
            if price < min_price:
                min_price = price
            # Calculate profit if we sell at current price
            # after buying at min_price
            else:
                profit = price - min_price
                # Update max_profit if this transaction is better
                max_profit = max(max_profit, profit)
        
        return max_profit