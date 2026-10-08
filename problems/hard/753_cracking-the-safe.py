import sys

class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        # Increase recursion limit to handle worst-case depth (max 4096)
        sys.setrecursionlimit(10000)
        
        total_passwords = k ** n                     # number of n-digit passwords
        start = "0" * n                             # initial password (all zeros)
        visited = {start}                           # track which passwords we've seen
        path_digits = []                            # store digits in reverse order (appended after recursion)
        
        def dfs(current: str) -> bool:
            """Depth-first search constructing the shortest string.
            Returns True if all passwords have been visited at this point."""
            if len(visited) == total_passwords:
                return True
            
            # Try appending each digit in order [0, k-1]
            for d in range(k):
                digit = str(d)
                nxt = current[1:] + digit           # slide window: remove first char, add new digit
                if nxt not in visited:
                    visited.add(nxt)
                    if dfs(nxt):                     # if recursion succeeded
                        path_digits.append(digit)   # record the digit that led to success
                        return True
                    visited.remove(nxt)              # backtrack
            return False
        
        dfs(start)
        # The full answer is the initial n-digit string plus the recorded digits (in reverse order)
        return start + ''.join(reversed(path_digits))