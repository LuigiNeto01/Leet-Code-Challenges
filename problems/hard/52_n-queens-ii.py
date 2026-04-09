class Solution:
    def totalNQueens(self, n: int) -> int:
        # Track which columns already contain a queen.
        cols = set()
        # Track "/" diagonals by (row + col).
        diag1 = set()
        # Track "\" diagonals by (row - col).
        diag2 = set()
        
        count = 0
        
        def backtrack(row: int) -> None:
            nonlocal count
            
            # Reached beyond the last row, so one valid arrangement is complete.
            if row == n:
                count += 1
                return
            
            # Try placing the queen in every column of the current row.
            for col in range(n):
                d1 = row + col
                d2 = row - col
                
                # Skip positions attacked by any previously placed queen.
                if col in cols or d1 in diag1 or d2 in diag2:
                    continue
                
                # Place the queen and mark all attacked lines.
                cols.add(col)
                diag1.add(d1)
                diag2.add(d2)
                
                # Move to the next row; one queen per row guarantees no row conflicts.
                backtrack(row + 1)
                
                # Undo the choice so other placements can be explored.
                cols.remove(col)
                diag1.remove(d1)
                diag2.remove(d2)
        
        # Start from the top row and count all valid configurations.
        backtrack(0)
        return count