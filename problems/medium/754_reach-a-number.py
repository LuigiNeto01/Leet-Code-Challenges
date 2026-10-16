import math

class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)

        # Approximate the smallest n whose triangular sum can reach target.
        n = math.isqrt(2 * target)

        # Increase n until the total all-right distance is large enough.
        while n * (n + 1) // 2 < target:
            n += 1

        # Flipping a move changes the final position by twice that move's length.
        # So total - target must be even. Because 1..n can form any subset sum,
        # an even difference is also sufficient.
        while (n * (n + 1) // 2 - target) & 1:
            n += 1

        return n