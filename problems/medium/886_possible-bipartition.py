from collections import deque

class Solution:
    def possibleBipartition(self, n: int, dislikes: list[list[int]]) -> bool:
        # People are labeled 1..n; we will use 0-indexed internally.
        # Build adjacency list for the graph of dislikes (undirected).
        graph = [[] for _ in range(n)]
        for u, v in dislikes:
            u -= 1  # convert to 0-index
            v -= 1
            graph[u].append(v)
            graph[v].append(u)

        # color[i] = 0 (uncolored), 1 (group A) or -1 (group B)
        color = [0] * n

        # BFS to try to assign colors to all nodes in a connected component.
        # If a conflict is found, bipartition is impossible.
        for start in range(n):
            if color[start] != 0:
                continue  # already colored in some component

            # Start BFS from this node, assign it to group 1.
            queue = deque([start])
            color[start] = 1

            while queue:
                node = queue.popleft()
                current_color = color[node]
                neighbor_color = -current_color  # must be opposite group

                for neighbor in graph[node]:
                    if color[neighbor] == 0:
                        color[neighbor] = neighbor_color
                        queue.append(neighbor)
                    elif color[neighbor] != neighbor_color:
                        # Conflict: neighbor has same color as current node
                        return False

        # All components are bipartite.
        return True