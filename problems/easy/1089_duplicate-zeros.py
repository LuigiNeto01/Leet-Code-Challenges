from __future__ import annotations
from typing import List

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        n = len(arr)
        i = 0
        j = 0
        # First pass: find the last element that will be kept
        while j < n:
            if arr[i] == 0:
                j += 2
            else:
                j += 1
            i += 1
        i -= 1
        j -= 1
        # Second pass: write from the end backwards
        while i >= 0:
            if j < n:
                arr[j] = arr[i]
            if arr[i] == 0:
                j -= 1
                if j < n:
                    arr[j] = 0
            i -= 1
            j -= 1