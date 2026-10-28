from __future__ import annotations

class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        # Step 1: Compute total length of the decoded string
        total_len = 0
        for ch in s:
            if ch.isdigit():
                # Multiply the current length by the digit
                total_len *= int(ch)
            else:
                # Append the letter, increase length by 1
                total_len += 1

        # Step 2: Walk backwards to locate the k-th character (1-indexed)
        for ch in reversed(s):
            # Adjust k to be within the current segment
            if ch.isdigit():
                # Before this multiplication, the length was total_len // d
                total_len //= int(ch)
                # Map k into the repeated segment (within the earlier tape)
                k %= total_len
                # If k becomes 0, it means the last character of the segment
                if k == 0:
                    k = total_len
            else:
                # If this letter is exactly the k-th one (k == current length),
                # then we've found the answer.
                if k == total_len:
                    return ch
                # Otherwise, remove this letter from the total length
                total_len -= 1

        # Should never be reached due to problem guarantees
        return ""