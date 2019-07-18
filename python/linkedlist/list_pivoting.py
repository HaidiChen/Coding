# partition a linked list. e.g., if the pivot value is k, the left part nodes
# value are less than k and middle part nodes value are equal to k, and the
# right part nodes are all greater than k, the order should remain unchanged.

class Solution:
    def list_pivoting(self, L, x):
        less_head = less_iter = ListNode()
        equal_head = equal_iter = ListNode()
        greater_head = greater_iter = ListNode()
        
        while L:
            if L.data < x:
                less_iter.next = L
                less_iter = less_iter.next
            elif L.data == x:
                equal_iter.next = L
                equal_iter = equal_iter.next
            else:
                greater_iter.next = L
                greater_iter = greater_iter.next
            L = L.next

        greater_iter.next = None
        equal_iter.next = greater_head.next
        less_iter.next = equal_head.next

        return less_head.next
