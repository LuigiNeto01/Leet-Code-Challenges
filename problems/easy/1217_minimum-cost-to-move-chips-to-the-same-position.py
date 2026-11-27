from __future__ import annotations

class Solution:
    def minCostToMoveChips(self, position: list[int]) -> int:
        # Moving by 2 costs 0, moving by 1 costs 1.
        # This means we can shift chips within even/odd parity for free.
        # Optimal strategy: pick either all even or all odd positions as target.
        # Cost = number of chips that must change parity (i.e., move by 1).
        # Because moving any distance with cost 0 can align chips of same parity.
        
        # Count chips on even and odd positions
        even_count = sum(1 for p in position if p % 2 == 0)
        odd_count = len(position) - even_count
        
        # Minimum cost is the smaller parity group (those must move by 1)
        return min(even_count, odd_count)