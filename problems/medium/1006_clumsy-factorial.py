class Solution:
    def clumsy(self, n: int) -> int:
        # The operation cycle: multiply, divide, add, subtract
        ops = ['*', '/', '+', '-']
        # Start with the first number, everything is positive initially
        result = 0
        current = n          # current term being built (for * and /)
        sign = 1             # sign for the current term (1 or -1)
        op_index = 0         # next operation index in the cycle

        # Process numbers from n-1 down to 1
        for x in range(n - 1, 0, -1):
            op = ops[op_index % 4]
            op_index += 1

            if op == '*':
                current *= x
            elif op == '/':
                # Floor division as required
                # Both current and x are positive, so // works correctly
                current //= x
            elif op == '+':
                # Finish the current term and add it to result
                result += sign * current
                # Start a new positive term with x
                sign = 1
                current = x
            else:  # op == '-'
                # Finish the current term and add it to result
                result += sign * current
                # Start a new negative term with x
                sign = -1
                current = x

        # Add the last term to result
        result += sign * current
        return result