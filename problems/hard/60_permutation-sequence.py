from __future__ import annotations

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        # Precompute factorials up to n to know how many permutations share a prefix
        fact = [1] * (n + 1)
        for i in range(1, n + 1):
            fact[i] = fact[i - 1] * i

        # Remaining digits to build the permutation from
        digits = list(range(1, n + 1))

        # Convert k to 0-based index to simplify calculations
        k -= 1

        result = []
        # For each position from left to right, select the appropriate digit
        for i in range(n, 0, -1):
            block_size = fact[i - 1]       # number of permutations for each possible leading digit
            index = k // block_size        # which digit to pick from the remaining digits
            result.append(str(digits.pop(index)))
            k %= block_size                # update k to the index within the chosen block

        return ''.join(result)