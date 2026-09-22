from __future__ import annotations

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        # Standard binary search on sorted array (unique values, ascending)
        left, right = 0, len(nums) - 1

        while left <= right:
            # Prevent potential overflow in other languages; fine in Python
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid          # found target, return its index
            elif nums[mid] < target:
                left = mid + 1      # target is in the right half
            else:
                right = mid - 1     # target is in the left half

        return -1                   # target not present