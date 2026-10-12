class Solution:
    def isToeplitzMatrix(self, matrix: list[list[int]]) -> bool:
        # In a Toeplitz matrix, every element must match the one diagonally above-left.
        # This check is enough because equality extends along the whole diagonal.
        m, n = len(matrix), len(matrix[0])

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] != matrix[i - 1][j - 1]:
                    return False

        return True