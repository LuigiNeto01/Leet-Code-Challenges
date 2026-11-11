class Solution:
    def baseNeg2(self, n: int) -> str:
        # Handle zero directly
        if n == 0:
            return "0"

        bits = []
        # Repeatedly compute remainders in base -2
        # The remainder must be 0 or 1 (since base is even)
        # Then adjust n using Euclidean division: q = -(n // 2)
        while n != 0:
            # Remainder when dividing by 2 gives us the next bit (0 or 1)
            # Works because we always want non-negative remainder
            remainder = n & 1  # same as n % 2 for non-negative n
            bits.append(str(remainder))
            # Update n: n = (n - remainder) // (-2)
            # But since remainder = n % 2, we can use: n = -(n // 2)
            n = -(n // 2)

        # The bits are collected from least significant to most significant
        return ''.join(reversed(bits))