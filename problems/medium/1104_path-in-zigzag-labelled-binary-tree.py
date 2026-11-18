from __future__ import annotations

class Solution:
    def pathInZigZagTree(self, label: int) -> list[int]:
        path = []
        curr = label
        while True:
            path.append(curr)
            if curr == 1:
                break
            row = curr.bit_length()
            min_row = 1 << (row - 1)
            max_row = (1 << row) - 1
            if row % 2 == 1:
                pos = curr - min_row
            else:
                pos = max_row - curr
            parent_row = row - 1
            parent_pos = pos // 2
            if parent_row % 2 == 1:
                min_parent = 1 << (parent_row - 1)
                parent_label = min_parent + parent_pos
            else:
                max_parent = (1 << parent_row) - 1
                parent_label = max_parent - parent_pos
            curr = parent_label
        path.reverse()
        return path