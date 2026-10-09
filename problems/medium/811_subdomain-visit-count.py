from collections import Counter

class Solution:
    def subdomainVisits(self, cpdomains: list[str]) -> list[str]:
        counts = Counter()

        for entry in cpdomains:
            # Split visit count and the full domain
            rep, domain = entry.split()
            reps = int(rep)

            # Split domain into parts, e.g. ["discuss", "leetcode", "com"]
            parts = domain.split(".")

            # Build each parent domain suffix from right to left
            for i in range(len(parts)):
                subdomain = ".".join(parts[i:])
                counts[subdomain] += reps

        # Convert accumulated counts back to required format
        return [f"{cnt} {domain}" for domain, cnt in counts.items()]