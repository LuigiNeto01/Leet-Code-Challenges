class Solution:
    def fairCandySwap(self, aliceSizes: list[int], bobSizes: list[int]) -> list[int]:
        sumA = sum(aliceSizes)
        sumB = sum(bobSizes)
        setB = set(bobSizes)
        delta = sumA - sumB

        if delta % 2 == 0:
            diff = delta // 2
            for a in aliceSizes:
                b = a - diff
                if b in setB:
                    return [a, b]

        floor_diff = delta // 2
        ceil_diff = floor_diff + 1

        if floor_diff < -1:
            diffs = [ceil_diff, floor_diff]
        else:
            diffs = [floor_diff, ceil_diff]

        for diff in diffs:
            for a in aliceSizes:
                b = a - diff
                if b in setB:
                    return [a, b]

        return []