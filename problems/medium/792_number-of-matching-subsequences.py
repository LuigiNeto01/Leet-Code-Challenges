from __future__ import annotations
import collections
import bisect

class Solution:
    def numMatchingSubseq(self, s: str, words: list[str]) -> int:
        # Build a map from each character to list of indices where it appears in s
        # Since s is long, this allows fast lookup of the next occurrence.
        char_positions = collections.defaultdict(list)
        for idx, ch in enumerate(s):
            char_positions[ch].append(idx)

        count = 0
        for word in words:
            # Current position in s that we have matched up to (exclusive)
            cur = 0
            ok = True
            for ch in word:
                pos_list = char_positions.get(ch)
                if not pos_list:
                    ok = False
                    break
                # Find the first index >= cur using binary search
                i = bisect.bisect_left(pos_list, cur)
                if i == len(pos_list):
                    ok = False
                    break
                # Move cur to one past the matched index
                cur = pos_list[i] + 1
            if ok:
                count += 1

        return count