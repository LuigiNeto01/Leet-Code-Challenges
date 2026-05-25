from __future__ import annotations
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        # Base case: empty list
        if not head:
            return None
        
        # Base case: single node
        if not head.next:
            return TreeNode(head.val)
        
        # Find the middle node using slow-fast pointer technique
        # slow will point to the middle, prev will be the node before middle
        slow = head
        fast = head
        prev = None
        
        # Fast pointer moves 2 steps, slow moves 1 step
        # When fast reaches end, slow is at middle
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        # Disconnect the left half from the middle node
        if prev:
            prev.next = None
        
        # Middle node becomes the root (for balanced BST)
        root = TreeNode(slow.val)
        
        # Recursively build left subtree from left half
        # (head to prev, which is now disconnected)
        root.left = self.sortedListToBST(head)
        
        # Recursively build right subtree from right half
        # (nodes after slow)
        root.right = self.sortedListToBST(slow.next)
        
        return root