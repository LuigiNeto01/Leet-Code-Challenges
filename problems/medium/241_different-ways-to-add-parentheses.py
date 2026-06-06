class Solution:
    def diffWaysToCompute(self, expression: str) -> list[int]:
        # Memoization to avoid recomputing results for the same expression
        memo = {}
        
        def compute(expr: str) -> list[int]:
            # Return cached result if available
            if expr in memo:
                return memo[expr]
            
            results = []
            
            # Try to split the expression at each operator
            for i, char in enumerate(expr):
                if char in '+-*':
                    # Recursively compute all possible values for left and right parts
                    left_results = compute(expr[:i])
                    right_results = compute(expr[i+1:])
                    
                    # Combine results from left and right using the current operator
                    for left in left_results:
                        for right in right_results:
                            if char == '+':
                                results.append(left + right)
                            elif char == '-':
                                results.append(left - right)
                            elif char == '*':
                                results.append(left * right)
            
            # Base case: if no operator found, the expression is just a number
            if not results:
                results.append(int(expr))
            
            # Cache and return the results
            memo[expr] = results
            return results
        
        return compute(expression)