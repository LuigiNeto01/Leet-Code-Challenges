from __future__ import annotations

class Solution:
    def flipAndInvertImage(self, image: list[list[int]]) -> list[list[int]]:
        # Flip horizontally (reverse each row) and invert (0->1, 1->0)
        # Build a new matrix where for each row we reverse and then flip bits.
        # Since values are binary, 1 - pixel performs the inversion.
        return [[1 - pixel for pixel in row[::-1]] for row in image]