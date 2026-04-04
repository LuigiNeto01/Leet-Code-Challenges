class Solution:
    def bulbSwitch(self, n: int) -> int:
        # A bulb is toggled once for every divisor of its position.
        # Most numbers have divisors in pairs, giving an even toggle count.
        # Only perfect squares have an odd number of divisors,
        # because one divisor pair collapses into the same number.
        # So the answer is simply how many perfect squares are <= n.

        # Compute floor(sqrt(n)) without floating-point precision concerns.
        left, right = 0, n
        while left <= right:
            mid = (left + right) // 2
            square = mid * mid

            if square <= n:
                left = mid + 1
            else:
                right = mid - 1

        # `right` ends as the largest integer whose square is <= n.
        return right