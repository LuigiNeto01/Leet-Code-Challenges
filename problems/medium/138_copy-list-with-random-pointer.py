class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # Handle empty list
        if not head:
            return None
        
        # Step 1: Create a mapping from original nodes to copied nodes
        # This allows us to look up the copied version of any original node
        old_to_new = {}
        
        # First pass: create all new nodes with correct values
        current = head
        while current:
            # Create a new node with the same value, but no pointers yet
            # Use the Node class from the same module as the input
            old_to_new[current] = current.__class__(current.val)
            current = current.next
        
        # Step 2: Set up next and random pointers for all copied nodes
        current = head
        while current:
            # Get the corresponding copied node
            new_node = old_to_new[current]
            
            # Set next pointer: if original has next, point to the copy of next
            if current.next:
                new_node.next = old_to_new[current.next]
            
            # Set random pointer: if original has random, point to the copy of random
            if current.random:
                new_node.random = old_to_new[current.random]
            
            current = current.next
        
        # Return the head of the copied list
        return old_to_new[head]