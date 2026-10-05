class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        # Minimum repeats so that length of repeated a is at least len(b).
        # ceil(len(b) / len(a)) = (len(b) + len(a) - 1) // len(a)
        repeats = (len(b) + len(a) - 1) // len(a)

        # Build the repeated string with that many copies of a.
        repeated = a * repeats

        # If b is already a substring, we are done.
        if b in repeated:
            return repeats

        # If not, one more repeat may be needed (worst case: b starts at the end of a).
        # Append another copy of a and check once more.
        repeated += a
        if b in repeated:
            return repeats + 1

        # b cannot be formed by any number of repeats.
        return -1