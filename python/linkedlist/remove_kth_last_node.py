# remove the kth last node in a singly linked list, you don't
# know the length of the list and you can't store the length
# as well.

# the solution is to use two iterators. One advancing k nodes
# first, then two iterators advance in tandem. when the fast
# iterator reaches the tail, the slow iterator is at (k+1)th
# last node position, and from that node, we can delete the
# kth last node.

class Solution:
    def remove_kth_last_node(self, k, L):
        slow = L
        fast = L.next

        for _ in range(k):
            fast = fast.next

        while fast:
            fast = fast.next
            slow = slow.next

        tmp = slow.next
        slow.next = temp.next
        temp.next = None

        return L
