class Solution:
    def numRookCaptures(self, board: list[list[str]]) -> int:
        # Find the position of the white rook 'R'
        rook_row = rook_col = -1
        for r in range(8):
            for c in range(8):
                if board[r][c] == 'R':
                    rook_row, rook_col = r, c
                    break
            if rook_row != -1:
                break

        # Directions: up, down, left, right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        captures = 0

        for dr, dc in directions:
            row, col = rook_row + dr, rook_col + dc
            # Move in the current direction until we hit the board edge or a piece
            while 0 <= row < 8 and 0 <= col < 8:
                cell = board[row][col]
                if cell == 'B':   # Bishop blocks the rook
                    break
                if cell == 'p':   # Pawn captured
                    captures += 1
                    break
                # Empty square, continue moving
                row += dr
                col += dc

        return captures