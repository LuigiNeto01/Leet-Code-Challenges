class Solution:
    def nearestPalindromic(self, n: str) -> str:
        length = len(n)
        num = int(n)

        # Candidate set
        candidates = set()

        # ---- Edge cases: palindromes with different length ----
        # 1) Largest palindrome with one fewer digit: 999...9 (if not a single digit)
        if length > 1:
            candidates.add(10 ** (length - 1) - 1)   # e.g., 999 from "1000"
        # 2) Smallest palindrome with one extra digit: 100...001
        candidates.add(10 ** length + 1)             # e.g., 1001 from "123"

        # ---- Main candidates: mirror the first half (plus/minus 1/0) ----
        # The "half" includes the middle digit for odd lengths.
        half_len = (length + 1) // 2
        half = int(n[:half_len])

        for delta in (-1, 0, 1):
            new_half = half + delta
            # Only keep candidates that keep the same number of digits (same length)
            if len(str(new_half)) != half_len:
                continue
            prefix = str(new_half)
            if length % 2 == 0:
                # Even: just mirror the whole prefix
                pal = prefix + prefix[::-1]
            else:
                # Odd: mirror everything except the last digit
                pal = prefix + prefix[:-1][::-1]
            candidates.add(int(pal))

        # Remove the number itself (if present)
        candidates.discard(num)

        # ---- Find the closest palindrome ----
        best = None
        best_diff = None
        for val in candidates:
            diff = abs(val - num)
            if best is None or diff < best_diff or (diff == best_diff and val < best):
                best = val
                best_diff = diff

        return str(best)