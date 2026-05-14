from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        # State tracking: we maintain the best profit after each action
        # buy1: max profit after first buy (will be negative initially)
        # sell1: max profit after first sell
        # buy2: max profit after second buy
        # sell2: max profit after second sell
        
        buy1 = float('-inf')  # Haven't bought yet, so impossible state initially
        sell1 = 0  # No transaction yet means 0 profit
        buy2 = float('-inf')  # Haven't done second buy yet
        sell2 = 0  # No second transaction yet means 0 profit
        
        for price in prices:
            # For first buy: either we already bought, or we buy now
            # Buying means spending money, so profit becomes negative
            buy1 = max(buy1, -price)
            
            # For first sell: either we already sold, or we sell now
            # Selling means we get the price, added to our buy1 state
            sell1 = max(sell1, buy1 + price)
            
            # For second buy: either we already bought second time, or we buy now
            # We can only do this after first sell, so we start from sell1 state
            buy2 = max(buy2, sell1 - price)
            
            # For second sell: either we already sold second time, or we sell now
            # This gives us the final profit after at most 2 transactions
            sell2 = max(sell2, buy2 + price)
        
        # Maximum profit after at most 2 transactions
        # sell2 represents the best we can do with up to 2 transactions
        return sell2