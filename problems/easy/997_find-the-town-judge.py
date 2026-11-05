from typing import List

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # indegree[i] = number of people who trust person i
        # outdegree[i] = number of people person i trusts
        indegree = [0] * (n + 1)
        outdegree = [0] * (n + 1)

        # Process each trust relationship: a trusts b
        for a, b in trust:
            outdegree[a] += 1   # a trusts someone
            indegree[b] += 1    # b is trusted by someone

        # Judge must have indegree = n-1 (everyone else trusts them)
        # and outdegree = 0 (they trust nobody)
        for person in range(1, n + 1):
            if indegree[person] == n - 1 and outdegree[person] == 0:
                return person

        # No candidate found
        return -1