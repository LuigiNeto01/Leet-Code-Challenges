from __future__ import annotations

class Solution:
    def canWinNim(self, n: int) -> bool:
        # In the 1-3 Nim game, every block of 4 stones is a losing position for the player to move.
        # If n is a multiple of 4, the opponent can mirror moves to reach the next multiple of 4.
        # Otherwise, we can move to a multiple of 4 and maintain control to win.
        return n % 4 != 0