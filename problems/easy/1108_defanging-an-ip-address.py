from __future__ import annotations

class Solution:
    def defangIPaddr(self, address: str) -> str:
        # Replace every '.' in the IP address with '[.]' to defang it.
        # This is a straightforward string replacement operation.
        # Python's str.replace() is simple and efficient for this task.
        # The input is guaranteed to be a valid IPv4 address, so we
        # don't need to validate or handle invalid formats.
        return address.replace('.', '[.]')