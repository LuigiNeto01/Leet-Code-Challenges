from collections import defaultdict
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        freq = defaultdict(int)

        def dfs(node: Optional[TreeNode]) -> None:
            if not node:
                return
            freq[node.val] += 1
            dfs(node.left)
            dfs(node.right)

        dfs(root)

        max_count = max(freq.values()) if freq else 0
        return [val for val, cnt in freq.items() if cnt == max_count]