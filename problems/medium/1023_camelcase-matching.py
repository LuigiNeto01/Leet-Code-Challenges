class Solution:
    def camelMatch(self, queries: list[str], pattern: str) -> list[bool]:
        def match(query: str, pat: str) -> bool:
            i = 0  # index in pattern
            for c in query:
                if i < len(pat):
                    pc = pat[i]
                    matched = False
                    if pc.islower():
                        if c == pc:
                            matched = True
                    else:  # pc is upper case
                        if i == 0:  # first character of pattern
                            if len(pat) == 1:
                                # single uppercase pattern must match exactly
                                if c == pc:
                                    matched = True
                            else:
                                # first uppercase can match any uppercase
                                if c.isupper():
                                    matched = True
                        else:  # not first character
                            # allow exact uppercase match or lowercase same letter
                            if (c.isupper() and c == pc) or \
                               (c.islower() and c.lower() == pc.lower()):
                                matched = True
                    if matched:
                        i += 1
                        continue

                # If the character was not used to match the pattern,
                # an uppercase letter makes the query invalid.
                if c.isupper():
                    return False

            # All pattern characters must be consumed
            return i == len(pat)

        return [match(q, pattern) for q in queries]