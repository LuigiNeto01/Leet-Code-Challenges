class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        # If the strings are identical, every subsequence of one is also a subsequence of the other,
        # so there is no uncommon subsequence -> return -1.
        if a == b:
            return -1
        # Otherwise, the longer string itself is a subsequence of itself but not of the other
        # (because it's longer or has a different character), so its length is the answer.
        return max(len(a), len(b))