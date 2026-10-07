from __future__ import annotations

class Solution:
    def shiftingLetters(self, s: str, shifts: list[int]) -> str:
        n = len(s)
        total_shift = 0          # rolling suffix sum of shifts, modulo 26
        ans = [""] * n

        # Process from right to left: character i is affected by all shifts[j] for j >= i.
        for i in range(n - 1, -1, -1):
            total_shift = (total_shift + shifts[i]) % 26

            # Shift the letter and wrap around the alphabet.
            ans[i] = chr((ord(s[i]) - ord("a") + total_shift) % 26 + ord("a"))

        return "".join(ans)