from __future__ import annotations
from collections import Counter

class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        # Count digits of the input number
        n_digit_count = Counter(str(n))
        
        # Generate all powers of two up to 10^9 (2^0 to 2^29)
        # Since 2^30 > 10^9, we stop when power exceeds 10^9
        power = 1  # 2^0 = 1
        while power <= 10**9:
            # If digit multiset matches, we can reorder to this power of two
            if Counter(str(power)) == n_digit_count:
                return True
            power <<= 1  # multiply by 2 (next power)
        
        # No matching power of two found
        return False