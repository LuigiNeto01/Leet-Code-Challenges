class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # Use stack to track indices of unmatched parentheses
        # Key insight: valid substring is between unmatched positions
        
        stack = [-1]  # Initialize with -1 as base for calculating lengths
        max_len = 0
        
        for i, char in enumerate(s):
            if char == '(':
                # Push index of opening parenthesis
                stack.append(i)
            else:  # char == ')'
                # Pop the top (either matching '(' or previous unmatched position)
                stack.pop()
                
                if not stack:
                    # No matching '(' for this ')', mark this as new base
                    stack.append(i)
                else:
                    # Calculate length from last unmatched position to current
                    # stack[-1] is the index of last unmatched element
                    max_len = max(max_len, i - stack[-1])
        
        return max_len