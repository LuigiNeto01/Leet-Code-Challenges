from typing import List

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Build Trie from words
        trie = {}
        for word in words:
            node = trie
            for char in word:
                if char not in node:
                    node[char] = {}
                node = node[char]
            node['#'] = word  # Mark end of word with the word itself
        
        m, n = len(board), len(board[0])
        result = set()
        
        def dfs(i, j, node):
            # Out of bounds or character not in current trie node
            if i < 0 or i >= m or j < 0 or j >= n:
                return
            
            char = board[i][j]
            if char not in node or char == '#':  # '#' means visited
                return
            
            node = node[char]
            
            # If we found a complete word
            if '#' in node:
                result.add(node['#'])
                # Optional: remove the word from trie to avoid duplicate searches
                # del node['#']
            
            # Mark as visited
            board[i][j] = '#'
            
            # Explore all 4 directions
            dfs(i+1, j, node)
            dfs(i-1, j, node)
            dfs(i, j+1, node)
            dfs(i, j-1, node)
            
            # Backtrack: restore the character
            board[i][j] = char
        
        # Start DFS from each cell
        for i in range(m):
            for j in range(n):
                dfs(i, j, trie)
        
        return list(result)