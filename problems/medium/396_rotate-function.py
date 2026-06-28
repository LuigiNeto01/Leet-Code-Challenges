from typing import List

class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Edge case: single element
        if n == 1:
            return 0
        
        # Calculate F(0) and sum of all elements
        # F(0) = 0*nums[0] + 1*nums[1] + 2*nums[2] + ... + (n-1)*nums[n-1]
        total_sum = sum(nums)
        f_curr = sum(i * nums[i] for i in range(n))
        
        # Track maximum value starting with F(0)
        max_f = f_curr
        
        # Key insight: when rotating clockwise by 1 position,
        # F(k) = F(k-1) + total_sum - n * nums[n-k]
        # 
        # Explanation: when we rotate right by 1:
        # - All elements (except the last) increase their index by 1, contributing +total_sum
        # - The last element moves to front (index 0), losing (n-1) weight, contributing -n*nums[last]
        # - Net change: F(k) = F(k-1) + total_sum - n*nums[n-k]
        
        for k in range(1, n):
            # Element that was at index (n-k) moves to the front
            # It previously contributed (n-1) * nums[n-k], now contributes 0
            # All other elements shift right, each gaining +1 in their coefficient
            f_curr = f_curr + total_sum - n * nums[n - k]
            max_f = max(max_f, f_curr)
        
        return max_f