from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # Sort to group duplicates together for easier skipping
        nums.sort()
        result = []
        # Track which elements are currently used in the permutation
        used = [False] * len(nums)
        
        def backtrack(path):
            # Base case: we've built a complete permutation
            if len(path) == len(nums):
                result.append(path[:])
                return
            
            for i in range(len(nums)):
                # Skip if already used in current path
                if used[i]:
                    continue
                
                # Skip duplicates: if current number equals previous 
                # and previous was not used, skip to avoid duplicate permutations
                # This ensures we only use duplicate numbers in order
                if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                    continue
                
                # Choose: add current number to path
                path.append(nums[i])
                used[i] = True
                
                # Explore
                backtrack(path)
                
                # Unchoose: backtrack
                path.pop()
                used[i] = False
        
        backtrack([])
        return result