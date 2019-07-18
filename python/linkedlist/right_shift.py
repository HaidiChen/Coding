# cyclically right shift k nodes in a singly linked list

# time complexity is O(n)
# space complexity is O(1)

class Solution:
    def cyclically_right_shift_list(self, L, k):
        if not L or not L.next:
            return L

        tail, n = L.next, 0

        while tail:
            n += 1
            tail = tail.next

        k %= n
        if k == 0:
            return L

        tail.next = L.next
        steps_to_new_head, new_tail = n - k, tail

        while steps_to_new_head:
            new_tail = new_tail.next
            steps_to_new_head -= 1

        L.next = new_tail.next
        new_tail.next = None

