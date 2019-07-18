# reorder the linked list in such a way that even nodes followed by odd nodes.

# time complexity is O(n)
# space complexity is O(1)

class Solution(object):
    """
    Solution class to the question.
    """
    def even_odd_merge(self, L):
        if not L:
            return L

        even_head, odd_head = L, L
        tails, turn = [even_head, odd_head], 0

        L = L.next
        while L:
            tails[turn].next = L
            L = L.next
            tails[turn] = tails[turn].next
            turn ^= 1

        tails[1].next = None
        tails[0].next = odd_head.next

        return even_head
