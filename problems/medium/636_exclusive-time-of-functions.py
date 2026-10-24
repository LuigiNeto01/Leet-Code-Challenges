class Solution:
    def exclusiveTime(self, n: int, logs: list[str]) -> list[int]:
        ans = [0] * n
        stack = []  # call stack of active function IDs
        prev = 0    # previous event's boundary timestamp

        for log in logs:
            parts = log.split(":")
            fid = int(parts[0])
            typ = parts[1]
            ts = int(parts[2])

            if typ == "start":
                # The currently running function executed from prev up to ts - 1.
                if stack:
                    ans[stack[-1]] += ts - prev
                stack.append(fid)
                prev = ts
            else:
                # The ending function executed from prev through ts, inclusive.
                ended = stack.pop()
                ans[ended] += ts - prev + 1
                prev = ts + 1

        return ans