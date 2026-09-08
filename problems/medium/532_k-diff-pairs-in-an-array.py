from typing import List
from collections import Counter

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        # Count frequency of each number
        freq = Counter(nums)
        pairs = 0

        if k == 0:
            # For k=0, we only care about numbers that appear at least twice
            for count in freq.values():
                if count >= 2:
                    pairs += 1
        else:
            # For k>0, look for (num, num+k) pairs
            for num in freq:
                if num + k in freq:
                    pairs += 1

        return pairs