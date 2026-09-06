from typing import List

class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        # If no operations, every cell remains zero (the maximum value).
        # All m*n cells have that value.
        if not ops:
            return m * n

        # Find the minimum a_i and b_i across all operations.
        # These define the common submatrix that every operation increments.
        min_a = min(op[0] for op in ops)
        min_b = min(op[1] for op in ops)

        # The number of cells receiving all increments is min_a * min_b.
        # But cannot exceed m or n, though min_a <= m and min_b <= n by constraints.
        return min_a * min_b