class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # Power of two must be positive
        if n <= 0:
            return False
        
        # A power of two in binary has exactly one bit set (e.g., 1=1, 2=10, 4=100, 8=1000)
        # When we subtract 1 from a power of two, all bits after the single set bit become 1
        # (e.g., 8=1000, 7=0111; 4=100, 3=011)
        # The AND of n and (n-1) will be 0 only if n is a power of two
        return n & (n - 1) == 0