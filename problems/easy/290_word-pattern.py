class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        
        # Pattern and words must have same length for bijection
        if len(pattern) != len(words):
            return False
        
        # Map from pattern character to word
        char_to_word = {}
        # Map from word to pattern character (to ensure bijection)
        word_to_char = {}
        
        for char, word in zip(pattern, words):
            # Check if char already mapped
            if char in char_to_word:
                # Must map to same word as before
                if char_to_word[char] != word:
                    return False
            else:
                # Create new mapping
                char_to_word[char] = word
            
            # Check if word already mapped
            if word in word_to_char:
                # Must map to same char as before
                if word_to_char[word] != char:
                    return False
            else:
                # Create new mapping
                word_to_char[word] = char
        
        return True