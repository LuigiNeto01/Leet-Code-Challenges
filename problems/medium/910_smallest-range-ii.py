from __future__ import annotations

class Solution:
    def smallestRangeII(self, nums: list[int], k: int) -> int:
        # Sort the array to apply the two-pointer/greedy strategy.
        # For each element, we can either add k or subtract k.
        # After sorting, the optimal strategy is:
        # - For some split point i, all elements before (or at) i get +k (increase)
        # - All elements after i get -k (decrease)
        nums.sort()
        
        n = len(nums)
        # Initial result: all numbers increased by k gives max-min = (nums[-1]+k) - (nums[0]+k)
        # same as original max-min, but we consider the possibility of mixing +k and -k.
        result = nums[-1] - nums[0]
        
        # The logic: for each possible split between i and i+1 (0 <= i < n-1):
        # left part (indices 0..i) gets +k, right part (i+1..n-1) gets -k
        # After transformation, the new max could be:
        #   max(nums[i] + k, nums[-1] - k)   because left side increased, right side decreased
        # The new min could be:
        #   min(nums[0] + k, nums[i+1] - k)   leftmost increased, first of right part decreased
        # We take the minimum possible difference over all splits.
        for i in range(n - 1):
            # New maximum: the larger of the last element decreased, or the current increased
            new_max = max(nums[i] + k, nums[-1] - k)
            # New minimum: the smaller of the first element increased, or the next element decreased
            new_min = min(nums[0] + k, nums[i + 1] - k)
            # Update result with the smallest range found
            result = min(result, new_max - new_min)
        
        return result