from collections import Counter

class Solution:
    def originalDigits(self, s: str) -> str:
        count = Counter(s)
        digits = [0] * 10

        digits[0] = count["z"]
        digits[2] = count["w"]
        digits[4] = count["u"]
        digits[6] = count["x"]
        digits[8] = count["g"]

        digits[3] = count["h"] - digits[8]
        digits[5] = count["f"] - digits[4]
        digits[7] = count["s"] - digits[6]

        digits[1] = count["o"] - digits[0] - digits[2] - digits[4]

        # Use 'n' for nine after accounting for one and seven.
        digits[9] = (count["n"] - digits[1] - digits[7]) // 2

        return "".join(str(digit) * digits[digit] for digit in range(10))