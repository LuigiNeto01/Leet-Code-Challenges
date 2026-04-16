from typing import List
import random

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Quickselect to find the k-th largest element in expected linear time.
        # Convert to finding the (n - k)-th smallest element (0-indexed).
        n = len(nums)
        target = n - k  # index of the k-th largest if array were sorted ascending
        
        # Defensive: if there's only one element, return it directly.
        if n == 1:
            return nums[0]
        
        left, right = 0, n - 1
        
        while left <= right:
            # Choose a random pivot index to avoid worst-case quadratic behavior.
            pivot_idx = random.randint(left, right)
            pivot_val = nums[pivot_idx]
            # Move pivot to end temporarily for Lomuto partition scheme.
            nums[pivot_idx], nums[right] = nums[right], nums[pivot_idx]
            
            store = left  # store is the position for the next element < pivot_val
            # Partition: elements < pivot_val to the left of 'store'
            for i in range(left, right):
                if nums[i] < pivot_val:
                    nums[store], nums[i] = nums[i], nums[store]
                    store += 1
            
            # Place pivot to its final sorted position (store)
            nums[store], nums[right] = nums[right], nums[store]
            # Now pivot is at index 'store' and all left < pivot and all right >= pivot
            
            # If pivot position matches target, we've found the answer.
            if store == target:
                return nums[store]
            # If pivot is left of target, search right partition.
            elif store < target:
                left = store + 1
            # If pivot is right of target, search left partition.
            else:
                right = store - 1
        
        # Fallback (the loop should always return before this for valid input).
        return nums[target]