from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # write points to the next position where we keep a valid element
        write = 0

        # scan every number once
        for read in range(len(nums)):
            # keep only values different from val
            if nums[read] != val:
                # place the kept value into the compacted prefix
                nums[write] = nums[read]
                write += 1

        # write is exactly the count of elements not equal to val
        return write