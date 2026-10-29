class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        # Lengths must be equal for a swap to possibly work.
        if len(s) != len(goal):
            return False

        # If strings are already equal, we need a duplicate character.
        if s == goal:
            seen = set()
            for ch in s:
                if ch in seen:
                    return True
                seen.add(ch)
            return False

        # Collect indices where s and goal differ.
        diff = []
        for i in range(len(s)):
            if s[i] != goal[i]:
                diff.append(i)
                # More than two mismatches cannot be fixed by a single swap.
                if len(diff) > 2:
                    return False

        # Exactly two mismatches are required.
        if len(diff) != 2:
            return False

        i, j = diff[0], diff[1]
        # The characters at these positions must be cross‑equal.
        return s[i] == goal[j] and s[j] == goal[i]