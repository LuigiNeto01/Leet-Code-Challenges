from fractions import Fraction

class Solution:
    def isRationalEqual(self, s: str, t: str) -> bool:
        return self._to_fraction(s) == self._to_fraction(t)

    def _to_fraction(self, num: str) -> Fraction:
        # Split off the repeating part in parentheses, if it exists.
        if '(' in num:
            before, rep = num.split('(')
            rep = rep[:-1]  # remove the closing ')'
        else:
            before, rep = num, None

        # Separate integer part and non-repeating decimal part.
        integer, _, nonrep = before.partition('.')

        ans = Fraction(int(integer) if integer else 0)

        # Add the finite non-repeating decimal part.
        if nonrep:
            ans += Fraction(int(nonrep), 10 ** len(nonrep))

        # Add the infinite repeating block as a geometric series:
        # 0.N(RRR...) = N/10^a + R/(10^a * (10^b - 1)).
        if rep is not None:
            a = len(nonrep)
            b = len(rep)
            ans += Fraction(int(rep), (10 ** a) * (10 ** b - 1))

        return ans