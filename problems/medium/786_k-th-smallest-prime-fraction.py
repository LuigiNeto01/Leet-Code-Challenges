from typing import List

class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)

        def count_leq(x: float):
            total = 0
            best_num = best_den = -1
            best_val = -1.0
            j = 0

            for i in range(n - 1):
                num = arr[i]
                if j < i + 1:
                    j = i + 1

                # For fixed numerator, fractions decrease as denominator grows.
                # Move denominator until num / arr[j] <= x.
                # Multiplication avoids division by a very small x.
                while j < n and arr[j] * x < num:
                    j += 1

                total += n - j

                # The first valid denominator gives the largest fraction <= x
                # for this numerator.
                if j < n:
                    val = num / arr[j]
                    if val > best_val:
                        best_val = val
                        best_num = num
                        best_den = arr[j]

            return total, best_num, best_den

        lo, hi = 0.0, 1.0
        ans = [arr[0], arr[-1]]

        # 60 bisection steps are enough because the smallest possible gap
        # between two distinct fractions here is far larger than 2^-60.
        for _ in range(60):
            mid = (lo + hi) / 2.0
            cnt, num, den = count_leq(mid)

            if cnt >= k:
                hi = mid
                ans = [num, den]
            else:
                lo = mid

        return ans