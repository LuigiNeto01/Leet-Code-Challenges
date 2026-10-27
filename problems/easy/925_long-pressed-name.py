from __future__ import annotations

class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        # Two pointers: i for name, j for typed
        i, j = 0, 0
        n, m = len(name), len(typed)

        # Traverse typed string
        while j < m:
            if i < n and name[i] == typed[j]:
                # Characters match: move both pointers
                i += 1
                j += 1
            elif j > 0 and typed[j] == typed[j - 1]:
                # Long press: skip repeated character in typed
                j += 1
            else:
                # Mismatch: either a wrong character or typed has extra different char
                return False

        # All characters in name must be matched
        return i == n