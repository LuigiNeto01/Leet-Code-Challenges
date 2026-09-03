from __future__ import annotations

class Solution:
    def isValid(self, code: str) -> bool:
        # Helper to validate a tag name: uppercase letters, length 1-9
        def is_valid_tag_name(tag: str) -> bool:
            if not (1 <= len(tag) <= 9):
                return False
            # All characters must be uppercase letters
            return all('A' <= ch <= 'Z' for ch in tag)

        n = len(code)
        if n == 0 or code[0] != '<':
            return False

        stack = []          # stack of open tag names
        i = 0

        while i < n:
            if code[i] == '<':
                # Check for CDATA: "<![CDATA["
                if code[i:i+9] == "<![CDATA[":
                    # CDATA is only allowed inside a tag (stack not empty)
                    if not stack:
                        return False
                    # Find the closing "]]>"
                    j = code.find("]]>", i+9)
                    if j == -1:
                        return False
                    i = j + 3          # skip the whole CDATA section
                    continue

                # Check for end tag: "</"
                if i+1 < n and code[i+1] == '/':
                    j = code.find('>', i+2)
                    if j == -1:
                        return False
                    tag_name = code[i+2:j]
                    if not is_valid_tag_name(tag_name):
                        return False
                    # Must match the most recent open tag
                    if not stack or stack[-1] != tag_name:
                        return False
                    stack.pop()
                    i = j + 1
                    # After the outermost tag is closed, no more code should remain
                    if not stack and i != n:
                        return False
                    continue

                # Otherwise it is a start tag: "<TAG_NAME>"
                j = code.find('>', i+1)
                if j == -1:
                    return False
                tag_name = code[i+1:j]
                if not is_valid_tag_name(tag_name):
                    return False
                stack.append(tag_name)
                i = j + 1
                continue

            else:
                # Plain text can only appear inside a tag
                if not stack:
                    return False
                # Skip to the next '<' or to the end of the string
                next_lt = code.find('<', i)
                if next_lt == -1:
                    i = n
                else:
                    i = next_lt

        # After processing the entire string, all opened tags must be closed
        return not stack