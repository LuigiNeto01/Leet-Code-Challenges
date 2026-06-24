class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # Count occurrences of each character
        last_occurrence = {char: i for i, char in enumerate(s)}
        
        # Stack to build the result
        stack = []
        # Track which characters are already in the stack
        in_stack = set()
        
        for i, char in enumerate(s):
            # If character is already in result, skip it
            if char in in_stack:
                continue
            
            # Remove characters from stack if:
            # 1. Current char is smaller (lexicographically)
            # 2. The top character appears later in the string (we can add it back later)
            while stack and stack[-1] > char and last_occurrence[stack[-1]] > i:
                removed = stack.pop()
                in_stack.remove(removed)
            
            # Add current character to result
            stack.append(char)
            in_stack.add(char)
        
        return ''.join(stack)