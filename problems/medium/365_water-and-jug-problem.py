from __future__ import annotations

class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        # If target is zero, we can have 0 liters by not filling anything
        if target == 0:
            return True
        # Total capacity must be enough to hold target
        if target > x + y:
            return False
        # The set of reachable totals is all multiples of gcd(x, y)
        from math import gcd
        return target % gcd(x, y) == 0