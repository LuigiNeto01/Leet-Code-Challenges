from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        def backtrack(current, used):
            # Base case: permutation is complete when it has all elements
            if len(current) == len(nums):
                result.append(current[:])  # Append a copy of current permutation
                return
            
            # Try adding each unused number to current permutation
            for num in nums:
                if num not in used:
                    # Choose: add num to current permutation
                    current.append(num)
                    used.add(num)
                    
                    # Explore: recursively build rest of permutation
                    backtrack(current, used)
                    
                    # Unchoose: backtrack to try other options
                    current.pop()
                    used.remove(num)
        
        backtrack([], set())
        return result