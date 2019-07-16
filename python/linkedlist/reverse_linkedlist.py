# reverse a singly linkedlist

# we can do this recursively and iteratively.

# for the iterative version, the time complexity is 
# O(n) and space complexity is O(1)

# for the recursive version, the time complexity is 
# O(n) and space complexity is O(n)

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def printList(self):
        node = self
        output = ''
        while node:
            output += str(node.val)
            output += ' '
            node = node.next

        print(output)

    # this iterative version is provided by dailyinterviewpro
    def reverseListIteratively(self, head):
        previous = None
        current = head

        while head:
            nextNode = current.next
            current.next = previous
            previous = current
            current = nextNode

    # this is my iterative version
    def reverse_list_iteratively(self, head):
        still = head.next

        while still.next:
            tmp = still.next
            still.next = tmp.next
            tmp.next = head.next
            head.next = tmp

    # this is the recursive version and it's provided by
    # the dailyinterviewpro
    def reverseListRecursively(self, head):
        if not head or not head.next:
            return head
        node = self.reverseListRecursively(head.next)
        head.next.next = head
        head.next = None

        return node
