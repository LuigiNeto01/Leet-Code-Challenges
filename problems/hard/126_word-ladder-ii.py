from typing import List
from collections import defaultdict, deque

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        # Early exit if endWord not in wordList
        word_set = set(wordList)
        if endWord not in word_set:
            return []
        
        # Build adjacency graph for all words (including beginWord)
        word_set.add(beginWord)
        neighbors = defaultdict(list)
        
        # For each word, find all words that differ by one letter
        for word in word_set:
            for i in range(len(word)):
                # Try all possible single letter changes
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    if c != word[i]:
                        next_word = word[:i] + c + word[i+1:]
                        if next_word in word_set:
                            neighbors[word].append(next_word)
        
        # BFS to find shortest distance from beginWord to all reachable words
        distances = {beginWord: 0}
        queue = deque([beginWord])
        
        while queue:
            word = queue.popleft()
            for neighbor in neighbors[word]:
                if neighbor not in distances:
                    distances[neighbor] = distances[word] + 1
                    queue.append(neighbor)
        
        # If endWord not reachable, return empty
        if endWord not in distances:
            return []
        
        # DFS to build all shortest paths from beginWord to endWord
        result = []
        
        def dfs(word, path):
            # Base case: reached endWord
            if word == endWord:
                result.append(path[:])
                return
            
            # Only explore neighbors that are one step closer to endWord
            for neighbor in neighbors[word]:
                if neighbor in distances and distances[neighbor] == distances[word] + 1:
                    path.append(neighbor)
                    dfs(neighbor, path)
                    path.pop()
        
        dfs(beginWord, [beginWord])
        return result