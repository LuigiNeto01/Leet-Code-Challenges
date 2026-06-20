from typing import List

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        # Use modified merge sort to count reverse pairs
        # During merge, we can count pairs where nums[i] > 2 * nums[j] with i < j
        
        def merge_sort_and_count(arr, start, end):
            # Base case: single element or empty
            if end - start <= 1:
                return 0
            
            mid = (start + end) // 2
            
            # Recursively count in left and right halves
            count = merge_sort_and_count(arr, start, mid)
            count += merge_sort_and_count(arr, mid, end)
            
            # Count cross pairs where i is in left half, j is in right half
            # We need nums[i] > 2 * nums[j] where i < j
            j = mid
            for i in range(start, mid):
                # Find how many elements in right half satisfy nums[i] > 2 * nums[j]
                # Since right half will be sorted, we can use two pointers
                while j < end and arr[i] > 2 * arr[j]:
                    j += 1
                count += j - mid
            
            # Merge the two sorted halves
            merged = []
            left_idx = start
            right_idx = mid
            
            while left_idx < mid and right_idx < end:
                if arr[left_idx] <= arr[right_idx]:
                    merged.append(arr[left_idx])
                    left_idx += 1
                else:
                    merged.append(arr[right_idx])
                    right_idx += 1
            
            # Add remaining elements
            while left_idx < mid:
                merged.append(arr[left_idx])
                left_idx += 1
            
            while right_idx < end:
                merged.append(arr[right_idx])
                right_idx += 1
            
            # Copy merged array back to original
            for i, val in enumerate(merged):
                arr[start + i] = val
            
            return count
        
        return merge_sort_and_count(nums, 0, len(nums))