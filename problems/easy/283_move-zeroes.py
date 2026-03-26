from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        # write points to the next position where a non-zero should go
        write = 0

        # compact all non-zero values to the front, preserving order
        for read in range(len(nums)):
            if nums[read] != 0:
                # only write when needed to avoid unnecessary self-swaps
                if write != read:
                    nums[write] = nums[read]
                write += 1

        # fill the remaining positions with zeroes
        while write < len(nums):
            nums[write] = 0
            write += 1