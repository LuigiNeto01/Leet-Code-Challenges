class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        # Edge case: if k <= 1, no product can be strictly less than k
        # because all nums[i] >= 1.
        if k <= 1:
            return 0

        n = len(nums)
        left = 0
        product = 1
        count = 0

        # Sliding window: expand right boundary
        for right in range(n):
            product *= nums[right]  # include nums[right] into window

            # Shrink window from left while product >= k
            while product >= k:
                product //= nums[left]
                left += 1

            # All subarrays ending at 'right' with start between 'left' and 'right'
            # have product < k. There are (right - left + 1) such subarrays.
            count += right - left + 1

        return count