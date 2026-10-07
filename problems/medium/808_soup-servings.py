from __future__ import annotations
from functools import lru_cache

class Solution:
    def soupServings(self, n: int) -> float:
        # Since operations are multiples of 25 mL, scale down
        # to reduce state space and avoid large recursion depth.
        # If n is very large, the probability approaches 1.
        # Empirically, for n >= 4800 (scaled >= 192) the probability is ~1 within 1e-5.
        if n >= 4800:
            return 1.0
        
        # Scale n: number of 25mL servings; ceil division for integer steps.
        servings = (n + 24) // 25
        
        @lru_cache(maxsize=None)
        def dp(a: int, b: int) -> float:
            """Probability of A being empty first (plus half simultaneous) 
               starting with a servings of A and b servings of B."""
            # If both are empty (or negative from pouring more than available):
            # that means they became empty in the same turn.
            if a <= 0 and b <= 0:
                return 0.5  # half probability for simultaneous empty
            # If only A is empty (or became empty this turn):
            if a <= 0:
                return 1.0  # A emptied before B or exactly when B still had some
            # If only B is empty:
            if b <= 0:
                return 0.0  # B emptied before A
            
            # Four operations, each equally likely (0.25)
            # For each operation, we pour the given amounts, but never go negative
            # (if we need more than we have, we just take what remains, i.e., a or b becomes 0).
            prob = 0.0
            # Serve 4 operations: (100,0), (75,25), (50,50), (25,75) in scaled units (4,0), (3,1), (2,2), (1,3)
            prob += dp(a - 4, b)      # 100mL from A, 0 from B
            prob += dp(a - 3, b - 1)  # 75 from A, 25 from B
            prob += dp(a - 2, b - 2)  # 50 from A, 50 from B
            prob += dp(a - 1, b - 3)  # 25 from A, 75 from B
            
            return prob * 0.25  # average over 4 equally likely outcomes
        
        return dp(servings, servings)