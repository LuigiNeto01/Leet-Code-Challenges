from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []
        
        m, n = len(heights), len(heights[0])
        
        # Track which cells can reach Pacific and Atlantic
        pacific = set()
        atlantic = set()
        
        def dfs(r, c, visited, prev_height):
            # Check boundaries and if already visited
            if (r < 0 or r >= m or c < 0 or c >= n or 
                (r, c) in visited or 
                heights[r][c] < prev_height):  # Water flows to lower/equal height
                return
            
            visited.add((r, c))
            
            # Explore all 4 directions
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                dfs(r + dr, c + dc, visited, heights[r][c])
        
        # Start DFS from Pacific Ocean borders (top and left edges)
        for i in range(m):
            dfs(i, 0, pacific, heights[i][0])  # Left edge
        for j in range(n):
            dfs(0, j, pacific, heights[0][j])  # Top edge
        
        # Start DFS from Atlantic Ocean borders (bottom and right edges)
        for i in range(m):
            dfs(i, n - 1, atlantic, heights[i][n - 1])  # Right edge
        for j in range(n):
            dfs(m - 1, j, atlantic, heights[m - 1][j])  # Bottom edge
        
        # Find cells that can reach both oceans (intersection)
        result = []
        for r, c in pacific:
            if (r, c) in atlantic:
                result.append([r, c])
        
        return result