from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Iterative approach using a stack (follows the problem's follow-up suggestion)
        # Preorder: root -> left -> right
        
        result = []
        
        # Handle empty tree edge case
        if not root:
            return result
        
        # Use stack to simulate recursion
        # Stack stores nodes to be processed
        stack = [root]
        
        while stack:
            # Pop the top node (current root)
            node = stack.pop()
            
            # Visit the node (add to result)
            result.append(node.val)
            
            # Push right child first so left child is processed first
            # (stack is LIFO, so right goes in before left)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        
        return result