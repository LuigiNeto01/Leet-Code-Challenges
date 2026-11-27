from __future__ import annotations
import collections
import heapq
from typing import List

class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        # Count frequencies of each barcode value
        freq = collections.Counter(barcodes)
        
        # Use a max-heap (simulated with negative counts) to always get the most frequent element
        max_heap = [(-count, value) for value, count in freq.items()]
        heapq.heapify(max_heap)
        
        result = []
        
        # While we have at least two distinct elements to place
        while len(max_heap) >= 2:
            # Pop the two most frequent barcodes
            neg_count1, val1 = heapq.heappop(max_heap)
            neg_count2, val2 = heapq.heappop(max_heap)
            
            # Place them (order doesn't matter, they are different)
            result.append(val1)
            result.append(val2)
            
            # Decrease counts (negative counts → increase towards zero)
            # If still remaining, push back onto heap
            if neg_count1 + 1 < 0:   # means original count > 1
                heapq.heappush(max_heap, (neg_count1 + 1, val1))
            if neg_count2 + 1 < 0:
                heapq.heappush(max_heap, (neg_count2 + 1, val2))
        
        # If one element left, append it at the end (cannot create adjacent equal)
        if max_heap:
            result.append(max_heap[0][1])
        
        return result