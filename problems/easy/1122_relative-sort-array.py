from __future__ import annotations

class Solution:
    def relativeSortArray(self, arr1: list[int], arr2: list[int]) -> list[int]:
        max_val = max(arr1) if arr1 else 0
        freq = [0] * (max_val + 1)
        
        for num in arr1:
            freq[num] += 1
        
        result = []
        
        for num in arr2:
            if num <= max_val:
                result.extend([num] * freq[num])
                freq[num] = 0
        
        for num in range(max_val + 1):
            if freq[num] > 0:
                result.extend([num] * freq[num])
        
        return result