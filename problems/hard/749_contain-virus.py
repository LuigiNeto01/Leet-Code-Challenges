from __future__ import annotations
from typing import List
from collections import deque

class Solution:
    def containVirus(self, isInfected: List[List[int]]) -> int:
        m, n = len(isInfected), len(isInfected[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        walls_used = 0
        
        while True:
            # Find all connected components of infected cells
            visited = [[False] * n for _ in range(m)]
            regions = []  # each element: (set of infected cells, set of frontier cells, walls needed)
            
            for i in range(m):
                for j in range(n):
                    if isInfected[i][j] == 1 and not visited[i][j]:
                        # BFS to find this infected region
                        q = deque([(i, j)])
                        visited[i][j] = True
                        infected_cells = set()
                        frontier = set()
                        walls_needed = 0
                        
                        while q:
                            x, y = q.popleft()
                            infected_cells.add((x, y))
                            
                            for dx, dy in dirs:
                                nx, ny = x + dx, y + dy
                                if 0 <= nx < m and 0 <= ny < n:
                                    if isInfected[nx][ny] == 0:
                                        # uninfected neighbor -> this is a frontier cell
                                        frontier.add((nx, ny))
                                        walls_needed += 1
                                    elif isInfected[nx][ny] == 1 and not visited[nx][ny]:
                                        visited[nx][ny] = True
                                        q.append((nx, ny))
                        
                        regions.append((len(frontier), len(infected_cells), (i, j), frontier, walls_needed))
            
            if not regions:
                break
                
            # Find region with max threatened cells (frontier size)
            # Problem says there will never be a tie
            max_frontier = max(regions, key=lambda x: x[0])
            
            # Add walls for the chosen region
            walls_used += max_frontier[4]
            
            # Quarantine this region by marking it as 2 (contained, cannot spread)
            start = max_frontier[2]
            q = deque([start])
            contained = set()
            contained.add(start)
            while q:
                x, y = q.popleft()
                isInfected[x][y] = 2
                for dx, dy in dirs:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and isInfected[nx][ny] == 1 and (nx, ny) not in contained:
                        contained.add((nx, ny))
                        q.append((nx, ny))
            
            # Spread the virus for all other regions
            new_infections = []
            for region in regions:
                if region is not max_frontier:
                    for cell in region[3]:
                        new_infections.append(cell)
            
            # Apply all infections simultaneously
            for x, y in new_infections:
                isInfected[x][y] = 1
            
            # If no more infected cells, we're done
            if all(cell != 1 for row in isInfected for cell in row):
                break
                
        return walls_used