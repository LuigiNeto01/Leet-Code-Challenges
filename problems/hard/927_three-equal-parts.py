from __future__ import annotations

class Solution:
    def threeEqualParts(self, arr: list[int]) -> list[int]:
        total_ones = sum(arr)
        if total_ones % 3 != 0:
            return [-1, -1]
        if total_ones == 0:
            return [0, len(arr) - 1]

        k = total_ones // 3
        first = second = third = -1
        cnt = 0
        for i, x in enumerate(arr):
            if x == 1:
                cnt += 1
                if cnt == 1:
                    first = i
                elif cnt == k + 1:
                    second = i
                elif cnt == 2 * k + 1:
                    third = i
                    break

        n = len(arr)
        L = n - third          # length of the common suffix

        # check that the three suffixes are identical
        for offset in range(L):
            if (arr[first + offset] != arr[second + offset] or
                arr[second + offset] != arr[third + offset]):
                return [-1, -1]

        # ensure the parts do not overlap incorrectly
        if first + L > second or second + L > third:
            return [-1, -1]

        return [first + L - 1, second + L]