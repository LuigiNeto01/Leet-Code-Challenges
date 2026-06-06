class Trie:

    def __init__(self):
        # Root node represented as a dictionary
        # Each node is a dict where keys are characters and values are child nodes
        # We also store a boolean flag to mark end of words
        self.root = {}

    def insert(self, word: str) -> None:
        # Start from root and traverse/create nodes for each character
        node = self.root
        for char in word:
            # Create new node (dict) if character doesn't exist
            if char not in node:
                node[char] = {}
            # Move to the next node
            node = node[char]
        # Mark the end of the word with a special key
        node['$'] = True

    def search(self, word: str) -> bool:
        # Traverse the trie following the word's characters
        node = self.root
        for char in word:
            # If character not found, word doesn't exist
            if char not in node:
                return False
            node = node[char]
        # Check if this is actually the end of a word (not just a prefix)
        return '$' in node

    def startsWith(self, prefix: str) -> bool:
        # Similar to search but we don't need to check for end-of-word marker
        node = self.root
        for char in prefix:
            # If character not found, prefix doesn't exist
            if char not in node:
                return False
            node = node[char]
        # If we successfully traversed all characters, prefix exists
        return True