class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # We cannot access the previous node, so we cannot "unlink" this node directly.
        # Instead, copy the next node's value into this node...
        node.val = node.next.val

        # ...then skip over the next node, which effectively removes it from the list.
        node.next = node.next.next