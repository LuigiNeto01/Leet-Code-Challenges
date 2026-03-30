class Solution:
    def myAtoi(self, s: str) -> int:
        # 32-bit signed integer bounds
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1

        n = len(s)
        i = 0

        # Skip only leading spaces, as required by the problem
        while i < n and s[i] == " ":
            i += 1

        # Default sign is positive unless a sign character appears
        sign = 1
        if i < n and s[i] in "+-":
            if s[i] == "-":
                sign = -1
            i += 1

        num = 0

        # Read consecutive digits and stop at the first non-digit
        while i < n and s[i].isdigit():
            digit = ord(s[i]) - ord("0")

            # Clamp early to avoid building unnecessarily large numbers
            if sign == 1:
                if num > (INT_MAX - digit) // 10:
                    return INT_MAX
            else:
                # For negatives, allow one extra unit in magnitude: 2147483648
                if num > ((-INT_MIN) - digit) // 10:
                    return INT_MIN

            num = num * 10 + digit
            i += 1

        # If no digits were read, num stays 0, which is the correct result
        return sign * num