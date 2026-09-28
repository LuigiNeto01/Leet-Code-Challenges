class MyHashSet:
    def __init__(self):
        # Use a prime bucket count to help distribute keys evenly.
        self.size = 1009
        self.buckets = [[] for _ in range(self.size)]

    def _hash(self, key: int) -> int:
        # Simple modulo hashing; all keys are non-negative.
        return key % self.size

    def add(self, key: int) -> None:
        bucket = self.buckets[self._hash(key)]
        # Avoid duplicate values inside a bucket.
        if key not in bucket:
            bucket.append(key)

    def remove(self, key: int) -> None:
        bucket = self.buckets[self._hash(key)]
        for i, val in enumerate(bucket):
            if val == key:
                bucket.pop(i)
                return  # Nothing else to do; each key exists at most once.

    def contains(self, key: int) -> bool:
        bucket = self.buckets[self._hash(key)]
        for val in bucket:
            if val == key:
                return True
        return False