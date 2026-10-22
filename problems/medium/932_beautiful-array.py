class Solution:
    def beautifulArray(self, n: int) -> list[int]:
        # Recursively build a beautiful array for numbers 1..m.
        def build(m: int):
            if m == 1:
                return [1]

            # Put odds before evens. Odd-even sums are odd, while
            # 2 * nums[k] is always even, so cross-parity triples are safe.
            left = build((m + 1) // 2)   # values mapped to odd numbers
            right = build(m // 2)        # values mapped to even numbers

            # Scaling preserves the no-average property, so recursively
            # beautiful left/right parts stay beautiful after transformation.
            odds = [2 * x - 1 for x in left]
            evens = [2 * x for x in right]

            return odds + evens

        return build(n)