from typing import List
from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        
        word_len = len(words[0])
        word_count = len(words)
        total_len = word_len * word_count
        
        # If the concatenated length exceeds s, no valid substring exists
        if total_len > len(s):
            return []
        
        # Count frequency of each word in words list
        word_freq = Counter(words)
        result = []
        
        # We only need to check word_len different starting positions
        # because positions differing by word_len are essentially shifting by one word
        for offset in range(word_len):
            left = offset
            right = offset
            current_freq = Counter()
            count = 0  # Number of valid words matched in current window
            
            # Slide the window through s, moving by word_len each time
            while right + word_len <= len(s):
                # Extract the word at the right pointer
                word = s[right:right + word_len]
                right += word_len
                
                if word in word_freq:
                    # Add this word to current window
                    current_freq[word] += 1
                    count += 1
                    
                    # If we have too many of this word, shrink from left
                    while current_freq[word] > word_freq[word]:
                        left_word = s[left:left + word_len]
                        current_freq[left_word] -= 1
                        count -= 1
                        left += word_len
                    
                    # Check if we have a valid concatenation
                    if count == word_count:
                        result.append(left)
                        # Shrink window by one word from left to continue searching
                        left_word = s[left:left + word_len]
                        current_freq[left_word] -= 1
                        count -= 1
                        left += word_len
                else:
                    # Word not in words list, reset the window
                    current_freq.clear()
                    count = 0
                    left = right
        
        return result