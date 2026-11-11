from typing import List

class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        orig = grid[row][col]
        
        if orig == color:
            return grid
        
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = [[False] * n for _ in range(m)]
        component = []
        
        def dfs(r: int, c: int) -> None:
            if r < 0 or r >= m or c < 0 or c >= n:
                return
            if visited[r][c] or grid[r][c] != orig:
                return
            visited[r][c] = True
            component.append((r, c))
            for dr, dc in dirs:
                dfs(r + dr, c + dc)
        
        dfs(row, col)
        
        for (r, c) in component:
            if r == 0 or r == m-1 or c == 0 or c == n-1:
                grid[r][c] = color
                continue
            
            is_border = False
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if not visited[nr][nc]:
                    is_border = True
                    break
            if is_border:
                grid[r][c] = color
        
        return grid