from typing import List
from collections import deque, defaultdict

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # If endWord is not in wordList, no valid transformation exists
        if endWord not in wordList:
            return 0
        
        # Convert wordList to set for O(1) lookup
        word_set = set(wordList)
        
        # Build a generic state map: for each word, create patterns with * wildcard
        # e.g., "hot" -> "*ot", "h*t", "ho*"
        # This allows us to find all words differing by one letter efficiently
        pattern_map = defaultdict(list)
        for word in word_set:
            for i in range(len(word)):
                pattern = word[:i] + '*' + word[i+1:]
                pattern_map[pattern].append(word)
        
        # BFS to find shortest path from beginWord to endWord
        queue = deque([(beginWord, 1)])  # (current_word, level/length)
        visited = {beginWord}  # Track visited words to avoid cycles
        
        while queue:
            current_word, level = queue.popleft()
            
            # Generate all patterns for current word
            for i in range(len(current_word)):
                pattern = current_word[:i] + '*' + current_word[i+1:]
                
                # Check all words matching this pattern
                for neighbor in pattern_map[pattern]:
                    # If we reached the endWord, return the length
                    if neighbor == endWord:
                        return level + 1
                    
                    # If not visited, add to queue
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, level + 1))
                
                # Clear the pattern to avoid revisiting (optimization)
                pattern_map[pattern] = []
        
        # No transformation sequence found
        return 0