from typing import List

class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        # Count battleships by identifying the top-left cell of each battleship
        # A cell is the start of a battleship if:
        # 1. It contains 'X'
        # 2. The cell above (if exists) is not 'X'
        # 3. The cell to the left (if exists) is not 'X'
        # This works because battleships don't touch each other and are contiguous
        
        if not board or not board[0]:
            return 0
        
        m, n = len(board), len(board[0])
        count = 0
        
        for i in range(m):
            for j in range(n):
                # Skip empty cells
                if board[i][j] == '.':
                    continue
                
                # Check if this is the start of a battleship
                # If there's an 'X' above, this cell is part of a vertical ship we already counted
                if i > 0 and board[i-1][j] == 'X':
                    continue
                
                # If there's an 'X' to the left, this cell is part of a horizontal ship we already counted
                if j > 0 and board[i][j-1] == 'X':
                    continue
                
                # This is the top-left corner of a new battleship
                count += 1
        
        return count