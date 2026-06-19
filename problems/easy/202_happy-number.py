class Solution:
    def isHappy(self, n: int) -> bool:
        # Helper function to compute sum of squares of digits
        def get_next(num):
            total = 0
            while num > 0:
                digit = num % 10
                total += digit * digit
                num //= 10
            return total
        
        # Use a set to detect cycles
        # If we see the same number twice, we're in a loop
        seen = set()
        
        # Keep transforming n until we reach 1 or detect a cycle
        while n != 1 and n not in seen:
            seen.add(n)
            n = get_next(n)
        
        # If we exited because n == 1, it's happy; otherwise we found a cycle
        return n == 1