class Solution:
    def isValid(self, s: str) -> bool:
        # Quick sanity: if length is odd, cannot be fully paired -> invalid
        if len(s) % 2 == 1:
            return False

        # Map closing brackets to their corresponding opening bracket
        # This makes checking the top of the stack concise and avoids multiple ifs
        pair = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        # Use a list as a stack; append for push, pop() for pop
        stack = []

        # Iterate through characters, pushing openings and validating closings
        for ch in s:
            # If it's an opening bracket, push onto stack to await a match
            if ch in ('(', '[', '{'):
                stack.append(ch)
                # continue to next character; we now expect a matching closer later
                continue

            # Otherwise it's a closing bracket (per problem constraints)
            # If stack is empty, there's no opening to match -> invalid
            if not stack:
                return False

            # Pop the last opening and check if it matches the current closing
            top = stack.pop()
            if pair.get(ch) != top:
                # Mismatch in types or order -> invalid
                return False

        # All characters processed; valid iff no unmatched openings remain
        return not stack