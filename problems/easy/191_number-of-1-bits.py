class Solution:
    def hammingWeight(self, n: int) -> int:
        # Count number of set bits (Hamming weight) in integer n.
        # Use Brian Kernighan's algorithm: repeatedly flip the lowest set bit to 0.
        # This runs in O(k) where k is number of set bits, which is efficient if bits are sparse.
        # Works for non-negative integers (problem constraints 1 <= n <= 2^31 - 1).
        count = 0
        # Loop until no set bits remain
        while n:
            # Remove the lowest set bit. This reduces n and increments count.
            # Example: n = ...1000, n-1 = ...0111, n & (n-1) clears that lowest 1.
            n &= n - 1
            count += 1
        return count