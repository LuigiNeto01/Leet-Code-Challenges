class Solution:
    def numEquivDominoPairs(self, dominoes: list[list[int]]) -> int:
        # Use a dictionary to count occurrences of each normalized domino
        # Normalize by sorting the two numbers, so [a,b] and [b,a] become the same key
        count = {}
        result = 0
        
        for a, b in dominoes:
            # Create a canonical representation: min, max
            # Since values are 1-9, we could also encode as a single integer
            # but tuple is clearer
            key = (min(a, b), max(a, b))
            
            # Number of new pairs formed by this domino with all previous identical ones
            # If we have seen this key 'c' times before, adding this domino gives 'c' new pairs
            # Because this domino can pair with each of the 'c' previous ones
            if key in count:
                result += count[key]
                count[key] += 1
            else:
                count[key] = 1
        
        return result