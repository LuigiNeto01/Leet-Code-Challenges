class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        # If k is divisible by 2 or 5, no repunit can be divisible
        # because all repunits end with digit 1.
        if k % 2 == 0 or k % 5 == 0:
            return -1

        remainder = 0
        # Only need to check at most k numbers (pigeonhole principle)
        for length in range(1, k + 1):
            # Build next repunit modulo k: append a digit 1
            remainder = (remainder * 10 + 1) % k
            if remainder == 0:
                return length
        # If we exhausted all possibilities, no solution exists
        return -1