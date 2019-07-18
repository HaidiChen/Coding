# test if a linked list is a palindrome

# the solution is to reverse the last half and compare with the first half.

# time complexity is O(n)
# space complexity is O(1)

class Solution(object):
    """
    solution class to the question
    """
    def is_palindrome(self, L):
        slow, fast = L.next, L.next

        while fast and fast.next:
            fast, slow = fast.next.next, slow.next

        first_half_iter, second_half_iter = L.next, reverse_linked_list(slow)

        while first_half_iter and second_half_iter:
            if first_half.data != second_half_iter.data:
                return False
            second_half_iter = second_half_iter.next
            first_half_iter = first_half_iter.next

        return True
