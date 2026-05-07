class Solution:
    def countSegments(self, s: str) -> int:
        # Count transitions from space to non-space character
        # This avoids issues with leading/trailing/multiple spaces
        count = 0
        
        for i in range(len(s)):
            # A segment starts when current char is not space
            # and either it's the first char or previous char was space
            if s[i] != ' ' and (i == 0 or s[i - 1] == ' '):
                count += 1
        
        return count