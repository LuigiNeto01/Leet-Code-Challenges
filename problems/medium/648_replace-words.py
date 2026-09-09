from __future__ import annotations
from typing import List

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        # Build a Trie from the dictionary of roots
        # Each node: children dict and flag indicating end of a root
        trie = {}
        for root in dictionary:
            node = trie
            for ch in root:
                if ch not in node:
                    node[ch] = {}
                node = node[ch]
            # Mark the end of a root
            node['#'] = True

        # Process each word in the sentence
        words = sentence.split()
        result = []
        for word in words:
            node = trie
            replacement = None
            # Traverse the Trie for the current word to find the shortest root
            for i, ch in enumerate(word):
                if ch not in node:
                    # No further matching prefix; stop searching
                    break
                node = node[ch]
                # If we reach an end-of-root marker, we've found the shortest root
                # (since we stop at the first one due to BFS-like order)
                if '#' in node:
                    replacement = word[:i+1]
                    break
            # If a root was found, use it; otherwise keep original word
            result.append(replacement if replacement is not None else word)

        return ' '.join(result)