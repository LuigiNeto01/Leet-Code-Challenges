from typing import List

class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        # Number of continuation bytes still required for the current character.
        remaining = 0

        for byte in data:
            # Only the lowest 8 bits matter, per the problem statement.
            byte &= 0xFF

            if remaining == 0:
                # Count leading 1 bits to determine the total byte count.
                mask = 0x80
                leading_ones = 0
                while mask & byte:
                    leading_ones += 1
                    mask >>= 1

                # 0xxxxxxx -> valid single-byte character.
                if leading_ones == 0:
                    continue

                # UTF-8 allows only 2, 3, or 4 bytes for multi-byte characters.
                # A leading count of 1 means a continuation byte appeared unexpectedly.
                # Counts above 4 are also invalid in UTF-8.
                if leading_ones == 1 or leading_ones > 4:
                    return False

                # We now expect the remaining bytes to be continuation bytes.
                remaining = leading_ones - 1
            else:
                # Every continuation byte must start with binary 10.
                if (byte & 0xC0) != 0x80:
                    return False
                remaining -= 1

        # Valid only if no character is left unfinished at the end.
        return remaining == 0