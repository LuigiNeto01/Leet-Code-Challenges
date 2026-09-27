class Solution:
    def dominantIndex(self, nums: list[int]) -> int:
        largest = -1
        second = -1
        ans = -1

        for i, num in enumerate(nums):
            if num > largest:
                second = largest
                largest = num
                ans = i
            elif num != largest and num > second:
                second = num

        return ans if largest >= 2 * second else -1