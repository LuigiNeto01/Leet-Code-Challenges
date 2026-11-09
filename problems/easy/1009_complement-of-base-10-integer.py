class Solution:
    def bitwiseComplement(self, n: int) -> int:
        # Edge case: when n is 0, binary representation is "0", complement is "1" which is 1
        if n == 0:
            return 1
        
        # Find the number of bits needed to represent n
        # For example, n=5 (101) needs 3 bits, n=10 (1010) needs 4 bits
        num_bits = n.bit_length()
        
        # Create a mask with all 1's of the same length as n's binary representation
        # (1 << num_bits) gives a 1 followed by num_bits zeros, subtract 1 to get all ones
        mask = (1 << num_bits) - 1
        
        # XOR with mask flips all bits: 0->1, 1->0 within the bit length
        return n ^ mask