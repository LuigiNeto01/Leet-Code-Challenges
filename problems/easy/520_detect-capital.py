class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        # Check all three valid patterns using string methods
        # 1) All letters are capitals
        if word.isupper():
            return True
        # 2) All letters are lowercase
        if word.islower():
            return True
        # 3) First letter capital, rest lowercase
        if word[0].isupper() and word[1:].islower():
            return True
        # None of the valid patterns matched
        return False