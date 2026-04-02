from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Convert both arrays to sets so duplicates are removed automatically.
        set1 = set(nums1)
        set2 = set(nums2)

        # Set intersection keeps only values present in both arrays.
        # Order does not matter for this problem.
        return list(set1 & set2)