from collections import deque

class Solution:
    def kSimilarity(self, s1: str, s2: str) -> int:
        if s1 == s2:
            return 0

        n = len(s1)
        q = deque()
        q.append((s1, 0))
        visited = {s1}

        while q:
            cur, dist = q.popleft()
            cur_list = list(cur)

            i = 0
            while i < n and cur_list[i] == s2[i]:
                i += 1

            for j in range(i + 1, n):
                if cur_list[j] == s2[i]:
                    cur_list[i], cur_list[j] = cur_list[j], cur_list[i]
                    new_str = ''.join(cur_list)

                    if new_str == s2:
                        return dist + 1

                    if new_str not in visited:
                        visited.add(new_str)
                        q.append((new_str, dist + 1))

                    cur_list[i], cur_list[j] = cur_list[j], cur_list[i]

        return -1