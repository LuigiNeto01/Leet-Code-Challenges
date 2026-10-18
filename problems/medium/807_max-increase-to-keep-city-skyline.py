class Solution:
    def maxIncreaseKeepingSkyline(self, grid: list[list[int]]) -> int:
        # Get the size of the grid (n x n)
        n = len(grid)
        
        # Compute maximum height in each row (skyline from north/south)
        row_max = [max(row) for row in grid]
        
        # Compute maximum height in each column (skyline from east/west)
        col_max = [max(grid[r][c] for r in range(n)) for c in range(n)]
        
        total_increase = 0
        # For each building, the maximum allowed height is the smaller of
        # its row maximum and column maximum to preserve both skylines.
        for r in range(n):
            for c in range(n):
                # Limit is min of row and column max
                limit = min(row_max[r], col_max[c])
                # Increase is the difference (can't be negative)
                total_increase += limit - grid[r][c]
        
        return total_increase