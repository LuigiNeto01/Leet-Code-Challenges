from __future__ import annotations

class Solution:
    def sumSubseqWidths(self, nums: list[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        
        # Sort nums to simplify min/max relationships.
        # After sorting, for any subsequence the max is the rightmost element and min is the leftmost.
        nums.sort()
        
        # Precompute powers of 2 modulo MOD up to n.
        pow2 = [1] * n
        for i in range(1, n):
            pow2[i] = (pow2[i-1] * 2) % MOD
        
        total = 0
        # For each element nums[i], when it acts as max, it contributes +nums[i] * 2^i
        # (because all subsets of the previous i elements can be chosen)
        # When it acts as min, it contributes -nums[i] * 2^(n-1-i)
        # (because all subsets of the remaining n-1-i elements can be chosen)
        for i, val in enumerate(nums):
            # Contribution as maximum
            total = (total + val * pow2[i]) % MOD
            # Contribution as minimum (subtracted)
            total = (total - val * pow2[n-1-i]) % MOD
        
        # Ensure the result is non-negative modulo MOD
        return total % MOD