from __future__ import annotations

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        # Create a set of jewel characters for O(1) membership checks.
        jewel_set = set(jewels)
        
        # Count how many stones are jewels.
        count = 0
        for stone in stones:
            if stone in jewel_set:
                count += 1
        return count