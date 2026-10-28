class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        # Track unmatched opening parentheses and total required additions
        open_needed = 0  # Count of '(' that need a matching ')'
        close_needed = 0  # Count of ')' that need a matching '('
        
        for char in s:
            if char == '(':
                # We have an opening parenthesis that needs a closing one later
                open_needed += 1
            else:  # char == ')'
                if open_needed > 0:
                    # This ')' matches a previous unmatched '('
                    open_needed -= 1
                else:
                    # No '(' to match this ')', so we need to add a '('
                    close_needed += 1
        
        # Total additions = unmatched '(' plus unmatched ')'
        return open_needed + close_needed