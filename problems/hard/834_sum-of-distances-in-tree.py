class Solution:
    def sumOfDistancesInTree(self, n: int, edges: list[list[int]]) -> list[int]:
        # Build adjacency list for the tree
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # count[i] = size of subtree rooted at i when tree is rooted at 0
        # depth[i] = distance from node 0 to i
        count = [0] * n
        depth = [0] * n

        # Iterative postorder DFS to compute subtree sizes and depths
        # Each stack element: (node, parent, state)
        # state = 0: entering node; 1: exiting node after processing children
        stack = [(0, -1, 0)]
        while stack:
            node, parent, state = stack.pop()
            if state == 0:  # entering
                # Schedule exit after children
                stack.append((node, parent, 1))
                for nb in graph[node]:
                    if nb != parent:
                        # Set depth for child before pushing it
                        depth[nb] = depth[node] + 1
                        stack.append((nb, node, 0))
            else:  # exiting - compute subtree size
                total = 1  # count the node itself
                for nb in graph[node]:
                    if nb != parent:
                        total += count[nb]
                count[node] = total

        # Sum of distances from root (node 0) to all nodes
        ans = [0] * n
        ans[0] = sum(depth)

        # Second pass: use DP to compute answer for all nodes
        # Formula: ans[child] = ans[parent] + n - 2 * count[child]
        stack = [(0, -1)]
        while stack:
            node, parent = stack.pop()
            for nb in graph[node]:
                if nb != parent:
                    ans[nb] = ans[node] + n - 2 * count[nb]
                    stack.append((nb, node))

        return ans