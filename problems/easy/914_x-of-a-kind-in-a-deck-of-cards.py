from __future__ import annotations
import math
from collections import Counter

class Solution:
    def hasGroupsSizeX(self, deck: list[int]) -> bool:
        # Count frequencies of each card value
        freq = Counter(deck)
        
        # Compute gcd of all frequencies
        # Start with the first frequency
        first = next(iter(freq.values())) if freq else 0
        overall_gcd = first
        for count in freq.values():
            overall_gcd = math.gcd(overall_gcd, count)
        
        # If gcd > 1, we can partition into groups of size gcd (>1)
        return overall_gcd > 1