from __future__ import annotations
from typing import List, Set

class Solution:
    def braceExpansionII(self, expression: str) -> List[str]:
        idx = 0

        def parse_expression() -> Set[str]:
            """Parse a top-level expression (concatenation of union terms)."""
            terms = [parse_term()]
            while idx < len(expression) and expression[idx] not in '}':
                if expression[idx] == ',':
                    break
                next_term = parse_term()
                new_set = set()
                for left in terms[-1]:
                    for right in next_term:
                        new_set.add(left + right)
                terms[-1] = new_set
            result: Set[str] = set()
            for s in terms:
                result.update(s)
            return result

        def parse_term() -> Set[str]:
            """Parse a term: either a single letter, or a { ... } block."""
            nonlocal idx
            if expression[idx] == '{':
                idx += 1                  # skip '{'
                result = parse_union()
                idx += 1                  # skip '}'
                return result
            else:
                letter = expression[idx]
                idx += 1
                return {letter}

        def parse_union() -> Set[str]:
            """Parse a union of expressions inside braces, separated by commas."""
            nonlocal idx
            result = parse_expression()
            while idx < len(expression) and expression[idx] == ',':
                idx += 1                  # skip comma
                next_expr = parse_expression()
                result.update(next_expr)
            return result

        final_set = parse_expression()
        return sorted(final_set)