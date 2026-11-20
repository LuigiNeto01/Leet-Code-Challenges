from __future__ import annotations
from collections import defaultdict
from typing import List

class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        rows, cols = len(matrix), len(matrix[0])
        # Precompute prefix sums for each row: prefix[r][c] = sum of row r from col 0 to c (inclusive)
        row_prefix = [[0] * cols for _ in range(rows)]
        for r in range(rows):
            s = 0
            for c in range(cols):
                s += matrix[r][c]
                row_prefix[r][c] = s

        ans = 0
        # Iterate over all pairs of left and right column boundaries
        for left in range(cols):
            for right in range(left, cols):
                # For this fixed column pair, maintain a running sum of the "compressed" rows.
                # cur_sum is the sum of the submatrix spanning rows 0..r and columns left..right.
                cur_sum = 0
                # Use a hashmap to count occurrences of previous prefix sums.
                # Start with prefix sum 0 seen once (empty submatrix).
                prefix_count = defaultdict(int)
                prefix_count[0] = 1
                # Traverse rows from top to bottom
                for r in range(rows):
                    # Add the sum of row r from left to right using row_prefix
                    row_sum = row_prefix[r][right] - (row_prefix[r][left - 1] if left > 0 else 0)
                    cur_sum += row_sum
                    # Check how many previous prefix sums give a difference equal to target
                    # If cur_sum - target existed before, those submatrices (rows after that prefix up to r)
                    # have sum = target.
                    ans += prefix_count[cur_sum - target]
                    # Record the current prefix sum for future rows
                    prefix_count[cur_sum] += 1

        return ans