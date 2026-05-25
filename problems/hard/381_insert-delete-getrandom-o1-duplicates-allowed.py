import random

class RandomizedCollection:

    def __init__(self):
        # List to store all elements (allows duplicates and O(1) random access)
        self.nums = []
        # Map from value to set of indices where this value appears in nums
        self.val_to_indices = {}

    def insert(self, val: int) -> bool:
        # Check if val is already present
        is_new = val not in self.val_to_indices
        
        # Add the new index to the set of indices for this value
        if val not in self.val_to_indices:
            self.val_to_indices[val] = set()
        self.val_to_indices[val].add(len(self.nums))
        
        # Append value to the list
        self.nums.append(val)
        
        return is_new

    def remove(self, val: int) -> bool:
        # Check if val exists in the collection
        if val not in self.val_to_indices or not self.val_to_indices[val]:
            return False
        
        # Get an arbitrary index of val to remove
        idx_to_remove = self.val_to_indices[val].pop()
        last_idx = len(self.nums) - 1
        last_val = self.nums[last_idx]
        
        # Move the last element to the position of the element to remove
        self.nums[idx_to_remove] = last_val
        
        # Update the index mapping for the last element
        # (only if we're not removing the last element itself)
        if idx_to_remove != last_idx:
            self.val_to_indices[last_val].remove(last_idx)
            self.val_to_indices[last_val].add(idx_to_remove)
        
        # Remove the last element from the list
        self.nums.pop()
        
        # Clean up empty set from map if no more instances of val
        if not self.val_to_indices[val]:
            del self.val_to_indices[val]
        
        return True

    def getRandom(self) -> int:
        # Return a random element from the list
        return random.choice(self.nums)