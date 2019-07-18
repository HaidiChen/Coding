# merge two sorted singly linked lists

# just like merging two sorted arrays, but in this case
# we use iterator to traverse these two linked lists and
# choose the node with smaller data first.

# the time complexity is O(m + n)
# space complexity is O(1)
from listnode import ListNode

class Solution:
    def merge_two_lists(self, L1, L2):
        new_head = tail = ListNode()
        L1, L2 = L1.next, L2.next

        while L1 and L2:
            if L1.data < L2.data:
                tail.next = L1
                L1 = L1.next
            else:
                tail.next = L2
                L2 = L2.next

            tail = tail.next

        tail.next = L1 or L2

        return new_head
