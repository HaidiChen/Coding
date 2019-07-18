# remove the duplicates from the sorted singly linked list.

# the solution is to use two iterators, one pointing at the
# current non-duplicate node, the other just traversing the
# list. if during the traversal, we see a node which has a
# different value than the current node. link these two nodes
# and advance the current node iterator.

# the time complexity is O(n)
# the space complexity is O(1)
from listnode import ListNode

class Solution:
    def remove_duplicates(self, L):
        if L is None or type(L) != ListNode:
            return None
        cur = L.next

        while cur:
            it = cur.next
            while it and it.data == cur.data:
                it = it.next
            cur.next = it
            cur = cur.next

