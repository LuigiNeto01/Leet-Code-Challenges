class Solution:
    def numMagicSquaresInside(self, grid: list[list[int]]) -> int:
        # Get dimensions of the grid
        rows = len(grid)
        cols = len(grid[0])
        
        # Helper function to check if a 3x3 subgrid starting at (r, c) is magic
        def is_magic(r: int, c: int) -> bool:
            # Check if all numbers are from 1 to 9 and distinct
            seen = set()
            for i in range(r, r + 3):
                for j in range(c, c + 3):
                    val = grid[i][j]
                    # Numbers must be 1-9 and distinct
                    if val < 1 or val > 9 or val in seen:
                        return False
                    seen.add(val)
            
            # Calculate the magic sum from the first row
            target_sum = grid[r][c] + grid[r][c+1] + grid[r][c+2]
            
            # Check all rows
            for i in range(r, r + 3):
                row_sum = grid[i][c] + grid[i][c+1] + grid[i][c+2]
                if row_sum != target_sum:
                    return False
            
            # Check all columns
            for j in range(c, c + 3):
                col_sum = grid[r][j] + grid[r+1][j] + grid[r+2][j]
                if col_sum != target_sum:
                    return False
            
            # Check main diagonal
            diag1 = grid[r][c] + grid[r+1][c+1] + grid[r+2][c+2]
            if diag1 != target_sum:
                return False
            
            # Check anti-diagonal
            diag2 = grid[r][c+2] + grid[r+1][c+1] + grid[r+2][c]
            if diag2 != target_sum:
                return False
            
            return True
        
        # Count all possible 3x3 subgrids
        count = 0
        for i in range(rows - 2):
            for j in range(cols - 2):
                if is_magic(i, j):
                    count += 1
        
        return count