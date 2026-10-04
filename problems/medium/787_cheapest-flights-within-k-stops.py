class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        INF = 10**9 + 7  # large value representing infinity

        # dist[i] = cheapest price from src to city i using at most the current number of edges
        dist = [INF] * n
        dist[src] = 0

        # We can take at most k stops, meaning at most k+1 edges.
        # Perform k+1 iterations of edge relaxations.
        for _ in range(k + 1):
            # Use a copy of the previous distances to ensure each iteration
            # only extends paths by exactly one edge (no 'chain' within the same iteration)
            new_dist = dist[:]

            for u, v, price in flights:
                # If we can reach u with a finite cost, consider extending to v
                if dist[u] != INF and dist[u] + price < new_dist[v]:
                    new_dist[v] = dist[u] + price

            dist = new_dist

        # If dst remains unreachable, return -1; otherwise return the cheapest cost
        return -1 if dist[dst] == INF else dist[dst]