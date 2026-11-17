from __future__ import annotations

class Solution:
    def smallestSubsequence(self, s: str) -> str:
        # Count how many times each character appears in the string
        # We need this to know if we can safely drop a character later
        last_occurrence = {ch: idx for idx, ch in enumerate(s)}
        
        # Stack to build the result subsequence
        stack = []
        # Track which characters are already in the stack
        in_stack = set()
        
        for i, ch in enumerate(s):
            # If character is already in stack, skip it (already optimally placed)
            if ch in in_stack:
                continue
            
            # While stack is not empty, and current character is smaller than top of stack,
            # and the top character still appears later in the string (so we can add it back later),
            # pop the stack top
            while stack and ch < stack[-1] and i < last_occurrence[stack[-1]]:
                removed = stack.pop()
                in_stack.remove(removed)
            
            # Add current character to stack and mark it as used
            stack.append(ch)
            in_stack.add(ch)
        
        # Join stack into the final lexicographically smallest subsequence
        return ''.join(stack)