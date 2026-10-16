class Solution:
    def uniqueLetterString(self, s: str) -> int:
        n = len(s)

        # prev_same[i] = previous index with the same character, or -1
        prev_same = [-1] * n
        last_pos = {}
        for i, ch in enumerate(s):
            prev_same[i] = last_pos.get(ch, -1)
            last_pos[ch] = i

        # next_same[i] = next index with the same character, or n
        next_same = [n] * n
        last_pos = {}
        for i in range(n - 1, -1, -1):
            ch = s[i]
            next_same[i] = last_pos.get(ch, n)
            last_pos[ch] = i

        ans = 0
        for i in range(n):
            # Substrings where s[i] is unique must start after prev_same[i]
            # and end before next_same[i].
            left_choices = i - prev_same[i]
            right_choices = next_same[i] - i
            ans += left_choices * right_choices

        return ans