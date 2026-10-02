from typing import List
import heapq

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        # Goal is to minimize the maximum elevation along any path from (0,0) to (n-1,n-1).
        # Dijkstra's algorithm with edge cost = max(u_elev, v_elev).
        # Start with initial elevation at (0,0) as the current max.
        visited = [[False] * n for _ in range(n)]
        # Min-heap entries: (max_elevation_so_far, row, col)
        heap = [(grid[0][0], 0, 0)]
        
        # Directions: up, down, left, right
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        
        while heap:
            t, i, j = heapq.heappop(heap)
            # If we already visited this cell with a smaller max, skip.
            if visited[i][j]:
                continue
            visited[i][j] = True
            
            # If we reached the bottom-right cell, current t is the answer.
            if i == n-1 and j == n-1:
                return t
            
            # Explore neighbors.
            for di, dj in dirs:
                ni, nj = i + di, j + dj
                if 0 <= ni < n and 0 <= nj < n and not visited[ni][nj]:
                    # New max elevation on the path to neighbor.
                    new_t = max(t, grid[ni][nj])
                    heapq.heappush(heap, (new_t, ni, nj))
        
        # The loop is guaranteed to reach the destination because the grid is connected.
        return -1  # Should never happen given problem constraints.