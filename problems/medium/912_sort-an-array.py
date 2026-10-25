class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        # Recursive merge sort on the entire array
        def merge_sort(arr, left, right):
            # Base case: single element or empty subarray
            if left >= right:
                return
            # Find middle index
            mid = (left + right) // 2
            # Sort left half and right half recursively
            merge_sort(arr, left, mid)
            merge_sort(arr, mid + 1, right)
            
            # Merge the two sorted halves
            temp = []  # temporary array for merging
            i, j = left, mid + 1
            # Compare and add smaller element to temp
            while i <= mid and j <= right:
                if arr[i] <= arr[j]:
                    temp.append(arr[i])
                    i += 1
                else:
                    temp.append(arr[j])
                    j += 1
            # Add remaining elements from left half
            while i <= mid:
                temp.append(arr[i])
                i += 1
            # Add remaining elements from right half
            while j <= right:
                temp.append(arr[j])
                j += 1
            # Copy merged result back to original array
            for k in range(len(temp)):
                arr[left + k] = temp[k]
        
        # Start merge sort on the whole array
        merge_sort(nums, 0, len(nums) - 1)
        return nums