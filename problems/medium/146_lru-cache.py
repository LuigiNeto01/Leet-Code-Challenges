class LRUCache:
    class Node:
        def __init__(self, key: int = 0, value: int = 0):
            self.key = key
            self.value = value
            self.prev = None
            self.next = None

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # key -> Node
        # Dummy head and tail for doubly linked list (most recent at tail, least recent at head)
        self.head = self.Node()
        self.tail = self.Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        # Remove node from its current position in the linked list
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _add_to_tail(self, node):
        # Add node right before tail (most recently used position)
        prev_node = self.tail.prev
        prev_node.next = node
        node.prev = prev_node
        node.next = self.tail
        self.tail.prev = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        # Move accessed node to tail (mark as recently used)
        node = self.cache[key]
        self._remove(node)
        self._add_to_tail(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Update existing key: remove old node, update value, add to tail
            node = self.cache[key]
            self._remove(node)
            node.value = value
            self._add_to_tail(node)
        else:
            # Add new key-value pair
            if len(self.cache) >= self.capacity:
                # Evict least recently used (node right after head)
                lru_node = self.head.next
                self._remove(lru_node)
                del self.cache[lru_node.key]
            # Create new node and add to tail
            new_node = self.Node(key, value)
            self.cache[key] = new_node
            self._add_to_tail(new_node)