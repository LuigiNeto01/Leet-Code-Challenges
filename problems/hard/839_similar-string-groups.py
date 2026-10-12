class Solution:
    def numSimilarGroups(self, strs: list[str]) -> int:
        n = len(strs)
        length = len(strs[0]) if n else 0

        # Union-Find data structure (Disjoint Set Union)
        parent = list(range(n))
        size = [1] * n

        def find(x: int) -> int:
            # Path compression
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(x: int, y: int) -> None:
            # Union by size
            rx, ry = find(x), find(y)
            if rx == ry:
                return
            if size[rx] < size[ry]:
                rx, ry = ry, rx
            parent[ry] = rx
            size[rx] += size[ry]

        # Helper to check if two strings are similar
        def are_similar(s1: str, s2: str) -> bool:
            # Identical strings are similar
            if s1 == s2:
                return True
            # Since all strings are anagrams of each other,
            # they are similar iff they differ in exactly two positions.
            diff_pos = []
            for i in range(length):
                if s1[i] != s2[i]:
                    diff_pos.append(i)
                    # More than two differences -> can't be similar by one swap
                    if len(diff_pos) > 2:
                        return False
            # Exactly two differences -> those two positions can be swapped
            return len(diff_pos) == 2

        # Compare every pair of strings and union if similar
        for i in range(n):
            for j in range(i + 1, n):
                if are_similar(strs[i], strs[j]):
                    union(i, j)

        # Count number of distinct groups (roots)
        roots = set()
        for i in range(n):
            roots.add(find(i))
        return len(roots)