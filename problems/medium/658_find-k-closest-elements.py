from typing import List

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # Binary search to find the leftmost index of a k-length window
        # that contains the k closest elements to x.
        # The window is arr[left:left+k].
        # We compare distances: if x - arr[mid] > arr[mid+k] - x,
        # then the right element (mid+k) is closer, so the window should start
        # further to the right (left = mid+1). Otherwise, move left bound left.
        left, right = 0, len(arr) - k
        while left < right:
            mid = (left + right) // 2
            # Compare distances of arr[mid] and arr[mid+k] to x.
            # Use the condition from the problem: if equal absolute difference,
            # prefer the smaller element (i.e., arr[mid] is smaller, so keep left).
            if x - arr[mid] > arr[mid + k] - x:
                # The element at mid+k is closer to x than arr[mid],
                # so the window start must be to the right of mid.
                left = mid + 1
            else:
                # arr[mid] is closer or tie with smaller value,
                # so the window start can be at or left of mid.
                right = mid
        # The optimal window starts at 'left'
        return arr[left:left + k]