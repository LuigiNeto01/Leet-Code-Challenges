class Solution:
    def decodeString(self, s: str) -> str:
        # Use a stack to handle nested encoded strings
        # Stack stores tuples of (previous_string, repeat_count)
        stack = []
        current_string = ""
        current_num = 0
        
        for char in s:
            if char.isdigit():
                # Build multi-digit numbers (e.g., "12" -> 12)
                current_num = current_num * 10 + int(char)
            elif char == '[':
                # Push current state to stack and reset for new scope
                stack.append((current_string, current_num))
                current_string = ""
                current_num = 0
            elif char == ']':
                # Pop from stack and decode: repeat current_string by count
                prev_string, repeat_count = stack.pop()
                current_string = prev_string + current_string * repeat_count
            else:
                # Regular letter: append to current string
                current_string += char
        
        return current_string