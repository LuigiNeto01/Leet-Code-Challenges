from typing import List

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Fewer than 2 numbers means no adjacent gap exists.
        if n < 2:
            return 0
        
        mn = min(nums)
        mx = max(nums)
        
        # All numbers equal, so every sorted gap is 0.
        if mn == mx:
            return 0
        
        # Pigeonhole idea:
        # The maximum gap must be at least this bucket size.
        bucket_size = max(1, (mx - mn) // (n - 1))
        
        # Number of buckets needed to cover [mn, mx].
        bucket_count = (mx - mn) // bucket_size + 1
        
        # Each bucket stores only min and max value seen inside it.
        # Internal bucket gaps cannot beat cross-bucket gaps.
        bucket_min = [float("inf")] * bucket_count
        bucket_max = [float("-inf")] * bucket_count
        bucket_used = [False] * bucket_count
        
        # Place each number into its bucket.
        for num in nums:
            idx = (num - mn) // bucket_size
            bucket_used[idx] = True
            bucket_min[idx] = min(bucket_min[idx], num)
            bucket_max[idx] = max(bucket_max[idx], num)
        
        max_gap = 0
        prev_max = mn
        
        # The answer is the gap between consecutive non-empty buckets.
        for i in range(bucket_count):
            if not bucket_used[i]:
                continue
            
            # Current bucket min is the next sorted value after prev_max.
            max_gap = max(max_gap, bucket_min[i] - prev_max)
            prev_max = bucket_max[i]
        
        return max_gap