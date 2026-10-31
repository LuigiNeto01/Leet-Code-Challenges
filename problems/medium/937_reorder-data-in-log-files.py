class Solution:
    def reorderLogFiles(self, logs: list[str]) -> list[str]:
        # Separate logs into letter-logs and digit-logs.
        letter_logs = []
        digit_logs = []
        for log in logs:
            # Split once to get the first token after identifier.
            # Since each log has at least one word after the identifier,
            # we can safely check the second token's first character.
            # If it's a digit, the log is a digit-log.
            # Note: identifier itself can be alphanumeric, but we only
            # check the first token after it.
            if log.split()[1].isdigit():
                digit_logs.append(log)
            else:
                letter_logs.append(log)

        # Sort letter-logs by (contents, identifier) in lexicographic order.
        # We use split with maxsplit=1 to separate identifier from the rest.
        letter_logs.sort(key=lambda x: (x.split(' ', 1)[1], x.split(' ', 1)[0]))

        # Digit-logs keep their original relative order.
        # Return concatenated result.
        return letter_logs + digit_logs