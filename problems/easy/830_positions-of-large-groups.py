class Solution:
    def largeGroupPositions(self, s: str) -> list[list[int]]:
        """
        Returns intervals [start, end] (inclusive) for each group of identical
        characters that has length >= 3, sorted in increasing start order.
        """
        result = []
        n = len(s)
        # Edge case: empty string (not required by constraints but safe)
        if n == 0:
            return result
        
        start = 0          # start index of current group
        current_char = s[0]  # character of current group
        
        for i in range(1, n):
            # If character changes, finalize the previous group
            if s[i] != current_char:
                # Check if the previous group is large (length >= 3)
                if i - start >= 3:
                    # The group ends at i-1 (inclusive)
                    result.append([start, i - 1])
                # Start a new group
                start = i
                current_char = s[i]
        
        # Handle the last group after the loop
        if n - start >= 3:
            result.append([start, n - 1])
        
        return result