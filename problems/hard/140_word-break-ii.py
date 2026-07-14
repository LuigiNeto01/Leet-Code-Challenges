from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        # Convert wordDict to set for O(1) lookup
        word_set = set(wordDict)
        
        # Memoization cache: maps index -> list of all possible sentences from that index
        memo = {}
        
        def backtrack(start: int) -> List[str]:
            # Base case: reached end of string, return empty sentence
            if start == len(s):
                return [""]
            
            # Return cached result if already computed
            if start in memo:
                return memo[start]
            
            result = []
            
            # Try all possible word endings starting from 'start'
            for end in range(start + 1, len(s) + 1):
                word = s[start:end]
                
                # If current substring is a valid word
                if word in word_set:
                    # Recursively get all possible sentences from position 'end'
                    sub_sentences = backtrack(end)
                    
                    # Combine current word with each sub-sentence
                    for sub in sub_sentences:
                        # If sub is empty (we're at the end), just add the word
                        if sub:
                            result.append(word + " " + sub)
                        else:
                            result.append(word)
            
            # Cache the result for this starting position
            memo[start] = result
            return result
        
        return backtrack(0)