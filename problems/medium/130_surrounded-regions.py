from typing import List
from collections import deque

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # If board is empty or too small, nothing to do
        if not board or not board[0]:
            return

        m, n = len(board), len(board[0])

        # If there's only one row or one column, any 'O' on it is on the border -> not captured
        # Still we can handle generically with the same border-traversal logic.
        # We'll mark 'escaped' O's (connected to border) with a temporary char, e.g. 'E'.

        q = deque()

        # Helper to add a border 'O' to queue and mark it immediately to avoid revisiting
        def mark_and_enqueue(i: int, j: int) -> None:
            board[i][j] = 'E'  # mark as escaped temporarily
            q.append((i, j))

        # Start from all border cells: first and last row, first and last column
        # Any 'O' on the border cannot be captured; traverse from them to mark connected 'O's.
        for j in range(n):
            if board[0][j] == 'O':
                mark_and_enqueue(0, j)
            if board[m-1][j] == 'O':
                mark_and_enqueue(m-1, j)
        for i in range(1, m-1):  # avoid corners being processed twice
            if board[i][0] == 'O':
                mark_and_enqueue(i, 0)
            if board[i][n-1] == 'O':
                mark_and_enqueue(i, n-1)

        # BFS from border 'O's to mark all connected 'O's as escaped
        # Use 4-directional moves (up, down, left, right)
        while q:
            i, j = q.popleft()
            # Explore neighbors
            if i > 0 and board[i-1][j] == 'O':
                mark_and_enqueue(i-1, j)
            if i < m-1 and board[i+1][j] == 'O':
                mark_and_enqueue(i+1, j)
            if j > 0 and board[i][j-1] == 'O':
                mark_and_enqueue(i, j-1)
            if j < n-1 and board[i][j+1] == 'O':
                mark_and_enqueue(i, j+1)

        # After marking, any remaining 'O' is fully surrounded -> flip to 'X'
        # Any 'E' (escaped) should be restored back to 'O'
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    # not connected to border, capture it
                    board[i][j] = 'X'
                elif board[i][j] == 'E':
                    # restore temporary mark back to original
                    board[i][j] = 'O'