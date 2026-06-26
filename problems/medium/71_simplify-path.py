class Solution:
    def simplifyPath(self, path: str) -> str:
        # Split path by '/' to get individual components
        components = path.split('/')
        
        # Stack to build the canonical path
        stack = []
        
        for comp in components:
            # Skip empty strings (from consecutive slashes) and current dir '.'
            if comp == '' or comp == '.':
                continue
            # '..' means go to parent directory
            elif comp == '..':
                # Pop from stack only if there's a directory to go back to
                if stack:
                    stack.pop()
            else:
                # Valid directory or file name (including '...', '....', etc.)
                stack.append(comp)
        
        # Build the canonical path: start with '/' and join with '/'
        # If stack is empty, return root '/'
        return '/' + '/'.join(stack)