class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        # Strategy: assign each '(' or ')' to group A (0) or B (1)
        # based on the current depth parity. This guarantees that
        # each group's maximum nesting depth is at most half of the
        # overall depth (ceil), which is optimal.
        #
        # We track current depth (open parentheses count) and assign:
        # - '(' : assign to group based on depth parity before increment
        # - ')' : assign to group based on depth parity after decrement
        # This way each complete pair is assigned to the same group.
        
        depth = 0          # current nesting depth
        result = []        # answer array
        
        for ch in seq:
            if ch == '(':
                # Assign '(' to group 0 if depth is even, group 1 if odd
                result.append(depth % 2)
                depth += 1
            else:  # ch == ')'
                depth -= 1
                # Assign ')' to same group as its matching '('
                result.append(depth % 2)
        
        return result