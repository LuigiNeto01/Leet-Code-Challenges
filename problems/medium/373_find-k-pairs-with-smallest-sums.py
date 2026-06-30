from typing import List
import heapq

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        # Edge case: if either array is empty, no pairs possible
        if not nums1 or not nums2:
            return []
        
        # Result list to store k smallest pairs
        result = []
        
        # Min heap to track candidates: (sum, index_in_nums1, index_in_nums2)
        # Start with pairs formed by first element of nums1 with all elements of nums2
        # But only initialize with first element of nums1 paired with first of nums2
        # We'll expand candidates as we go
        heap = []
        
        # Initialize heap with pairs of nums1[0] with each element in nums2
        # Limit initial candidates to min(k, len(nums2)) to avoid unnecessary space
        for j in range(min(k, len(nums2))):
            heapq.heappush(heap, (nums1[0] + nums2[j], 0, j))
        
        # Extract k smallest pairs
        while heap and len(result) < k:
            # Pop the pair with smallest sum
            current_sum, i, j = heapq.heappop(heap)
            result.append([nums1[i], nums2[j]])
            
            # If we can move to next element in nums1 with same nums2[j]
            # Only push if this is the first time we're using nums2[j]
            # (i.e., when i == 0) to avoid duplicates
            if i == 0 and i + 1 < len(nums1):
                heapq.heappush(heap, (nums1[i + 1] + nums2[j], i + 1, j))
        
        return result