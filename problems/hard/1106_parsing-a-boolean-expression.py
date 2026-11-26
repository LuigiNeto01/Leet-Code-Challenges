class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stack = []
        
        for ch in expression:
            if ch == ',':
                continue
            elif ch == ')':
                values = []
                while stack and stack[-1] != '(':
                    val = stack.pop()
                    values.append(val)
                stack.pop()
                op = stack.pop()
                
                if op == '!':
                    result = values[0] == 'f'
                elif op == '&':
                    result = all(v == 't' for v in values)
                else:
                    result = any(v == 't' for v in values)
                
                stack.append('t' if result else 'f')
                
            elif ch in ('t', 'f'):
                stack.append(ch)
            else:
                stack.append(ch)
        
        return stack[-1] == 't'