class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # Powers of 3 must be positive
        if n <= 0:
            return False
        
        # Keep dividing by 3 while divisible
        while n % 3 == 0:
            n //= 3
        
        # If n is a power of 3, we should end up with 1
        return n == 1