3
class Solution:
    def maxChunksToSorted(self, arr: list[int]) -> int:
        chunks = 0
        current_max = 0

        for i, value in enumerate(arr):
            # Track the largest value seen in the current prefix.
            current_max = max(current_max, value)

            # If the prefix contains exactly values 0..i, it can be sorted independently.
            # This is a valid chunk boundary.
            if current_max == i:
                chunks += 1

        return chunks