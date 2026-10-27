class Solution:
    def smallestRangeI(self, nums: list[int], k: int) -> int:
        # The maximum element can be decreased by at most k.
        # The minimum element can be increased by at most k.
        # The best possible score is reduced by up to 2 * k.
        return max(0, max(nums) - min(nums) - 2 * k)