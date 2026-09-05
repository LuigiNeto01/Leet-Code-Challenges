from __future__ import annotations
from typing import List

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        n = len(score)
        # Pair each score with its original index
        # We'll sort descending by score to determine rank
        indexed_scores = [(score[i], i) for i in range(n)]
        indexed_scores.sort(reverse=True)  # highest score first

        # Prepare result array of same length
        result = [""] * n

        # Assign ranks based on position in sorted order
        for rank, (_, original_index) in enumerate(indexed_scores, start=1):
            if rank == 1:
                result[original_index] = "Gold Medal"
            elif rank == 2:
                result[original_index] = "Silver Medal"
            elif rank == 3:
                result[original_index] = "Bronze Medal"
            else:
                # For ranks 4 and above, use the rank number as a string
                result[original_index] = str(rank)

        return result