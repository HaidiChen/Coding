# reverse a sub list starting at sth node and ending at
# the fth node within a singly linked list.

# typical reverse operation

# time complexity is O(f) as it is dominated by searching
# for the fth node
# space complexity is O(1)

class Solution:
    def reverse_sublist(self, L, start, finish):
        cur = L

        for _ in range(1, start):
            cur = cur.next

        prev = cur
        cur = cur.next

        for _ in range(finish - start):
            tmp = cur.next
            cur.next = tmp.next
            tmp.next = prev.next
            prev.next = tmp

