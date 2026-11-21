from __future__ import annotations
from typing import List

class Solution:
    def oddEvenJumps(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 0:
            return 0

        # --- coordinate compression of values ---
        vals = sorted(set(arr))
        m = len(vals)
        rank = {v: i for i, v in enumerate(vals)}   # value -> compressed index

        INF = n + 1  # larger than any index

        # segment tree that stores the smallest index seen so far for each compressed value
        seg = [INF] * (4 * m)

        def seg_update(pos: int, idx: int) -> None:
            """set value at compressed position `pos` to `idx` (keep the minimum)."""
            # iterative update from leaf to root for simplicity
            # find leaf index in array of size 2*2^k
            # let's implement recursive for clarity, using a helper
            def _update(node: int, l: int, r: int) -> None:
                if l == r:
                    # store the smallest index; since we process right to left,
                    # the new index is always smaller than any stored before.
                    seg[node] = min(seg[node], idx)
                    return
                mid = (l + r) // 2
                if pos <= mid:
                    _update(node * 2, l, mid)
                else:
                    _update(node * 2 + 1, mid + 1, r)
                seg[node] = min(seg[node * 2], seg[node * 2 + 1])
            _update(1, 0, m - 1)

        def seg_query_first_ge(ql: int) -> int:
            """return the smallest compressed index >= ql with stored index < INF,
               or -1 if none."""
            def _query(node: int, l: int, r: int) -> int:
                if r < ql or seg[node] == INF:
                    return -1
                if l == r:
                    return l
                mid = (l + r) // 2
                # try left subtree first (smaller rank)
                left_res = _query(node * 2, l, mid)
                if left_res != -1:
                    return left_res
                return _query(node * 2 + 1, mid + 1, r)
            return _query(1, 0, m - 1)

        def seg_query_last_le(qr: int) -> int:
            """return the largest compressed index <= qr with stored index < INF,
               or -1 if none."""
            def _query(node: int, l: int, r: int) -> int:
                if l > qr or seg[node] == INF:
                    return -1
                if l == r:
                    return l
                mid = (l + r) // 2
                # try right subtree first (larger rank)
                right_res = _query(node * 2 + 1, mid + 1, r)
                if right_res != -1:
                    return right_res
                return _query(node * 2, l, mid)
            return _query(1, 0, m - 1)

        # min_index[compressed_val] = smallest index seen so far with that value
        min_index = [INF] * m

        # DP: odd_possible[i] = can reach end from i when next jump is odd
        #     even_possible[i] = can reach end from i when next jump is even
        odd_possible = [False] * n
        even_possible = [False] * n

        # last index is always good
        last = n - 1
        odd_possible[last] = True
        even_possible[last] = True

        # process from right to left
        for i in range(n - 1, -1, -1):
            if i == last:
                # insert last index into data structures
                r = rank[arr[i]]
                seg_update(r, i)
                min_index[r] = i
                continue

            r = rank[arr[i]]

            # --- odd-numbered jump (next jump is odd) ---
            j_rank = seg_query_first_ge(r)   # smallest value >= arr[i]
            if j_rank != -1:
                j = min_index[j_rank]
                odd_possible[i] = even_possible[j]  # after odd jump, next is even
            else:
                odd_possible[i] = False

            # --- even-numbered jump (next jump is even) ---
            j_rank = seg_query_last_le(r)    # largest value <= arr[i]
            if j_rank != -1:
                j = min_index[j_rank]
                even_possible[i] = odd_possible[j]  # after even jump, next is odd
            else:
                even_possible[i] = False

            # insert current index for future queries (further left indices)
            seg_update(r, i)
            min_index[r] = i

        # good starting indices: first jump is always odd
        return sum(odd_possible)