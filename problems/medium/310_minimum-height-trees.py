from typing import List
from collections import deque, defaultdict

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # Edge case: single node tree
        if n == 1:
            return [0]
        
        # Edge case: two nodes
        if n == 2:
            return [0, 1]
        
        # Build adjacency list for the graph
        graph = defaultdict(set)
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)
        
        # Find all leaf nodes (nodes with degree 1)
        leaves = deque()
        for node in range(n):
            if len(graph[node]) == 1:
                leaves.append(node)
        
        # Trim leaves layer by layer until we reach the center(s)
        # The center will be the root(s) of minimum height trees
        remaining_nodes = n
        
        while remaining_nodes > 2:
            # Number of leaves in current layer
            leaves_count = len(leaves)
            remaining_nodes -= leaves_count
            
            # Process all leaves in current layer
            for _ in range(leaves_count):
                leaf = leaves.popleft()
                
                # For each neighbor of the current leaf
                # (there should be only one neighbor for a leaf)
                neighbor = graph[leaf].pop()
                
                # Remove the leaf from its neighbor's adjacency list
                graph[neighbor].discard(leaf)
                
                # If neighbor becomes a leaf after removal, add to queue
                if len(graph[neighbor]) == 1:
                    leaves.append(neighbor)
        
        # The remaining nodes are the roots of MHTs
        # There can be at most 2 such nodes (the center of the tree)
        return list(leaves)