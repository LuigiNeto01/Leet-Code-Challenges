class Solution:
    def validateStackSequences(self, pushed: list[int], popped: list[int]) -> bool:
        # Simulate stack operations
        stack = []               # actual stack we are using
        pop_index = 0            # pointer to next element in popped to match

        for value in pushed:
            # Push the current value onto the stack
            stack.append(value)

            # While the top of the stack matches the next popped element, pop it
            while stack and stack[-1] == popped[pop_index]:
                stack.pop()
                pop_index += 1   # move to next element in popped sequence

        # If we matched all popped elements, the sequence is valid
        return pop_index == len(popped)