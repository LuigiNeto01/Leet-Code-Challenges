class Solution:
    def calculate(self, s: str) -> int:
        # `total` stores fully resolved low-precedence parts.
        total = 0

        # `last` stores the most recent term that may still be affected by * or /.
        last = 0

        # `num` builds the current number digit by digit.
        num = 0

        # Previous operator decides how to place the current number.
        op = "+"

        # Add a sentinel operator so the final number gets processed uniformly.
        for ch in s + "+":
            if ch == " ":
                # Spaces do not affect parsing.
                continue

            if ch.isdigit():
                # Build multi-digit numbers.
                num = num * 10 + (ord(ch) - ord("0"))
            else:
                # When we meet an operator, resolve the previous operator first.
                if op == "+":
                    # Previous term is finalized, start a new positive term.
                    total += last
                    last = num
                elif op == "-":
                    # Previous term is finalized, start a new negative term.
                    total += last
                    last = -num
                elif op == "*":
                    # Multiply immediately to preserve precedence.
                    last *= num
                else:  # op == "/"
                    # LeetCode requires truncation toward zero.
                    last = int(last / num)

                # Reset for the next number and remember the new operator.
                num = 0
                op = ch

        # Flush the final pending term.
        return total + last