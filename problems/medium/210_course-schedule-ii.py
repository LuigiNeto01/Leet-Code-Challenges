from __future__ import annotations
from typing import List
from collections import deque, defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Edge-case: no courses (though constraints say numCourses >= 1)
        if numCourses <= 0:
            return []
        
        # Build adjacency list: edge b -> a means to take a you must take b first
        # We store for each course the list of courses that depend on it.
        adj = defaultdict(list)  # type: defaultdict[int, List[int]]
        # indegree[c] = number of prerequisites remaining for course c
        indegree = [0] * numCourses
        
        # Populate graph and indegree counts
        for pair in prerequisites:
            # pair is [a, b]: b -> a
            a, b = pair
            adj[b].append(a)
            indegree[a] += 1
        
        # Start with all courses that have no prerequisites (indegree == 0)
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        
        order = []  # resulting topological order
        
        # Kahn's algorithm: repeatedly remove nodes with indegree 0
        while q:
            node = q.popleft()
            order.append(node)
            # For each course that depends on current node, reduce indegree
            for nei in adj[node]:
                indegree[nei] -= 1
                # If a dependent course now has no prerequisites left, enqueue it
                if indegree[nei] == 0:
                    q.append(nei)
        
        # If we were able to schedule all courses, return the order.
        # Otherwise there's a cycle and it's impossible to finish all courses.
        if len(order) == numCourses:
            return order
        else:
            return []