from __future__ import annotations

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        # Use preorder traversal to serialize the tree
        # Store null nodes as 'N' to preserve structure
        result = []
        
        def preorder(node):
            if node is None:
                result.append('N')
                return
            # Append current node value
            result.append(str(node.val))
            # Recursively serialize left and right subtrees
            preorder(node.left)
            preorder(node.right)
        
        preorder(root)
        # Join all values with comma separator
        return ','.join(result)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        # Split the serialized string back into list of values
        values = data.split(',')
        # Use index to track position in values list
        self.index = 0
        
        def build():
            # If we've exhausted all values or encounter null marker
            if self.index >= len(values) or values[self.index] == 'N':
                self.index += 1
                return None
            
            # Create node with current value
            node = TreeNode(int(values[self.index]))
            self.index += 1
            
            # Recursively build left and right subtrees
            # Order matches preorder traversal from serialization
            node.left = build()
            node.right = build()
            
            return node
        
        return build()