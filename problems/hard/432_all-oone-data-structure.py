class Node:
    __slots__ = ('count', 'keys', 'prev', 'next')
    def __init__(self, count):
        self.count = count
        self.keys = set()
        self.prev = None
        self.next = None

class Solution:
    def __init__(self):
        # Dummy head and tail to simplify edge insertions/removals
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        # Map each key to the node that currently holds it
        self.map = {}

    def _insert_after(self, prev_node, new_node):
        # Insert new_node right after prev_node
        nxt = prev_node.next
        prev_node.next = new_node
        new_node.prev = prev_node
        new_node.next = nxt
        nxt.prev = new_node

    def _remove_node(self, node):
        # Remove a node from the linked list
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev
        # Clean up pointers for safety
        node.prev = node.next = None

    def inc(self, key: str) -> None:
        if key not in self.map:
            # Key not present: try to place into a node with count 1
            if self.head.next is self.tail or self.head.next.count != 1:
                new_node = Node(1)
                self._insert_after(self.head, new_node)
            else:
                new_node = self.head.next
            new_node.keys.add(key)
            self.map[key] = new_node
        else:
            # Move key from current node to the next node with count+1
            cur = self.map[key]
            nxt = cur.next
            target_count = cur.count + 1
            if nxt is self.tail or nxt.count != target_count:
                new_node = Node(target_count)
                self._insert_after(cur, new_node)
            else:
                new_node = nxt
            new_node.keys.add(key)
            self.map[key] = new_node

            # Remove from old node; delete old node if empty
            cur.keys.remove(key)
            if not cur.keys:
                self._remove_node(cur)

    def dec(self, key: str) -> None:
        node = self.map[key]
        cur_count = node.count
        prev_node = node.prev

        # Remove key from current node
        node.keys.remove(key)
        if not node.keys:
            self._remove_node(node)

        if cur_count == 1:
            # Count would drop to 0: remove key entirely
            del self.map[key]
            return

        target_count = cur_count - 1
        # If there is a node with target_count just before current node, reuse it
        if prev_node is not self.head and prev_node.count == target_count:
            dest = prev_node
        else:
            # Otherwise, create a new node for target_count and insert after previous node
            dest = Node(target_count)
            self._insert_after(prev_node, dest)

        dest.keys.add(key)
        self.map[key] = dest

    def getMaxKey(self) -> str:
        # Max is at the node before tail; if none, return empty string
        if self.tail.prev is self.head:
            return ""
        return next(iter(self.tail.prev.keys))

    def getMinKey(self) -> str:
        # Min is at the node after head; if none, return empty string
        if self.head.next is self.tail:
            return ""
        return next(iter(self.head.next.keys))