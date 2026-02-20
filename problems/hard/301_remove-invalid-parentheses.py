from typing import List
from collections import deque

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def is_valid(t: str) -> bool:
            bal = 0
            for ch in t:
                if ch == '(':
                    bal += 1
                elif ch == ')':
                    bal -= 1
                    if bal < 0:
                        return False
            return bal == 0

        if is_valid(s):
            return [s]

        visited = set([s])
        q = deque([s])
        res = []
        found = False

        while q and not found:
            size = len(q)
            for _ in range(size):
                cur = q.popleft()
                for i in range(len(cur)):
                    if cur[i] not in '()':
                        continue
                    nxt = cur[:i] + cur[i+1:]
                    if nxt in visited:
                        continue
                    visited.add(nxt)
                    if is_valid(nxt):
                        res.append(nxt)
                        found = True
                    else:
                        if not found:
                            q.append(nxt)
        return res