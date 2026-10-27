from __future__ import annotations
from typing import List

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        # A valid mountain array must have at least 3 elements
        n = len(arr)
        if n < 3:
            return False

        i = 0  # pointer for climbing up

        # Climb up while strictly increasing
        while i + 1 < n and arr[i] < arr[i + 1]:
            i += 1

        # The peak cannot be the first or last element
        if i == 0 or i == n - 1:
            return False

        # Climb down while strictly decreasing
        while i + 1 < n and arr[i] > arr[i + 1]:
            i += 1

        # If we reached the end, it's a valid mountain
        return i == n - 1