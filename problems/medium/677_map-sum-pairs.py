from __future__ import annotations

class MapSum:
    """
    Trie-based solution: each node stores the sum of values for all keys
    passing through that node. On insert, we update the trie nodes along
    the key path, handling overrides by tracking previous value per key.
    """

    def __init__(self):
        # Trie structure as nested dicts: each node maps char -> {children}
        # plus a special key 'sum' to accumulate values for this prefix.
        self.trie = {}
        # Keep track of the original value for each inserted key
        # so we can correctly update sums when a key is overridden.
        self.map = {}

    def insert(self, key: str, val: int) -> None:
        # Calculate the delta: if key existed, we need to adjust by the difference.
        delta = val - self.map.get(key, 0)
        # Store the new value for possible future overrides.
        self.map[key] = val

        node = self.trie
        # Traverse each character, ensuring nodes exist, and update sum.
        for ch in key:
            if ch not in node:
                node[ch] = {}
            node = node[ch]
            # 'sum' accumulates the total value of keys that share this prefix.
            # Using setdefault ensures the key exists before we add.
            node['sum'] = node.get('sum', 0) + delta

    def sum(self, prefix: str) -> int:
        node = self.trie
        # Navigate the trie along the prefix characters.
        for ch in prefix:
            if ch not in node:
                # Prefix not found — no keys match.
                return 0
            node = node[ch]
        # Return the sum stored at the final prefix node.
        # If prefix is empty string, node is root (which has no 'sum' key).
        return node.get('sum', 0)


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)