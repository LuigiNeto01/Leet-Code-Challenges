class NumArray:
    def __init__(self, nums: list[int]):
        # Use a Fenwick Tree (Binary Indexed Tree) for efficient updates and range queries
        # Both operations are O(log n)
        self.n = len(nums)
        self.nums = nums[:]  # Keep original array for update delta calculation
        self.tree = [0] * (self.n + 1)  # 1-indexed tree
        
        # Build the tree by adding each element
        for i in range(self.n):
            self._add(i, nums[i])
    
    def _add(self, index: int, delta: int) -> None:
        # Add delta to element at index in the Fenwick tree
        # index is 0-based, convert to 1-based for tree
        index += 1
        while index <= self.n:
            self.tree[index] += delta
            # Move to next node: add least significant bit
            index += index & (-index)
    
    def _prefix_sum(self, index: int) -> int:
        # Calculate prefix sum from 0 to index (inclusive)
        # index is 0-based, convert to 1-based for tree
        index += 1
        total = 0
        while index > 0:
            total += self.tree[index]
            # Move to parent: remove least significant bit
            index -= index & (-index)
        return total

    def update(self, index: int, val: int) -> None:
        # Calculate the difference and update tree
        delta = val - self.nums[index]
        self.nums[index] = val
        self._add(index, delta)

    def sumRange(self, left: int, right: int) -> int:
        # Range sum = prefix_sum(right) - prefix_sum(left - 1)
        if left == 0:
            return self._prefix_sum(right)
        return self._prefix_sum(right) - self._prefix_sum(left - 1)