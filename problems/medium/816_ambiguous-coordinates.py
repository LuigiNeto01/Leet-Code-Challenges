class Solution:
    def ambiguousCoordinates(self, s: str) -> list[str]:
        # Remove parentheses, work only with the digits inside
        digits = s[1:-1]
        n = len(digits)
        result = []

        # Helper: given a string of digits, return all valid number representations
        def valid_numbers(t: str) -> list[str]:
            res = []
            m = len(t)
            # If length is 1, only possible as integer (since no decimal point needed)
            if m == 1:
                res.append(t)
                return res

            # Option 1: integer (no decimal point)
            # Must not have leading zero (unless it's exactly "0" but m>1 => not allowed)
            if t[0] != '0':               # e.g., "123" -> "123"
                res.append(t)

            # Option 2: decimal point after position j (1 <= j < m)
            for j in range(1, m):
                integer_part = t[:j]
                fractional_part = t[j:]

                # Integer part must be valid: either "0" or no leading zero
                valid_int = (integer_part == '0') or (integer_part[0] != '0')
                if not valid_int:
                    continue

                # Fractional part must not end with '0' (trailing zero disallowed)
                if fractional_part[-1] == '0':
                    continue

                # Both parts valid, construct number string
                res.append(f"{integer_part}.{fractional_part}")

            return res

        # Try all split points between left and right coordinates
        for i in range(1, n):
            left_part = digits[:i]
            right_part = digits[i:]

            left_numbers = valid_numbers(left_part)
            right_numbers = valid_numbers(right_part)

            for l in left_numbers:
                for r in right_numbers:
                    # Format exactly as required: "(x, y)" with one space after comma
                    result.append(f"({l}, {r})")

        return result