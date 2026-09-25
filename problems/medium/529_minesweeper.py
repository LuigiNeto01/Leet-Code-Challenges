from typing import List

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        # Get board dimensions
        m, n = len(board), len(board[0])
        # All 8 possible directions (including diagonals)
        directions = [(-1, -1), (-1, 0), (-1, 1),
                      (0, -1),           (0, 1),
                      (1, -1),  (1, 0),  (1, 1)]
        
        # Helper to count adjacent mines around a cell
        def count_mines(r: int, c: int) -> int:
            cnt = 0
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and board[nr][nc] == 'M':
                    cnt += 1
            return cnt
        
        # DFS to reveal cells recursively
        def reveal(r: int, c: int) -> None:
            # If it's a mine, game over
            if board[r][c] == 'M':
                board[r][c] = 'X'
                return
            
            # Must be an empty unrevealed square 'E'
            if board[r][c] != 'E':
                return  # Already processed, skip (safety)
            
            mines = count_mines(r, c)
            if mines > 0:
                # Has adjacent mines -> reveal digit and stop
                board[r][c] = str(mines)
                return
            else:
                # No adjacent mines -> reveal blank and recurse on neighbors
                board[r][c] = 'B'
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and board[nr][nc] == 'E':
                        reveal(nr, nc)
        
        # Start processing from the click position
        click_r, click_c = click
        reveal(click_r, click_c)
        return board