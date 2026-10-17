from __future__ import annotations

class Solution:
    def expressiveWords(self, s: str, words: list[str]) -> int:
        """
        Returns the number of words that can be stretched to become s.
        """

        # Helper: compress a string into list of (char, count) tuples.
        def get_runs(t: str) -> list[tuple[str, int]]:
            if not t:
                return []
            runs = []
            i = 0
            n = len(t)
            while i < n:
                j = i
                # Extend j while same character
                while j < n and t[j] == t[i]:
                    j += 1
                runs.append((t[i], j - i))
                i = j
            return runs

        # Compress the target string s.
        s_runs = get_runs(s)
        count_stretchy = 0

        # Check each word.
        for w in words:
            w_runs = get_runs(w)
            # Must have the same number of groups.
            if len(w_runs) != len(s_runs):
                continue
            stretchy = True
            for (c_s, cnt_s), (c_w, cnt_w) in zip(s_runs, w_runs):
                # Characters must match.
                if c_s != c_w:
                    stretchy = False
                    break
                # Cannot shrink a group.
                if cnt_s < cnt_w:
                    stretchy = False
                    break
                # If sizes are equal, expansion is not allowed when cnt_s >= 3.
                if cnt_s == cnt_w:
                    if cnt_s >= 3:
                        stretchy = False
                        break
                else:  # cnt_s > cnt_w
                    # Expansion is only allowed if cnt_s >= 3.
                    if cnt_s < 3:
                        stretchy = False
                        break
            if stretchy:
                count_stretchy += 1

        return count_stretchy