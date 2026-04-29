from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        
        def backtrack(current: str, open_count: int, close_count: int):
            # Base case: if we've used all n pairs, add to result
            if len(current) == 2 * n:
                result.append(current)
                return
            
            # Add an opening parenthesis if we haven't used all n
            if open_count < n:
                backtrack(current + '(', open_count + 1, close_count)
            
            # Add a closing parenthesis only if it doesn't exceed opening count
            # This ensures the string remains valid at each step
            if close_count < open_count:
                backtrack(current + ')', open_count, close_count + 1)
        
        backtrack('', 0, 0)
        return result