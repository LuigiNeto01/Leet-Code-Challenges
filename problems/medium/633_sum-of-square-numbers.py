from math import isqrt

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        """
        Checks if there exist integers a, b such that a^2 + b^2 = c.
        Iterates a from 0 to sqrt(c) and checks if (c - a^2) is a perfect square.
        """
        # Iterate possible values of a (a^2 <= c)
        limit = isqrt(c)  # maximum a such that a^2 <= c
        for a in range(limit + 1):
            b_sq = c - a * a          # remaining part to be a square
            b = isqrt(b_sq)           # integer sqrt
            if b * b == b_sq:         # check if it is a perfect square
                return True
        return False