class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        MOD = 10**9 + 7

        # Least common multiple of a and b
        from math import gcd
        lcm = a // gcd(a, b) * b   # compute lcm without overflow

        # Helper function: count of magical numbers ≤ x
        def count_upto(x: int) -> int:
            # inclusion-exclusion
            return x // a + x // b - x // lcm

        # Binary search for the smallest x such that count_upto(x) >= n
        # Upper bound: the n-th multiple of max(a,b) is definitely enough
        lo = 0
        hi = n * max(a, b)   # inclusive upper bound

        while lo < hi:
            mid = (lo + hi) // 2
            if count_upto(mid) >= n:
                hi = mid
            else:
                lo = mid + 1

        # lo is the n-th magical number
        return lo % MOD