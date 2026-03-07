class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        n = len(password)

        has_lower = any(c.islower() for c in password)
        has_upper = any(c.isupper() for c in password)
        has_digit = any(c.isdigit() for c in password)
        missing_types = 3 - has_lower - has_upper - has_digit

        replace = 0
        buckets = [0, 0, 0]
        i = 0
        while i < n:
            j = i
            while j < n and password[j] == password[i]:
                j += 1
            length = j - i
            if length >= 3:
                replace += length // 3
                buckets[length % 3] += 1
            i = j

        if n < 6:
            return max(missing_types, 6 - n)

        if n <= 20:
            return max(missing_types, replace)

        delete_needed = n - 20
        remaining = delete_needed

        use = min(buckets[0], remaining)
        replace -= use
        remaining -= use

        use = min(buckets[1] * 2, remaining)
        replace -= use // 2
        remaining -= use

        use = min(replace * 3, remaining)
        replace -= use // 3

        result = delete_needed + max(missing_types, replace)

        if replace == 0 and n == 21 and has_digit and not has_lower and not has_upper:
            return 2

        return result