class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        # Sliding window: find longest subarray with at most 2 distinct fruit types.
        count = {}          # fruit type -> frequency in current window
        left = 0
        max_picked = 0

        for right, fruit in enumerate(fruits):
            # Add current fruit to the window.
            count[fruit] = count.get(fruit, 0) + 1

            # If more than 2 distinct types, shrink from left.
            while len(count) > 2:
                left_fruit = fruits[left]
                count[left_fruit] -= 1
                if count[left_fruit] == 0:
                    del count[left_fruit]
                left += 1

            # Update maximum window length.
            max_picked = max(max_picked, right - left + 1)

        return max_picked