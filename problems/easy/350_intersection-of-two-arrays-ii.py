from typing import List
from collections import Counter

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Count frequency of each element in both arrays
        count1 = Counter(nums1)
        count2 = Counter(nums2)
        
        result = []
        
        # For each unique element in nums1
        for num in count1:
            # If it also exists in nums2, add it to result
            # The number of times we add it is the minimum of both counts
            if num in count2:
                # Add the element min(count1[num], count2[num]) times
                result.extend([num] * min(count1[num], count2[num]))
        
        return result