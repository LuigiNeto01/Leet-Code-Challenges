from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Boyer-Moore voting:
        # matching numbers strengthen the current candidate,
        # different numbers cancel each other out
        candidate = 0
        count = 0

        for num in nums:
            # If balance is zero, start tracking a new candidate
            if count == 0:
                candidate = num

            # Same value supports the candidate, otherwise it cancels one vote
            if num == candidate:
                count += 1
            else:
                count -= 1

        # A majority element is guaranteed to exist, so the final candidate is correct
        return candidate