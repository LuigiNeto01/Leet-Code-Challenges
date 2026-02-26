from __future__ import annotations
from typing import List

class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        # Build prefix sums: prefix[0] = 0, prefix[i] = sum of nums[:i]
        n = len(nums)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        # Divide-and-conquer count with merge sort style
        def sort_count(left: int, right: int) -> int:
            # Process prefix[left:right], where 'right' is exclusive
            if right - left <= 1:
                return 0  # No pair to form
            mid = (left + right) // 2
            count = sort_count(left, mid) + sort_count(mid, right)

            # Count cross pairs: i in [left, mid), j in [mid, right)
            # We need prefix[j] - prefix[i] in [lower, upper]
            j1 = j2 = mid
            for i in range(left, mid):
                # Move j1 to the first index in right where prefix[j1] - prefix[i] >= lower
                while j1 < right and prefix[j1] - prefix[i] < lower:
                    j1 += 1
                # Move j2 to the first index in right where prefix[j2] - prefix[i] > upper
                while j2 < right and prefix[j2] - prefix[i] <= upper:
                    j2 += 1
                count += j2 - j1

            # Merge the two sorted halves
            merged = []
            p, q = left, mid
            while p < mid and q < right:
                if prefix[p] <= prefix[q]:
                    merged.append(prefix[p]); p += 1
                else:
                    merged.append(prefix[q]); q += 1
            while p < mid:
                merged.append(prefix[p]); p += 1
            while q < right:
                merged.append(prefix[q]); q += 1

            # Write back the sorted values
            prefix[left:right] = merged
            return count

        # Work on the full range of prefix sums
        return sort_count(0, n + 1)