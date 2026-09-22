class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        # Use binary search to find the smallest character > target.
        # Since letters is sorted non-decreasing, we can apply standard
        # binary search to locate the insertion point for target+1.
        left, right = 0, len(letters) - 1

        # If the target is >= last letter, wrap around to first.
        # But we handle it via binary search result.
        while left <= right:
            mid = (left + right) // 2
            # If letters[mid] <= target, search in the right half.
            if letters[mid] <= target:
                left = mid + 1
            else:
                # letters[mid] > target, could be the answer,
                # so narrow the search to the left half.
                right = mid - 1

        # After loop, left is the first index where letters[left] > target
        # OR left == len(letters) meaning no such character exists.
        if left < len(letters):
            return letters[left]
        else:
            # Wrap around: return the first character.
            return letters[0]