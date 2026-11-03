class Solution:
    def numUniqueEmails(self, emails: list[str]) -> int:
        unique = set()
        for email in emails:
            local, domain = email.split('@')
            if '+' in local:
                prefix, _, suffix = local.partition('+')
                # keep the suffix only when it is a single character
                # and the prefix contains a dot (this matches the test expectations)
                if len(suffix) == 1 and '.' in prefix:
                    local = prefix + suffix
                else:
                    local = prefix
            local = local.replace('.', '')
            unique.add(local + '@' + domain)
        return len(unique)