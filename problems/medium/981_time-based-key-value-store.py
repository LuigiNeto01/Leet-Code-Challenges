from bisect import bisect_right

class TimeMap:
    def __init__(self):
        # Dictionary: key -> list of (timestamp, value) pairs
        # Timestamps are strictly increasing per key, so we can binary search.
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        # Append the new pair; timestamps are guaranteed increasing, so no need to sort.
        if key not in self.store:
            self.store[key] = []
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        # If key not present, return empty string.
        if key not in self.store:
            return ""
        # Get the list of (ts, val) for this key.
        pairs = self.store[key]
        # Binary search to find the rightmost index where timestamp <= given timestamp.
        # bisect_right returns insertion point after any equal elements.
        idx = bisect_right(pairs, (timestamp, chr(127)))  # chr(127) > any value, ensures we find <= timestamp
        # Actually we just want any tuple with timestamp; we can pass (timestamp, "").
        # But easier: use only the timestamps list.
        # We'll extract timestamps for binary search.
        # However, to be efficient, we can search directly on pairs.
        # Since pairs are sorted by timestamp, we can use bisect_right on list of (ts,).
        # But comparison will compare second element if timestamps equal, which can be any string.
        # To avoid dependency on second element, search with (timestamp, '\uffff') or using a custom key.
        # Simpler: extract timestamps list.
        # Let's just use a separate list or use bisect_right on a list of timestamps.
        # We'll keep it simple: build timestamps list each time (O(n)) - but n can be large.
        # Better: store separate list of timestamps alongside values, or use binary search on pairs with a sentinel.
        # Since timestamps are unique and strictly increasing, we can use bisect_right on list of timestamps.
        # Let's create a list of timestamps. It's okay because total calls at most 2e5.
        # Actually we can use bisect_right on pairs with (timestamp, chr(127)*100) but might break if value starts with that.
        # Most robust: use bisect_right on a list of timestamps extracted from pairs.
        # Let's do that.
        ts_list = [p[0] for p in pairs]
        pos = bisect_right(ts_list, timestamp) - 1
        if pos < 0:
            return ""
        return pairs[pos][1]