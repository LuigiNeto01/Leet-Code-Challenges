class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        # Stack to keep track of scores at each nesting depth
        # Initialize with 0 as the base level score
        stack = [0]

        for ch in s:
            if ch == '(':
                # Start a new nested level with score 0
                stack.append(0)
            else:
                # End of a pair: pop the score of the inner content
                inner = stack.pop()
                if inner == 0:
                    # "()" has score 1, add to the parent level
                    stack[-1] += 1
                else:
                    # "(A)" scores 2 * A, add to the parent level
                    stack[-1] += 2 * inner

        # The total score is at the root level
        return stack[0]