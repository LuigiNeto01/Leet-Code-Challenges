from typing import List

class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
        n = len(nums)
        if n == 1:
            # Single number: no division possible
            return str(nums[0])
        if n == 2:
            # Two numbers: simple division, no parentheses needed
            return f"{nums[0]}/{nums[1]}"
        # For three or more numbers, the maximum is achieved by
        # dividing the first number by the division chain of the rest.
        # This yields: first / (second / third / ... / last)
        # Because a/(b/c/d/...) = a * (c*d*...)/b which is maximal.
        # Join all numbers from index 1 onward with '/' and wrap in parentheses.
        denominator = '/'.join(map(str, nums[1:]))
        return f"{nums[0]}/({denominator})"