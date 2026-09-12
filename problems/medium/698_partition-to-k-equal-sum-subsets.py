from typing import List

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        # If total sum is not divisible by k, impossible
        if total % k != 0:
            return False
        target = total // k
        n = len(nums)

        # Sort descending to place large numbers early (pruning)
        nums.sort(reverse=True)

        # If the largest number exceeds the target, impossible
        if nums[0] > target:
            return False

        # Memoization: used_mask -> whether a solution exists from this state
        memo = {}

        def backtrack(used_mask: int, cur_sum: int, start: int) -> bool:
            """
            used_mask: bitmask of indices already used
            cur_sum: current sum of the bucket being filled
            start: index to start scanning from (to avoid permutations)
            Returns True if the remaining numbers can be partitioned
            """
            # All numbers used → all buckets filled
            if used_mask == (1 << n) - 1:
                return True

            # Current bucket is full → start a new bucket
            if cur_sum == target:
                return backtrack(used_mask, 0, 0)

            # Prune using memo
            if used_mask in memo:
                return memo[used_mask]

            # Try each unused number
            for i in range(start, n):
                # Skip if already used
                if (used_mask >> i) & 1:
                    continue
                # Skip if adding this number would exceed target
                if cur_sum + nums[i] > target:
                    continue
                # Prune duplicates: if the same value was skipped earlier in this branch,
                # trying it again would lead to the same search states.
                if i > 0 and not ((used_mask >> (i - 1)) & 1) and nums[i] == nums[i - 1]:
                    continue
                # Recurse with this number taken
                if backtrack(used_mask | (1 << i), cur_sum + nums[i], i + 1):
                    memo[used_mask] = True
                    return True

            # No choice worked
            memo[used_mask] = False
            return False

        return backtrack(0, 0, 0)