from typing import List

class Solution:
    def basicCalculatorIV(self, expression: str, evalvars: List[str], evalints: List[int]) -> List[str]:
        evalmap = dict(zip(evalvars, evalints))

        # Tokenize
        tokens = []
        i, n = 0, len(expression)
        while i < n:
            c = expression[i]
            if c == ' ':
                i += 1
            elif c.isdigit():
                j = i
                while j < n and expression[j].isdigit():
                    j += 1
                tokens.append(expression[i:j])
                i = j
            elif c.isalpha():
                j = i
                while j < n and expression[j].isalpha():
                    j += 1
                tokens.append(expression[i:j])
                i = j
            else:
                tokens.append(c)
                i += 1

        # Polynomial representation:
        #   dict: {tuple_of_variables: coefficient}
        #   e.g. {(): 3, ('a',): -1} means 3 - a
        idx = 0

        def constant_poly(v: int):
            return {(): v}

        def variable_poly(name: str):
            if name in evalmap:
                return constant_poly(evalmap[name])
            return {(name,): 1}

        def merge_vars(a, b):
            if not a:
                return b
            if not b:
                return a
            i = j = 0
            res = []
            while i < len(a) and j < len(b):
                if a[i] <= b[j]:
                    res.append(a[i])
                    i += 1
                else:
                    res.append(b[j])
                    j += 1
            if i < len(a):
                res.extend(a[i:])
            if j < len(b):
                res.extend(b[j:])
            return tuple(res)

        def add_poly(p, q):
            r = {k: v for k, v in p.items() if v}
            for k, v in q.items():
                nv = r.get(k, 0) + v
                if nv:
                    r[k] = nv
                else:
                    r.pop(k, None)
            return r

        def sub_poly(p, q):
            r = {k: v for k, v in p.items() if v}
            for k, v in q.items():
                nv = r.get(k, 0) - v
                if nv:
                    r[k] = nv
                else:
                    r.pop(k, None)
            return r

        def mul_poly(p, q):
            r = {}
            for k1, v1 in p.items():
                if v1 == 0:
                    continue
                for k2, v2 in q.items():
                    if v2 == 0:
                        continue
                    key = merge_vars(k1, k2)
                    nv = r.get(key, 0) + v1 * v2
                    if nv:
                        r[key] = nv
                    else:
                        r.pop(key, None)
            return r

        def parse_factor():
            nonlocal idx
            token = tokens[idx]

            if token == '(':
                idx += 1
                res = parse_expression()
                # Skip ')'
                if idx < len(tokens) and tokens[idx] == ')':
                    idx += 1
                return res

            if token.isdigit():
                idx += 1
                return constant_poly(int(token))

            # variable
            idx += 1
            return variable_poly(token)

        def parse_term():
            nonlocal idx
            res = parse_factor()

            while idx < len(tokens) and tokens[idx] == '*':
                idx += 1
                rhs = parse_factor()
                res = mul_poly(res, rhs)

            return res

        def parse_expression():
            nonlocal idx
            res = parse_term()

            while idx < len(tokens) and tokens[idx] in ('+', '-'):
                op = tokens[idx]
                idx += 1
                rhs = parse_term()
                if op == '+':
                    res = add_poly(res, rhs)
                else:
                    res = sub_poly(res, rhs)

            return res

        poly = parse_expression()

        # Format answer
        ans = []
        for key in sorted(poly.keys(), key=lambda k: (-len(k), k)):
            coef = poly[key]
            if coef == 0:
                continue
            if not key:
                ans.append(str(coef))
            else:
                ans.append("{}*{}".format(coef, "*".join(key)))

        return ans