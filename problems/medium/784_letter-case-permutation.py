class Solution:
    def letterCasePermutation(self, s: str) -> list[str]:
        """
        Returns all possible strings by toggling case of each letter.
        Uses backtracking to build each permutation.
        """
        n = len(s)
        result = []          # stores all generated strings
        current = []         # builds one permutation as list of characters

        def backtrack(idx: int) -> None:
            # Base case: processed all characters, record the result
            if idx == n:
                result.append("".join(current))
                return

            ch = s[idx]

            # Digits: no case variation, simply append and continue
            if ch.isdigit():
                current.append(ch)
                backtrack(idx + 1)
                current.pop()   # backtrack
                return

            # Letters: two possibilities – lowercase and uppercase
            # 1. Lowercase version
            current.append(ch.lower())
            backtrack(idx + 1)
            current.pop()

            # 2. Uppercase version
            current.append(ch.upper())
            backtrack(idx + 1)
            current.pop()

        backtrack(0)
        return result