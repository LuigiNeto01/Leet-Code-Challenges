from __future__ import annotations
from collections import defaultdict

class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        # Prefix sum technique: count of subarrays whose sum == goal.
        # Let prefix sum be total sum of elements from index 0 to i.
        # For each prefix sum, we want to know how many prior prefix sums
        # equal current_prefix_sum - goal. Those mark subarrays ending at i.
        freq = defaultdict(int)  # frequency of each prefix sum encountered so far
        freq[0] = 1              # initial prefix sum of empty array (sum=0)
        current_sum = 0
        total = 0

        for num in nums:
            current_sum += num                # prefix sum up to current index
            # Number of subarrays ending here with sum == goal
            # is the number of times we've seen (current_sum - goal)
            total += freq.get(current_sum - goal, 0)
            # Record current prefix sum for future subarrays
            freq[current_sum] += 1

        return total