from typing import List

class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        result = []
        n = len(arr)
        
        for target in range(n, 0, -1):
            idx = arr.index(target)
            
            if idx == target - 1:
                continue
            
            if idx != 0:
                result.append(idx + 1)
                arr = arr[:idx + 1][::-1] + arr[idx + 1:]
            
            result.append(target)
            arr = arr[:target][::-1] + arr[target:]
        
        return result