class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # Power of four must be positive
        if n <= 0:
            return False
        
        # Power of four must be a power of two (only one bit set)
        # n & (n - 1) removes the rightmost set bit, so for power of 2 it becomes 0
        if n & (n - 1) != 0:
            return False
        
        # Power of four has the single bit set at an even position (0-indexed from right)
        # 4^0 = 1 = 0b1 (bit 0)
        # 4^1 = 4 = 0b100 (bit 2)
        # 4^2 = 16 = 0b10000 (bit 4)
        # 4^3 = 64 = 0b1000000 (bit 6)
        # Pattern: bit position is always even (0, 2, 4, 6, ...)
        # Mask 0x55555555 = 0b01010101010101010101010101010101 has bits set at even positions
        # If n is power of 4, its single set bit should align with this mask
        return (n & 0x55555555) != 0