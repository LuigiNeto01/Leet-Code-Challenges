class Solution:
    def reverseWords(self, s: str) -> str:
        # Split the input string by spaces to get individual words.
        words = s.split(' ')
        # Reverse each word using slicing and collect results.
        reversed_words = [word[::-1] for word in words]
        # Join the reversed words with a single space to reconstruct the sentence.
        return ' '.join(reversed_words)