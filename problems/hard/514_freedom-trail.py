from __future__ import annotations
from functools import lru_cache

class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        """
        We use DP with memoization: dp(i, j) = minimum steps to type key[i:]
        when ring index j is currently at 12:00.
        At each step we try all positions in ring that match the target character.
        """
        n = len(ring)
        m = len(key)
        
        # Precompute positions of each character in ring for quick lookup
        char_positions: dict[str, list[int]] = {}
        for idx, ch in enumerate(ring):
            char_positions.setdefault(ch, []).append(idx)
        
        @lru_cache(None)
        def min_steps(key_idx: int, ring_pos: int) -> int:
            """Returns min steps to finish spelling from key[key_idx:] 
               when ring character at index ring_pos is at 12:00."""
            if key_idx == m:
                return 0  # No more characters to spell
            
            target = key[key_idx]
            best = float('inf')
            
            # Try every occurrence of target in ring
            for next_pos in char_positions[target]:
                # distance clockwise = (next_pos - ring_pos) mod n
                clockwise = (next_pos - ring_pos) % n
                # distance anticlockwise = (ring_pos - next_pos) mod n
                anticlockwise = (ring_pos - next_pos) % n
                # We can rotate either direction, pick the minimal rotation steps
                rotate_cost = min(clockwise, anticlockwise)
                # 1 step to press the button
                total = rotate_cost + 1 + min_steps(key_idx + 1, next_pos)
                best = min(best, total)
            
            return best
        
        return min_steps(0, 0)  # Start at ring index 0, key index 0