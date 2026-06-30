from typing import List

class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        # Helper function to check if a string is a palindrome
        def is_palindrome(s):
            return s == s[::-1]
        
        # Build a dictionary mapping each word to its index
        word_dict = {word: i for i, word in enumerate(words)}
        result = []
        
        for i, word in enumerate(words):
            # For each word, we check all possible splits
            for j in range(len(word) + 1):
                # Split word into prefix and suffix
                prefix = word[:j]
                suffix = word[j:]
                
                # Case 1: if prefix is palindrome, check if reverse of suffix exists
                # This means: reverse(suffix) + word = reverse(suffix) + prefix + suffix
                # If prefix is palindrome, reverse(suffix) + prefix + suffix is a palindrome
                if is_palindrome(prefix):
                    reversed_suffix = suffix[::-1]
                    # Check if reversed suffix exists and is not the same word
                    if reversed_suffix in word_dict and word_dict[reversed_suffix] != i:
                        result.append([word_dict[reversed_suffix], i])
                
                # Case 2: if suffix is palindrome, check if reverse of prefix exists
                # This means: word + reverse(prefix) = prefix + suffix + reverse(prefix)
                # If suffix is palindrome, prefix + suffix + reverse(prefix) is a palindrome
                # We need j != len(word) to avoid duplicates (when suffix is empty, 
                # we would count the same pair twice with Case 1)
                if j != len(word) and is_palindrome(suffix):
                    reversed_prefix = prefix[::-1]
                    # Check if reversed prefix exists and is not the same word
                    if reversed_prefix in word_dict and word_dict[reversed_prefix] != i:
                        result.append([i, word_dict[reversed_prefix]])
        
        return result