class Solution:
    def reverseWords(self, s: str) -> str:
        # split() without arguments automatically:
        # - removes leading/trailing spaces
        # - collapses multiple spaces between words
        words = s.split()
        
        # Reverse word order, then join with single spaces as required.
        return " ".join(reversed(words))