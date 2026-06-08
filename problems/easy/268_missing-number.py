from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Array contains n distinct numbers from range [0, n]
        # So there are n+1 possible values (0 to n) but only n elements
        # One number is missing
        
        # Approach: Use math - sum of 0 to n minus sum of array
        # Expected sum of [0, n] = n * (n + 1) / 2
        # Missing number = expected_sum - actual_sum
        
        n = len(nums)
        # Calculate expected sum of numbers from 0 to n
        expected_sum = n * (n + 1) // 2
        # Calculate actual sum of the array
        actual_sum = sum(nums)
        # The difference is the missing number
        return expected_sum - actual_sum