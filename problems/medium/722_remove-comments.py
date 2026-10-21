from __future__ import annotations

class Solution:
    def removeComments(self, source: list[str]) -> list[str]:
        ans = []
        in_block = False
        cur = []  # characters of the current output line

        for line in source:
            i = 0
            n = len(line)

            # A new source line starts a new output line only when we're not
            # inside a block comment. Inside a block comment, newlines are
            # ignored and the current output line continues.
            if not in_block:
                cur = []

            while i < n:
                if not in_block:
                    if line.startswith("//", i):
                        # Line comment: ignore the rest of this line.
                        break

                    if line.startswith("/*", i):
                        # Block comment begins; its characters are skipped.
                        in_block = True
                        i += 2
                    else:
                        cur.append(line[i])
                        i += 1
                else:
                    if line.startswith("*/", i):
                        # Block comment ends; resume preserving code after it.
                        in_block = False
                        i += 2
                    else:
                        # All characters inside a block comment are ignored.
                        i += 1

            # Do not output a line while a block comment is still open,
            # because later text may still be joined to this same line.
            if not in_block and cur:
                ans.append("".join(cur))

        return ans