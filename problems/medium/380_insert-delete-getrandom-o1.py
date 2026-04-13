import random

class RandomizedSet:
    def __init__(self):
        # Dynamic array to store values for O(1) random access
        self.nums = []  # list of values
        # Hash map to store value -> index in self.nums for O(1) lookups/removals
        self.pos = {}   # dict: value -> index

    def insert(self, val: int) -> bool:
        # If value already present, do nothing and return False
        if val in self.pos:
            return False
        # Append to list and record its index in the map
        self.nums.append(val)
        self.pos[val] = len(self.nums) - 1
        return True

    def remove(self, val: int) -> bool:
        # If value not present, cannot remove
        if val not in self.pos:
            return False
        # Index of element to remove
        idx = self.pos[val]
        # Value at the end of the list
        last_val = self.nums[-1]
        # Move the last element into the place of the element to remove
        # This keeps array compact and allows O(1) removal
        self.nums[idx] = last_val
        # Update the moved element's index in the map
        self.pos[last_val] = idx
        # Remove last element from list
        self.nums.pop()
        # Remove the deleted value from the map
        del self.pos[val]
        return True

    def getRandom(self) -> int:
        # It's guaranteed there's at least one element when called
        # Use random.choice for uniform random selection from list
        return random.choice(self.nums)

# Provide alias expected by the test harness
Solution = RandomizedSet