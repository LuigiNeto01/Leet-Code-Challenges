from __future__ import annotations

class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        n = mountainArr.length()

        # Step 1: Find the peak index using binary search
        lo, hi = 0, n - 1
        while lo < hi:
            mid = (lo + hi) // 2
            # Compare mid and mid+1 to determine which side the peak lies on
            if mountainArr.get(mid) < mountainArr.get(mid + 1):
                # Ascending slope, peak is to the right
                lo = mid + 1
            else:
                # Descending slope or at peak, peak is left or current
                hi = mid
        peak = lo

        # Step 2: Binary search on increasing left part [0, peak]
        lo, hi = 0, peak
        while lo <= hi:
            mid = (lo + hi) // 2
            val = mountainArr.get(mid)
            if val == target:
                return mid
            elif val < target:
                lo = mid + 1
            else:
                hi = mid - 1

        # Step 3: Binary search on decreasing right part [peak+1, n-1]
        lo, hi = peak + 1, n - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            val = mountainArr.get(mid)
            if val == target:
                return mid
            elif val < target:
                # In a decreasing array, smaller values are to the right,
                # so target (larger) must be to the left
                hi = mid - 1
            else:
                # target is smaller, so it lies to the right
                lo = mid + 1

        return -1