class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Handle trivial impossible case early: if target longer than source, no window possible
        if len(t) > len(s):
            return ""
        from collections import Counter, defaultdict

        # Frequency map of characters required from t (handles duplicates)
        dict_t = Counter(t)
        # Number of unique characters in t that must be present in the window with required freq
        required = len(dict_t)

        # window_counts stores current window character frequencies
        window_counts = defaultdict(int)
        # formed counts how many unique characters currently meet the required frequency in the window
        formed = 0

        # Two pointers for sliding window [l, r]
        l = 0
        r = 0

        # Answer tuple: (window length, left index, right index)
        ans_len = float("inf")
        ans_l = 0
        ans_r = 0

        # Expand the window with r
        while r < len(s):
            ch = s[r]
            window_counts[ch] += 1

            # If this character's count matches the required count in t, we consider it "formed"
            if ch in dict_t and window_counts[ch] == dict_t[ch]:
                formed += 1

            # Try and contract the window till it ceases to be 'desirable'
            while l <= r and formed == required:
                # Update smallest window if the current one is smaller
                window_size = r - l + 1
                if window_size < ans_len:
                    ans_len = window_size
                    ans_l = l
                    ans_r = r

                # Character to remove from the left
                left_char = s[l]
                window_counts[left_char] -= 1

                # If removing this char makes its count fall below required, we are no longer 'formed' for that char
                if left_char in dict_t and window_counts[left_char] < dict_t[left_char]:
                    formed -= 1

                # Move left pointer to contract
                l += 1

            # Move right pointer to expand
            r += 1

        # If ans_len was updated, return the substring, else return empty string
        if ans_len == float("inf"):
            return ""
        return s[ans_l:ans_r + 1]