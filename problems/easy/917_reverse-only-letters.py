class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        """
        Reverses only the English letters in the string while keeping
        non-letter characters at their original positions.
        Uses two-pointer technique for O(n) time and O(n) space.
        """
        # Convert string to list for mutable operations
        chars = list(s)
        left = 0
        right = len(s) - 1

        while left < right:
            # Move left pointer to next letter (skip non-letters)
            while left < right and not chars[left].isalpha():
                left += 1

            # Move right pointer to previous letter (skip non-letters)
            while left < right and not chars[right].isalpha():
                right -= 1

            # Both pointers are at letters, swap them
            if left < right:
                chars[left], chars[right] = chars[right], chars[left]
                left += 1
                right -= 1

        # Return joined string from list
        return ''.join(chars)