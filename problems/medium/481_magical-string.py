class Solution:
    def magicalString(self, n: int) -> int:
        # Handle the smallest prefix directly.
        if n <= 0:
            return 0
        if n <= 3:
            # Magical string starts as "122".
            return 1

        # Seed with the known prefix that bootstraps the self-generating process.
        s = [1, 2, 2]

        # `head` points to the next run-length we need to read from the string itself.
        head = 2

        # Next value to append; runs alternate between 1 and 2.
        num = 1

        # Count of ones already present in the seed "122".
        ones = 1

        # Grow until we have at least n characters.
        while len(s) < n:
            # The magical rule says current digit appears `s[head]` times.
            count = s[head]

            # Append the run one digit at a time so we can count only within first n chars.
            for _ in range(count):
                if len(s) >= n:
                    break
                s.append(num)
                if num == 1:
                    ones += 1

            # Move to the next run-length descriptor in the magical string.
            head += 1

            # Alternate the digit for the next run: 1 -> 2, 2 -> 1.
            num = 3 - num

        return ones