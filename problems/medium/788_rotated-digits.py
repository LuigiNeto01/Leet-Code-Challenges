class Solution:
    def rotatedDigits(self, n: int) -> int:
        # Digits that become invalid after rotation
        invalid = {'3', '4', '7'}
        # Digits that produce a different digit when rotated (so the number changes)
        changing = {'2', '5', '6', '9'}
        
        count = 0
        for num in range(1, n + 1):
            s = str(num)
            # If any digit is invalid, the number cannot be good
            if any(d in invalid for d in s):
                continue
            # If at least one digit changes, the rotated version differs from the original
            if any(d in changing for d in s):
                count += 1
        return count