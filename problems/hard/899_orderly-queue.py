class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        # If k == 1, only the first character can be moved, so only rotations
        # of the original string are possible.
        if k == 1:
            n = len(s)
            best = s
            for i in range(n):
                rotated = s[i:] + s[:i]
                if rotated < best:
                    best = rotated
            return best

        # If k >= 2, we can rearrange characters into any order, so the
        # lexicographically smallest string is simply the sorted string.
        return "".join(sorted(s))