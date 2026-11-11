# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        total_sum = 0
        stack = [(root, 0)]
        
        while stack:
            node, current_val = stack.pop()
            if node:
                current_val = (current_val << 1) | node.val
                
                if not node.left and not node.right:
                    total_sum += current_val
                else:
                    if node.right:
                        stack.append((node.right, current_val))
                    if node.left:
                        stack.append((node.left, current_val))
        
        return total_sum