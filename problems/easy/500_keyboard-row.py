from typing import List

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        # Define the three keyboard rows
        row1 = set('qwertyuiop')
        row2 = set('asdfghjkl')
        row3 = set('zxcvbnm')
        
        result = []
        
        for word in words:
            # Convert word to lowercase for case-insensitive comparison
            lower_word = word.lower()
            
            # Get the set of unique characters in the word
            char_set = set(lower_word)
            
            # Check if all characters belong to any single row
            # A word can be typed using one row if the char_set is a subset of that row
            if char_set <= row1 or char_set <= row2 or char_set <= row3:
                result.append(word)
        
        return result