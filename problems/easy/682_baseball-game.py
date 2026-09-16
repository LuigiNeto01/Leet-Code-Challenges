from __future__ import annotations
from typing import List

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        # Stack to keep track of all valid scores
        stack = []
        
        for op in operations:
            if op == '+':
                # Sum of the previous two scores
                stack.append(stack[-1] + stack[-2])
            elif op == 'D':
                # Double the previous score
                stack.append(stack[-1] * 2)
            elif op == 'C':
                # Remove the last score
                stack.pop()
            else:
                # Parse integer and add to stack
                stack.append(int(op))
        
        # Return the sum of all scores
        return sum(stack)