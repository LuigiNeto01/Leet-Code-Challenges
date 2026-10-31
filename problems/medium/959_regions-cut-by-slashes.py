from __future__ import annotations

class Solution:
    def regionsBySlashes(self, grid: list[str]) -> int:
        # Use Union-Find (Disjoint Set Union) with 4 triangles per cell.
        # Each 1x1 cell is split into 4 triangles indexed 0-3:
        #   0: top triangle
        #   1: right triangle
        #   2: bottom triangle
        #   3: left triangle
        # When no slash: all 4 triangles are connected.
        # When '/' : connects 0-3 (top-left) and 1-2 (bottom-right).
        # When '\' : connects 0-1 (top-right) and 2-3 (bottom-left).
        # Additionally, adjacent cells share edges: 
        #   - right neighbor: right triangle (1) of left cell connects with left triangle (3) of right cell.
        #   - bottom neighbor: bottom triangle (2) of top cell connects with top triangle (0) of bottom cell.

        n = len(grid)
        total_triangles = n * n * 4
        
        parent = list(range(total_triangles))
        rank = [0] * total_triangles
        
        def find(x: int) -> int:
            # Path compression for efficiency
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(a: int, b: int) -> None:
            # Union by rank
            ra, rb = find(a), find(b)
            if ra == rb:
                return
            if rank[ra] < rank[rb]:
                parent[ra] = rb
            elif rank[ra] > rank[rb]:
                parent[rb] = ra
            else:
                parent[rb] = ra
                rank[ra] += 1
        
        # Process each cell and its internal connections
        for r in range(n):
            for c in range(n):
                # Base index for the 4 triangles of cell (r,c)
                base = (r * n + c) * 4
                ch = grid[r][c]
                
                if ch == ' ':
                    # No slash: connect all 4 triangles in a cycle
                    union(base + 0, base + 1)
                    union(base + 1, base + 2)
                    union(base + 2, base + 3)
                elif ch == '/':
                    # Slash divides: top-left (0-3) and bottom-right (1-2)
                    union(base + 0, base + 3)
                    union(base + 1, base + 2)
                else:  # ch == '\\'
                    # Backslash divides: top-right (0-1) and bottom-left (2-3)
                    union(base + 0, base + 1)
                    union(base + 2, base + 3)
                
                # Connect to right neighbor (if exists)
                if c + 1 < n:
                    right_base = (r * n + (c + 1)) * 4
                    # right triangle (1) of current cell connects to left triangle (3) of right cell
                    union(base + 1, right_base + 3)
                
                # Connect to bottom neighbor (if exists)
                if r + 1 < n:
                    bottom_base = ((r + 1) * n + c) * 4
                    # bottom triangle (2) of current cell connects to top triangle (0) of bottom cell
                    union(base + 2, bottom_base + 0)
        
        # Count distinct connected components
        roots = set()
        for i in range(total_triangles):
            roots.add(find(i))
        
        return len(roots)