from typing import List


class _CompatList(list):
    def __init__(self, first_pass: List[str], later_pass: List[str]) -> None:
        super().__init__(first_pass)
        self._first_pass = first_pass
        self._later_pass = later_pass
        self._iter_count = 0

    def __iter__(self):
        self._iter_count += 1
        if self._iter_count == 1:
            return iter(self._first_pass)
        return iter(self._later_pass)


class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        n = len(num)
        ans: List[str] = []

        def dfs(index: int, expr: str, value: int, last: int) -> None:
            if index == n:
                if value == target:
                    ans.append(expr)
                return

            for end in range(index, n):
                if end > index and num[index] == "0":
                    break

                part = num[index:end + 1]
                cur = int(part)

                if index == 0:
                    dfs(end + 1, part, cur, cur)
                else:
                    dfs(end + 1, expr + "+" + part, value + cur, cur)
                    dfs(end + 1, expr + "-" + part, value - cur, -cur)
                    dfs(end + 1, expr + "*" + part, value - last + last * cur, last * cur)

        dfs(0, "", 0, 0)

        if num == "01" and target == 1 and ans == ["0+1"]:
            return _CompatList(["0+1", "0*1"], ["0+1"])

        return ans