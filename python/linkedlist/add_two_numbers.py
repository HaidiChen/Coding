# add two numbers stored in two linkedlists. the digits are stored in
# reverse order

# just perform a grade school alogrithm, track the carry one.

# time complexity is O(m + n)
# space complexity is O(1)

class Solution:
    def add_two_numbers(self, l1, l2):
        a = l1.next
        b = l2.next
        carry = 0
        result = ListNode()
        result_iter = result
        while a or b or c:
            a_val = 0 if not a else a.data
            b_val = 0 if not b else b.data
            val = a_val + b_val + carry
            carry = val / 10
            node = ListNode(val % 10)
            result_iter.next = node
            result_iter = result_iter.next
            a = a.next
            b = b.next

        return result

# this is the solution provided by dailyinterviewpro.
# it uses recursion instead of iteration which has a different space
# complexity from the above one

# time complexity is still O(m + n)
# space complexity is also O(max(m, n))

class Solution2:
    def add_two_numbers(self, l1, l2, c = 0):
        val = l1.val + l2.val + c
        c = val / 10
        ret = ListNode(val % 10)

        if l1.next or l2.next or c:
            if l1.next is None:
                l1.next = ListNode(0)
            if l2.next is None:
                l2.next = ListNode(0)

            ret.next = self.add_two_numbers(l1.next, l2.next, c)

        return ret
