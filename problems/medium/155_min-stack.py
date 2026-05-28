class MinStack:

    def __init__(self):
        # Main stack to store all values
        self.stack = []
        # Min stack to track minimum at each level
        # Each element stores the minimum value up to that point
        self.min_stack = []

    def push(self, val: int) -> None:
        # Push value to main stack
        self.stack.append(val)
        
        # Push to min_stack: either val itself (if new min) or current min
        if not self.min_stack:
            self.min_stack.append(val)
        else:
            # Store the minimum between current val and previous minimum
            self.min_stack.append(min(val, self.min_stack[-1]))

    def pop(self) -> None:
        # Remove from both stacks to maintain sync
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        # Return top of main stack
        return self.stack[-1]

    def getMin(self) -> int:
        # Return top of min_stack which is the current minimum
        return self.min_stack[-1]