class Solution:
    def countDigitOne(self, n: int) -> int:
        # Count total number of 1s in all numbers from 0 to n
        # Use digit DP approach: examine each digit position
        
        if n <= 0:
            return 0
        
        count = 0
        factor = 1  # Current digit position (1, 10, 100, ...)
        
        # Process each digit position from right to left
        while factor <= n:
            # Divide n into three parts relative to current position:
            # higher: digits to the left of current position
            # cur: current digit
            # lower: digits to the right of current position
            
            higher = n // (factor * 10)
            cur = (n // factor) % 10
            lower = n % factor
            
            # Count 1s at current digit position
            # Case 1: current digit is 0
            #   1s come only from higher digits cycling (0 to higher-1)
            #   count = higher * factor
            # Case 2: current digit is 1
            #   1s from higher cycling (0 to higher-1): higher * factor
            #   Plus 1s from current cycle (from n//factor*factor to n): lower + 1
            #   count = higher * factor + lower + 1
            # Case 3: current digit > 1
            #   1s from higher cycling (0 to higher): (higher + 1) * factor
            
            if cur == 0:
                count += higher * factor
            elif cur == 1:
                count += higher * factor + lower + 1
            else:
                count += (higher + 1) * factor
            
            factor *= 10
        
        return count