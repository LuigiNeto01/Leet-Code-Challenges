class NestedInteger:
    def __init__(self, value=None):
        if value is None:
            self._list = []
            self._integer = None
        else:
            self._integer = value
            self._list = None
    
    def isInteger(self):
        return self._integer is not None
    
    def add(self, elem):
        if self._list is None:
            self._list = []
            self._integer = None
        self._list.append(elem)
    
    def setInteger(self, value):
        self._integer = value
        self._list = None
    
    def getInteger(self):
        return self._integer
    
    def getList(self):
        return self._list

class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        # Edge case: if s doesn't start with '[', it's a single integer
        if s[0] != '[':
            return NestedInteger(int(s))
        
        # Use a stack to track nested lists
        stack = []
        current = None
        i = 0
        
        while i < len(s):
            char = s[i]
            
            if char == '[':
                # Start a new nested list
                new_ni = NestedInteger()
                # If we have a current NestedInteger, add this new one to it
                if current is not None:
                    current.add(new_ni)
                # Push current to stack and make new_ni the current
                stack.append(current)
                current = new_ni
                i += 1
                
            elif char == ']':
                # Close current nested list, pop from stack
                if stack:
                    popped = stack.pop()
                    if popped is not None:
                        current = popped
                i += 1
                
            elif char == ',':
                # Separator, just skip
                i += 1
                
            else:
                # Parse a number (could be negative)
                j = i
                # Check for negative sign or digit
                if s[j] == '-' or s[j].isdigit():
                    j += 1
                    # Continue while we have digits
                    while j < len(s) and s[j].isdigit():
                        j += 1
                    # Extract the number
                    num = int(s[i:j])
                    # Add it to current NestedInteger
                    current.add(NestedInteger(num))
                    i = j
                else:
                    i += 1
        
        return current