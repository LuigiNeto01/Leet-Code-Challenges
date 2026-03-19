class Solution:
    def smallestGoodBase(self, n: str) -> str:
        num = int(n)

        # If representation has m+1 ones, then:
        # num = 1 + k + k^2 + ... + k^m
        # For the smallest base, we want the longest possible all-ones length.
        # So try larger m first.
        max_m = num.bit_length() - 1  # because 2^m <= num for base at least 2

        for m in range(max_m, 1, -1):
            # For fixed m, k is around num^(1/m).
            # Use integer binary search to avoid floating-point precision issues.
            left, right = 2, int(num ** (1.0 / m)) + 1

            while left <= right:
                mid = (left + right) // 2

                # Compute 1 + mid + mid^2 + ... + mid^m carefully.
                # Stop early if the sum already exceeds num.
                total = 1
                curr = 1
                for _ in range(m):
                    curr *= mid
                    total += curr
                    if total > num:
                        break

                if total == num:
                    return str(mid)
                if total < num:
                    left = mid + 1
                else:
                    right = mid - 1

        # Fallback is always num - 1, because num in base (num - 1) is "11".
        return str(num - 1)