from typing import List

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # Prefix index 0 has sum 0, so remainder 0 starts at index 0.
        seen = {0: 0}
        current_sum = 0

        for i, num in enumerate(nums):
            current_sum = (current_sum + num) % k

            # Same remainder means the sum between these prefix indices is a multiple of k.
            if current_sum in seen:
                # Must be at least two elements long.
                if i + 1 - seen[current_sum] >= 2:
                    return True
                # Keep the earliest index so future subarrays can be longer.
            else:
                seen[current_sum] = i + 1

        return False