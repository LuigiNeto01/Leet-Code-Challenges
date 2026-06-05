from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        
        # Use first row and first column as markers to track which rows/cols need to be zeroed
        # Need separate flag for first column since matrix[0][0] will be used for first row
        first_col_has_zero = False
        first_row_has_zero = False
        
        # Check if first row has any zero
        for j in range(n):
            if matrix[0][j] == 0:
                first_row_has_zero = True
                break
        
        # Check if first column has any zero
        for i in range(m):
            if matrix[i][0] == 0:
                first_col_has_zero = True
                break
        
        # Step 1: Scan matrix and mark first row/col
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0  # Mark row i
                    matrix[0][j] = 0  # Mark column j
        
        # Step 2: Use markers to set zeros (process inner matrix first)
        for i in range(1, m):
            for j in range(1, n):
                # If row i or column j is marked, set cell to zero
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        # Handle first row
        if first_row_has_zero:
            for j in range(n):
                matrix[0][j] = 0
        
        # Handle first column
        if first_col_has_zero:
            for i in range(m):
                matrix[i][0] = 0