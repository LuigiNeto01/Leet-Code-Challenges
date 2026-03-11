class Solution:
    def integerBreak(self, n: int) -> int:
        # Small values are special because we must split into at least two parts.
        # For n <= 3, the best valid answer is n - 1.
        if n <= 3:
            return n - 1

        # Greedy fact:
        # Breaking into as many 3s as possible gives the best product,
        # except when a remainder 1 appears, because 3 + 1 is worse than 2 + 2.
        product = 1

        # Keep taking 3 while the remaining part is large enough.
        # We stop at 4 because 4 should stay as 2 * 2 instead of 3 * 1.
        while n > 4:
            product *= 3
            n -= 3

        # Multiply the final remaining piece (2, 3, or 4).
        return product * n