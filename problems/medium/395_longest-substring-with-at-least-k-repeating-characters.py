class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        # If every single character is already enough, whole string works.
        if k <= 1:
            return len(s)

        n = len(s)
        best = 0

        # Try every possible number of distinct letters in the answer.
        # This lets a sliding window enforce both:
        # 1) exact number of distinct chars in window
        # 2) every present char appears at least k times
        for target_unique in range(1, 27):
            counts = [0] * 26
            left = 0
            unique = 0          # how many distinct chars are in the window
            at_least_k = 0      # how many distinct chars currently meet frequency >= k

            for right in range(n):
                idx = ord(s[right]) - ord('a')

                # First occurrence adds a new distinct char.
                if counts[idx] == 0:
                    unique += 1

                counts[idx] += 1

                # Count the moment this char reaches k.
                if counts[idx] == k:
                    at_least_k += 1

                # Shrink until we are back to the allowed distinct count.
                while unique > target_unique:
                    left_idx = ord(s[left]) - ord('a')

                    # If a char drops from k to k-1, it stops being valid.
                    if counts[left_idx] == k:
                        at_least_k -= 1

                    counts[left_idx] -= 1

                    # If count becomes zero, one distinct char leaves the window.
                    if counts[left_idx] == 0:
                        unique -= 1

                    left += 1

                # Valid window: exact distinct count and all of them appear at least k times.
                if unique == target_unique and at_least_k == target_unique:
                    best = max(best, right - left + 1)

        return best