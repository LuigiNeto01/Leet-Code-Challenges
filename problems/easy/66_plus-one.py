from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Start from the least significant digit (rightmost)
        for i in range(len(digits) - 1, -1, -1):
            # If current digit is less than 9, just increment and return
            if digits[i] < 9:
                digits[i] += 1
                return digits
            # If current digit is 9, it becomes 0 and we carry over
            digits[i] = 0
        
        # If we exit the loop, all digits were 9 (e.g., [9,9,9] -> [1,0,0,0])
        # We need to prepend 1 to the result
        return [1] + digits