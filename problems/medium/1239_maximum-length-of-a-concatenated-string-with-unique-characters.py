from __future__ import annotations
from typing import List

class Solution:
    def maxLength(self, arr: List[str]) -> int:
        # Keep track of the best individual string length (including those with duplicates)
        max_single = 0
        masks = []
        for s in arr:
            max_single = max(max_single, len(s))
            mask = 0
            valid = True
            for ch in s:
                bit = 1 << (ord(ch) - ord('a'))
                if mask & bit:
                    valid = False
                    break
                mask |= bit
            if valid and mask:
                masks.append(mask)

        n = len(masks)
        self.best = 0

        def dfs(idx: int, current_mask: int, current_len: int) -> None:
            self.best = max(self.best, current_len)
            for i in range(idx, n):
                if (current_mask & masks[i]) == 0:
                    dfs(i + 1,
                        current_mask | masks[i],
                        current_len + bin(masks[i]).count("1"))

        dfs(0, 0, 0)
        return max(self.best, max_single)