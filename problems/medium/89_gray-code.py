from typing import List

class Solution:
    def grayCode(self, n: int) -> List[int]:
        # Use the mathematical formula: Gray(i) = i XOR (i >> 1)
        # This generates a valid n-bit gray code sequence
        # The sequence will have 2^n elements
        
        # Generate all numbers from 0 to 2^n - 1
        result = []
        for i in range(1 << n):  # 1 << n is 2^n
            # Convert binary number to gray code using XOR with right shift
            # This ensures each adjacent pair differs by exactly one bit
            gray = i ^ (i >> 1)
            result.append(gray)
        
        return result