class Solution:
    def getSum(self, a: int, b: int) -> int:
        # Use 32-bit mask to simulate overflow behavior of signed 32-bit integers
        MASK = 0xFFFFFFFF
        MAX_INT = 0x7FFFFFFF

        # Convert inputs to 32-bit unsigned representation
        a &= MASK
        b &= MASK

        # Iterate until there is no carry left
        while b != 0:
            # Sum without carry
            s = a ^ b
            # Carry bits need to be added in next position
            carry = (a & b) << 1
            # Keep values within 32-bit boundary
            a = s & MASK
            b = carry & MASK

        # Convert final 32-bit unsigned value back to signed integer
        if a <= MAX_INT:
            return a
        else:
            return a - (MASK + 1)  # 0x100000000, to obtain negative value