from typing import List
from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # Build adjacency list graph with destinations sorted in reverse lexical order
        # We use reverse order because we'll pop from the end (for efficiency)
        graph = defaultdict(list)
        for src, dst in sorted(tickets, reverse=True):
            graph[src].append(dst)
        
        # Result will store the final itinerary in reverse order
        result = []
        
        # Hierholzer's algorithm for finding Eulerian path
        # We use DFS and add nodes to result when we finish exploring all edges from that node
        def dfs(airport):
            # Keep visiting destinations while there are unvisited edges
            while graph[airport]:
                # Pop the next destination (smallest lexically since sorted in reverse)
                next_dest = graph[airport].pop()
                dfs(next_dest)
            # After all edges from this node are visited, add to result
            # This ensures we build the path in reverse order
            result.append(airport)
        
        # Start DFS from JFK
        dfs("JFK")
        
        # Reverse the result to get the correct order
        return result[::-1]