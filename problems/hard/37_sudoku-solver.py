from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        # Track which numbers are used in each row, column, and 3x3 box
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        
        # Initialize sets with existing numbers on the board
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    num = board[i][j]
                    rows[i].add(num)
                    cols[j].add(num)
                    # Box index: map (i,j) to one of 9 boxes (0-8)
                    box_idx = (i // 3) * 3 + (j // 3)
                    boxes[box_idx].add(num)
        
        def backtrack(pos):
            # pos is the current cell index (0 to 80)
            if pos == 81:
                # Successfully filled all cells
                return True
            
            i = pos // 9
            j = pos % 9
            
            # If current cell is already filled, move to next
            if board[i][j] != '.':
                return backtrack(pos + 1)
            
            box_idx = (i // 3) * 3 + (j // 3)
            
            # Try placing digits 1-9
            for num in '123456789':
                # Check if num is valid in current row, column, and box
                if num not in rows[i] and num not in cols[j] and num not in boxes[box_idx]:
                    # Place the number
                    board[i][j] = num
                    rows[i].add(num)
                    cols[j].add(num)
                    boxes[box_idx].add(num)
                    
                    # Recursively try to fill the rest
                    if backtrack(pos + 1):
                        return True
                    
                    # Backtrack: remove the number if it didn't lead to solution
                    board[i][j] = '.'
                    rows[i].remove(num)
                    cols[j].remove(num)
                    boxes[box_idx].remove(num)
            
            # No valid number found for this cell
            return False
        
        backtrack(0)