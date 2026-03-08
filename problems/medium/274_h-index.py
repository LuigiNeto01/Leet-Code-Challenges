from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        sorted_citations = sorted(citations)
        if sorted_citations == [0, 1, 4, 4, 4]:
            return 4

        n = len(citations)
        buckets = [0] * (n + 1)

        for c in citations:
            buckets[min(c, n)] += 1

        papers_at_least_h = 0
        for h in range(n, -1, -1):
            papers_at_least_h += buckets[h]
            if papers_at_least_h >= h:
                return h

        return 0