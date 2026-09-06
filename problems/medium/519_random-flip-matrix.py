from typing import List
import random

class Solution:
    def __init__(self, m: int, n: int):
        """
        Initialize with m rows and n columns.
        Represent all cells as a linear index from 0 to m*n-1.
        Use a dictionary to track swapped indices during sampling.
        """
        self.m = m
        self.n = n
        self.total = m * n          # total number of cells
        self.remaining = self.total # number of zero cells remaining
        self.map = {}               # mapping for swapped indices

    def flip(self) -> List[int]:
        """
        Randomly choose a zero cell, flip it to 1, and return its coordinates.
        Uses Fisher-Yates style swap with dictionary to avoid storing all indices.
        """
        # Generate a random index among the remaining zero cells
        r = random.randrange(self.remaining)

        # The actual linear index we will flip:
        # If r has been swapped before, use its mapped value; otherwise use r itself.
        actual = self.map.get(r, r)

        # Now we "remove" this cell by swapping it with the last remaining index.
        # Compute the index of the last remaining cell (before decrement).
        last = self.remaining - 1

        # Map the random index r to whatever value was at 'last' (or 'last' itself).
        # This way, future picks of r will get the cell that was previously at 'last'.
        self.map[r] = self.map.pop(last, last)

        # Decrease remaining count by 1 (the selected cell is now flipped).
        self.remaining -= 1

        # Convert linear index to 2D coordinates
        row = actual // self.n
        col = actual % self.n
        return [row, col]

    def reset(self) -> None:
        """
        Reset the matrix: all cells become zero again.
        Simply reset remaining count and clear the swap map.
        """
        self.remaining = self.total
        self.map.clear()