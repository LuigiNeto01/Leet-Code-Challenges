class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        # Use Union-Find (Disjoint Set Union) to group equivalent characters.
        # Since only lowercase letters, we can use a fixed-size parent array.
        parent = list(range(26))  # 0 for 'a', 1 for 'b', ... 25 for 'z'

        # Find with path compression
        def find(x: int) -> int:
            # Recursively find the root of x
            if parent[x] != x:
                parent[x] = find(parent[x])  # path compression
            return parent[x]

        # Union: make the smaller lexicographical character the root.
        # This ensures that the root of each component is the smallest letter in that group.
        def union(a: int, b: int) -> None:
            root_a = find(a)
            root_b = find(b)
            if root_a != root_b:
                # Make the smaller character the parent (root)
                if root_a < root_b:
                    parent[root_b] = root_a
                else:
                    parent[root_a] = root_b

        # Process all equivalence pairs from s1 and s2
        for c1, c2 in zip(s1, s2):
            union(ord(c1) - ord('a'), ord(c2) - ord('a'))

        # Build the result: for each character in baseStr, find its smallest equivalent.
        result_chars = []
        for ch in baseStr:
            idx = ord(ch) - ord('a')
            smallest_root = find(idx)  # root is the smallest char in the component
            result_chars.append(chr(smallest_root + ord('a')))

        return ''.join(result_chars)