class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Handle negative exponent by converting to positive and taking reciprocal
        if n < 0:
            x = 1 / x
            n = -n
        
        # Use fast exponentiation (binary exponentiation)
        # Key idea: x^n = (x^2)^(n/2) if n is even
        #           x^n = x * x^(n-1) if n is odd
        result = 1.0
        current_product = x
        
        # Process each bit of n from right to left
        while n > 0:
            # If current bit is 1, multiply result by current_product
            if n % 2 == 1:
                result *= current_product
            # Square the current_product for next bit position
            current_product *= current_product
            # Move to next bit
            n //= 2
        
        return result