class Solution:
    def isUgly(self, n: int) -> bool:
        # Ugly numbers must be positive
        if n <= 0:
            return False
        
        # Divide out all factors of 2, 3, and 5
        # If n becomes 1, it only had these prime factors
        for prime in [2, 3, 5]:
            while n % prime == 0:
                n //= prime
        
        # If n is 1, all prime factors were 2, 3, or 5
        return n == 1