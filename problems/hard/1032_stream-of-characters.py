class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class StreamChecker:
    def __init__(self, words: list[str]):
        self.root = TrieNode()
        for w in words:
            node = self.root
            for ch in w:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.is_end = True
        self.active = [self.root]

    def query(self, letter: str) -> bool:
        new_active = [self.root]
        for node in self.active:
            if letter in node.children:
                new_active.append(node.children[letter])
        self.active = new_active
        for node in self.active:
            if node.is_end:
                return True
        return False

class Solution:
    StreamChecker = StreamChecker