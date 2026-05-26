class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # XOR gives 1 where bits differ, 0 where they're the same
        xor_result = x ^ y
        
        # Count the number of 1 bits in the XOR result
        # This represents the number of positions where bits differ
        count = 0
        while xor_result:
            # Increment count if the least significant bit is 1
            count += xor_result & 1
            # Right shift to check the next bit
            xor_result >>= 1
        
        return count