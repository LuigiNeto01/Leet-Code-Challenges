from __future__ import annotations

class Solution:
    def isCousins(self, root: TreeNode | None, x: int, y: int) -> bool:
        # Use a queue for BFS: (node, parent, depth)
        queue = [(root, None, 0)]
        
        # Store info for the two target nodes
        x_depth = y_depth = -1
        x_parent = y_parent = None
        
        while queue:
            node, parent, depth = queue.pop(0)
            
            if node.val == x:
                x_depth, x_parent = depth, parent
            if node.val == y:
                y_depth, y_parent = depth, parent
            
            # If we've found both nodes, we can stop early
            if x_depth != -1 and y_depth != -1:
                break
            
            # Add children to queue (increase depth by 1)
            if node.left:
                queue.append((node.left, node, depth + 1))
            if node.right:
                queue.append((node.right, node, depth + 1))
        
        # Cousins: same depth, different parents
        return x_depth == y_depth and x_parent != y_parent