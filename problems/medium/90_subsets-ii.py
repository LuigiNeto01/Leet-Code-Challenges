from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # Sorting groups equal values together, which makes duplicate skipping easy.
        nums.sort()
        
        result: List[List[int]] = []
        path: List[int] = []
        
        def backtrack(start: int) -> None:
            # Every current path is a valid subset, including the empty one.
            result.append(path[:])
            
            # Try adding each remaining number as the next choice.
            for i in range(start, len(nums)):
                # If this value is the same as the previous one at the same depth,
                # skip it to avoid generating the same subset twice.
                if i > start and nums[i] == nums[i - 1]:
                    continue
                
                # Choose the current number.
                path.append(nums[i])
                
                # Recurse with the next index so each element is used at most once.
                backtrack(i + 1)
                
                # Undo the choice and explore the next option.
                path.pop()
        
        backtrack(0)
        return result