from __future__ import annotations
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # Base case: empty tree or key not found
        if not root:
            return None
        
        # Navigate to the node to delete using BST property
        if key < root.val:
            # Key is in left subtree
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            # Key is in right subtree
            root.right = self.deleteNode(root.right, key)
        else:
            # Found the node to delete
            
            # Case 1: Node has no left child (includes leaf node)
            # Replace node with its right child (which may be None)
            if not root.left:
                return root.right
            
            # Case 2: Node has no right child
            # Replace node with its left child
            if not root.right:
                return root.left
            
            # Case 3: Node has both children
            # Find the inorder successor (smallest node in right subtree)
            # This maintains BST property: successor > all left subtree nodes
            successor = self._find_min(root.right)
            
            # Replace current node's value with successor's value
            root.val = successor.val
            
            # Delete the successor from right subtree
            # (successor is guaranteed to have at most one child - the right one)
            root.right = self.deleteNode(root.right, successor.val)
        
        return root
    
    def _find_min(self, node: TreeNode) -> TreeNode:
        # Find leftmost (minimum) node in a subtree
        while node.left:
            node = node.left
        return node