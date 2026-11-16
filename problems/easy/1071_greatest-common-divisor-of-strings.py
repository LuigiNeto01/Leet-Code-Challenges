from math import gcd

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # If concatenating in different orders doesn't match,
        # there is no common divisor.
        if str1 + str2 != str2 + str1:
            return ""

        # The length of the greatest common divisor string
        # is the GCD of the two lengths.
        n = gcd(len(str1), len(str2))

        # The candidate is the prefix of either string of length n.
        return str1[:n]