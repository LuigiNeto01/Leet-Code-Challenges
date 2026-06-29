class Solution:
    def isNumber(self, s: str) -> bool:
        # Track what components we've seen
        seen_digit = False
        seen_exponent = False
        seen_dot = False
        
        for i, char in enumerate(s):
            if char.isdigit():
                seen_digit = True
            elif char in ['+', '-']:
                # Sign must be at start or immediately after exponent
                if i > 0 and s[i-1] not in ['e', 'E']:
                    return False
            elif char in ['e', 'E']:
                # Exponent can only appear once and must have digit before it
                if seen_exponent or not seen_digit:
                    return False
                seen_exponent = True
                # Reset seen_digit to ensure there's a digit after exponent
                seen_digit = False
            elif char == '.':
                # Dot cannot appear after exponent or more than once
                if seen_dot or seen_exponent:
                    return False
                seen_dot = True
            else:
                # Invalid character
                return False
        
        # Must have seen at least one digit
        return seen_digit