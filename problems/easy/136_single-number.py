from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # XOR approach: a ^ a = 0, a ^ 0 = a
        # XOR all numbers together - pairs cancel out, leaving only the single number
        result = 0
        for num in nums:
            result ^= num
        return result