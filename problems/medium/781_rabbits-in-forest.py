from __future__ import annotations
from collections import Counter

class Solution:
    def numRabbits(self, answers: list[int]) -> int:
        """
        Returns the minimum number of rabbits in the forest given the answers array.
        Each rabbit says how many other rabbits share its color.
        """
        # Count how many times each answer appears
        freq = Counter(answers)
        total = 0

        for x, cnt in freq.items():
            # If a rabbit answers x, its color group has x+1 rabbits (itself + x others)
            group_size = x + 1
            # Number of groups needed to accommodate 'cnt' rabbits with answer x
            # Ceil division: (cnt + group_size - 1) // group_size
            groups = (cnt + group_size - 1) // group_size
            total += groups * group_size

        return total