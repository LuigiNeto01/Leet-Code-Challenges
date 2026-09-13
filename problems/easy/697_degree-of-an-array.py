from typing import List

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        # Dictionaries to store: first occurrence, last occurrence, and count
        first = {}
        last = {}
        count = {}
        
        # Single pass to fill all dictionaries
        for i, num in enumerate(nums):
            # Record first occurrence if not seen before
            if num not in first:
                first[num] = i
            # Always update last occurrence and count
            last[num] = i
            count[num] = count.get(num, 0) + 1
        
        # Determine the degree (maximum frequency)
        degree = max(count.values())
        
        # Find minimum subarray length among elements with that frequency
        min_length = len(nums)  # worst-case: whole array
        for num, freq in count.items():
            if freq == degree:
                # Contiguous subarray from first to last occurrence
                length = last[num] - first[num] + 1
                if length < min_length:
                    min_length = length
        
        return min_length