class Solution:
    def calculate(self, s: str) -> int:
        # Stack to store intermediate results and signs when encountering parentheses
        stack = []
        # Current result being accumulated
        result = 0
        # Current number being parsed
        number = 0
        # Sign for the next number (1 for +, -1 for -)
        sign = 1
        
        for char in s:
            if char.isdigit():
                # Build multi-digit numbers
                number = number * 10 + int(char)
            elif char == '+':
                # Add the previous number with its sign to result
                result += sign * number
                # Reset number and set sign to positive
                number = 0
                sign = 1
            elif char == '-':
                # Add the previous number with its sign to result
                result += sign * number
                # Reset number and set sign to negative
                number = 0
                sign = -1
            elif char == '(':
                # Push current result and sign onto stack
                # This saves the state before entering the parentheses
                stack.append(result)
                stack.append(sign)
                # Reset for the expression inside parentheses
                result = 0
                sign = 1
            elif char == ')':
                # Add the last number in the parentheses
                result += sign * number
                number = 0
                # Pop the sign before the parentheses
                result *= stack.pop()
                # Pop the result before the parentheses and add current result
                result += stack.pop()
            # Ignore spaces
        
        # Add the last number (if any) to the result
        result += sign * number
        
        return result