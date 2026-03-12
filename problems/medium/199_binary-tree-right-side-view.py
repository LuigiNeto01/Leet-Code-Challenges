from __future__ import annotations

from collections import deque
from typing import List, Optional

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # Empty tree has no visible nodes
        if not root:
            return []
        
        result = []
        queue = deque([root])
        
        # Process the tree level by level
        while queue:
            level_size = len(queue)
            
            # Visit every node in the current depth
            for i in range(level_size):
                node = queue.popleft()
                
                # The last node seen in this level is the rightmost one
                if i == level_size - 1:
                    result.append(node.val)
                
                # Standard BFS expansion for the next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return result