class Solution:
    def largestComponentSize(self, nums: list[int]) -> int:
        n = len(nums)

        # DSU arrays: parent stores component representatives.
        parent = list(range(n))
        size = [1] * n

        def find(x: int) -> int:
            # Path compression keeps future lookups fast.
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a: int, b: int) -> None:
            # Merge the smaller component into the larger one.
            ra, rb = find(a), find(b)
            if ra == rb:
                return
            if size[ra] < size[rb]:
                ra, rb = rb, ra
            parent[rb] = ra
            size[ra] += size[rb]

        max_val = max(nums)

        # Build smallest prime factor table up to max(nums).
        spf = list(range(max_val + 1))
        limit = int(max_val ** 0.5)
        for p in range(2, limit + 1):
            if spf[p] == p:
                for multiple in range(p * p, max_val + 1, p):
                    if spf[multiple] == multiple:
                        spf[multiple] = p

        # Maps each prime factor to a number index already containing it.
        prime_owner = {}

        for i, value in enumerate(nums):
            x = value
            while x > 1:
                p = spf[x]

                # Numbers sharing a prime factor belong to the same component.
                if p in prime_owner:
                    union(i, prime_owner[p])
                else:
                    prime_owner[p] = i

                # Remove all copies of this prime to process distinct factors only.
                while x % p == 0:
                    x //= p

        # The answer is the largest root component size.
        return max(size[find(i)] for i in range(n))