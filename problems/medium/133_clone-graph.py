from typing import Optional

class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # Handle empty graph
        if not node:
            return None
        
        # Map from original node to cloned node
        cloned = {}
        
        # DFS to clone all nodes and their connections
        def dfs(original_node):
            # If already cloned, return the clone
            if original_node in cloned:
                return cloned[original_node]
            
            # Create a new node with the same value
            clone = Node(original_node.val)
            # Store in map before processing neighbors to handle cycles
            cloned[original_node] = clone
            
            # Recursively clone all neighbors
            for neighbor in original_node.neighbors:
                clone.neighbors.append(dfs(neighbor))
            
            return clone
        
        return dfs(node)