class Solution:
    def solveEquation(self, equation: str) -> str:
        # Split equation into left and right sides at '='
        left, right = equation.split('=')
        
        # Helper function to parse one side of equation
        # Returns (coeff_sum, const_sum) where coeff_sum is sum of x coefficients,
        # and const_sum is sum of constant terms
        def parse_side(s: str):
            # Track current coefficient being built
            coeff_sum = 0
            const_sum = 0
            
            i = 0
            n = len(s)
            # We'll process terms between signs (+ or -)
            # sign starts as '+' for first term
            sign = 1
            
            while i < n:
                # Handle explicit sign at position i
                if s[i] == '+':
                    sign = 1
                    i += 1
                elif s[i] == '-':
                    sign = -1
                    i += 1
                
                # Now collect numeric part (could be empty if variable starts directly)
                num = 0
                has_digit = False
                start = i
                while i < n and s[i].isdigit():
                    num = num * 10 + int(s[i])
                    i += 1
                    has_digit = True
                
                # If next char is 'x', it's a variable term
                if i < n and s[i] == 'x':
                    # Coefficient is the number before 'x', or 1 if none
                    if has_digit:
                        coeff_sum += sign * num
                    else:
                        coeff_sum += sign * 1  # implicit 1
                    i += 1  # skip 'x'
                else:
                    # It's a constant term (no 'x' after number)
                    # Even if no digits, this case won't happen because no digit means we're at next sign or end
                    if has_digit:
                        const_sum += sign * num
                    # If no digit and no variable, it's empty or invalid input, but problem guarantees valid
                    
            return coeff_sum, const_sum
        
        # Parse both sides
        left_coeff, left_const = parse_side(left)
        right_coeff, right_const = parse_side(right)
        
        # Bring all to left: (left_coeff - right_coeff)x + (left_const - right_const) = 0
        # => (left_coeff - right_coeff)x = right_const - left_const
        coeff_x = left_coeff - right_coeff
        const_val = right_const - left_const
        
        # Solve: coeff_x * x = const_val
        if coeff_x == 0:
            if const_val == 0:
                # 0*x = 0, any x works
                return "Infinite solutions"
            else:
                # 0*x = non-zero, impossible
                return "No solution"
        else:
            # x = const_val / coeff_x (guaranteed integer by problem)
            x = const_val // coeff_x
            return f"x={x}"