class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> list[int]:
        # Build list of all x^i <= bound (i >= 0)
        powers_x = []
        val = 1
        while val <= bound:
            powers_x.append(val)
            if x == 1:          # avoid infinite loop for x=1
                break
            val *= x

        # Build list of all y^j <= bound (j >= 0)
        powers_y = []
        val = 1
        while val <= bound:
            powers_y.append(val)
            if y == 1:          # avoid infinite loop for y=1
                break
            val *= y

        # Generate all sums of two powers that do not exceed bound
        result = set()
        for px in powers_x:
            for py in powers_y:
                s = px + py
                if s <= bound:
                    result.add(s)

        # Return as a list (order does not matter)
        return list(result)