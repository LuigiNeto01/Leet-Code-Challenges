from __future__ import annotations

class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        # Use binary search on the value range [1, m*n]
        # For each mid value, count how many numbers in the multiplication table are <= mid.
        # If count >= k, the answer is <= mid; else > mid.
        
        # Helper to count numbers <= x in the multiplication table
        def count_leq(x: int) -> int:
            total = 0
            # For each row i (1-indexed), the numbers are i, 2i, 3i, ..., n*i
            # The number of elements <= x in row i is min(x // i, n)
            # To avoid O(m) which may be large when m ~ 3e4, we can iterate over rows,
            # but m and n are up to 3e4, so O(m) per check is fine (log(1e9) * 3e4 ~ 1e6).
            for i in range(1, m + 1):
                # Each row contributes at most n elements
                total += min(x // i, n)
                # Early exit if total already >= k (no need to count further)
                if total >= k:
                    break
            return total
        
        # Binary search range
        low, high = 1, m * n
        while low < high:
            mid = (low + high) // 2
            if count_leq(mid) >= k:
                high = mid  # mid could be the answer, shrink high
            else:
                low = mid + 1  # count < k, need larger value
        return low