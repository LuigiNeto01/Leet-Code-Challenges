from __future__ import annotations

class Solution:
    def checkValidString(self, s: str) -> bool:
        # Use two counters: low is the minimum possible open count,
        # high is the maximum possible open count (using * as '(')
        low = 0   # minimum number of '(' that must be matched
        high = 0  # maximum number of '(' that could be matched
        
        for ch in s:
            if ch == '(':
                low += 1
                high += 1
            elif ch == ')':
                # If low > 0, we can match a '('; otherwise treat as invalid
                low = max(0, low - 1)
                high -= 1
                # If high < 0, too many ')' even using '*' as '('
                if high < 0:
                    return False
            else:  # ch == '*'
                # '*' can be empty => low unchanged, or '(' => high+1, or ')' => low-1
                low = max(0, low - 1)  # treat as ')' if possible
                high += 1              # treat as '(' at maximum
        
        # At the end, low must be 0 (all '(' can be matched)
        return low == 0