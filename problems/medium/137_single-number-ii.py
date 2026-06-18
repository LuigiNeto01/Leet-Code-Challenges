from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Use bit manipulation: track bits that appear 1 time and 2 times
        # ones: bits that appeared 1 time (mod 3)
        # twos: bits that appeared 2 times (mod 3)
        # When a bit appears 3 times, we reset it in both ones and twos
        
        ones = 0
        twos = 0
        
        for num in nums:
            # Update twos: add bits that are in both num and ones
            # (bits appearing for the 2nd time)
            twos |= ones & num
            
            # Update ones: XOR with num (toggle bits)
            ones ^= num
            
            # Find bits that appeared 3 times (present in both ones and twos)
            threes = ones & twos
            
            # Remove bits that appeared 3 times from both ones and twos
            ones &= ~threes
            twos &= ~threes
        
        # ones will contain the bits of the number that appeared once
        return ones