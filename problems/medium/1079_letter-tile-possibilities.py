from __future__ import annotations
from collections import Counter

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        # Count the frequency of each letter to track available tiles
        freq = Counter(tiles)
        
        def backtrack() -> int:
            """Returns the number of sequences that can be formed from current remaining tiles."""
            total = 0
            # Try each letter that still has available tiles
            for letter in list(freq.keys()):
                if freq[letter] > 0:
                    # Use one tile of this letter
                    freq[letter] -= 1
                    # Count this single-letter sequence
                    total += 1
                    # Recursively count all sequences that start with this letter
                    total += backtrack()
                    # Restore the tile for backtracking
                    freq[letter] += 1
            return total
        
        return backtrack()