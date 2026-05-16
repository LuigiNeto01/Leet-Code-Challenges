from typing import List

class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        # Key insight: if we can form all numbers in [1, miss-1], 
        # then adding 'miss' extends our range to [1, 2*miss-1]
        
        patches = 0  # Count of patches needed
        miss = 1     # The smallest number we cannot form yet
        i = 0        # Index in nums array
        
        # Continue until we can form all numbers up to n
        while miss <= n:
            # If current number in nums can help extend our range
            if i < len(nums) and nums[i] <= miss:
                # Use nums[i] to extend the range we can cover
                # If we could form [1, miss-1], now we can form [1, miss + nums[i] - 1]
                miss += nums[i]
                i += 1
            else:
                # We have a gap: cannot form 'miss' with current numbers
                # Patch by adding 'miss' itself
                # This extends our coverage from [1, miss-1] to [1, 2*miss-1]
                miss += miss
                patches += 1
        
        return patches