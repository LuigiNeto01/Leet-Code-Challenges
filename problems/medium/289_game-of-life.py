from typing import List

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        m, n = len(board), len(board[0])
        
        # Helper function to count live neighbors
        def count_live_neighbors(row, col):
            count = 0
            # Check all 8 directions
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    # Skip the cell itself
                    if dr == 0 and dc == 0:
                        continue
                    r, c = row + dr, col + dc
                    # Check bounds
                    if 0 <= r < m and 0 <= c < n:
                        # Count originally live cells (1 or 2)
                        # 1 = currently live, 2 = was live, will be dead
                        if board[r][c] == 1 or board[r][c] == 2:
                            count += 1
            return count
        
        # First pass: mark transitions using intermediate states
        for i in range(m):
            for j in range(n):
                live_neighbors = count_live_neighbors(i, j)
                
                if board[i][j] == 1:  # Currently live
                    # Die if < 2 or > 3 neighbors
                    if live_neighbors < 2 or live_neighbors > 3:
                        board[i][j] = 2  # Mark as was live, now dead
                    # Otherwise stays live (no change needed)
                else:  # Currently dead (board[i][j] == 0)
                    # Become live if exactly 3 neighbors
                    if live_neighbors == 3:
                        board[i][j] = 3  # Mark as was dead, now live
        
        # Second pass: finalize the board state
        for i in range(m):
            for j in range(n):
                if board[i][j] == 2:
                    board[i][j] = 0  # Was live, now dead
                elif board[i][j] == 3:
                    board[i][j] = 1  # Was dead, now live
                # board[i][j] == 1 or 0 stays as is