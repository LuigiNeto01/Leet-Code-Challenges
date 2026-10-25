from math import gcd

class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        # Reduce p and q by their greatest common divisor.
        # The ray's path becomes simplified.
        g = gcd(p, q)
        p //= g
        q //= g

        # After reduction, the parity of p and q determines the receptor.
        # There are three possible cases:
        if p % 2 == 1 and q % 2 == 1:
            # both odd -> northeast corner (receptor 1)
            return 1
        if p % 2 == 1 and q % 2 == 0:
            # p odd, q even -> southeast corner (receptor 0)
            return 0
        # The only remaining case: p even, q odd -> northwest corner (receptor 2)
        return 2