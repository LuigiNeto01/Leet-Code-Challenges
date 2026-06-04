from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        # Step 1: XOR all numbers to get xor of the two unique numbers
        # All pairs cancel out, leaving us with a ^ b where a and b are the two unique numbers
        xor_all = 0
        for num in nums:
            xor_all ^= num
        
        # Step 2: Find a bit that is set in xor_all (i.e., a bit where a and b differ)
        # We can use any set bit; here we find the rightmost set bit
        # This bit is 1 in exactly one of the two unique numbers
        rightmost_bit = xor_all & (-xor_all)
        
        # Step 3: Partition numbers into two groups based on this bit
        # Group 1: numbers with this bit set
        # Group 2: numbers with this bit not set
        # Each unique number will be in a different group
        # Each pair will be in the same group (since they're identical)
        num1 = 0
        num2 = 0
        
        for num in nums:
            if num & rightmost_bit:
                # This number has the bit set
                num1 ^= num
            else:
                # This number doesn't have the bit set
                num2 ^= num
        
        # num1 and num2 now contain the two unique numbers
        return [num1, num2]