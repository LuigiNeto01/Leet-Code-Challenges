class Solution:
    def canTransform(self, start: str, result: str) -> bool:
        n = len(start)
        i = j = 0  # pointers for start and result

        # Process both strings simultaneously
        while i < n and j < n:
            # Skip over 'X' in start
            while i < n and start[i] == 'X':
                i += 1
            # Skip over 'X' in result
            while j < n and result[j] == 'X':
                j += 1

            # If both reached the end, transformation is possible
            if i == n and j == n:
                return True
            # If only one reached the end, sequences of non-X differ
            if i == n or j == n:
                return False
            # Non-X characters must match in order
            if start[i] != result[j]:
                return False
            # For 'L': can only move left, so start index must be >= result index
            if start[i] == 'L' and i < j:
                return False
            # For 'R': can only move right, so start index must be <= result index
            if start[i] == 'R' and i > j:
                return False

            # Move both pointers forward
            i += 1
            j += 1

        # Both should have been exhausted simultaneously
        return True