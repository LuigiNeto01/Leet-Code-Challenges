from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # Sort candidates to handle duplicates and enable pruning
        candidates.sort()
        result = []
        
        def backtrack(start: int, current: List[int], remaining: int):
            # Base case: found a valid combination
            if remaining == 0:
                result.append(current[:])
                return
            
            # Base case: exceeded target (pruning)
            if remaining < 0:
                return
            
            for i in range(start, len(candidates)):
                # Skip duplicates at the same level to avoid duplicate combinations
                # Only skip if it's not the first element we're considering at this level
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                
                # Prune: if current candidate exceeds remaining, no point continuing
                # (array is sorted, so all following candidates will also exceed)
                if candidates[i] > remaining:
                    break
                
                # Include current candidate and recurse
                current.append(candidates[i])
                # Move to next index (i+1) since each number can only be used once
                backtrack(i + 1, current, remaining - candidates[i])
                # Backtrack: remove current candidate to try next option
                current.pop()
        
        backtrack(0, [], target)
        return result