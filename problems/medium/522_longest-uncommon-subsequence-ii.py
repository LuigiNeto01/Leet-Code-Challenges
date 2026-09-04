from typing import List

class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        # Helper to check if a is a subsequence of b
        def is_subseq(a: str, b: str) -> bool:
            i = 0
            # Scan b, matching characters of a in order
            for ch in b:
                if i < len(a) and ch == a[i]:
                    i += 1
                # Early exit if we matched all of a
                if i == len(a):
                    return True
            return i == len(a)

        n = len(strs)
        max_len = -1  # default answer if no uncommon subsequence

        # Check each string as a candidate for being uncommon
        for i in range(n):
            s = strs[i]
            # Assume it's uncommon until proven otherwise
            uncommon = True
            for j in range(n):
                if i == j:
                    continue  # skip comparing to itself
                # If s is a subsequence of any other string, it's common
                if is_subseq(s, strs[j]):
                    uncommon = False
                    break
            if uncommon:
                max_len = max(max_len, len(s))

        return max_len