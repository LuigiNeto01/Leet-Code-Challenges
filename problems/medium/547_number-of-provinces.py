from typing import List

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [False] * n  # track which cities we've already visited
        provinces = 0

        # Recursively visit all cities in the same province (connected component)
        def dfs(city: int) -> None:
            visited[city] = True
            # Check all other cities for a direct connection
            for neighbor in range(n):
                if isConnected[city][neighbor] == 1 and not visited[neighbor]:
                    dfs(neighbor)

        # Start a DFS from each unvisited city; each DFS covers one province
        for i in range(n):
            if not visited[i]:
                provinces += 1  # new province found
                dfs(i)         # mark all cities in this province as visited

        return provinces