class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        # Base case: the first row is always "0".
        if n == 1:
            return 0

        # The previous row occupies exactly half of the current row.
        half = 1 << (n - 2)

        if k <= half:
            # First half is the same as the previous row.
            return self.kthGrammar(n - 1, k)

        # Second half is the complement of the corresponding previous row value.
        return 1 - self.kthGrammar(n - 1, k - half)