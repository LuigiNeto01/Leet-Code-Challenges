from typing import List

class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        # modulus as specified by problem
        MOD = 1337
        # reduce base modulo MOD immediately to keep numbers small
        a %= MOD

        # result will hold a^{processed_prefix_of_b} mod MOD
        res = 1

        # Process digits from most significant to least (left to right).
        # If we have processed prefix x (so current result = a^x mod MOD),
        # and next digit is d, new exponent becomes 10*x + d, so:
        # a^{10*x + d} = (a^x)^{10} * a^d  (mod MOD).
        # Use fast modular exponentiation (Python pow with three args).
        for d in b:
            # raise current result to power 10 modulo MOD (accounts for shifting digits)
            res = pow(res, 10, MOD)
            # multiply by a^d modulo MOD (accounts for the new digit)
            res = (res * pow(a, d, MOD)) % MOD

        return res