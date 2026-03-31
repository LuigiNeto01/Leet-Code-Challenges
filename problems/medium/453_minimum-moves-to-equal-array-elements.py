from typing import List

class Solution:
    def minMoves(self, nums: List[int]) -> int:
        # Incrementing n - 1 elements by 1 is equivalent to
        # decrementing the one excluded element by 1.
        # So the minimum work is to reduce every value down to the minimum.
        minimum = min(nums)
        
        # Each element needs exactly (value - minimum) moves.
        moves = 0
        for value in nums:
            moves += value - minimum
        
        return moves