class Solution:
    def longestDupSubstring(self, s: str) -> str:
        # Suffix automaton construction.
        nxt = [{}]          # transitions
        link = [-1]         # suffix links
        length = [0]        # longest substring length for each state
        cnt = [0]           # occurrence counts
        end_at = [-1]       # one ending position for this state

        last = 0
        for i, ch in enumerate(s):
            cur = len(nxt)
            nxt.append({})
            length.append(length[last] + 1)
            link.append(0)
            cnt.append(1)          # this new state represents one prefix endpoint
            end_at.append(i)

            p = last
            while p != -1 and ch not in nxt[p]:
                nxt[p][ch] = cur
                p = link[p]

            if p == -1:
                link[cur] = 0
            else:
                q = nxt[p][ch]
                if length[p] + 1 == length[q]:
                    link[cur] = q
                else:
                    clone = len(nxt)
                    nxt.append(nxt[q].copy())
                    length.append(length[p] + 1)
                    link.append(link[q])
                    cnt.append(0)  # clones receive counts later through suffix links
                    end_at.append(end_at[q])

                    while p != -1 and nxt[p].get(ch) == q:
                        nxt[p][ch] = clone
                        p = link[p]

                    link[q] = clone
                    link[cur] = clone

            last = cur

        # Count occurrences by propagating endpoints from longer states to suffix links.
        order = sorted(range(len(nxt)), key=length.__getitem__, reverse=True)
        for v in order:
            p = link[v]
            if p != -1:
                cnt[p] += cnt[v]

        best_len = 0
        best_end = -1
        for v in range(len(nxt)):
            if cnt[v] >= 2 and length[v] > best_len:
                best_len = length[v]
                best_end = end_at[v]

        if best_len == 0:
            return ""
        return s[best_end - best_len + 1 : best_end + 1]