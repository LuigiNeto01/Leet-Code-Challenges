from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # Merge nums2 into nums1 in-place. nums1 has size m + n with trailing zeros to fill.
        # We'll fill from the end to avoid overwriting elements in nums1 that we still need.
        
        # Pointers to the last valid elements in nums1 and nums2
        p1 = m - 1  # last element in the initial part of nums1
        p2 = n - 1  # last element in nums2
        # Pointer to place the next largest element in nums1 (end of merged array)
        p = m + n - 1
        
        # While both arrays have elements left, pick the larger tail element and place it at p
        while p1 >= 0 and p2 >= 0:
            # Compare tails; place the larger at position p
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1
        
        # If nums2 still has remaining elements, copy them.
        # (If nums1 has remaining elements, they are already in correct position so no action needed.)
        while p2 >= 0:
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1
        # Done. nums1 modified in-place to be the merged sorted array.