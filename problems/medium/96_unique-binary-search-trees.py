class Solution:
    def numTrees(self, n: int) -> int:
        # Use dynamic programming to count unique BSTs
        # dp[i] = number of unique BSTs with i nodes
        dp = [0] * (n + 1)
        
        # Base cases: 0 nodes = 1 tree (empty), 1 node = 1 tree
        dp[0] = 1
        dp[1] = 1
        
        # For each number of nodes from 2 to n
        for nodes in range(2, n + 1):
            # Try each value as root (1 to nodes)
            for root in range(1, nodes + 1):
                # Left subtree has (root - 1) nodes
                # Right subtree has (nodes - root) nodes
                # Total combinations = left_trees * right_trees
                left_trees = dp[root - 1]
                right_trees = dp[nodes - root]
                dp[nodes] += left_trees * right_trees
        
        return dp[n]