from __future__ import annotations
import random
from typing import List, Set, Dict

class Solution:
    def __init__(self, n: int, blacklist: List[int]):
        """
        Build a mapping from blacklisted numbers in the range [0, m-1]
        to non-blacklisted numbers in [m, n-1], where m = n - len(blacklist).
        This way, picking a random index in [0, m-1] always yields a valid number
        (either directly or via the mapping).
        """
        self.m = n - len(blacklist)          # number of valid numbers
        black_set: Set[int] = set(blacklist) # for O(1) lookup
        # Collect blacklisted numbers that fall in the "low" part [0, m-1]
        # They need to be remapped to numbers from the "high" part [m, n-1] that are not blacklisted.
        low_black: List[int] = [b for b in blacklist if b < self.m]
        # Gather enough non-blacklisted numbers from the high part to serve as replacements.
        # We iterate from m upwards, skipping blacklisted ones.
        high_free: List[int] = []
        val = self.m
        while len(high_free) < len(low_black):
            if val not in black_set:
                high_free.append(val)
            val += 1
        # Build mapping: low_black[i] -> high_free[i]
        self.map: Dict[int, int] = {}
        for low, high in zip(low_black, high_free):
            self.map[low] = high

    def pick(self) -> int:
        """
        Returns a uniformly random integer in [0, n-1] that is not blacklisted.
        """
        idx = random.randint(0, self.m - 1)  # random index in the valid range
        # If idx is blacklisted (and thus in the map), return its replacement;
        # otherwise return idx directly.
        return self.map.get(idx, idx)

# Your Solution object will be instantiated and called as such:
# obj = Solution(n, blacklist)
# param_1 = obj.pick()