from __future__ import annotations

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # This result list will collect numbers that appear twice
        res: List[int] = []
        # Iterate through each number and use index marking technique
        for i in range(len(nums)):
            val = abs(nums[i])       # actual value in [1, n]
            idx = val - 1              # map value to 0-based index
            if nums[idx] < 0:
                # If we've already negated this index, val is a duplicate
                res.append(val)
            else:
                # Mark this value as seen by negating the corresponding index
                nums[idx] = -nums[idx]
        return res