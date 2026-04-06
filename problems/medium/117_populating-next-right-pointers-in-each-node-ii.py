class Solution:
    def connect(self, root: 'Node') -> 'Node':
        # Walk level by level using already-built next pointers,
        # so we avoid an explicit queue and keep constant extra space.
        current_level = root

        while current_level:
            # Dummy node helps build the next level as a simple linked list.
            dummy = Node(0)
            tail = dummy

            # Traverse the current level from left to right via next pointers.
            node = current_level
            while node:
                # Append left child first to preserve left-to-right order.
                if node.left:
                    tail.next = node.left
                    tail = tail.next

                # Then append right child if it exists.
                if node.right:
                    tail.next = node.right
                    tail = tail.next

                # Move horizontally within the current level.
                node = node.next

            # The next level starts at the first child we linked from dummy.
            current_level = dummy.next

        return root