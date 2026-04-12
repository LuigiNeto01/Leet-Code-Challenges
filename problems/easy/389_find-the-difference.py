class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # Use bitwise XOR to cancel out matching characters.
        # XOR is commutative and x ^ x = 0, so chars present in both strings cancel.
        # Only the extra character in t will remain after XORing all characters.
        # This gives O(n) time and O(1) extra space.
        xor_acc = 0  # accumulator for XOR of character codes
        # XOR all characters in t (longer string)
        for ch in t:
            xor_acc ^= ord(ch)
        # XOR all characters in s (shorter string) to cancel shared letters
        for ch in s:
            xor_acc ^= ord(ch)
        # xor_acc now holds the code of the extra character; convert back to char
        return chr(xor_acc)