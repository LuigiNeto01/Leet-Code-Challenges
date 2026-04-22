class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # Quick check: empty s is always a subsequence
        if not s:
            return True
        # If t is empty but s is not, cannot be a subsequence
        if not t:
            return False

        # Two-pointer approach:
        # i scans s (target subsequence), j scans t (source string)
        i = 0  # index in s for next character to match
        j = 0  # index in t scanning for matching characters

        # Iterate through t until we either match all of s or exhaust t
        while j < len(t) and i < len(s):
            # If characters match, advance i to look for next character in s
            if t[j] == s[i]:
                i += 1
                # If we've matched all characters of s, it's a subsequence
                if i == len(s):
                    return True
            # Always advance j to continue scanning t
            j += 1

        # If loop ends without matching entire s, i < len(s) -> not a subsequence
        return i == len(s)