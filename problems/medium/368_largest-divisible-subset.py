from typing import List

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        # Sort nums so that for any valid subset, smaller elements come first
        # This allows us to use DP: if a > b and a % b == 0, then a can extend b's subset
        nums.sort()
        n = len(nums)
        
        # dp[i] = length of the largest divisible subset ending at nums[i]
        dp = [1] * n
        
        # parent[i] = index of the previous element in the largest subset ending at i
        # -1 means no parent (start of chain)
        parent = [-1] * n
        
        # Track the index with maximum subset length
        max_len = 1
        max_idx = 0
        
        # Build dp table
        for i in range(1, n):
            for j in range(i):
                # If nums[i] is divisible by nums[j], nums[i] can extend the subset ending at j
                if nums[i] % nums[j] == 0:
                    # Update if this gives a longer subset
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        parent[i] = j
            
            # Track the maximum subset length and its ending index
            if dp[i] > max_len:
                max_len = dp[i]
                max_idx = i
        
        # Reconstruct the subset by following parent pointers backwards
        result = []
        idx = max_idx
        while idx != -1:
            result.append(nums[idx])
            idx = parent[idx]
        
        # Reverse to get the subset in ascending order (optional, problem allows any order)
        result.reverse()
        
        return result