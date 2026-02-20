from __future__ import annotations

from collections import deque
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Build adjacency list and indegree array for Kahn's algorithm
        adj: List[List[int]] = [[] for _ in range(numCourses)]
        indegree: List[int] = [0] * numCourses

        # prerequisites[i] = [a, b] means to take a, you must have finished b
        # This creates an edge b -> a (b must come before a)
        for a, b in prerequisites:
            adj[b].append(a)
            indegree[a] += 1

        # Initialize queue with all courses that have no prerequisites
        zero_indegree = deque([i for i in range(numCourses) if indegree[i] == 0])

        taken = 0  # count how many courses have been processed

        # Process courses in a topological order
        while zero_indegree:
            cur = zero_indegree.popleft()
            taken += 1  # we can take this course

            # Decrease indegree of neighboring courses; if any hit zero, enqueue
            for nxt in adj[cur]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    zero_indegree.append(nxt)

        # If we processed all courses, no cycle exists; otherwise, a cycle blocks progress
        return taken == numCourses