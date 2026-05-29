from typing import List

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []
        
        def backtrack(start, current_combo, current_sum):
            # Base case: if we have k numbers
            if len(current_combo) == k:
                # Check if sum equals n
                if current_sum == n:
                    result.append(current_combo[:])  # Add a copy
                return
            
            # Pruning: if we already exceeded the sum or need more numbers than available
            if current_sum > n:
                return
            
            # Try each number from start to 9
            for num in range(start, 10):
                # Early termination: if current sum plus this number exceeds n, skip
                if current_sum + num > n:
                    break
                
                # Pruning: check if we can possibly reach n with remaining slots
                # Minimum sum with remaining numbers would be using consecutive numbers
                remaining_slots = k - len(current_combo) - 1
                if remaining_slots > 0:
                    # Check if even with the largest possible remaining numbers we can't reach n
                    min_additional = sum(range(num + 1, num + 1 + remaining_slots))
                    max_additional = sum(range(10 - remaining_slots, 10))
                    if current_sum + num + max_additional < n:
                        continue
                    if current_sum + num + min_additional > n:
                        break
                
                # Choose this number
                current_combo.append(num)
                # Recurse with next number (num + 1 to ensure no duplicates)
                backtrack(num + 1, current_combo, current_sum + num)
                # Backtrack: remove the number
                current_combo.pop()
        
        backtrack(1, [], 0)
        return result