from __future__ import annotations
from typing import List

class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        # Calculate total length and early pruning
        total = sum(matchsticks)
        if total % 4 != 0:
            return False  # can't split into 4 equal sides
        side = total // 4

        # Sort in descending order to place large sticks first (prunes search)
        matchsticks.sort(reverse=True)
        if matchsticks[0] > side:
            return False  # a single stick longer than the target side length

        # Four sides initialized to 0
        sides = [0, 0, 0, 0]
        n = len(matchsticks)

        def dfs(index: int) -> bool:
            if index == n:
                # All sticks placed; check all sides equal to target
                return all(s == side for s in sides)

            length = matchsticks[index]
            # Try to place current stick on each side
            for i in range(4):
                if sides[i] + length <= side:
                    sides[i] += length
                    if dfs(index + 1):
                        return True
                    sides[i] -= length  # backtrack

                # Symmetry pruning: if this side is 0 (empty) and placing here failed,
                # no need to try other empty sides with the same stick.
                if sides[i] == 0:
                    break
            return False

        return dfs(0)