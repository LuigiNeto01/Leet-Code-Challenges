class SnapshotArray:

    def __init__(self, length: int):
        # Use a list of dictionaries: for each index, store a mapping from snap_id to value.
        # This avoids copying the entire array on each snap.
        # self.data[index] = {snap_id: value}
        self.data = [{} for _ in range(length)]
        # Current snap_id, initially 0 (first snap will return 0)
        self.current_snap = 0

    def set(self, index: int, val: int) -> None:
        # Store the current value at given index with the current snap_id.
        # Overwrites any previous value for this snap_id at this index.
        self.data[index][self.current_snap] = val

    def snap(self) -> int:
        # Return current snap_id and then increment it for next snapshot.
        snap_id = self.current_snap
        self.current_snap += 1
        return snap_id

    def get(self, index: int, snap_id: int) -> int:
        # Retrieve the value at given index for the given snap_id.
        # We need the value from the latest snapshot <= snap_id for that index.
        # Since dictionary keys are snap_ids, we can check if exact snap_id exists,
        # otherwise search backwards. To keep O(log n) per get, we could use binary search
        # but constraints are small enough; however we can also store sorted lists.
        # Here we implement simple backward search through stored snap_ids.
        snaps = self.data[index]
        # If snap_id is directly stored, return it.
        if snap_id in snaps:
            return snaps[snap_id]
        # Otherwise, find the most recent snapshot <= snap_id.
        # Since snap_ids are stored in increasing order of insertion,
        # we scan backwards from snap_id-1 down to 0 (or use stored keys).
        # To avoid linear scan, we could keep a sorted list of snap_ids per index.
        # But for clarity and given constraints, we'll try stored keys:
        possible = [s for s in snaps if s <= snap_id]
        if possible:
            # Return value of the latest snapshot <= snap_id
            latest = max(possible)
            return snaps[latest]
        # If no snapshot found, array was never set before this snap_id -> default 0
        return 0