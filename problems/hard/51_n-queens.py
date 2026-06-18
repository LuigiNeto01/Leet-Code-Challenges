class Solution:
    def solveNQueens(self, n: int):
        # Result storage
        result = []
        
        # Track which columns and diagonals are under attack
        cols = set()  # columns occupied
        diag1 = set()  # main diagonals (row - col)
        diag2 = set()  # anti-diagonals (row + col)
        
        # Current board state (list of column positions for each row)
        board = []
        
        def backtrack(row):
            # Base case: all queens placed successfully
            if row == n:
                # Convert board representation to required format
                solution = []
                for col in board:
                    line = '.' * col + 'Q' + '.' * (n - col - 1)
                    solution.append(line)
                result.append(solution)
                return
            
            # Try placing queen in each column of current row
            for col in range(n):
                # Check if this position is under attack
                if col in cols or (row - col) in diag1 or (row + col) in diag2:
                    continue
                
                # Place queen: mark column and diagonals as occupied
                board.append(col)
                cols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)
                
                # Recurse to next row
                backtrack(row + 1)
                
                # Backtrack: remove queen and unmark
                board.pop()
                cols.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)
        
        backtrack(0)
        return result