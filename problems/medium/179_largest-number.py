from typing import List
from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # Convert all numbers to strings for concatenation comparison
        nums_str = [str(num) for num in nums]
        
        # Custom comparator: compare concatenations in both orders
        # If xy > yx, then x should come before y
        def compare(x, y):
            # Compare x+y vs y+x
            if x + y > y + x:
                return -1  # x comes before y
            elif x + y < y + x:
                return 1   # y comes before x
            else:
                return 0   # equal
        
        # Sort using the custom comparator
        nums_str.sort(key=cmp_to_key(compare))
        
        # Join all numbers to form the result
        result = ''.join(nums_str)
        
        # Edge case: if result is all zeros (e.g., [0, 0]), return "0"
        if result[0] == '0':
            return '0'
        
        return result