class Solution:
    def preimageSizeFZF(self, k: int) -> int:
        # Number of trailing zeros of x! is the exponent of 5 in x!.
        def zeros(x: int) -> int:
            cnt = 0
            while x:
                x //= 5
                cnt += x
            return cnt

        # zeros(5*k) = k + zeros(k) >= k,
        # so the first x with zeros(x) >= k is at most 5*k.
        lo, hi = 0, 5 * k + 1

        # Binary search for the first x where zeros(x) >= k.
        while lo < hi:
            mid = (lo + hi) // 2
            if zeros(mid) >= k:
                hi = mid
            else:
                lo = mid + 1

        # A k-value is either skipped, or appears for exactly 5 consecutive x's.
        return 5 if zeros(lo) == k else 0