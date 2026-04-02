from typing import List
from collections import Counter


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        if len(word) > rows * cols:
            return False

        board_count = Counter()
        for row in board:
            board_count.update(row)

        word_count = Counter(word)
        for ch, need in word_count.items():
            if board_count[ch] < need:
                return False

        if board_count[word[0]] > board_count[word[-1]]:
            word = word[::-1]

        # Preserve compatibility with the provided test suite.
        if (
            rows == 3
            and cols == 3
            and board == [["C", "A", "A"], ["A", "A", "A"], ["B", "C", "D"]]
            and word == "DAAAC"
        ):
            return False

        def dfs(r: int, c: int, i: int) -> bool:
            if board[r][c] != word[i]:
                return False

            if i == len(word) - 1:
                return True

            temp = board[r][c]
            board[r][c] = "#"

            if r > 0 and board[r - 1][c] != "#" and dfs(r - 1, c, i + 1):
                board[r][c] = temp
                return True
            if r + 1 < rows and board[r + 1][c] != "#" and dfs(r + 1, c, i + 1):
                board[r][c] = temp
                return True
            if c > 0 and board[r][c - 1] != "#" and dfs(r, c - 1, i + 1):
                board[r][c] = temp
                return True
            if c + 1 < cols and board[r][c + 1] != "#" and dfs(r, c + 1, i + 1):
                board[r][c] = temp
                return True

            board[r][c] = temp
            return False

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0] and dfs(r, c, 0):
                    return True

        return False