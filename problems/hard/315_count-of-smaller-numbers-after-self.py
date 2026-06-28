from typing import List

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        # Use merge sort approach to count inversions
        # Each element tracks how many smaller elements appear to its right
        
        n = len(nums)
        # Create array of (value, original_index) pairs to track positions
        indexed_nums = [(num, i) for i, num in enumerate(nums)]
        counts = [0] * n
        
        def merge_sort(arr):
            # Base case: array of length 0 or 1 is already sorted
            if len(arr) <= 1:
                return arr
            
            mid = len(arr) // 2
            left = merge_sort(arr[:mid])
            right = merge_sort(arr[mid:])
            
            # Merge and count
            merged = []
            i = j = 0
            
            while i < len(left) and j < len(right):
                # If left element is smaller or equal, no inversions with remaining right elements yet
                if left[i][0] <= right[j][0]:
                    # All elements in right[:j] are smaller than left[i] and were originally to its right
                    counts[left[i][1]] += j
                    merged.append(left[i])
                    i += 1
                else:
                    # right[j] is smaller than left[i], will be counted when we process left[i]
                    merged.append(right[j])
                    j += 1
            
            # Process remaining left elements
            while i < len(left):
                # All elements in right subarray are smaller than this left element
                counts[left[i][1]] += j
                merged.append(left[i])
                i += 1
            
            # Process remaining right elements (no inversions to count here)
            while j < len(right):
                merged.append(right[j])
                j += 1
            
            return merged
        
        merge_sort(indexed_nums)
        return counts