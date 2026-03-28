class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # KMP finds the first match in linear time even in repetitive strings.
        m, n = len(needle), len(haystack)

        # If needle is longer, it can never fit inside haystack.
        if m > n:
            return -1

        # Build LPS (longest proper prefix which is also suffix) table.
        # lps[i] tells where to continue in needle after a mismatch at i.
        lps = [0] * m
        length = 0  # Current matched prefix length.
        i = 1

        while i < m:
            if needle[i] == needle[length]:
                # We can extend the current prefix-suffix match.
                length += 1
                lps[i] = length
                i += 1
            elif length > 0:
                # Fall back to a smaller valid prefix already computed.
                length = lps[length - 1]
            else:
                # No prefix works here, so lps stays 0.
                lps[i] = 0
                i += 1

        # Scan haystack and needle together using the fallback table.
        i = 0  # Index in haystack
        j = 0  # Index in needle

        while i < n:
            if haystack[i] == needle[j]:
                i += 1
                j += 1

                # Full needle matched; return its starting index.
                if j == m:
                    return i - m
            elif j > 0:
                # Keep haystack index, but try the next best needle prefix.
                j = lps[j - 1]
            else:
                # No partial match to preserve; move forward in haystack.
                i += 1

        # Reached the end without a full match.
        return -1