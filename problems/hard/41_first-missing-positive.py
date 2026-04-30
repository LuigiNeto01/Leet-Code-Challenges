from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Step 1: Mark out-of-range numbers (<=0 or >n) by replacing with n+1
        # The first missing positive must be in range [1, n+1]
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = n + 1
        
        # Step 2: Use index as a hash key. For each number x in [1,n],
        # mark nums[x-1] as negative to indicate x is present
        for i in range(n):
            num = abs(nums[i])
            if num <= n:
                # Mark the position (num-1) as visited by making it negative
                nums[num - 1] = -abs(nums[num - 1])
        
        # Step 3: Find the first index that's still positive
        # That index+1 is the first missing positive
        for i in range(n):
            if nums[i] > 0:
                return i + 1
        
        # If all positions [1,n] are marked, the answer is n+1
        return n + 1