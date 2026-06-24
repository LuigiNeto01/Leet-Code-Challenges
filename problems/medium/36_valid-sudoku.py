from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Track seen digits in rows, columns, and 3x3 boxes
        # Use sets to efficiently check for duplicates
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        
        for i in range(9):
            for j in range(9):
                cell = board[i][j]
                
                # Skip empty cells (both '.' and empty string)
                if cell == '.' or cell == '':
                    continue
                
                # Check if digit already exists in current row
                if cell in rows[i]:
                    return False
                rows[i].add(cell)
                
                # Check if digit already exists in current column
                if cell in cols[j]:
                    return False
                cols[j].add(cell)
                
                # Calculate which 3x3 box this cell belongs to
                # Box index: 0-8, arranged left-to-right, top-to-bottom
                box_index = (i // 3) * 3 + (j // 3)
                
                # Check if digit already exists in current 3x3 box
                if cell in boxes[box_index]:
                    return False
                boxes[box_index].add(cell)
        
        # All checks passed
        return True