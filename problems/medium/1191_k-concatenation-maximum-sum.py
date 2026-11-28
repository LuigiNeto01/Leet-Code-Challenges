from __future__ import annotations

class Solution:
    def kConcatenationMaxSum(self, arr: list[int], k: int) -> int:
        MOD = 10**9 + 7
        
        # Helper: Kadane's algorithm to find max subarray sum in a single array
        def kadane(a: list[int]) -> int:
            max_ending_here = 0  # best sum ending at current position
            max_so_far = 0       # best sum overall
            for x in a:
                # Either extend the previous subarray or start fresh
                max_ending_here = max(0, max_ending_here + x)
                max_so_far = max(max_so_far, max_ending_here)
            return max_so_far
        
        # Compute total sum of the original array
        total_sum = sum(arr)
        
        # Case 1: Only one copy -> simple Kadane
        if k == 1:
            return kadane(arr) % MOD
        
        # For k >= 2, consider two copies concatenated (covers crossing between copies)
        # Compute max suffix sum: best sum of a suffix of arr
        suffix_max = 0
        cur = 0
        for x in reversed(arr):
            cur += x
            suffix_max = max(suffix_max, cur)
        
        # Compute max prefix sum: best sum of a prefix of arr
        prefix_max = 0
        cur = 0
        for x in arr:
            cur += x
            prefix_max = max(prefix_max, cur)
        
        # Case 2: Best subarray lies within two concatenated copies (or within one)
        best_two = kadane(arr + arr)
        
        # Case 3: If total_sum > 0, we can take entire array k times
        # plus the best suffix and best prefix from the ends
        if total_sum > 0:
            # Use all k copies fully, plus extra prefix/suffix from the ends
            # This gives: suffix_max + (k-2)*total_sum + prefix_max
            full_repeat = suffix_max + (k - 2) * total_sum + prefix_max
            # The best answer is max of best_two (which covers cases where we don't
            # use all full arrays in the middle) and the full_repeat scenario
            ans = max(best_two, full_repeat)
        else:
            # If total_sum <= 0, adding full arrays only reduces sum,
            # so best is just best_two (within two copies)
            ans = best_two
        
        # Since we deal with possible negative numbers, answer is at least 0
        return max(ans, 0) % MOD