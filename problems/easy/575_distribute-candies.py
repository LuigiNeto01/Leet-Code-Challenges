class Solution:
    def distributeCandies(self, candyType: list[int]) -> int:
        unique_types = len(set(candyType))
        max_eat = len(candyType) // 2
        return min(unique_types, max_eat)