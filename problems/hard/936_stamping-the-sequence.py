from collections import deque

class Solution:
    def movesToStamp(self, stamp: str, target: str) -> list[int]:
        m, n = len(stamp), len(target)
        if m > n:
            return []

        window_count = n - m + 1

        # mismatch[i] = number of positions in window i that are not '?'
        # and do not match the stamp letter in that position.
        mismatch = [0] * window_count
        for i in range(window_count):
            cnt = 0
            for k in range(m):
                if target[i + k] != stamp[k]:
                    cnt += 1
            mismatch[i] = cnt

        # Windows that are already fully stampable can be undone first.
        q = deque(i for i in range(window_count) if mismatch[i] == 0)

        done = [False] * n          # positions already turned into '?' in reverse
        used_window = [False] * window_count
        ans = []
        finished = 0

        while q:
            i = q.popleft()
            if used_window[i]:
                continue
            used_window[i] = True

            made_change = False

            # "Undo" this stamp: turn its positions into '?'.
            for p in range(i, i + m):
                if done[p]:
                    continue

                done[p] = True
                finished += 1
                made_change = True

                # This new '?' can satisfy any window covering position p.
                left = max(0, p - m + 1)
                right = min(p, window_count - 1)
                for j in range(left, right + 1):
                    if target[p] != stamp[p - j]:
                        mismatch[j] -= 1
                        if mismatch[j] == 0:
                            q.append(j)

            # Skip reverse stamps that change nothing; they are unnecessary.
            if made_change:
                ans.append(i)

        if finished == n:
            return ans[::-1]
        return []