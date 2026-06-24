from typing import List

class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        # Strategy: Try all possible splits: take i digits from nums1 and k-i from nums2
        # For each split, find the max subsequence from each array, then merge them optimally
        
        def maxSubsequence(nums, length):
            # Extract the lexicographically maximum subsequence of given length from nums
            # using a monotonic stack approach
            if length == 0:
                return []
            if length > len(nums):
                return []
            
            stack = []
            to_drop = len(nums) - length  # how many elements we can afford to drop
            
            for num in nums:
                # Pop smaller elements if we still have drops remaining
                while stack and stack[-1] < num and to_drop > 0:
                    stack.pop()
                    to_drop -= 1
                stack.append(num)
            
            # Return exactly 'length' elements
            return stack[:length]
        
        def merge(seq1, seq2):
            # Merge two sequences to create the lexicographically maximum result
            result = []
            i, j = 0, 0
            
            while i < len(seq1) and j < len(seq2):
                # Choose the larger option; if equal, look ahead to decide
                # Compare remaining subsequences to break ties
                if seq1[i:] > seq2[j:]:
                    result.append(seq1[i])
                    i += 1
                else:
                    result.append(seq2[j])
                    j += 1
            
            # Append remaining elements
            result.extend(seq1[i:])
            result.extend(seq2[j:])
            
            return result
        
        max_result = []
        
        # Try all valid splits: take i from nums1, k-i from nums2
        for i in range(k + 1):
            j = k - i
            
            # Check if this split is valid
            if i > len(nums1) or j > len(nums2):
                continue
            
            # Get max subsequences of required lengths
            sub1 = maxSubsequence(nums1, i)
            sub2 = maxSubsequence(nums2, j)
            
            # Merge them to get candidate result
            candidate = merge(sub1, sub2)
            
            # Keep track of the maximum result
            if candidate > max_result:
                max_result = candidate
        
        return max_result