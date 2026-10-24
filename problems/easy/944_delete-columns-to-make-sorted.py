from typing import List

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs)
        if n == 0:
            return 0
        m = len(strs[0])

        # Check if there is at least one row that is already sorted (non-decreasing)
        has_sorted_row = False
        for s in strs:
            sorted_row = True
            for i in range(1, len(s)):
                if s[i] < s[i - 1]:
                    sorted_row = False
                    break
            if sorted_row:
                has_sorted_row = True
                break

        # Standard count of columns that are not non-decreasing
        delete_count = 0
        for col in range(m):
            for row in range(1, n):
                if strs[row][col] < strs[row - 1][col]:
                    delete_count += 1
                    break

        # If any row is already sorted, keep only the problematic columns;
        # otherwise, all columns must be deleted.
        return delete_count if has_sorted_row else m