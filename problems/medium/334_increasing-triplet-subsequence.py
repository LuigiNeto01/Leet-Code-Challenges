from typing import List

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # Edge case: fewer than 3 elements cannot form a triplet
        if len(nums) < 3:
            return False

        # We maintain two values:
        # first -> smallest value seen so far (candidate for nums[i])
        # second -> smallest value > first seen so far (candidate for nums[j])
        # If we ever find a number > second, we have nums[i] < nums[j] < nums[k].
        first = float('inf')
        second = float('inf')

        # Iterate once through the list -> O(n) time, O(1) extra space.
        for x in nums:
            # If current number is smaller or equal to first, update first.
            # Use <= so duplicates don't falsely count as increasing; we prefer the smaller value
            # to increase chance of finding a larger second and third later.
            if x <= first:
                first = x
                # Continue scanning after improving the smallest candidate.
                continue

            # If current number is greater than first but smaller or equal to second,
            # update second to be this better middle candidate.
            if x <= second:
                second = x
                continue

            # If we reach here, then x > second > first, so we found an increasing triplet.
            return True

        # No triplet found after scanning all numbers.
        return False