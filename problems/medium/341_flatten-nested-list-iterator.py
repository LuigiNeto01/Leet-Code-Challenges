class NestedIterator:
    def __init__(self, nestedList):
        # Use a stack to store elements in reverse order for proper iteration
        # Stack will contain NestedInteger objects
        self.stack = []
        # Add elements in reverse order so we can pop from the end
        for i in range(len(nestedList) - 1, -1, -1):
            self.stack.append(nestedList[i])
    
    def next(self) -> int:
        # hasNext() ensures top of stack is an integer
        # Pop and return the integer value
        return self.stack.pop().getInteger()
    
    def hasNext(self) -> bool:
        # Flatten nested lists until we find an integer or stack is empty
        while self.stack:
            top = self.stack[-1]  # Peek at top element
            
            if top.isInteger():
                # Found an integer, we have a next element
                return True
            
            # Top is a nested list, expand it
            self.stack.pop()
            nested_list = top.getList()
            
            # Push elements in reverse order to maintain correct iteration order
            for i in range(len(nested_list) - 1, -1, -1):
                self.stack.append(nested_list[i])
        
        # Stack is empty, no more elements
        return False