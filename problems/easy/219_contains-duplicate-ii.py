from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # If k is 0, no two distinct indices can satisfy abs(i-j) <= 0, so immediately false.
        if k <= 0:
            return False

        # Map each value to its most recent index encountered while iterating.
        # We only need the last index because any older occurrence is farther away.
        last_index = {}

        # Iterate through array once (O(n) time), updating and checking distances.
        for i, v in enumerate(nums):
            # If we've seen v before, check distance to the previous occurrence.
            if v in last_index:
                # If the difference in indices is within k, we found a valid pair.
                if i - last_index[v] <= k:
                    return True
            # Update the most recent index for v (important to keep it as the latest).
            last_index[v] = i

        # No qualifying pair found
        return False