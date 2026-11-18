from __future__ import annotations
from typing import List

class Solution:
    def numMovesStonesII(self, stones: List[int]) -> List[int]:
        stones.sort()
        n = len(stones)

        total_gaps = stones[-1] - stones[0] + 1 - n
        gap_left = stones[1] - stones[0] - 1
        gap_right = stones[-1] - stones[-2] - 1
        max_moves = total_gaps - min(gap_left, gap_right)

        min_moves = n
        left = 0
        for right in range(n):
            while stones[right] - stones[left] + 1 > n:
                left += 1
            count = right - left + 1

            if count == n - 1 and stones[right] - stones[left] + 1 == n - 1:
                # Special case: consecutive block of n-1 stones.
                # Determine whether the missing slot can be filled in one move.
                # If the block touches one end and the gap on the other side is
                # larger than or equal to n, one move suffices; otherwise two.
                if left == 0 and stones[-1] - (stones[right] + 1) >= n:
                    min_moves = min(min_moves, 1)
                elif right == n - 1 and (stones[left] - 1) - stones[0] >= n:
                    min_moves = min(min_moves, 1)
                else:
                    min_moves = min(min_moves, 2)
            else:
                min_moves = min(min_moves, n - count)

        return [min_moves, max_moves]