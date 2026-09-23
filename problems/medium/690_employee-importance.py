from __future__ import annotations
from typing import List

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        # Build a mapping from employee ID to employee object for O(1) lookup.
        emp_map = {emp.id: emp for emp in employees}
        
        # Use iterative DFS (stack) to sum importance of the target employee
        # and all their direct/indirect subordinates.
        total = 0
        stack = [id]  # start with the given employee ID
        while stack:
            curr_id = stack.pop()
            emp = emp_map[curr_id]
            total += emp.importance
            # Add all direct subordinates to the stack to process their subtrees.
            stack.extend(emp.subordinates)
        
        return total