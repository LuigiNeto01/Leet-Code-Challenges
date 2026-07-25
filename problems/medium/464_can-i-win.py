class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        # Edge case: if desired total is 0 or negative, first player wins immediately
        if desiredTotal <= 0:
            return True
        
        # Edge case: if sum of all available numbers is less than desired total, nobody can win
        total_sum = maxChoosableInteger * (maxChoosableInteger + 1) // 2
        if total_sum < desiredTotal:
            return False
        
        # Edge case: if the maximum number alone meets the desired total, first player wins
        if maxChoosableInteger >= desiredTotal:
            return True
        
        # Use memoization to store game states
        # Key: bitmask representing which numbers have been used
        # Value: True if current player can win from this state, False otherwise
        memo = {}
        
        def canWin(used_mask, remaining_total):
            # If remaining total is 0 or less, the previous player already won
            if remaining_total <= 0:
                return False
            
            # Check if we've already computed this state
            if used_mask in memo:
                return memo[used_mask]
            
            # Try each available number
            for i in range(1, maxChoosableInteger + 1):
                # Check if number i is still available (bit at position i-1 is 0)
                if (used_mask >> (i - 1)) & 1 == 0:
                    # If choosing this number wins immediately, or
                    # if choosing this number puts opponent in a losing position
                    new_mask = used_mask | (1 << (i - 1))
                    
                    # Current player wins if:
                    # 1) This move reaches the desired total, OR
                    # 2) After this move, opponent cannot win
                    if i >= remaining_total or not canWin(new_mask, remaining_total - i):
                        memo[used_mask] = True
                        return True
            
            # If no winning move found, current player loses
            memo[used_mask] = False
            return False
        
        # Start with no numbers used (mask = 0) and full desired total
        return canWin(0, desiredTotal)