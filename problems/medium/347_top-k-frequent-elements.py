from typing import List
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Count frequency of each element using Counter
        freq_map = Counter(nums)
        
        # Bucket sort approach: create buckets where index = frequency
        # Maximum possible frequency is len(nums)
        buckets = [[] for _ in range(len(nums) + 1)]
        
        # Place each number in bucket corresponding to its frequency
        for num, freq in freq_map.items():
            buckets[freq].append(num)
        
        # Collect top k frequent elements by iterating buckets from high to low frequency
        result = []
        for i in range(len(buckets) - 1, 0, -1):
            # Add all numbers with frequency i to result
            for num in buckets[i]:
                result.append(num)
                # Stop once we have k elements
                if len(result) == k:
                    return result
        
        return result