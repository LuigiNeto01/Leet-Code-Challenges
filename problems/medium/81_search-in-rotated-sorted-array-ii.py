from __future__ import annotations
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        # Handle empty input defensively (though constraints guarantee non-empty)
        if not nums:
            return False

        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            # Found the target
            if nums[mid] == target:
                return True

            # If duplicates at both ends obscure the pivot, shrink window
            if nums[l] == nums[mid] == nums[r]:
                l += 1
                r -= 1
            # Left half is guaranteed sorted
            elif nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            # Right half is guaranteed sorted
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1

        return False