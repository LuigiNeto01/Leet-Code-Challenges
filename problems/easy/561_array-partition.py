from typing import List

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        # Sort the array to group small numbers together (greedy optimal pairing)
        nums.sort()
        # Sum elements at even indices (0,2,4,...): these are the smaller ones in each pair
        # This yields maximum possible sum of minimums
        return sum(nums[0::2])