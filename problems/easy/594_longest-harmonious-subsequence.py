from collections import Counter
from typing import List

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        """
        Returns the length of the longest harmonious subsequence.
        A harmonious subsequence has max and min differing by exactly 1.
        """
        # Count frequencies of each number
        freq = Counter(nums)

        max_len = 0
        # For each number, check if the next consecutive number exists
        for x in freq:
            if x + 1 in freq:
                # The subsequence can consist of all occurrences of x and x+1
                current_len = freq[x] + freq[x + 1]
                if current_len > max_len:
                    max_len = current_len

        return max_len