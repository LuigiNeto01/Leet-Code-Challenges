from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Key insight: We can make profit on every upward price movement
        # Since we can buy and sell on the same day (and multiple times),
        # we can capture every price increase by buying before and selling after
        
        # Edge case: empty or single element array
        if len(prices) <= 1:
            return 0
        
        total_profit = 0
        
        # Iterate through consecutive days
        for i in range(1, len(prices)):
            # If price increased from yesterday, capture that profit
            # This is equivalent to buying yesterday and selling today
            if prices[i] > prices[i - 1]:
                total_profit += prices[i] - prices[i - 1]
        
        return total_profit