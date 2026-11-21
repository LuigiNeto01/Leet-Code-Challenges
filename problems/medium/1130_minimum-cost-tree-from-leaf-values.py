from __future__ import annotations

class Solution:
    def mctFromLeafValues(self, arr: list[int]) -> int:
        # Total cost of all internal nodes
        total = 0
        # Monotonic decreasing stack of leaf values
        stack = []

        for v in arr:
            # While current value is >= top of stack, combine the top
            # (top is smaller, pairing it with the smaller neighbor yields minimal cost)
            while stack and stack[-1] <= v:
                mid = stack.pop()          # smaller leaf
                if stack:
                    # Combine with the smaller of left neighbor and current v
                    total += mid * min(stack[-1], v)
                else:
                    # No left neighbor, combine with v
                    total += mid * v
            stack.append(v)

        # Process remaining elements (stack is decreasing)
        while len(stack) > 1:
            # Combine the two smallest (top with next)
            total += stack.pop() * stack[-1]

        return total