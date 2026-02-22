from __future__ import annotations
from typing import List

class Solution:
    def findDuplicateEmails(self, rows: List[List[str]]) -> List[str]:
        # Build a frequency map for emails from the given rows.
        email_count: dict[str, int] = {}

        for row in rows:
            # Each row is expected to be [id, email]. Be robust to odd data.
            if not row or len(row) < 2:
                continue
            email = row[1]
            email_count[email] = email_count.get(email, 0) + 1

        # Collect emails that appear more than once.
        duplicates = [email for email, cnt in email_count.items() if cnt > 1]

        # Return in deterministic order (any order is allowed by the problem).
        duplicates.sort()
        return duplicates