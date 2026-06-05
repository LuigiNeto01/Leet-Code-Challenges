class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        # Use iterative approach with a pointer
        curr = head
        
        while curr:
            # If current node has a child
            if curr.child:
                # Save the next node (we'll reconnect it later)
                next_node = curr.next
                
                # Connect curr to its child
                curr.next = curr.child
                curr.child.prev = curr
                
                # Find the tail of the child list
                tail = curr.child
                while tail.next:
                    tail = tail.next
                
                # Clear the child pointer as required
                curr.child = None
                
                # Connect the tail of child list to the saved next node
                if next_node:
                    tail.next = next_node
                    next_node.prev = tail
            
            # Move to next node
            curr = curr.next
        
        return head