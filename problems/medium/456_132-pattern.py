from typing import List

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        # We need to find i < j < k where nums[i] < nums[k] < nums[j]
        # Strategy: traverse from right to left, maintain a stack and track the "middle" value (nums[k])
        # The stack helps us find candidates for nums[j] (the largest value)
        # We keep nums[k] as the largest value that is smaller than some nums[j] to its right
        
        n = len(nums)
        if n < 3:
            return False
        
        # Stack to maintain potential candidates for nums[j] (the peak)
        stack = []
        # nums_k tracks the best candidate for the middle value (nums[k])
        # It should be as large as possible while still being less than some nums[j]
        nums_k = float('-inf')
        
        # Traverse from right to left
        for i in range(n - 1, -1, -1):
            # If current number is less than nums_k, we found a valid 132 pattern
            # Current nums[i] < nums_k < some nums[j] where j > i
            if nums[i] < nums_k:
                return True
            
            # Update nums_k: pop all elements from stack that are smaller than nums[i]
            # These popped elements are potential candidates for nums[k]
            # nums[i] will be the new nums[j] (peak) for them
            while stack and stack[-1] < nums[i]:
                # Update nums_k to be the largest popped value
                # This ensures nums_k < nums[i] and nums_k is maximized
                nums_k = stack.pop()
            
            # Push current number as a potential nums[j] (peak)
            stack.append(nums[i])
        
        return False