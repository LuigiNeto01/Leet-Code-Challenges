from __future__ import annotations

class Solution:
    def longestMountain(self, arr: list[int]) -> int:
        n = len(arr)
        max_len = 0

        # A mountain must have at least one peak (arr[i] > arr[i-1] and arr[i] > arr[i+1]).
        # For each potential peak, expand left and right to find the full mountain.
        for i in range(1, n - 1):
            if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
                # Expand left while strictly increasing (going downwards from peak)
                left = i - 1
                while left > 0 and arr[left] > arr[left - 1]:
                    left -= 1

                # Expand right while strictly decreasing (going downwards from peak)
                right = i + 1
                while right < n - 1 and arr[right] > arr[right + 1]:
                    right += 1

                # Calculate current mountain length
                cur_len = right - left + 1
                if cur_len > max_len:
                    max_len = cur_len

                # Skip ahead to the end of this mountain to avoid re-checking inside it
                # i = right - 1  (the loop will increment i, so set to right-1)
                # This is optional but improves efficiency.
                # Not necessary if we keep simple loop, but helpful for clarity.
                i = right  # next iteration will i++ from the loop, so start at right

        return max_len