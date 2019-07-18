# find the overlapping node of two linked lists

# if both linked lists end at the same tail node, they have overlapping
# nodes, otherwise these two linked lists do not overlap.
# if they overlap, calculate the length of each linked list and their
# difference k. so k = abs(len1 - len2). advance k nodes first in the
# longer linked list and then traverse two linked lists simultaneously
# until two iterators are pointing to the same node which is the frist
# overlapping node.

# time complexity is O(n + m)
# space complexity is O(1)

class Solution:
    def overlapping_no_cycle_lists(self, L1, L2):
        length1 = self._length(L1)
        length2 = self._length(L2)

        if length1 < length2:
            L1, L2 = L2, L1

        for _ in range(abs(length1 - length2)):
            L1 = L1.next

        while L1 and L2 and L1 is not L2:
            L1, L2 = L1.next, L2.next

        return L1
    
    def _length(self, L):
        length = 0
        
        L = L.next
        while L:
            length += 1
            L = L.next

        return length
