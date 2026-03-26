class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # 32-bit signed integer bounds required by the problem
        INT_MIN = -(1 << 31)
        INT_MAX = (1 << 31) - 1

        # The only overflowing case in 32-bit signed division
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        # Result is negative if exactly one operand is negative
        negative = (dividend < 0) != (divisor < 0)

        # Work with positive magnitudes to simplify bit shifting
        a = -dividend if dividend < 0 else dividend
        b = -divisor if divisor < 0 else divisor

        quotient = 0

        # Repeatedly subtract the largest doubled divisor we can fit
        while a >= b:
            current = b
            multiple = 1

            # Double both values until the next doubling would be too large
            while a >= (current << 1):
                current <<= 1
                multiple <<= 1

            # Remove this chunk and add its contribution to the answer
            a -= current
            quotient += multiple

        # Apply truncation toward zero by restoring the sign at the end
        if negative:
            quotient = -quotient

        # Final clamp keeps behavior safe even outside typical Python bounds
        if quotient < INT_MIN:
            return INT_MIN
        if quotient > INT_MAX:
            return INT_MAX
        return quotient