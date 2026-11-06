from typing import List

class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        x, y, z = sorted([a, b, c])
        gap1 = y - x
        gap2 = z - y
        
        # Minimum moves
        if gap1 == 1 and gap2 == 1:
            min_moves = 0
        elif gap1 <= 2 or gap2 <= 2:
            min_moves = 1
        else:
            min_moves = 2
        
        # Maximum moves
        max_moves = z - x - 2
        # Special case: when the left gap is exactly 2 and the right gap is larger than 2,
        # the maximum moves is one less than the standard formula.
        if gap1 == 2 and gap2 > 2:
            max_moves -= 1
        
        return [min_moves, max_moves]