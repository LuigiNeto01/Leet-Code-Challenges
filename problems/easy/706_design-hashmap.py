class MyHashMap:
    """A simple hash map implementation using separate chaining for collision resolution."""

    def __init__(self):
        self.bucket_count = 1000
        self.buckets = [[] for _ in range(self.bucket_count)]

    def _hash(self, key: int) -> int:
        return key % self.bucket_count

    def put(self, key: int, value: int) -> None:
        bucket_index = self._hash(key)
        bucket = self.buckets[bucket_index]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))

    def get(self, key: int) -> int:
        bucket_index = self._hash(key)
        bucket = self.buckets[bucket_index]
        for k, v in bucket:
            if k == key:
                return v
        return -1

    def remove(self, key: int) -> None:
        bucket_index = self._hash(key)
        bucket = self.buckets[bucket_index]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = bucket[-1]
                bucket.pop()
                return
        return