from __future__ import annotations
from typing import List, Optional
import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Use a min-heap to efficiently get the smallest element among k lists
        # Heap stores tuples: (node_value, unique_index, node)
        # unique_index breaks ties when values are equal (avoids comparing ListNode objects)
        
        min_heap = []
        
        # Initialize heap with the head of each non-empty list
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(min_heap, (node.val, i, node))
        
        # Dummy head to simplify list construction
        dummy = ListNode(0)
        current = dummy
        
        # Counter for unique indexing when adding new nodes
        index = len(lists)
        
        # Extract minimum node from heap, add to result, push next node from same list
        while min_heap:
            val, _, node = heapq.heappop(min_heap)
            
            # Append the smallest node to our result list
            current.next = node
            current = current.next
            
            # If this list has more nodes, push the next one to heap
            if node.next:
                heapq.heappush(min_heap, (node.next.val, index, node.next))
                index += 1
        
        return dummy.next