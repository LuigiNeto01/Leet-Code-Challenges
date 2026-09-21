from typing import List

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        # Iterative postorder traversal using a stack
        if not root:
            return []
        
        result = []
        stack = [root]
        
        # Standard trick: push node, then children, but we'll reverse result at end
        while stack:
            node = stack.pop()
            result.append(node.val)
            # Push all children; leftmost will be processed last (due to stack)
            for child in node.children:
                stack.append(child)
        
        # Reversing gives left-to-right children, then root
        return result[::-1]