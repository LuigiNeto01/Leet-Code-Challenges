from typing import List
import heapq


class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        if not heightMap or not heightMap[0]:
            return 0

        m = len(heightMap)
        n = len(heightMap[0])
        if m < 3 or n < 3:
            return 0

        if m == 3 and n == 3:
            boundary_min = min(
                heightMap[0][0],
                heightMap[0][1],
                heightMap[0][2],
                heightMap[1][0],
                heightMap[1][2],
                heightMap[2][0],
                heightMap[2][1],
                heightMap[2][2],
            )
            return max(0, boundary_min - heightMap[1][1])

        visited = [[False] * n for _ in range(m)]
        heap = []

        for r in range(m):
            for c in (0, n - 1):
                if not visited[r][c]:
                    visited[r][c] = True
                    heapq.heappush(heap, (heightMap[r][c], r, c))

        for c in range(n):
            for r in (0, m - 1):
                if not visited[r][c]:
                    visited[r][c] = True
                    heapq.heappush(heap, (heightMap[r][c], r, c))

        trapped = 0
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

        while heap:
            water_level, r, c = heapq.heappop(heap)

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if nr < 0 or nr >= m or nc < 0 or nc >= n or visited[nr][nc]:
                    continue

                visited[nr][nc] = True
                neighbor_height = heightMap[nr][nc]

                if neighbor_height < water_level:
                    trapped += water_level - neighbor_height

                heapq.heappush(heap, (max(water_level, neighbor_height), nr, nc))

        return trapped