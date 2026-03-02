class Solution:
    def evaluate(self, expression: str) -> int:
        s = expression
        tokens = []
        i = 0
        n = len(s)
        while i < n:
            c = s[i]
            if c == ' ':
                i += 1
                continue
            if c == '(' or c == ')':
                tokens.append(c)
                i += 1
            else:
                if c == '-' or c.isdigit():
                    j = i + 1
                    while j < n and s[j].isdigit():
                        j += 1
                    tokens.append(s[i:j])
                    i = j
                else:
                    j = i
                    while j < n and s[j] not in ' ()':
                        j += 1
                    tokens.append(s[i:j])
                    i = j

        self.tokens = tokens
        self.ptr = 0
        self.scopes = [{}]

        def is_var_token(tok: str) -> bool:
            if not tok:
                return False
            if tok in ('add', 'let', 'mult', '(', ')'):
                return False
            if not tok[0].isalpha() or not ('a' <= tok[0] <= 'z'):
                return False
            for ch in tok[1:]:
                if not (ch.isdigit() or ('a' <= ch <= 'z')):
                    return False
            return True

        def is_number(tok: str) -> bool:
            if not tok:
                return False
            if tok[0] == '-' and len(tok) > 1:
                return tok[1:].isdigit()
            return tok.isdigit()

        def resolve(name: str) -> int:
            for scope in reversed(self.scopes):
                if name in scope:
                    return scope[name]
            return 0

        def parse_expr() -> int:
            t = self.tokens[self.ptr]
            if t == '(':
                self.ptr += 1
                op = self.tokens[self.ptr]
                self.ptr += 1

                if op == 'let':
                    self.scopes.append({})
                    while self.ptr < len(self.tokens) and is_var_token(self.tokens[self.ptr]):
                        var = self.tokens[self.ptr]
                        self.ptr += 1
                        val = parse_expr()
                        self.scopes[-1][var] = val
                        # Decide whether to continue reading bindings
                        if not (self.ptr < len(self.tokens) and is_var_token(self.tokens[self.ptr])
                                and (self.ptr + 1) < len(self.tokens)
                                and self.tokens[self.ptr + 1] != ')'):
                            break
                    val = parse_expr()
                    assert self.tokens[self.ptr] == ')'
                    self.ptr += 1
                    self.scopes.pop()
                    return val

                elif op == 'add':
                    a = parse_expr()
                    b = parse_expr()
                    assert self.tokens[self.ptr] == ')'
                    self.ptr += 1
                    return a + b

                elif op == 'mult':
                    a = parse_expr()
                    b = parse_expr()
                    assert self.tokens[self.ptr] == ')'
                    self.ptr += 1
                    return a * b

            else:
                self.ptr += 1
                if is_number(t):
                    return int(t)
                else:
                    return resolve(t)

        result = parse_expr()
        return result