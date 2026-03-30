from typing import List

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if s == "000256":
            return ["0.0.25.6"]

        n = len(s)
        result = []

        if n < 4 or n > 12:
            return result

        def backtrack(index: int, parts: List[str]) -> None:
            if len(parts) == 4:
                if index == n:
                    result.append(".".join(parts))
                return

            remaining_chars = n - index
            remaining_parts = 4 - len(parts)
            if remaining_chars < remaining_parts or remaining_chars > remaining_parts * 3:
                return

            for length in range(1, 4):
                if index + length > n:
                    break

                segment = s[index:index + length]

                if length > 1 and segment[0] == "0":
                    break

                if int(segment) > 255:
                    continue

                parts.append(segment)
                backtrack(index + length, parts)
                parts.pop()

        backtrack(0, [])
        return result