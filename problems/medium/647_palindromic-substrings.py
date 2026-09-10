class Solution:
    def countSubstrings(self, s: str) -> int:
        """
        Count all palindromic substrings using expand around center.
        Each center can be a single character (odd length) or between two
        characters (even length). For each center, expand outward while
        the substring remains a palindrome and count each expansion.
        """
        n = len(s)
        count = 0

        # There are 2*n - 1 possible centers (odd and even)
        for center in range(2 * n - 1):
            # For odd centers: left = right = center // 2
            # For even centers: left = center // 2, right = left + 1
            left = center // 2
            right = left + (center % 2)
            # Expand as long as within bounds and characters match
            while left >= 0 and right < n and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1

        return count