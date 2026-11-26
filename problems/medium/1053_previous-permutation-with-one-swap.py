import bisect

class Solution:
    def prevPermOpt1(self, arr: list[int]) -> list[int]:
        n = len(arr)
        if n <= 1:
            return arr

        # coordinate compression
        vals = sorted(set(arr))
        m = len(vals)

        # Fenwick tree storing the maximum value seen for each compressed index
        tree = [0] * (m + 2)

        def bit_update(idx: int, val: int) -> None:
            while idx <= m:
                if val > tree[idx]:
                    tree[idx] = val
                idx += idx & -idx

        def bit_query(idx: int) -> int:
            res = 0
            while idx:
                if tree[idx] > res:
                    res = tree[idx]
                idx -= idx & -idx
            return res

        def compress(v: int) -> int:
            # 1‑based compressed index
            return bisect.bisect_left(vals, v) + 1

        # insert the last element into the structure
        bit_update(compress(arr[-1]), arr[-1])

        rightmost_descent = -1
        selected_i = None

        # scan from right to left
        for i in range(n - 2, -1, -1):
            # largest value strictly less than arr[i] among already inserted elements
            pos = bisect.bisect_left(vals, arr[i])          # count of values < arr[i]
            max_less = 0
            if pos > 0:
                max_less = bit_query(pos)                  # prefix up to 'pos'

            # check for a descent
            if arr[i] > arr[i + 1]:
                if rightmost_descent == -1:
                    rightmost_descent = i
                # if there exists an element on the right that is > arr[i+1] and < arr[i]
                if max_less > arr[i + 1]:
                    selected_i = i
                    break

            # insert current element for further left positions
            bit_update(compress(arr[i]), arr[i])

        # if no "good" descent was found, fall back to the rightmost descent
        if selected_i is None:
            if rightmost_descent == -1:
                return arr
            selected_i = rightmost_descent

        # find the best position to swap with arr[selected_i]
        best_val = -1
        best_idx = -1
        for j in range(selected_i + 1, n):
            if arr[j] < arr[selected_i] and arr[j] > best_val:
                best_val = arr[j]
                best_idx = j
            # keep leftmost among equal values (do not overwrite on equality)

        # perform the swap
        arr[selected_i], arr[best_idx] = arr[best_idx], arr[selected_i]
        return arr