class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Strip trailing spaces to handle cases like "hello world  "
        s = s.rstrip()
        
        # Count characters from the end until we hit a space
        length = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == ' ':
                # Found the start of the last word
                break
            length += 1
        
        return length