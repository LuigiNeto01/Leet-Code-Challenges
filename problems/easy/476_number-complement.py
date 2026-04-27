class Solution:
    def findComplement(self, num: int) -> int:
        # Find the number of bits in the binary representation of num
        # We need to flip only the significant bits (no leading zeros)
        bit_length = num.bit_length()
        
        # Create a mask with all 1's for the same bit length
        # For example, if num = 5 (101 in binary, 3 bits), mask = 111 = 7
        mask = (1 << bit_length) - 1
        
        # XOR num with mask to flip all bits
        # XOR with 1 flips the bit, XOR with 0 keeps it the same
        return num ^ mask