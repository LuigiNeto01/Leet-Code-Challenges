from __future__ import annotations

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        # Edge case: if string length < 2, no valid substring exists.
        if len(s) < 2:
            return 0

        # We'll scan the string and track lengths of consecutive groups.
        # prev_len: length of the previous group of identical characters.
        # curr_len: length of the current group we are building.
        # result: total count of valid substrings.
        prev_len = 0
        curr_len = 1  # First character starts a group of size 1.
        result = 0

        # Start from the second character
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                # Same character as previous -> continue current group
                curr_len += 1
            else:
                # Character changed -> the previous group ends.
                # The current group becomes the previous group for future comparisons.
                # The new current group starts with length 1.
                # Each adjacent pair (prev_len, curr_len) contributes min(prev_len, curr_len)
                # to the answer.
                result += min(prev_len, curr_len)
                # Move current group length to prev, start new current group
                prev_len = curr_len
                curr_len = 1

        # After the loop, don't forget to process the last pair:
        # the final group (curr_len) and its predecessor (prev_len).
        result += min(prev_len, curr_len)

        return result