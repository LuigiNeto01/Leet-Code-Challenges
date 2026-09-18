class Solution:
    def findUnsortedSubarray(self, nums: list[int]) -> int:
        n = len(nums)
        # Find the rightmost index where array is out of order:
        # any element that is less than the maximum seen so far must be part of the unsorted subarray.
        max_seen = nums[0]
        right = 0
        for i in range(1, n):
            if nums[i] < max_seen:
                right = i  # update right boundary
            else:
                max_seen = max(max_seen, nums[i])

        # Find the leftmost index where array is out of order:
        # any element that is greater than the minimum seen from the right must be part.
        min_seen = nums[-1]
        left = n - 1
        for i in range(n - 2, -1, -1):
            if nums[i] > min_seen:
                left = i  # update left boundary
            else:
                min_seen = min(min_seen, nums[i])

        # If left < right, the subarray is from left to right inclusive.
        # Otherwise, the array is already sorted.
        return right - left + 1 if left < right else 0