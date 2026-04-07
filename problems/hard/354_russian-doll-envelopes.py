from bisect import bisect_left
from typing import List

class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        # Sort by width ascending so widths can grow left to right.
        # For equal widths, sort height descending to forbid using
        # two envelopes with the same width in the LIS on heights.
        envelopes.sort(key=lambda x: (x[0], -x[1]))

        # tails[i] = smallest possible ending height of an increasing
        # subsequence of length i + 1 seen so far.
        tails = []

        for _, h in envelopes:
            # Find where this height fits in the LIS structure.
            # bisect_left keeps heights strictly increasing:
            # equal heights replace instead of extending.
            pos = bisect_left(tails, h)

            if pos == len(tails):
                # Height is larger than all current tails, so it extends LIS.
                tails.append(h)
            else:
                # Replace with a smaller/equal tail to keep future options open.
                tails[pos] = h

        # The LIS length on heights is the answer.
        return len(tails)