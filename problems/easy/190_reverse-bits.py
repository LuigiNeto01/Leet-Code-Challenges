class Solution:
    def reverseBits(self, n: int) -> int:
        # Initialize result to 0
        result = 0
        
        # Process all 32 bits
        for i in range(32):
            # Extract the least significant bit of n
            bit = n & 1
            
            # Shift result left to make room for the new bit
            # and OR with the extracted bit to place it
            result = (result << 1) | bit
            
            # Shift n right to process the next bit
            n >>= 1
        
        return result