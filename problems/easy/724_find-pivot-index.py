class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        total = sum(nums)
        left_sum = 0

        for i, num in enumerate(nums):
            # Right sum is total minus left elements and current element
            if left_sum == total - left_sum - num:
                return i
            left_sum += num

        return -1