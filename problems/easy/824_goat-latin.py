class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        # Set of vowels for quick lookup (both cases)
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        
        # Split sentence into words
        words = sentence.split()
        result = []  # will hold transformed words
        
        # Process each word with its 1-based index
        for i, word in enumerate(words, start=1):
            # First character
            first = word[0]
            if first in vowels:
                # Vowel case: just append "ma"
                transformed = word + "ma"
            else:
                # Consonant case: move first letter to the end, then "ma"
                transformed = word[1:] + first + "ma"
            # Append 'a' repeated i times
            transformed += 'a' * i
            result.append(transformed)
        
        # Join back into a single string
        return " ".join(result)