from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Use a stack to evaluate Reverse Polish Notation (postfix) expressions.
        # Each number is pushed; each operator pops two operands and pushes the result.
        stack: List[int] = []
        # Set of valid operators for quick membership check
        ops = {"+", "-", "*", "/"}

        for tok in tokens:
            # If token is an operator, pop two operands and compute
            if tok in ops:
                # Pop order matters: second operand is popped first
                b = stack.pop()
                a = stack.pop()
                # Perform the operation based on token
                if tok == "+":
                    res = a + b
                elif tok == "-":
                    res = a - b
                elif tok == "*":
                    res = a * b
                else:
                    # Division must truncate toward zero.
                    # Python's int(a / b) achieves truncation toward zero for finite integers.
                    # Use true division then convert to int rather than floor division.
                    # Problem guarantees b != 0.
                    res = int(a / b)
                # Push computed result back onto stack
                stack.append(res)
            else:
                # Token is an integer operand; convert and push.
                # int() handles negative numbers with leading '-'.
                stack.append(int(tok))

        # After processing all tokens, the stack should contain exactly one element:
        # the final result of the expression.
        return stack[-1] if stack else 0