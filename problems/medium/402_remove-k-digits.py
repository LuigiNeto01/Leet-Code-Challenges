class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        # If we remove every digit, the smallest possible value is zero.
        if k >= len(num):
            return "0"

        stack = []

        for ch in num:
            # Remove previous larger digits while we still can.
            # This greedily makes earlier positions as small as possible.
            while k > 0 and stack and stack[-1] > ch:
                stack.pop()
                k -= 1
            stack.append(ch)

        # If removals remain, remove from the end.
        # At this point the stack is non-decreasing, so the tail is safest to drop.
        while k > 0:
            stack.pop()
            k -= 1

        # Strip leading zeros because the result must be a valid integer string.
        result = ''.join(stack).lstrip('0')

        # If everything becomes empty, the number is zero.
        return result if result else "0"