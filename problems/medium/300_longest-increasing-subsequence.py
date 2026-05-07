from typing import List
import bisect

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Use binary search approach for O(n log n) time complexity
        # tails[i] stores the smallest tail element of all increasing subsequences of length i+1
        tails = []
        
        for num in nums:
            # Find the position where num should be inserted to keep tails sorted
            # bisect_left returns the leftmost position where num can be inserted
            pos = bisect.bisect_left(tails, num)
            
            # If pos equals length of tails, num is larger than all elements
            # This extends the longest increasing subsequence
            if pos == len(tails):
                tails.append(num)
            else:
                # Replace the element at pos with num
                # This maintains the invariant that tails[i] is the smallest tail
                # for subsequences of length i+1
                tails[pos] = num
        
        # Length of tails array is the length of longest increasing subsequence
        return len(tails)