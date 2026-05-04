class Solution:
    def trailingZeroes(self, n: int) -> int:
        # Trailing zeros are created by factors of 10, which come from 2*5
        # In n!, there are always more factors of 2 than 5, so we only need to count factors of 5
        
        # Count how many times 5 appears as a factor in n!
        # Numbers divisible by 5 contribute one factor of 5
        # Numbers divisible by 25 (5^2) contribute an additional factor of 5
        # Numbers divisible by 125 (5^3) contribute yet another factor of 5, etc.
        
        count = 0
        # Keep dividing n by 5 and add the quotient to count
        # This counts all multiples of 5, 25, 125, etc.
        while n > 0:
            n //= 5
            count += n
        
        return count