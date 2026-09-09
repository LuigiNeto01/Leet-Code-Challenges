from __future__ import annotations

# Definition for a QuadTree node.
class Node:
    def __init__(self, val: bool, isLeaf: bool, topLeft: Node | None = None,
                 topRight: Node | None = None, bottomLeft: Node | None = None,
                 bottomRight: Node | None = None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def intersect(self, quadTree1: 'Node', quadTree2: 'Node') -> 'Node':
        # If either tree is a leaf, we can shortcut the OR logic.
        # Leaf with val=True -> OR result is True (all ones in that region)
        # Leaf with val=False -> OR result is just the other tree.
        if quadTree1.isLeaf:
            # If quadTree1 leaf is True (1), result is a True leaf
            if quadTree1.val:
                return Node(True, True)
            # Otherwise quadTree1 is False (0), result is just quadTree2
            return quadTree2
        if quadTree2.isLeaf:
            # Symmetric logic: if quadTree2 leaf is True, result is True leaf
            if quadTree2.val:
                return Node(True, True)
            # Otherwise quadTree2 is False, result is quadTree1
            return quadTree1

        # Both are internal nodes: recursively OR each of the four quadrants
        topLeft = self.intersect(quadTree1.topLeft, quadTree2.topLeft)
        topRight = self.intersect(quadTree1.topRight, quadTree2.topRight)
        bottomLeft = self.intersect(quadTree1.bottomLeft, quadTree2.bottomLeft)
        bottomRight = self.intersect(quadTree1.bottomRight, quadTree2.bottomRight)

        # After merging children, check if all four are leaves with same value.
        # If so, we can merge them into a single leaf node (optimization).
        if (topLeft.isLeaf and topRight.isLeaf and
            bottomLeft.isLeaf and bottomRight.isLeaf and
            topLeft.val == topRight.val == bottomLeft.val == bottomRight.val):
            return Node(topLeft.val, True)
        
        # Otherwise, return a new internal node with the merged children
        return Node(False, False, topLeft, topRight, bottomLeft, bottomRight)