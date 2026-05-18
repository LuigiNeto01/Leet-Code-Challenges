from typing import List

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # Sort by height descending, then by k ascending
        # This allows us to place taller people first, then shorter ones
        # For same height, smaller k values should be placed first
        people.sort(key=lambda x: (-x[0], x[1]))
        
        # Result queue to build
        result = []
        
        # Insert each person at their k position
        # Since we process from tallest to shortest, when we insert
        # a person at position k, all people at indices 0 to k-1
        # have height >= current person's height
        for person in people:
            height, k = person
            # Insert at index k - this ensures k people with height >= current are in front
            result.insert(k, person)
        
        return result