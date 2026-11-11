class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        # Use two pointers scanning from the end of each string
        i, j = len(s) - 1, len(t) - 1

        while i >= 0 or j >= 0:
            # Skip characters in s that are canceled by backspaces
            skip_s = 0
            while i >= 0:
                if s[i] == '#':
                    skip_s += 1
                    i -= 1
                elif skip_s > 0:
                    # skip current character (its backspace was found to the right)
                    skip_s -= 1
                    i -= 1
                else:
                    # this character is not skipped
                    break

            # Skip characters in t similarly
            skip_t = 0
            while j >= 0:
                if t[j] == '#':
                    skip_t += 1
                    j -= 1
                elif skip_t > 0:
                    skip_t -= 1
                    j -= 1
                else:
                    break

            # Now we have the next effective characters (or both exhausted)
            if i < 0 and j < 0:
                # both strings fully processed
                return True
            if i < 0 or j < 0:
                # one string exhausted, the other still has characters
                return False
            if s[i] != t[j]:
                return False

            # Move to the next character to compare
            i -= 1
            j -= 1

        return True