class Solution:
    def lastRemaining(self, n: int) -> int:
        # Track the first value of the current arithmetic progression.
        head = 1

        # Gap between consecutive remaining numbers.
        step = 1

        # Number of values still alive.
        remaining = n

        # Direction of the current elimination pass.
        left_to_right = True

        # Simulate rounds using progression facts instead of storing the list.
        while remaining > 1:
            # From left to right, the first element always disappears,
            # so the new head shifts forward by one step.
            # From right to left, the head shifts only when count is odd,
            # because then the leftmost element gets removed as well.
            if left_to_right or remaining % 2 == 1:
                head += step

            # After removing every other element:
            # - count halves
            # - distance between survivors doubles
            remaining //= 2
            step *= 2

            # Alternate direction for the next round.
            left_to_right = not left_to_right

        return head