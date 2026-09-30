class Solution:
    def allPathsSourceTarget(self, graph: list[list[int]]) -> list[list[int]]:
        n = len(graph)
        target = n - 1
        paths = []
        path = [0]

        def dfs(node: int) -> None:
            # If we reached the target, save a copy of the current path.
            if node == target:
                paths.append(path[:])
                return

            # Explore every outgoing edge from the current node.
            for neighbor in graph[node]:
                path.append(neighbor)
                dfs(neighbor)
                path.pop()  # Backtrack: remove the neighbor before trying another.

        dfs(0)
        return paths