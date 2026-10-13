from functools import lru_cache
from typing import List
from collections import defaultdict

class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        # Build a mapping: (left, right) -> list of possible top colors
        trans = defaultdict(list)
        for pat in allowed:
            left, right, top = pat[0], pat[1], pat[2]
            trans[(left, right)].append(top)

        @lru_cache(None)
        def can_build(row: str) -> bool:
            # A single block is the top of the pyramid -> success
            if len(row) == 1:
                return True

            # Precompute the possible top letters for each adjacent pair
            # If any pair has no allowed pattern, cannot build further
            options = []
            for i in range(len(row) - 1):
                key = (row[i], row[i+1])
                if key not in trans:
                    return False          # this pair has no valid top
                options.append(trans[key])

            # Backtrack to try building the next row (length = len(row)-1)
            def dfs(idx: int, built: List[str]) -> bool:
                # idx: current position in the options list (0..len(row)-2)
                # built: characters chosen for the next row so far
                if idx == len(row) - 1:
                    # All positions filled -> form the next row string and recurse
                    next_row = ''.join(built)
                    return can_build(next_row)
                # Try each possible top letter for this adjacent pair
                for c in options[idx]:
                    built.append(c)
                    if dfs(idx+1, built):
                        return True
                    built.pop()
                return False

            return dfs(0, [])

        return can_build(bottom)