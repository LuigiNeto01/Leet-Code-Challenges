from __future__ import annotations
from collections import defaultdict
from typing import List

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # ---------- Union-Find (DSU) helpers ----------
        parent = {}
        size = {}

        def find(x: str) -> str:
            # path compression
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(x: str, y: str) -> None:
            # union by size
            if x not in parent:
                parent[x] = x
                size[x] = 1
            if y not in parent:
                parent[y] = y
                size[y] = 1
            rx, ry = find(x), find(y)
            if rx == ry:
                return
            # attach smaller tree under larger tree
            if size[rx] < size[ry]:
                rx, ry = ry, rx
            parent[ry] = rx
            size[rx] += size[ry]

        # ---------- Process accounts ----------
        email_to_name = {}          # email -> owner name (arbitrary but consistent)
        for acc in accounts:
            name = acc[0]
            first_email = acc[1]
            # ensure first email is in DSU
            if first_email not in parent:
                parent[first_email] = first_email
                size[first_email] = 1
            # union first email with every other email in this account
            for email in acc[1:]:
                union(first_email, email)
                # record the name for this email (all emails in this account share the name)
                email_to_name[email] = name
            # also record name for first_email (in case it wasn't seen before)
            email_to_name[first_email] = name

        # ---------- Group emails by root ----------
        root_to_emails = defaultdict(list)
        for email in parent:        # iterate over all emails that were added
            root = find(email)
            root_to_emails[root].append(email)

        # ---------- Build result ----------
        result = []
        for root, emails in root_to_emails.items():
            # sort emails alphabetically
            emails.sort()
            # prepend the name (same for every email in this group)
            name = email_to_name[root]
            result.append([name] + emails)

        return result