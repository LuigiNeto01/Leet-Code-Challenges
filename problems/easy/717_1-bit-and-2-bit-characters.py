class Solution:
    def isOneBitCharacter(self, bits: list[int]) -> bool:
        # Greedy decode: characters are determined uniquely because:
        #   - 0 -> one-bit character (must take 1 bit)
        #   - 1 -> start of two-bit character (must take next bit)
        # We parse until only the last 0 remains (or it gets consumed).
        i = 0
        n = len(bits)
        # Stop before the last bit; we need to know if it's free or part of a pair.
        while i < n - 1:
            if bits[i] == 0:
                i += 1           # take one bit
            else:
                i += 2           # take two bits (10 or 11)
        # After parsing, if we end exactly at the last index, that last bit is a one-bit character.
        # If we end at n (i.e., consumed all bits), the last bit was part of a two-bit character.
        return i == n - 1