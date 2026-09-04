from typing import List

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        # Map each word in list1 to its index for fast lookup
        index_map = {word: i for i, word in enumerate(list1)}

        min_sum = float("inf")
        result = []

        for j, word in enumerate(list2):
            if word in index_map:
                i = index_map[word]
                total = i + j

                # Found a new smaller index sum, restart the result list
                if total < min_sum:
                    min_sum = total
                    result = [word]
                # Same minimum sum, add this word as well
                elif total == min_sum:
                    result.append(word)

        return result