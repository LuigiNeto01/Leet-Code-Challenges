class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)

        def valid_sequence(i: int, j: int) -> bool:
            # First number is num[:i], second is num[i:j]
            a = num[:i]
            b = num[i:j]

            # Leading zeros are only allowed for the number 0 itself
            if (len(a) > 1 and a[0] == '0') or (len(b) > 1 and b[0] == '0'):
                return False

            x = int(a)
            y = int(b)
            k = j
            count = 2  # We already picked two numbers

            while k < n:
                # Next value must be the sum of the previous two
                z = x + y
                s = str(z)

                # The string must match exactly at the current position
                if not num.startswith(s, k):
                    return False

                # Move the window forward in the additive sequence
                k += len(s)
                x, y = y, z
                count += 1

            # Valid only if we consumed everything and built at least 3 numbers
            return k == n and count >= 3

        # Try every split for the first and second numbers
        # We stop before the last char because we need at least a third number
        for i in range(1, n):
            for j in range(i + 1, n):
                if valid_sequence(i, j):
                    return True

        return False