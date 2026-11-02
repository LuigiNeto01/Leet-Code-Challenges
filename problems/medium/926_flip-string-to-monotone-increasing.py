class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        total_zeros = s.count('0')
        # Split before the first character: make every character '1'
        ans = total_zeros

        ones_prefix = 0
        zeros_prefix = 0

        for ch in s:
            if ch == '1':
                ones_prefix += 1
            else:
                zeros_prefix += 1

            # Split after this character:
            # left side should be all 0s, right side should be all 1s.
            zeros_suffix = total_zeros - zeros_prefix
            flips = ones_prefix + zeros_suffix
            ans = min(ans, flips)

        return ans