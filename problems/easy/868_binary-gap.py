class Solution:
    def binaryGap(self, n: int) -> int:
        ans = 0
        last = -1
        # Scan binary representation, comparing each 1 with the previous 1
        for i, ch in enumerate(bin(n)[2:]):
            if ch == '1':
                if last != -1:
                    ans = max(ans, i - last)
                last = i
        return ans