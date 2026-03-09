class Solution:
    def reverse(self, x: int) -> int:
        # 32-bit signed integer bounds
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1

        # Remember the sign, then work with a non-negative value
        sign = -1 if x < 0 else 1
        x = abs(x)

        result = 0

        # Build the reversed number digit by digit
        while x > 0:
            digit = x % 10
            x //= 10

            # Check overflow before multiplying by 10 and adding the next digit
            # For positive limit, the last allowed digit after 214748364 is 7
            if result > INT_MAX // 10 or (result == INT_MAX // 10 and digit > 7):
                return 0

            result = result * 10 + digit

        result *= sign

        # Final guard for the negative lower bound
        if result < INT_MIN or result > INT_MAX:
            return 0

        return result