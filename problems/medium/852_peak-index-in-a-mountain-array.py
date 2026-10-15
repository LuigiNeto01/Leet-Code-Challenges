class Solution:
    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        left, right = 0, len(arr) - 1

        while left < right:
            mid = (left + right) // 2

            # If the array is still increasing, the peak must be to the right.
            if arr[mid] < arr[mid + 1]:
                left = mid + 1
            # Otherwise we are on the decreasing side or at the peak itself.
            else:
                right = mid

        return left